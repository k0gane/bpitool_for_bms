from bs4 import BeautifulSoup
import math
import json
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

black_list = [114328, 111023, 122738, 108312, 141249, 114453, 111571, 113171, 113693, 140162, 71767, 144372, 159674]
BPI_per = [0.0003791, 0.0008341, 0.0018335, 0.00403067, 0.00886266, 0.01948992, 0.04286059, 0.09425297, 0.2072687]

lr2_word = ['星の器～STAR OF ANDROMEDA (ANOTHER)', 'ハルトマンの妖怪少女～VirusⅤ [ANOTHER]', 'The Ray of Sunlight <sunny>', 'JULIAN "for B.O.F. 2009" [SP-RX INSANE]',
'Little "Sister" Bitch', 'REWD "B159 mix" // (kei another7)', 'HAMMER the TANGRAM\u3000（苦しさアナザー満天の星空）', 'BRILLIANT STAR ～煌星の雫～ [WHITE ANOTHER]',
'感情の摩天楼～PandoraBox', 'ROTTELER\'S HOME "seven eduardo edit"', '死腐乃美「彼岸花」第二～空虚偽心～赤紅 [Lycoris]', 'Love & Justice [AFOTHER]', 
'エストポリス伝記II ～バトル#2～ (SP BLACK ANOTHER)', 'Angelic layer\u3000 ～Reincarnation～', 'Red-rize "B172 mix" // 7keys Afother', 'Another Sky\u3000 [7key/Ex]', 
'Atomic Bomb [㌧に捧げる譜面]', 'Cosmoscape\u3000 [kei another]', '春色小径 ～ Colorful Path -lunatic7-', '彼女の言い分 -ﾋﾟｺﾋﾟｺedit- [だって～でも]', 'Theme of "ULTIMATE IRIS" [VEGA]', 
'アズール <ANOTHER>', 'Satori ～3rd EyEs (bms edit) [ANOTHER]', 'ひつぎとふたご ～狂気ノ宴～', 'REWD "B159 mix" // (kei-transcended 7)', '少女の檻 "Last Night, Last Dancing."', 
'舞姫 ～buki～\u3000 [7key AFOTHER]', 'Candy & Baguette [SP INSANE]', 'Red-rize "B172 mix" // 7keys ManiaQ', 'Remilia ～吸血鬼の為の協奏曲 [ANOTHER]', 
'暁月～蒼い夢 夢うつつ (kuso edition)', '白山比咩神 (ANOTHER)', '先手必勝戦闘機\u3000鳳 -上昇-', 'ピアノ協奏曲第１番"蠍火"（なんでも吸い込むピンク色のための）', 
'ＤＱⅢ\u3000Battle -Normal-', 'スプラッシュコード－０６ [ANOTHER7]', '架空ユリカゴ\u3000 [SABOTHER]', 'Little "Sister" Bitch', '月時計\u3000Last・Dial (MANIAC)', 
'水晶世界 ～Fracture～ [Insane]', 'Harmony (*｡> × <｡*人) ☆ﾟ.*･｡ﾟ', '旧地獄街道を行く ～反逆のパルスィ～ [MANIAC]', '%E3%83%96%E3%83%B3%E3%82%BF%E3%83%B3 ～Falling in "B" mix～ (樹海)', 
'CHRONO TRIGGER ～世界変革の時～ [HARDEST]', '日溜りの街－あ！－ (MANIAQ)', 'gravitronicⅡ', '絵空事の世界と私\u3000 [SABOTHER]', '少女の檻 "Last Night, Last Dancing."',
'ＤＱⅢ\u3000Battle -Hyper-', '旧地獄街道を行く ～反逆のパルスィ～ [妬まスィ]', 'Love & Justice [MANIAQ]', '芥川龍之介の河童\u3000～Candid Friend [NORMAL]', 
'爆走中年 ～ENDLESS RUN～ (かっとべ♂マグナム)', '星の器～STAR OF ANDROMEDA [ALITHER]', 'REWD "B159 mix" // (kei-unmeasured 7)', 'ROTTELER\'S HOME "seven bottakuri edit"', 
'Yakumo >>JOINT STRUGGLE -隙間-', '人形裁判\u3000～ 人の形弄びし少女 -3rd stage-', '日溜りの街－あ！－ (EXTREME)', 'アズール <鬼畜>', '白山比咩神 (FOOLISH)', 
'pumpkin man [>w<]', 'スプラッシュコード－０６ [MANIAC7]', 'Whiteout [&]', 'Satori ～3rd EyEs -EXTRA-', '稲田姫様に叱られるから\u3000 (BEGINNER)', 'gravitronicⅢ', 
'U.N.Owen ～戯れしは狂妹か？～ [abolish19]', '水晶世界 ～Fracture～ [yumether]', 'Yakumo >>JOINT STRUGGLE -EXTRA-', 'ＤＱⅢ\u3000Battle -Another-', 
'稲田姫様ご乱心 <bms edit> -Lunatic7-', '英雄 ～氷の妖精のお話～ [INFELNO]', 'Love & Justice [EXTREME]', 'Skull & Witch [黒色破壊光線]', 'Little "Sister" Bitch',
'myste`re\u3000 -LAST BOSS-', 'アズール リミックス <MANIAC>', '人形裁判\u3000～ 人の形弄びし少女 -EXTRA-', '%E3%83%96%E3%83%B3%E3%82%BF%E3%83%B3 ～Falling in "B" mix～ (EXPERT)', 
'Love & Justice [GOD]', 'gravitronicⅠ -ANOTHER-']


