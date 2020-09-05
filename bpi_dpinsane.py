import json
from .culc_bpi import BPI_calc, sougou_BPI
from .html_write import html_write
from .data_stopped import make_data

def dpex_bpi(n):
    with open("bpitool/score_data/songs_dpinsane.json", "r") as f:
        songs_data = json.load(f)
    with open("bpitool/score_data/playerdata_dpinsane.json", "r") as f:
        player_data = json.load(f)
    try:
        user_data = player_data[n]
        player_name = user_data.pop(-1)
    except KeyError:
        return "Error!!", "<p>指定したLR2IDが見つかりませんでした。</p>", ""
    l = ["★" + str(i) for i in range(1, 14)]
    l.append("★？")
    rd, labels, each_num, songs_data, sougou = make_data(14, user_data, songs_data, "dpex")
    html_string = html_write(l, rd, labels, each_num, songs_data, "ex")
    
    return sougou, html_string, player_name
