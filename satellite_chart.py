import json
import math

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
        return max(-100*(pow(-math.log(S_dash),p))/(pow(math.log(Z_dash),p)), -15)

score = []


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

with open("bpitool/score_data/songs_satellite.json", "r") as f:
    songs_data = json.load(f)


AAA = 88.88
AAA_BPI = []
over100 = []

for song in songs_data:
    AAA_score = int(songs_data[song]['max_score'] * AAA / 100) + 1
    AAA_BPI.append(round(BPI_calc(AAA_score, songs_data[song]['average'], songs_data[song]['zenichi'], songs_data[song]['max_score'], songs_data[song]['p']), 2))


aaa = sorted(AAA_BPI)
l = len(aaa)
aaa_border = []
num = 30
num_border = l // 30
for i in range(num_border):
    aaa_border.append(aaa[30*i])
aaa_border.append(100)

for song in songs_data:
    title = songs_data[song]['title']
    md5 = songs_data[song]['md5']
    AAA_score = int(songs_data[song]['max_score'] * AAA / 100) + 1
    AAABPI = round(BPI_calc(AAA_score, songs_data[song]['average'], songs_data[song]['zenichi'], songs_data[song]['max_score'], songs_data[song]['p']), 2)
    g = 0
    if(AAABPI<100):
        while(AAABPI>=aaa_border[g]):
            g += 1
        grade = str(aaa_border[g-1]) + "..." + str(round(aaa_border[g]-0.01, 2))
    else:
        grade = "100..."
    score.append({"title":title, "md5":md5, "level":grade, "AAA":AAABPI})


score_chart = sorted(score, key=lambda x:x["AAA"])

with open("bpitool/static/json/sl_sc.json", "w") as f:
    json.dump(score_chart, f, ensure_ascii=False, indent=4)
