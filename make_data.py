import json
import math


def culc_stob(zenichi, average, p, mscore, BPI):
    a = (BPI/100)**(1/p)
    try:
        z = mscore/(2 * (mscore-zenichi))
    except ZeroDivisionError:
        z = mscore
    k = mscore / (2 * (mscore - average))
    zz = math.log(z / k) * a
    u = k * math.exp(zz)
    return int((2*mscore*u- mscore)/(2 * u))


def culc_measurescore(zenichi, average, p, mscore):
    kijyun = [90, 80, 70, 60, 50, 40, 30, 20, 10]
    return [culc_stob(zenichi, average, p, mscore, i) for i in kijyun]


def make_data(json_name):
    html_string = '''
                <div id="tabulator-chart"></div>
                <script type="text/javascript">
                    var userdata = [\n
                '''

    with open("bpitool/score_data/" + json_name + ".json", "r") as f:
        data = json.load(f)

        for bm5 in data:
            songs_data = data[bm5]
            try:
                if(json_name == "songs_satellite"):
                    songs_data['link'] = "<a href=" + 'song_information/sl/' + bm5  + '>' + songs_data["title"] + "</a>"
                elif(json_name == "songs_stella"):
                    songs_data['link'] = "<a href=" + 'song_information/st/' + bm5  + '>' + songs_data["title"] + "</a>"
                elif(json_name == "songs_dpsatellite"):
                    songs_data['link'] = "<a href=" + 'song_information/dpsl/' + bm5  + '>' + songs_data["title"] + "</a>"
                elif(json_name == "songs_overjoy"):
                    songs_data['link'] = "<a href=" + 'song_information/oj/' + bm5  + '>' + songs_data["title"] + "</a>"
                elif(json_name == "songs_insane"):
                    songs_data['link'] = "<a href=" + 'song_information/ex/' + bm5  + '>' + songs_data["title"] + "</a>"
                elif(json_name == "songs_dpinsane"):
                    songs_data['link'] = "<a href=" + 'song_information/dpex/' + bm5  + '>' + songs_data["title"] + "</a>"
                elif(json_name == "songs_dpoverjoy"):
                    songs_data['link'] = "<a href=" + 'song_information/dpoj/' + bm5  + '>' + songs_data["title"] + "</a>"
            except OverflowError:
                print(songs_data)
                break
            html_string += "\t\t\t\t" + str(songs_data) + ",\n"
        html_string += ''']
                    var table = new Tabulator("#tabulator-chart",{
                    layout:"fitColumns",
                    data:userdata,
                    pagination:"local",
                    paginationSize:50,
                    initialSort:[
                        {column:"grade", dir:"asc"},
                    ],
                    columns:[
                '''
    if json_name == "songs_satellite" or json_name == "songs_dpsatellite":
        html_string +=  '{title:"sl", field:"grade", headerFilter:true, headerSort:true, width:"3%", align:"center", sorter:"number"},\n'
    elif json_name == "songs_stella":
        html_string +=  '{title:"st", field:"grade", headerFilter:true, headerSort:true, width:"3%", align:"center", sorter:"number"},\n'
    elif json_name == "songs_insane" or json_name == "songs_dpinsane":
        html_string +=  '{title:"★", field:"grade", headerFilter:true, headerSort:true, width:"3%", align:"center", sorter:"number"},\n'
    elif json_name == "songs_dpoverjoy" or json_name == "songs_overjoy":
        html_string +=  '{title:"★★", field:"grade", headerFilter:true, headerSort:true, width:"3%", align:"center", sorter:"number"},\n'
    html_string +=  '''
                    {title:"Name",formatter:"html",field:"link", headerFilter:true, width:"27%", align:"center"},
                ],
            });
        </script>
    '''
    return html_string
