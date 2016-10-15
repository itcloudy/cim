//form表单验证客户端js代码
$(document).ready(function(){

    //修改密码验证
    $('#change-password-form').bootstrapValidator({
        message:'该值无效',
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields:{
            old_password:{
                 validators:{
                    notEmpty:{
                        message:'旧密码不能为空',
                    },
                 }
            },
            new_password:{
                 validators:{
                    notEmpty:{
                        message:'新密码不能为空',
                    },
                    stringLength: {
                        min: 6,
                        max: 30,
                        message: '密码长度为6~30',
                    },
                    identical: {
                        field: 'new_password',
                        message: '新密码和确认密不一致',
                    },
                    different: {
                        field: 'old_password',
                        message: '新密码不能和旧密码相同'
                    }
                 }
            },
            confirm_password:{
                 validators:{
                    notEmpty:{
                        message:'确认密码不能为空',
                    },
                    stringLength: {
                        min: 6,
                        max: 30,
                        message: '密码长度为6~30',
                    },
                    identical: {
                        field: 'new_password',
                        message: '确认密码和新密码不一致',
                    },
                 }
            },
        }
    });
    //添加用户验证
    $("#add-user-form").bootstrapValidator({
        message:'该值无效',
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields:{
            username:{
                validators:{
                    notEmpty:{
                        message:'用户不能为空',
                    },
                }
            },
            username_zh:{
                validators:{
                    notEmpty:{
                        message:"中文名不能为空",
                    }
                }
            },
            mobile:{
                validators: {
                    notEmpty: {
                        message:"电话号码不能为空",
                    },
                    digits: {
                        message:"电话号码只能为数字",
                    },
                    phone: {
                        country: 'CN',
                        message:"请输入有效的电话号码",
                    }
                }
            },
            password:{
                 validators:{
                    notEmpty:{
                        message:'密码不能为空',
                    },
                    stringLength: {
                        min: 6,
                        max: 30,
                        message: '密码长度为6~30',
                    },
                    identical: {
                        field: 'new_password',
                        message: '密码和确认密不一致',
                    },
                 }
            },
            confirm_password:{
                 validators:{
                    notEmpty:{
                        message:'确认密码不能为空',
                    },
                    stringLength: {
                        min: 6,
                        max: 30,
                        message: '密码长度为6~30',
                    },
                    identical: {
                        field: 'new_password',
                        message: '确认密码和密码不一致',
                    },
                 }
            },
        },
    });
});