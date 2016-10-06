$(function(){
    //限定输入的值为0~10
    $('.form-assessment-line').on('change',function(e){
        console.log(e);
        var value = e.currentTarget.value;
        value = parseFloat(value);
        if (value>10){
            e.currentTarget.value = 10;
        }
        if(value<0){
            e.currentTarget.value = 0;
        }
    });


});