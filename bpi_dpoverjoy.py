import json
from .html_write import html_write
from .data_stopped import make_data

def dpoj_bpi(n):
    with open("bpitool/score_data/songs_dpoverjoy.json", "r") as f:
        songs_data = json.load(f)
    with open("bpitool/score_data/playerdata_dpoverjoy.json", "r") as f:
        player_data = json.load(f)
    try:
        user_data = player_data[n]
        player_name = user_data.pop(-1)
    except KeyError:
        return "Error!!", "<p>指定したLR2IDが見つかりませんでした。</p>", ""
    l = ["★★" + str(i) for i in range(1, 13)]
    l.append("★★ω")
    rd, labels, each_num, songs_data, sougou = make_data(13, user_data, songs_data, "dpoj")
    html_string = html_write(l, rd, labels, each_num, songs_data, "oj")
    
    return sougou, html_string, player_name
