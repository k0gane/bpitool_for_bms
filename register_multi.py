from bs4 import BeautifulSoup
import math
import json
import csv
import requests
import urllib
def PGF(x,m):
    try:
        return 1+(x-0.5)/(1-x)
    except:
        return m

def BPI_calc(s,k,z,m,p):
    S=PGF(s/m,m)
    K=PGF(k/m,m)
    Z=PGF(z/m,m)
    S_dash=S/K
    Z_dash=Z/K
    if(s>=k):
        return 100*(pow(math.log(S_dash),p))/(pow(math.log(Z_dash),p))
    else:
        return -100*(pow(-math.log(S_dash),p))/(pow(math.log(Z_dash),p))

black_list = [114328, 111023, 122738, 108312, 141249, 114453, 111571, 113171, 113693, 140162, 71767, 144372, 159674, 51364]
BPI_per = [0.0003791, 0.0008341, 0.0018335, 0.00403067, 0.00886266, 0.01948992, 0.04286059, 0.09425297, 0.2072687]


def make_chart(json_url, songs_dir, players_dir, border):
    si = 1
    songs_data = {}
    songs_title = []
    songs_md5 = []
    pname = []
    got_name = []
    frag = not(songs_dir == "songs_satellite" or songs_dir == "songs_stella" or songs_dir == "songs_insane")
    if(frag):
        lr2_score = [[] for _ in range(170000)]
    response = requests.get(json_url)
    json_data = response.json()

    for song in json_data:
        ranking_url = "http://www.dream-pro.info/~lavalse/LR2IR/search.cgi?mode=ranking&bmsmd5=" + str(song['md5'])
        s_title = song['title']
        s_md5 = song['md5']
        max_record = 2
        page = 1
        BPI_rank = []#理想BPIを格納
        ranking_data = [] #スコア
        while True:#page1~n
            IR_URL=ranking_url+"&page="+str(page)
            IR_html=urllib.request.urlopen(IR_URL).read().decode('shift_JIS', 'ignore')
            IR_soup = BeautifulSoup(IR_html, "html.parser")
            try:
                IR_list=str(IR_soup.findAll("table")[3]).split("\n")[2:-1][0::2]
                if(max_record):
                    max_score = int(IR_list[0].split('>')[14].split('/')[1].split('(')[0])
                    max_record -= 1
            except:
                break
            for IR_player in IR_list:
                IR = IR_player.split('>')
                player_ID = int(IR[4].split("=")[3].strip('"'))
                if(player_ID in black_list):
                    continue
                else:
                    player_name = IR[5].split("<")[0]
                    if(frag):
                        if(not(player_name in got_name)):
                            pname.append([player_ID, player_name])
                            got_name.append(player_name)
                    player_score = int(IR[14].split('/')[0])
                    score_rate = float(IR[14].split('/')[1].split('(')[1].split('%')[0])
                    min_BP = int(IR[18].split("<")[0])
                    if(score_rate >= border):
                        ranking_data.append(player_score)
                        user_lank = len(ranking_data)
                        if(frag):
                            lr2_score[player_ID-1].append([s_title, s_md5, player_score, user_lank, min_BP])
                    elif(len(ranking_data) == 0):
                        continue
                    else:
                        break
            page += 1
        for i in range(170000):
            try:
                q = lr2_score[i][si-1]
            except IndexError:
                lr2_score[i].append([s_title, s_md5, 0, 0, 0])
        while ranking_data[0] > max_score:
            ranking_data.pop(0)
        zenichi = ranking_data[0]
        average = sum(ranking_data) / len(ranking_data)
        players = len(ranking_data)
        print("Title:" + s_title)
        print("md5:" + s_md5)
        print("理論値:" + str(max_score))
        print("全1:" + str(zenichi))
        print("平均:" + str(average))
        if players < 12: #プレイヤー人数で場合分け
            great_p = 1.5
        else:#11人以下ならスキップ
            for bpn in BPI_per:
                rank_append = math.ceil(bpn * players)
                if(rank_append == 1):
                    rank_append += 1
                if(rank_append in BPI_rank):
                    rank_append = max(BPI_rank) + 1
                BPI_rank.append(rank_append)
            BPI_score = []
            for bp in BPI_rank:
                BPI_score.append(ranking_data[bp + 1])
            BPI_otehon = [90, 80, 70, 60, 50, 40, 30, 20, 10]
            great_p = 1.8
            min_bunsan = 1e9
            for kouho_p in range(1, 1501):#p=(0.01, 1.5)で最小二乗法
                BPI_zissai = []
                kouho_p /= 1000
                for bs in BPI_score:
                    if(bs <= max_score):
                        BPI_zissai.append(BPI_calc(bs,average,zenichi,max_score,kouho_p))
                    else:
                        BPI_zissai.append(90)
                bunsan = 0
                for j in range(len(BPI_score)):
                    bunsan += (BPI_otehon[j] - BPI_zissai[j])**2
                if(min_bunsan > bunsan):
                    great_p = kouho_p
                    min_bunsan = bunsan
        print("理想のp値:" + str(great_p))
        if(song['level'] == '？' or song['level'] == '???'):
            song['level'] = 99      
        else:
            songs_data[s_md5] = {"title":s_title, "grade":int(song['level']), "max_score":max_score, "zenichi":zenichi, "average":average, "p":great_p, "players":len(ranking_data), "md5":s_md5}
            print(songs_data[s_md5])
        si += 1
        songs_md5.append(s_md5)
        songs_title.append(s_title)

    with open("bpitool/score_data/" + songs_dir + ".json", 'w') as f:
        json.dump(songs_data, f, ensure_ascii=False, indent=4)
    if(frag):
        with open("bpitool/score_data/" + players_dir + ".csv", "w") as g:
            w = csv.writer(g)
            w.writerows(lr2_score)
        with open("bpitool/score_data/" + players_dir + "_pname.csv", "w") as h:
            ww = csv.writer(h)
            w.writerows(pname)