stairway_word = ['星の器〜STAR OF ANDROMEDA (ANOTHER)', 'ハルトマンの妖怪少女〜VirusX [ANOTHER]',  'The Ray of Sunlight ', "JULIAN 'for B.O.F. 2009' [SP-RX INSANE]",
"Little 'Sister' Bitch", "REWD 'B159 mix' // (kei another7)",'HAMMER the TANGRAM （苦しさアナザー満天の星空）', 'BRILLIANT STAR 〜煌星の雫〜 [WHITE ANOTHER]', 
'感情の摩天楼〜PandoraBox', "ROTTELER'S HOME 'seven eduardo edit'",  '死腐乃美「彼岸花」第二〜空虚偽心〜赤紅 [Lycoris]','Love &amp; Justice [AFOTHER]',
'エストポリス伝記II 〜バトル#2〜 (SP BLACK ANOTHER)', 'Angelic layer  〜Reincarnation〜', "Red-rize 'B172 mix' // 7keys Afother",'Another Sky  [7key/Ex]',
'Atomic Bomb [dに捧げる譜面]', 'Cosmoscape  [kei another]',  '春色小径 〜 Colorful Path -lunatic7-', '彼女の言い分 -ﾋﾟｺﾋﾟｺedit- [だって〜でも]','Theme of ULTIMATE IRIS',
'アズール ','Satori 〜3rd EyEs (bms edit) [ANOTHER]','ひつぎとふたご 〜狂気ノ宴〜', "REWD 'B159 mix' // (kei-transcended 7)", "少女の檻 'Last Night, Last Dancing.",
'舞姫 〜buki〜  [7key AFOTHER]','Candy &amp; Baguette [SP INSANE]', "Red-rize 'B172 mix' // 7keys ManiaQ", 'Remilia 〜吸血鬼の為の協奏曲 [ANOTHER]',
'暁月〜蒼い夢 夢うつつ (kuso edition)', '白山比盗_ (ANOTHER)','先手必勝戦闘機 鳳 -上昇-',"ピアノ協奏曲第１番'蠍火'（なんでも吸い込むピンク色のための）",
'ＤＱV Battle -Normal-', 'スプラッシュコード−０６ [ANOTHER7]', '架空ユリカゴ  [SABOTHER]',"Little 'Sister' Bitch", '月時計 Last・Dial (MANIAC)',
'水晶世界 〜Fracture〜 [Insane]', 'Harmony (*｡&gt; × &lt;｡*人) ☆ﾟ.*･｡ﾟ','旧地獄街道を行く 〜反逆のパルスィ〜 [MANIAC]',"%E3%83%96%E3%83%B3%E3%82%BF%E3%83%B3 〜Falling in 'B' mix〜 (樹海)",
'CHRONO TRIGGER 〜世界変革の時〜 [HARDEST]', '日溜りの街−あ！− (MANIAQ)', 'gravitronicU', '絵空事の世界と私  [SABOTHER]', "少女の檻 'Last Night, Last Dancing.",
'ＤＱV Battle -Hyper-','旧地獄街道を行く 〜反逆のパルスィ〜 [妬まスィ]', 'Love &amp; Justice [MANIAQ]',  '芥川龍之介の河童 〜Candid Friend [NORMAL]', 
'爆走中年 〜ENDLESS RUN〜 (かっとべ♂マグナム)', '星の器〜STAR OF ANDROMEDA [ALITHER]',"REWD 'B159 mix' // (kei-unmeasured 7)", "ROTTELER'S HOME 'seven bottakuri edit'",  
'Yakumo &gt;&gt;JOINT STRUGGLE -隙間-', '人形裁判 〜 人の形弄びし少女 -3rd stage-','日溜りの街−あ！− (EXTREME)', 'アズール &lt;鬼畜&gt;','白山比盗_ (FOOLISH)',
'pumpkin man [&gt;w&lt;]', 'スプラッシュコード−０６ [MANIAC7]', 'Whiteout [&amp;]', 'Satori 〜3rd EyEs -EXTRA-', '稲田姫様に叱られるから  (BEGINNER)', 'gravitronicV',
'U.N.Owen 〜戯れしは狂妹か？〜 [abolish19]', '水晶世界 〜Fracture〜 [yumether]','Yakumo &gt;&gt;JOINT STRUGGLE -EXTRA-','ＤＱV Battle -Another-', 
'稲田姫様ご乱心 ', '英雄 〜氷の妖精のお話〜 [INFELNO]',  'Love &amp; Justice [EXTREME]','Skull &amp; Witch [黒色破壊光線]', "Little 'Sister' Bitch", 
'myste`re  -LAST BOSS-', 'アズール リミックス ', '人形裁判 〜 人の形弄びし少女 -EXTRA-',"%E3%83%96%E3%83%B3%E3%82%BF%E3%83%B3 〜Falling in 'B' mix〜 (EXPERT)",
'Love &amp; Justice [GOD]', 'gravitronicT -ANOTHER-']

