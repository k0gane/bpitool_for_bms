import json
from .html_write import html_write
from .data_stopped import make_data

def sl2_bpi(n):
    with open("bpitool/score_data/songs_satellite.json", "r") as f:
        songs_data = json.load(f)
    with open("bpitool/score_data/playerdata_satellite.json", "r") as f:
        player_data = json.load(f)
    try:
        user_data = player_data[n]
        player_name = user_data.pop(-1)
    except KeyError:
        return "Error!!", "<p>指定したLR2IDが見つかりませんでした。</p>", ""
    l = ["sl" + str(i) for i in range(13)]
    rd, labels, each_num, songs_data, sougou = make_data(13, user_data, songs_data)
    html_string = html_write(l, rd, labels, each_num, songs_data, "sl")
    return sougou, html_string, player_name