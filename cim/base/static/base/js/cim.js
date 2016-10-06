

$(function(){
    //设置登录弹框的高度和位置信息
    $('#loginModal').on('show.bs.modal', function (e) {
        $(this).find('.modal-dialog').css({
            'margin-top': function () {
                var modalHeight = $('#loginModal').find('.modal-dialog').height();
                return ($(window).height() /4- (modalHeight/2) );
            }
        });
    });
    //密码修改
     $('#old_password,#new_password,#confirm_password').bind('keydown',function(){
        var changeSubmit = $('#change-password-submit');
        if (changeSubmit != undefined){

            changeSubmit.attr('disabled',false);
        }
    });


});