with open("bpitool/score_data/insane_songdata.json", "r") as f:
    insane_data = json.load(f)

songs_data = {}
lr2_score = {}
songs_title = []
songs_md5 = []
pname = []
got_name = []

response = requests.get("http://www.ribbit.xyz/bms/tables/insane_body.json")
json_data = response.json()
si = 1

for song in json_data:
    ranking_url = "http://www.dream-pro.info/~lavalse/LR2IR/search.cgi?mode=ranking&bmsmd5=" + str(song['md5'])
    s_title = song['title']
    if(s_title in lr2_word):
        s_title = stairway_word[lr2_word.index(s_title)]
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
                player_score = int(IR[14].split('/')[0])
                score_rate = float(IR[14].split('/')[1].split('(')[1].split('%')[0])
                min_BP = int(IR[18].split("<")[0])
                if(score_rate >= 40):
                    ranking_data.append(player_score)
                    user_lank = len(ranking_data)
                elif(len(ranking_data) == 0):
                    continue
                else:
                    break
        page += 1
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
    if(song['level'] == '???'):
        song['level'] = 99      
    for i in insane_data:
        if(insane_data[i]['title'] == s_title and insane_data[i]['dif'] == int(song['level'])):
            s_id = i
    songs_data[s_id] = {"title":s_title, "grade":int(song['level']), "max_score":max_score, "zenichi":zenichi, "average":average, "p":great_p, "players":len(ranking_data), "md5":s_md5}
    print(songs_data[s_id])
    si += 1
    songs_md5.append(s_md5)
    songs_title.append(s_title)

with open("bpitool/score_data/songs_insane.json", 'w') as f:
    json.dump(songs_data, f, ensure_ascii=False, indent=4)
