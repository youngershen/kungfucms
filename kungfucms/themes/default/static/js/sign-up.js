(function (window, $) {

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
        $('#sign-up-form-input-username').change(function(){
            let username = $('#sign-up-form-input-username').val();
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
                        $('#sign-up-form-input-username').attr('status', 'false');

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
                        $('#sign-up-form-input-username').attr('status', 'true');
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


        $('#sign-up-form-input-password').change(function(){

            let password = $('#sign-up-form-input-password').val();
            $('#kf-signup-message-network-error').addClass('d-none');
            $('#kf-signup-form-password-tip').addClass('d-none');

            let regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[\s\S]{8,}$/;
            if(regex.test(password))
            {
                $('#kf-signup-form-password-tip').addClass('d-none');
                $('#sign-up-form-input-password').attr('status', 'true');

            }else
            {
                $('#kf-signup-form-password-tip').removeClass('d-none');
            }
        });


        $('#sign-up-form-input-password-confirm').change(function(){
            $('#sign-up-form-input-password-confirm-tip').addClass('d-none');

            let password_confirm = $('#sign-up-form-input-password-confirm').val();
            let password = $('#sign-up-form-input-password').val();

            if(password === password_confirm)
            {
                $('#sign-up-form-input-password-confirm-tip').addClass('d-none');
                $('#sign-up-form-input-password-confirm').attr('status', 'true');
            }
            else
            {
                $('#sign-up-form-input-password-confirm-tip').removeClass('d-none');
            }
        });

        $('#sign-up-form-input-password-confirm-show-password').mousedown(function(){
            $('#sign-up-form-input-password-confirm').attr('type', 'text');

        });
        $('#sign-up-form-input-password-confirm-show-password').mouseup(function(){
            $('#sign-up-form-input-password-confirm').attr('type', 'password');
        });


        $('#sign-up-form-input-password-show-password').mousedown(function () {
            $('#sign-up-form-input-password').attr('type', 'text')
        });

        $('#sign-up-form-input-password-show-password').mouseup(function () {
            $('#sign-up-form-input-password').attr('type', 'password')
        });
    });


    signup.submit = function()
    {
        let username_status = $('#sign-up-form-input-username').attr('status');
        let password_status = $('#sign-up-form-input-password').attr('status');
        let password_confirm_status = $('#sign-up-form-input-password-confirm').attr('status');

        return username_status === 'true' && password_status === 'true' && password_confirm_status === 'true';
    }
})(window, $);