$(function(){
    //限定输入的值为0~10
    $('.form-assessment-line').on('change',function(e){

        var value = e.currentTarget.value;
        value = parseFloat(value);
        if (isNaN(value) || value==undefined  || value<0){
            value = 0;
        }
        if (value>10){
            value = 10;

        }
        value = value.toFixed(1);
        e.currentTarget.value = value;
    });


});
$(".department-select").change(function(e){
    var department = $('.department-select')[0].value;
    $('.month-select')[0].value='';
    $('.name-search')[0].value='';
    $.post('/performance/result/',{'department':department,'month':'','name':''},function(data){

        if(data.code =='200'){
            var month_list = data.month_list;
            var len = month_list.length;
            var html ='<option value="">全部月份</option>';
            for(var i=0;i<len;i++){
                html += '<option value="'+month_list[i].id+'">'+month_list[i].name+'</option>'
            }
            $('.month-select')[0].innerHTML =html;
            var resultInfo = "";
            var infoHtml ='<table class="table table-hover table-condensed table-striped table-bordered"><thead><tr>';
            var table_title = data.result_data.table_title;
            var table_list = data.result_data.table_list;
            var d_len = table_list.length;
            var h_len = table_title.length;
            for(var i=0;i<h_len;i++){
                infoHtml += '<th>'+table_title[i]+'</th>';
            }
            infoHtml += '</tr> </thead> <tbody>';
            for(var i=0;i<d_len;i++){
                infoHtml += '<tr>';
                for(var j=0;j<table_list[i].length;j++){
                    infoHtml += '<td>'+table_list[i][j]+'</td>';
                }
                infoHtml += '</tr>';

            }
            infoHtml += '</tbody></table>';

            var pageHtml = '<div class="pagination"><span class="step-links">';
            if (data.result_data.previous != undefined){
                pageHtml += '<a href="/performance/result/?department='+data.result_data.department_id+'&name='+data.result_data.name+'&page='+data.result_data.previous;
                if(parseInt(data.result_data.month_id) >0){
                     pageHtml += '&month='+data.result_data.month_id
                }
                pageHtml += '">上一页</a>';
            }
            pageHtml += '<span class="current">当前页: '+data.result_data.current_page+'共'+data.result_data.all_page+'页</span>'
            if (data.result_data.next != undefined){

                pageHtml += '<a href="/performance/result/?department='+data.result_data.department_id+'&name='+data.result_data.name+'&page='+data.result_data.next;
                if(parseInt(data.result_data.month_id) >0){
                     pageHtml += '&month='+data.result_data.month_id
                }
                pageHtml += '">下一页</a>';
            }
            pageHtml += '</span></div>';
            infoHtml += pageHtml;
            $('#result-info')[0].innerHTML=infoHtml;
        }else{
            $('.month-select')[0].innerHTML ="";
            $('#result-info')[0].innerHTML ="<br/><p class='text-center'>没有符合要求的结果，请更改搜索条件</p>";
        }
    });

});
$(".month-select").change(function(e){
    var department = $('.department-select')[0].value;

    var month = $('.month-select')[0].value;
    $('.name-search')[0].value ='';
    $.post('/performance/result/',{'department':department,'month':month,'name':''},function(data){
        if(data.code =='200'){
            var month_list = data.month_list;
            var len = month_list.length;
            var resultInfo = "";
            var infoHtml ='<table class="table table-hover table-condensed table-striped table-bordered"><thead><tr>';
            var table_title = data.result_data.table_title;
            var table_list = data.result_data.table_list;
            var d_len = table_list.length;
            var h_len = table_title.length;
            for(var i=0;i<h_len;i++){
                infoHtml += '<th>'+table_title[i]+'</th>';
            }
            infoHtml += '</tr> </thead> <tbody>';
            for(var i=0;i<d_len;i++){
                infoHtml += '<tr>';
                for(var j=0;j<table_list[i].length;j++){
                    infoHtml += '<td>'+table_list[i][j]+'</td>';
                }
                infoHtml += '</tr>';

            }
            infoHtml += '</tbody></table>';

            var pageHtml = '<div class="pagination"><span class="step-links">';
            if (data.result_data.previous != undefined){
                pageHtml += '<a href="/performance/result/?department='+data.result_data.department_id+'&name='+data.result_data.name+'&page='+data.result_data.previous;
                if(parseInt(data.result_data.month_id) >0){
                     pageHtml += '&month='+data.result_data.month_id
                }
                pageHtml += '">上一页</a>';
            }
            pageHtml += '<span class="current">当前页: '+data.result_data.current_page+'共'+data.result_data.all_page+'页</span>'
            if (data.result_data.next != undefined){

                pageHtml += '<a href="/performance/result/?department='+data.result_data.department_id+'&name='+data.result_data.name+'&page='+data.result_data.next;
                if(parseInt(data.result_data.month_id) >0){
                     pageHtml += '&month='+data.result_data.month_id
                }
                pageHtml += '">下一页</a>';
            }
            pageHtml += '</span></div>';
            infoHtml += pageHtml;
            $('#result-info')[0].innerHTML=infoHtml;
        }else{

            $('#result-info')[0].innerHTML ="<br/><p class='text-center'>没有符合要求的结果，请更改搜索条件</p>";
        }
    });

});
$(".name-search").change(function(e){
    var department = $('.department-select')[0].value;
    var month = $('.month-select')[0].value;
    var name = $('.name-search')[0].value;
    $.post('/performance/result/',{'department':department,month:month,'name':name},function(data){
        if(data.code =='200'){
            var month_list = data.month_list;
            var len = month_list.length;

            var resultInfo = "";
            var infoHtml ='<table class="table table-hover table-condensed table-striped table-bordered"><thead><tr>';
            var table_title = data.result_data.table_title;
            var table_list = data.result_data.table_list;
            var d_len = table_list.length;
            var h_len = table_title.length;
            for(var i=0;i<h_len;i++){
                infoHtml += '<th>'+table_title[i]+'</th>';
            }
            infoHtml += '</tr> </thead> <tbody>';
            for(var i=0;i<d_len;i++){
                infoHtml += '<tr>';
                for(var j=0;j<table_list[i].length;j++){
                    infoHtml += '<td>'+table_list[i][j]+'</td>';
                }
                infoHtml += '</tr>';

            }
            infoHtml += '</tbody></table>';

            var pageHtml = '<div class="pagination"><span class="step-links">';
            if (data.result_data.previous != undefined){
                pageHtml += '<a href="/performance/result/?department='+data.result_data.department_id+'&name='+data.result_data.name+'&page='+data.result_data.previous;
                if(parseInt(data.result_data.month_id) >0){
                     pageHtml += '&month='+data.result_data.month_id
                }
                pageHtml += '">上一页</a>';
            }
            pageHtml += '<span class="current">当前页: '+data.result_data.current_page+'共'+data.result_data.all_page+'页</span>'
            if (data.result_data.next != undefined){

                pageHtml += '<a href="/performance/result/?department='+data.result_data.department_id+'&name='+data.result_data.name+'&page='+data.result_data.next;
                if(parseInt(data.result_data.month_id) >0){
                     pageHtml += '&month='+data.result_data.month_id
                }
                pageHtml += '">下一页</a>';
            }
            pageHtml += '</span></div>';
            infoHtml += pageHtml;
            $('#result-info')[0].innerHTML=infoHtml;
        }else{

            $('#result-info')[0].innerHTML ="<br/><p class='text-center'>没有符合要求的结果，请更改搜索条件</p>";
        }
    });

});
//$(".form-assessment-line").change(function(e){
//
//    var node = $('li.active')[0];
//    if (node != undefined){
//        var score_list = $(".form-assessment-line");
//        console.log(score_list);
//        var len = score_list.length;
//        var sum = 0;
//        for(var i=0;i<len;i++){
//            var nodeChild = score_list[i];
//            console.log(nodeChild.attributes('data-percent'));
//        }
//    }
//    console.log(node);
//});