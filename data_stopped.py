import json
from .culc_bpi import BPI_calc, sougou_BPI, culc_stob

def make_data(dif_num, user_data, songs_data, chart):
    scorerate_data = [[] for _ in range(dif_num)]#難易度の数
    my_data = {}
    for i in range(len(user_data)):
        au = user_data[i][0] #タイトル
        md5 = user_data[i][1]
        my_score = user_data[i][2] #スコア
        if(my_score == 0):
            my_score = ''
            rank = ''
            rate = ''
            bp = ''
        else:
            rank = user_data[i][3] #順位
            rate = round((100 * my_score / songs_data[md5]['max_score']), 2)
            bp = user_data[i][4]
        my_data[md5] = [my_score, rank, rate , bp, au]
    BPI_data = []
    for song in songs_data:
        try:
            songs_data[song]['score'] = my_data[song][0]
            songs_data[song]['rank'] = my_data[song][1]
            songs_data[song]['minBP'] = my_data[song][3]
            songs_data[song]['rate'] = my_data[song][2]
            songs_data[song]['bpi'] = round(BPI_calc(songs_data[song]['score'], songs_data[song]['average'], songs_data[song]['zenichi'], songs_data[song]['max_score'], songs_data[song]['p']), 2)
            BPI_data.append(songs_data[song]['bpi'])
            if(songs_data[song]['grade'] == 99):
                scorerate_data[-1].append(songs_data[song]['rate'])
            elif(chart == "oj" or chart == "sl" or chart == "st"):#0スタート
                scorerate_data[songs_data[song]['grade']].append(songs_data[song]['rate'])
            else:
                scorerate_data[songs_data[song]['grade']-1].append(songs_data[song]['rate'])
        except (KeyError, TypeError):
            songs_data[song]['score'] = ''
            songs_data[song]['rank'] = ''
            songs_data[song]['minBP'] = ''
            songs_data[song]['rate'] = ''
            songs_data[song]['bpi'] = ''
            if(songs_data[song]['grade'] == 99):
                scorerate_data[-1].append(0)
            else:
                scorerate_data[songs_data[song]['grade']-1].append(0)
    
    sougou = round(sougou_BPI(BPI_data), 2)
    for song in songs_data:
        try:
            songs_data[song]['diff'] = culc_stob(songs_data[song]['zenichi'], songs_data[song]['average'], songs_data[song]['p'], songs_data[song]['max_score'], sougou) - songs_data[song]['score']
        except (KeyError, TypeError):
            songs_data[song]['diff'] = ''
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
        rank_data = [[0 for _ in range(9)] for _ in range(dif_num)]
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
        rd = [[0 for _ in range(dif_num)] for _ in range(9)]
        for j in range(9):
            for k in range(dif_num):
                rd[j][k] = rank_data[k][j]
    return rd, labels, each_num, songs_data, sougou