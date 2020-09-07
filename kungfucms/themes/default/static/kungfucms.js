// kungfucms.js

// base

(function (window, $) {
    let kungfucms = {};

    if (window.kungfucms) {
        kungfucms = window.kungfucms;
    } else {
        window.kungfucms = kungfucms;
    }

    function get_meta_content(name)
    {
        let query = 'meta[name="' + name + '"]';
        return  $(query).attr('content');
    }

    function get_csrf_token() {
        return $('meta[name="CSRF_TOKEN"]').attr('content');
    }

    function csrf_safe_method(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    function ajax_setup() {
        let token = get_csrf_token();

        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!csrf_safe_method(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", token);
                }
            }
        });
    }

    function ajax(payload)
    {
        ajax_setup();
        $.ajax(payload);
    }

    kungfucms.get_csrf_token = get_csrf_token;
    kungfucms.ajax_setup = ajax_setup;
    kungfucms.ajax = ajax;
    kungfucms.get_meta_content = get_meta_content;

    window.K = kungfucms;

})(window, $);

// singup
(function (window, $){

    let signup = {};

    if(window.kungfucms)
    {
        window.kungfucms.signup = signup;
    }
    else
    {
        window.kungfucms = {};
        window.kungfucms.signup = signup
    }

    $('document').ready(function(){
        $('#kf-signup-form-input-username').change(function(){
            let username = $('#kf-signup-form-input-username').val();
            let url = kungfucms.get_meta_content('check-username-url');
            $('#kf-signup-message-network-error').addClass('d-none');

            kungfucms.ajax({
                'url': url,
                'type': 'post',
                'data': {
                    'username': username
                },
                'success': function(r){
                    console.log(r.status);
                    if(!r.status)
                    {
                        $('#kf-signup-form-input-username').attr('status', 'false');

                        if(r.message.username['min_length'])
                        {
                            console.log(r.message.username['min_length']);
                            $('#kf-signup-form-username-min-length-tip').html(r.message.username['min_length']).removeClass('d-none');
                        }
                        else
                        {
                            $('#kf-signup-form-username-min-length-tip').addClass('d-none') ;
                        }

                        if(r.message.username['required'])
                        {
                            console.log(r.message.username['required']);
                            $('#kf-signup-form-username-required-tip').html(r.message.username['required']).removeClass('d-none') ;
                        }
                        else
                        {
                            $('#kf-signup-form-username-required-tip').addClass('d-none') ;
                        }

                        if(r.message.username['unique'])
                        {
                            console.log(r.message.username['unique']);
                            $('#kf-signup-form-username-unique-tip').html(r.message.username['unique']).removeClass('d-none') ;
                        }
                        else
                        {
                            $('#kf-signup-form-username-unique-tip').addClass('d-none') ;
                        }

                    }
                    else {
                        $('#kf-signup-form-input-username').attr('status', 'true');
                        $('#kf-signup-form-username-min-length-tip').addClass('d-none');
                        $('#kf-signup-form-username-required-tip').addClass('d-none') ;
                        $('#kf-signup-form-username-unique-tip').addClass('d-none') ;
                    }
                },
                'error': function(r){
                    console.log(r);
                    $('#kf-signup-message-network-error').removeClass('d-none');
                }
            });
        });

        $('#kf-signup-form-input-password').change(function(){

            let password = $('#kf-signup-form-input-password').val();
            $('#kf-signup-message-network-error').addClass('d-none');
            $('#kf-signup-form-password-tip').addClass('d-none');

            let regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[\s\S]{8,}$/;
            if(regex.test(password))
            {
                $('#kf-signup-form-password-tip').addClass('d-none');
                $('#kf-signup-form-input-password').attr('status', 'true');

            }else
            {
                $('#kf-signup-form-password-tip').removeClass('d-none');
            }
        });

        $('#kf-signup-form-input-password-confirm').change(function(){
            $('#kf-signup-form-input-password-confirm-tip').addClass('d-none');

            let password_confirm = $('#kf-signup-form-input-password-confirm').val();
            let password = $('#kf-signup-form-input-password').val();

            if(password === password_confirm)
            {
                $('#kf-signup-form-input-password-confirm-tip').addClass('d-none');
                $('#kf-signup-form-input-password-confirm').attr('status', 'true');
            }
            else
            {
                $('#kf-signup-form-input-password-confirm-tip').removeClass('d-none');
            }
        });
        $('#kf-signup-form-input-password-confirm').focus(function(){

            $('#kf-signup-form-input-password-confirm').val('');

        });

        $('#kf-signup-form-input-password-confirm-show-password').mousedown(function(){
            $('#kf-signup-form-input-password-confirm').attr('type', 'text');

        });
        $('#kf-signup-form-input-password-confirm-show-password').mouseup(function(){
            $('#kf-signup-form-input-password-confirm').attr('type', 'password');
        });

        $('#kf-signup-form-input-password-show-password').mousedown(function () {
            $('#kf-signup-form-input-password').attr('type', 'text')
        });
        $('#kf-signup-form-input-password-show-password').mouseup(function () {
            $('#kf-signup-form-input-password').attr('type', 'password')
        });

        $('#kf-signup-form-input-captcha-image').click(function(){

            let url = kungfucms.get_meta_content('get-captcha-url');

            kungfucms.ajax({
                'url': url,
                'type': 'post',
                'success': function(r) {
                    console.log(r);
                },
                'error': function(r) {
                    console.log(r)
                }
            })
        });
    });

    signup.submit = function()
    {
        let username_status = $('#kf-signup-form-input-username').attr('status');
        let password_status = $('#kf-signup-form-input-password').attr('status');
        let password_confirm_status = $('#kf-signup-form-input-password-confirm').attr('status');

        return username_status === 'true' && password_status === 'true' && password_confirm_status === 'true';
    }
})(window, $);
