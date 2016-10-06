$(document).ready(function(){
    $('#start_date').bind('change',function(){
        var changeSubmit = $('#change-password-submit');
        if (changeSubmit != undefined){

            changeSubmit.attr('disabled',false);
        }
    });
    $('#performance-setting-form').bootstrapValidator({
        message:'该值无效',
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields:{
            start_date:{
                     validators:{
                        notEmpty:{
                            message:'日期不能为空',
                        },
                     }
                },
        },
    });

});