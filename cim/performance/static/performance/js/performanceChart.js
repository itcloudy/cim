$(function(){
    var performanceChart = $("#performance-trend-chart");
    //设置div显示区域的高度，宽度系统指定
    if (performanceChart != undefined){
        performanceChart.height(function(){
            return performanceChart[0].clientWidth/2;
        });
    }
    var performanceChart = $("#performanceDetailChart");
    //设置div显示区域的高度，宽度系统指定
    if (performanceChart != undefined){
        performanceChart.height(function(){
            return performanceChart[0].clientWidth/2;
        });
    }



});

//绘制绩效得分趋势图
var showPerformanceTrendChart = function(idObj){
    var structrue_data = [];
    var legend_data = [];
    var xAxis_data = [];
    var yAxis_right_data = [];
    var yAxis_left_data = [];
    var series = [];

    $.post('/performance/echart/',{'style':'trend'},function(json_data){
        if (json_data.code =='200'){
            legend_data = json_data.legend_data || [];
            xAxis_data = json_data.xAxis_data || [];
            yAxis_left_data = json_data.yAxis_left_data || [];
            series = json_data.series || [];
            series[0]['itemStyle'] = { normal: {label : {show: true}}};

            renderChart();
        }
    });
    var renderChart = function(){
        var performanceTrendChart = echarts.init(idObj);
        performanceTrendChart.setOption({
            tooltip : {
                trigger: 'axis'
            },
            legend: {
                data:legend_data
            },
            toolbox: {
                show : true,
                orient:'vertical',
                x:'right',
                y:'center',
                feature : {
                    mark : {show: true},
                    dataView : {show: true, readOnly: false},
                    magicType : {show: true, type: ['line', 'bar', 'stack', 'tiled']},
                    restore : {show: true},
                    saveAsImage : {show: true}
                }
            },
            itemStyle : { normal: {label : {show: true}}},
            calculable : true,
            xAxis : [
                {
                    type : 'category',

                    data : xAxis_data
                }
            ],
            yAxis : [
                {
                    type : 'value',
                    boundaryGap:[0,10],
                    max:10,
                    name : '分数',
                    data:yAxis_left_data,
                },

            ],
            series : series
        });
    }
}
//绩效考核详情
var showPerformanceDetailChart = function(idObj){
    $.post('/performance/echart/',{'style':'detail'},function(json_data){
        if (json_data.code =='200'){

            renderChart();
        }
    });
    var renderChart = function(){
        var performanceDetailChart = echarts.init(idObj);
        performanceDetailChart.setOption({
            tooltip : {
                trigger: 'axis'
            },
            legend: {
                data:['邮件营销','联盟广告','视频广告','直接访问','搜索引擎']
            },
            toolbox: {
                show : true,
                feature : {
                    mark : {show: true},
                    dataView : {show: true, readOnly: false},
                    magicType : {show: true, type: ['line', 'bar', 'stack', 'tiled']},
                    restore : {show: true},
                    saveAsImage : {show: true}
                }
            },
            calculable : true,
            xAxis : [
                {
                    type : 'category',
                    boundaryGap : false,
                    data : ['周一','周二','周三','周四','周五','周六','周日']
                }
            ],
            yAxis : [
                {
                    type : 'value'
                }
            ],
            series : [
                {
                    name:'邮件营销',
                    type:'line',
                    stack: '总量',
                    data:[120, 132, 101, 134, 90, 230, 210]
                },
                {
                    name:'联盟广告',
                    type:'line',
                    stack: '总量',
                    data:[220, 182, 191, 234, 290, 330, 310]
                },
                {
                    name:'视频广告',
                    type:'line',
                    stack: '总量',
                    data:[150, 232, 201, 154, 190, 330, 410]
                },
                {
                    name:'直接访问',
                    type:'line',
                    stack: '总量',
                    data:[320, 332, 301, 334, 390, 330, 320]
                },
                {
                    name:'搜索引擎',
                    type:'line',
                    stack: '总量',
                    data:[820, 932, 901, 934, 1290, 1330, 1320]
                }
            ]
        });
    }
}
//绘制所有的图
$(".echarts-drow").each(function(){
    var showId = $(this).attr('id');
    switch(showId){
        case 'performance-trend-chart':
            showPerformanceTrendChart(document.getElementById(showId));
            break;
        case 'performanceDetailChart':
            showPerformanceDetailChart(document.getElementById(showId));
            break;
    }
});