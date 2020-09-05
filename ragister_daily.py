import ragister_multi
import datetime



dpoj_url = "http://ereter.net/static/analyzer/json/overjoy.json"
ragister_multi.make_chart(dpoj_url, "songs_dpoverjoy", "playerdata_dpoverjoy", 0)
dpoj_now = datetime.datetime.now()


dpex_url = "http://dpbmsdelta.web.fc2.com/table/data/insane_data.json"
ragister_multi.make_chart(dpex_url, "songs_dpinsane", "playerdata_dpinsane", 0)
dpex_now = datetime.datetime.now()


dpsl_url = "https://stellabms.xyz/dp/score.json"
ragister_multi.make_chart(dpsl_url, "songs_dpsatellite", "playerdata_dpsatellite", 0)
dpsl_now = datetime.datetime.now()

st_url = "https://stellabms.xyz/st/score.json"
ragister_multi.make_chart(st_url, "songs_stella", "playerdata_stella", 0)
st_now = datetime.datetime.now()


sl_url = "https://stellabms.xyz/sl/score.json"
ragister_multi.make_chart(sl_url, "songs_satellite", "playerdata_satellite", 40)
sl_now = datetime.datetime.now()


oj_url = "http://www.ribbit.xyz/bms/tables/overjoy2nd_body.json"
ragister_multi.make_chart(oj_url, "songs_overjoy", "playerdata_overjoy", 0)
oj_now = datetime.datetime.now()


with open("bpitool/scoredata/last_update.txt", "w") as f:
    f.write("Last update time\n")
    f.write("DP Overjoy: " + str(dpoj_now) + "\n")
    f.write("DP Insane: " + str(dpex_now) + "\n")
    f.write("DP Satellite: " + str(dpsl_now) + "\n")
    f.write("SP Stella: " + str(st_now) + "\n")
    f.write("SP Satellite: " + str(sl_now) + "\n")
    f.write("SP overjoy: " + str(oj_now) + "\n")
