from django.shortcuts import render
from django.http import HttpResponse
from .forms import LR2IDForm
from .bpi_exec import ex_bpi
from .bpi_overjoy import oj_bpi
from .bpi_stella import st_bpi
from .bpi_satellite import sl_bpi
from .bpi_dpinsane import dpex_bpi
from .bpi_dpsatellite import dpsl_bpi
from .bpi_dpoverjoy import dpoj_bpi
from .make_data import make_data
from .culc_bpi import BPI_calc, sougou_BPI, culc_stob
import os
import json
# Create your views here.

def insane_table(request):
    return render(request, 'bpitool/insane_table.html')

def satellite_table(request):
    return render(request, 'bpitool/satellite_table.html')

def stella_table(request):
    return render(request, 'bpitool/stella_table.html')

def song_information(request, table, song_id):
    song_id = song_id
    song_table = table
    if(song_table == "ex"):
        with open("bpitool/score_data/songs_insane.json", "r") as f:
            data = json.load(f)
    elif(song_table == "st"):
        with open("bpitool/score_data/songs_stella.json", "r") as f:
            data = json.load(f)    
    elif(song_table == "sl"):
        with open("bpitool/score_data/songs_satellite.json", "r") as f:
            data = json.load(f)
    elif(song_table == "oj"):
        with open("bpitool/score_data/songs_overjoy.json", "r") as f:
            data = json.load(f)
    elif(song_table == "dpex"):
        with open("bpitool/score_data/songs_dpinsane.json", "r") as f:
            data = json.load(f)    
    elif(song_table == "dpsl"):
        with open("bpitool/score_data/songs_dpsatellite.json", "r") as f:
            data = json.load(f)
    elif(song_table == "dpoj"):
        with open("bpitool/score_data/songs_dpoverjoy.json", "r") as f:
            data = json.load(f)
    song = data[song_id]
    kijyun = [90, 80, 70, 60, 50, 40, 30, 20, 10]
    score = [song['zenichi']]
    for i in range(9):
        score.append(culc_stob(song['zenichi'], song['average'], song['p'], song['max_score'], kijyun[i]))
    score.append(int(song['average'])+1)
    song_data = {
        'title':song['title'],
        'grade':song['grade'],
        'max_score':song['max_score'],
        'players':song['players'],
        'p':song['p'],
        'score':score
    }
    if(len(song_id) < 10):#ex
        song_data['md5'] = song['md5']
    else:
        song_data['md5'] = song_id   
    return render(request, 'bpitool/song_information.html', song_data)

def satellite_score(request):
    my_dict = {}
    my_dict['html_string'] = make_data("songs_satellite")
    print(my_dict['html_string'])
    return render(request, 'bpitool/satellite_score.html', my_dict)

def stella_score(request):
    my_dict = {}
    my_dict['html_string'] = make_data("songs_stella")
    return render(request, 'bpitool/stella_score.html', my_dict)

def insane_score(request):
    my_dict = {}
    my_dict['html_string'] = make_data("songs_insane")
    return render(request, 'bpitool/insane_score.html', my_dict)

def dpsl_score(request):
    my_dict = {}
    my_dict['html_string'] = make_data("songs_dpsatellite")
    return render(request, 'bpitool/dpsl_score.html', my_dict)

def dpoj_score(request):
    my_dict = {}
    my_dict['html_string'] = make_data("songs_dpoverjoy")
    return render(request, 'bpitool/dpoj_score.html', my_dict)

def overjoy_score(request):
    my_dict = {}
    my_dict['html_string'] = make_data("songs_overjoy")
    return render(request, 'bpitool/overjoy_score.html', my_dict)

def dpex_score(request):
    my_dict = {}
    my_dict['html_string'] = make_data("songs_dpinsane")
    return render(request, 'bpitool/dpex_score.html', my_dict)

def index(request):
    my_dict = {
        'input_lr2id':'あなたのLR2 IDを入力してください。(IDが5桁以下の方は頭に0を入れないでください)',
        'caution':'発狂BMSのデータはStairway、Stella, Satelliteのデータはstellabms.xyzから引用しています。',
        'time':'Stairwayとstella,satellite、その他で読み込み時間に差があります。ご了承下さい。',
        'form':LR2IDForm(),
        'chart':'',
        'insert_forms':'',
        'sougou_bpi':'',
        'html_string':'', 
        'player_name':''
    }
    if(request.method == 'POST'):
        if "sp_insane" in request.POST['table']:
            curl_data = ex_bpi(request.POST['lr2id'])
            my_dict['chart'] = 'SP 発狂BMS'
        elif "sp_overjoy" in request.POST['table']:
            curl_data = oj_bpi(request.POST['lr2id'])
            my_dict['chart'] = 'SP overjoy'
        elif "sp_stella" in request.POST['table']:
            curl_data = st_bpi(request.POST['lr2id'])
            my_dict['chart'] = 'SP Stella'
        elif "sp_satellite" in request.POST['table']:
            curl_data = sl_bpi(request.POST['lr2id'])
            my_dict['chart'] = 'SP Satellite'
        elif "dp_insane" in request.POST['table']:
            curl_data = dpex_bpi(request.POST['lr2id'])
            my_dict['chart'] = 'DP 発狂BMS' 
        elif "dp_overjoy" in request.POST['table']:
            curl_data = dpoj_bpi(request.POST['lr2id'])
            my_dict['chart'] = 'DP overjoy'    
        elif "dp_satellite" in request.POST['table']:
            curl_data = dpsl_bpi(request.POST['lr2id'])
            my_dict['chart'] = 'DP Satellite'
        sougou_bpi = curl_data[0]
        html_string = curl_data[1]
        my_dict['insert_forms'] = "LR2ID:" + request.POST['lr2id'] 
        my_dict['sougou_bpi'] = "総合BPI:" + str(sougou_bpi)
        my_dict['html_string'] = html_string
        my_dict['caution'] = ''
        my_dict['time'] = ''
        my_dict['player_name'] = curl_data[2]
    return render(request, 'bpitool/index.html', my_dict)

