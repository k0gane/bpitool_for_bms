import json
import requests
from .culc_bpi import BPI_calc, sougou_BPI, culc_stob
from .html_write import html_write

def sl_bpi(n):
    with open("bpitool/score_data/songs_satellite.json", "r") as f:
        sl_data = json.load(f)
    url = "https://stellabms.xyz/api/user/" + str(n)
    r = requests.post(url)
    json_data = json.loads(r.text)
    if(json_data['success']):
        scorerate_data = [[] for _ in range(13)]
        player_name = json_data['nickname']
        #dani_sp = json_data['dan']	

        sl_scoredata = json_data["stairway2"]

        BPI_data = []
       
        for song in sl_scoredata:
            song_md5 = song['md5']
            try:
                sl_data[song_md5]['score'] = song['score']
                sl_data[song_md5]['rank'] = song['rank']
                sl_data[song_md5]['minBP'] = song['minbp']
                sl_data[song_md5]['rate'] = round(float(song['percent']), 2)
                sl_data[song_md5]['bpi'] = round(BPI_calc(sl_data[song_md5]['score'], sl_data[song_md5]['average'], sl_data[song_md5]['zenichi'], sl_data[song_md5]['max_score'], sl_data[song_md5]['p']), 2)
                BPI_data.append(sl_data[song_md5]['bpi'])
                scorerate_data[sl_data[song_md5]['grade']].append(sl_data[song_md5]['rate'])
            except KeyError:
                continue
        sougou = round(sougou_BPI(BPI_data), 2)
        if(sougou == -20):
            return "Error!!", "<p>指定したLR2IDが見つかりませんでした。</p>", ""
        for song in sl_data:
            try:
                sl_data[song]['diff'] = culc_stob(sl_data[song]['zenichi'], sl_data[song]['average'], sl_data[song]['p'], sl_data[song]['max_score'], sougou) - sl_data[song]['score']
            except KeyError:
                sl_data[song]['score'] = ''
                sl_data[song]['rank'] = ''
                sl_data[song]['minBP'] = ''
                sl_data[song]['rate'] = ''
                sl_data[song]['bpi'] = ''
                sl_data[song]['diff'] = ''
                scorerate_data[sl_data[song]['grade']].append(0)
        #グラフや表パート
        BPI_number = len(BPI_data)
        if(BPI_number >= 5):
            BPI_sorted = sorted(BPI_data)
            q1 = BPI_number // 5
            q4 = int(BPI_number * 0.8)
            q1_atai = int(BPI_sorted[q1-1])
            q4_atai = int(BPI_sorted[q4-1])
            q2_atai = (q4_atai-q1_atai) // 3 + q1_atai
            q3_atai = int((q4_atai-q1_atai) * 0.67) + q1_atai
            labels = ["〜" + str(q1_atai), str(q1_atai) + "〜" + str(q2_atai), str(q2_atai) + "〜" + str(q3_atai),
                    str(q3_atai) + "〜" + str(q4_atai), str(q4_atai) + "〜"]
            each_num = [0 for _ in range(5)]
            for b in range(BPI_number):
                if(BPI_sorted[b] < q1_atai):
                    each_num[0] += 1
                elif(q1_atai <= BPI_sorted[b] < q2_atai):
                    each_num[1] += 1
                elif(q2_atai <= BPI_sorted[b] < q3_atai):
                    each_num[2] += 1
                elif(q3_atai <= BPI_sorted[b] < q4_atai):
                    each_num[3] += 1
                else:
                    each_num[4] += 1
        rank_data = [[0 for _ in range(9)] for _ in range(13)]
        l = -1
        for grade in scorerate_data:
            l += 1
            for score in grade:
                if(score == 0):
                    rank_data[l][8] += 1
                elif(0 < score <= 22.22):
                    rank_data[l][7] += 1
                elif(22.22 < score <= 33.33):
                    rank_data[l][6] += 1
                elif(33.33 < score <= 44.44):
                    rank_data[l][5] += 1
                elif(44.44 < score <= 55.55):
                    rank_data[l][4] += 1
                elif(55.55 < score <= 66.66):
                    rank_data[l][3] += 1
                elif(66.66 < score <= 77.77):
                    rank_data[l][2] += 1
                elif(77.77 < score <= 88.88):
                    rank_data[l][1] += 1
                else:
                    rank_data[l][0] += 1   
        l = ["sl" + str(i) for i in range(13)]
        rd = [[0 for _ in range(13)] for _ in range(9)]
        for j in range(9):
            for k in range(13):
                rd[j][k] = rank_data[k][j]
        html_string = html_write(l, rd, labels, each_num, sl_data, "sl")

        return sougou, html_string, player_name
    else:
        return "Error!!", "<p>指定したLR2IDが見つかりませんでした。</p>", ""
