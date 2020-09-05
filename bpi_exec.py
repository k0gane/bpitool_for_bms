import json
from bs4 import BeautifulSoup
import sys
import urllib.request
from .culc_bpi import BPI_calc, sougou_BPI, culc_stob
from .html_write import html_write

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

def ex_bpi(n):
    url_stairway = "http://stairway.sakura.ne.jp/bms/LunaticRave2/?contents=player&page="
    link_lr2mypage = "http://www.dream-pro.info/~lavalse/LR2IR/search.cgi?mode=mypage&playerid=" + str(n)
    with open("bpitool/score_data/songs_insane.json", "r") as f:
        songs_data = json.load(f)

    url = url_stairway + str(n)
    tag_html = urllib.request.urlopen(url).read().decode('shift_JIS', 'ignore')
    tag_soup = BeautifulSoup(tag_html, "html.parser")
    try:
        song_table=str(tag_soup.findAll("table")[5]).split("\n")
    except IndexError:
        return "Error!!", "<p>指定したLR2IDが見つかりませんでした。</p>", ""
    clear_table = song_table[5].split('>')[2:]
    clear_number = []

    for i in range(0, len(clear_table)-2, 2):
        clear_number.append(clear_table[i].split('<')[0])


    score_table= song_table[-5].split('>')[2:]
    score_number = []

    for i in range(0, len(score_table)-2, 2):
        score_number.append(score_table[i].split('<')[0])
    my_data = {}

    tag_html = urllib.request.urlopen(link_lr2mypage).read().decode('shift_JIS', 'ignore')
    tag_soup = BeautifulSoup(tag_html, "html.parser")
    status_table=str(tag_soup.findAll("table")[0]).split("\n")
    player_name = status_table[1].split('>')[4].split('<')[0]

    url = url_stairway + str(n)
    tag_html = urllib.request.urlopen(url).read().decode('shift_JIS', 'ignore')
    tag_soup = BeautifulSoup(tag_html, "html.parser")
    song_table=str(tag_soup.findAll("table")[5]).split("\n")
    clear_table = song_table[5].split('>')[2:]
    clear_number = []

    for i in range(0, len(clear_table)-2, 2):
        clear_number.append(clear_table[i].split('<')[0])


    score_table= song_table[-5].split('>')[2:]
    score_number = []

    for i in range(0, len(score_table)-2, 2):
        score_number.append(score_table[i].split('<')[0])
    my_data = {}

    tag_html = urllib.request.urlopen(link_lr2mypage).read().decode('shift_JIS', 'ignore')
    tag_soup = BeautifulSoup(tag_html, "html.parser")
    status_table=str(tag_soup.findAll("table")[0]).split("\n")
    player_name = status_table[1].split('>')[4].split('<')[0]
    scorerate_data = [[] for _ in range(26)]#難易度の数

    for i in range(1, 1036):
        song_id = i
        au = song_table[14 * i + 4].split('>')[2].split('<')[0] #タイトル
        if(au in stairway_word):
            au = lr2_word[stairway_word.index(au)]
        try:
            my_score = int(song_table[14 * i + 7].split('>')[1].strip('</td')) #スコア
            rank = int(song_table[14 * i + 6].split('>')[1].strip('</td')) #順位
            rate = float(song_table[14 * i + 8].split('>')[1].strip('</td'))
            bp = int(song_table[14 * i + 10].split('>')[1].strip('</td'))
        except ValueError:
            my_score = ''
            rank = ''
            rate = ''
            bp = ''
        my_data[str(song_id)] = {"title":au, "score":my_score, "rank":rank, "score_rate":rate, "miss_count":bp}
    BPI_list = []
    data = {}
    for i in range(1, 1036):
        data[i] = {'grade':songs_data[str(i)]['grade'], 
                'title':my_data[str(i)]['title'],
                'max_score':songs_data[str(i)]['max_score'],
                'zenichi':songs_data[str(i)]['zenichi'],
                'average':songs_data[str(i)]['average'],
                'score':my_data[str(i)]['score'],
                'rate':my_data[str(i)]['score_rate'],
                'rank':my_data[str(i)]['rank'],
                'minBP':my_data[str(i)]['miss_count'],
                'p':songs_data[str(i)]['p'],
                'player':songs_data[str(i)]['players'],
                'md5':songs_data[str(i)]['md5']
                }
        try:
            bpi = round(max(BPI_calc(data[i]['score'], data[i]['average'], data[i]['zenichi'], data[i]['max_score'], data[i]['p']),-15), 2)
            BPI_list.append(bpi)
            data[i]['bpi'] = bpi
            if int(data[i]['grade']) == 99:
                scorerate_data[25].append(data[i]['rate'])
            else:
                scorerate_data[int(data[i]['grade'])-1].append(data[i]['rate'])
        except (ValueError, TypeError):
            BPI_list.append(-20)
            if int(data[i]['grade']) == 99:
                scorerate_data[25].append(0)
            else:
                scorerate_data[int(data[i]['grade'])-1].append(0)
    sougou = round(sougou_BPI(BPI_list), 2)
    for i in range(1, 1036):
        try:
            data[i]['diff'] = culc_stob(data[i]['zenichi'], data[i]['average'], data[i]['p'], data[i]['max_score'], sougou) - data[i]['score']
        except (TypeError, ValueError):
            data[i]['diff'] = ''
    BPI_number = len(BPI_list)
    if(BPI_number >= 5):
        BPI_sorted = sorted(BPI_list)
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
        rank_data = [[0 for _ in range(9)] for _ in range(26)]
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
        l = ["★" + str(i) for i in range(1, 26)]
        l.append("★99")
        rd = [[0 for _ in range(26)] for _ in range(9)]
        for j in range(9):
            for k in range(26):
                rd[j][k] = rank_data[k][j]
        html_string = html_write(l, rd, labels, each_num, data, "ex")

    return sougou, html_string, player_name


