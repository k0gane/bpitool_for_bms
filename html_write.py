def html_write(l, rd, labels, each_num, data, diftable):
    html_string = '''
                <div class="Rate_chart" style="display:inline-block;">
                    <canvas id="score_rate" width="720" height="300"></canvas>
                </div>
                <div class="BPI_chart" style="display:inline-block;">
                    <canvas id="canvas" width="720" height="300"></canvas>
                </div>
                <script>
                var ctx_sr = document.getElementById("score_rate");
                var ctx = document.getElementById("canvas");
                var data_sr = {
                '''
    html_string += "labels: " + str(l) + ",\n"
    html_string += '''
                datasets:[
                        {
                            label:"AAA",
                        '''
    html_string += "\t\t\t\t\t\t\t\tdata: " + str(rd[0]) + ",\n"
    html_string +=  '''
                            backgroundColor: "#ff8484",
                        },
                        {
                            label:"AA",
                        '''
    html_string += "\t\t\t\t\t\t\t\tdata: " + str(rd[1]) + ",\n"
    html_string +=  '''
                            backgroundColor: "#ffc184",
                        },
                        {
                            label:"A",
                        '''
    html_string += "\t\t\t\t\t\t\t\tdata: " + str(rd[2]) + ",\n"
    html_string +=  '''
                            backgroundColor: "#ffff84",
                        },
                        {
                            label:"B",
                        '''
    html_string += "\t\t\t\t\t\t\t\tdata: " + str(rd[3]) + ",\n"
    html_string +=  '''
                            backgroundColor: "#84ff84",
                        },
                        {
                            label:"C",
                        '''
    html_string += "\t\t\t\t\t\t\t\tdata: " + str(rd[4]) + ",\n"
    html_string +=  '''
                            backgroundColor: "#84ffff",
                        },
                        {
                            label:"D",
                        '''
    html_string += "\t\t\t\t\t\t\t\tdata: " + str(rd[5]) + ",\n"
    html_string +=  '''
                            backgroundColor: "#84c1ff",
                        },
                        {
                            label:"E",
                        '''
    html_string += "\t\t\t\t\t\t\t\tdata: " + str(rd[6]) + ",\n"
    html_string +=  '''
                            backgroundColor: "#8484ff",
                        },
                        {
                            label:"F",
                        '''
    html_string += "\t\t\t\t\t\t\t\tdata: " + str(rd[7]) + ",\n"
    html_string +=  '''
                            backgroundColor: "#c184ff",
                        },
                        {
                            label:"No play",
                        '''
    html_string += "\t\t\t\t\t\t\t\tdata: " + str(rd[8]) + ",\n"
    html_string +=  '''
                            backgroundColor: "#cccccc",
                        },
                    ]
                };
                var option_sr =  {
                    plugins: {
                        stacked100: {enable: true}
                    },
                    responsive: false,
                    scales: {
                        yAxes: [{
                            stacked: true,
                        }],
                        xAxes:[{
                            stacked: true,
                        }]
                    }
                };
                var rate_chart = new Chart(ctx_sr, {
                    type: "horizontalBar",
                    data: data_sr,
                    options: option_sr
                });
                var data = {
                '''
    html_string += "labels:" + str(labels) + ",\n"
    html_string += "datasets:[{\n\t\t\t\tdata: " + str(each_num) + ",\n"
    html_string += "\t\t\t\tbackgroundColor: '#98fb98',\n"
    html_string += "\t\t\t\tlabel: '曲数'\n"
    html_string += '''
                        }]
                    };
                    var options =  {
                        responsive: false,
                        scales: {
                            yAxes: [{
                                ticks:{ min:0
                                }
                            }],
                            xAxes:[{
                                ticks:{ min:0
                                }
                            }]
                        }
                    };
                    var BPI_charts = new Chart(ctx, {
                        type: 'horizontalBar',
                        data: data,
                        options: options
                });
                </script>
                <div id="tabulator-chart"></div>
                <script type="text/javascript">
                    var userdata = [\n
    '''
    if(diftable == "ex"):
        for song in data:
            data[song]["link"] = "<a href='http://www.dream-pro.info/~lavalse/LR2IR/search.cgi?mode=ranking&bmsmd5=" + data[song]["md5"] + "'>" + data[song]["title"] + "</a>"
            html_string += "\t\t\t\t" + str(data[song]) + ",\n"
    else:
        for song in data:
            data[song]["link"] = "<a href='http://www.dream-pro.info/~lavalse/LR2IR/search.cgi?mode=ranking&bmsmd5=" + song + "'>" + data[song]["title"] + "</a>"
            html_string += "\t\t\t\t" + str(data[song]) + ",\n"

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
    if diftable == "sl" or diftable == "dpsl":
        html_string +=  '{title:"sl", field:"grade", headerFilter:true, headerSort:true, width:"3%", align:"center", sorter:"number"},\n'
    elif diftable == "st":
        html_string +=  '{title:"st", field:"grade", headerFilter:true, headerSort:true, width:"3%", align:"center", sorter:"number"},\n'
    elif diftable == "ex":
        html_string +=  '{title:"★", field:"grade", headerFilter:true, headerSort:true, width:"3%", align:"center", sorter:"number"},\n'
    elif diftable == "oj":
        html_string +=  '{title:"★★", field:"grade", headerFilter:true, headerSort:true, width:"3%", align:"center", sorter:"number"},\n'
    html_string +=  '''
                    {title:"Name",formatter:"html",field:"link", headerFilter:true, width:"27%", align:"center"},
                    {title:"Rank", field:"rank", width:"10%", headerSort:true, align:"center", sorter:"number"},
                    {title:"score", field:"score", width:"10%", headerSort:true, align:"center", sorter:"number"},
                    {title:"score rate", field:"rate", headerFilter:true, headerFilterPlaceholder:"Limit Rate", headerFilterFunc:"<=", width:"10%", headerSort:true, align:"center"},
                    {title:"最小BP", field:"minBP", headerFilter:true, headerFilterPlaceholder:"Max BP", headerFilterFunc:"<=",  width:"5%", headerSort:true, align:"center", sorter:"number"},
                    {title:"BPI", field:"bpi", width:"10%", headerFilter:true, headerFilterPlaceholder:"Max BPI", headerFilterFunc:"<=", headerSort:true, align:"center", sorter:"number"},
                    {title:"BPI graph", field:"bpi", headerSort:false, formatter:"progress", width:"20%"},
                    {title:"target", field:"diff", headerFilter:true, headerFilterPlaceholder:"Max dif", headerFilterFunc:"<=", width:"5%", headerSort:true, align:"center",sorter:"number"},
                    ],
                });
            </script>
    '''
    return html_string