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
                            $('#kf-signin-form-username-min-length-tip').html(r.message.username['min_length']).removeClass('d-none') ;
                        }
                        else
                        {
                            $('#kf-signin-form-username-min-length-tip').addClass('d-none') ;
                        }

                        if(r.message.username['required'])
                        {
                            console.log(r.message.username['required']);
                            $('#kf-signin-form-username-required-tip').html(r.message.username['required']).removeClass('d-none') ;
                        }
                        else
                        {
                            $('#kf-signin-form-username-required-tip').addClass('d-none') ;
                        }

                        if(r.message.username['unique'])
                        {
                            console.log(r.message.username['unique']);
                            $('#kf-signin-form-username-unique-tip').html(r.message.username['unique']).removeClass('d-none') ;
                        }
                        else
                        {
                            $('#kf-signin-form-username-unique-tip').addClass('d-none') ;
                        }

                    }
                    else {
                        $('#sign-up-form-input-username').attr('status', 'true');
                        $('#kf-signin-form-username-min-length-tip').addClass('d-none');
                        $('#kf-signin-form-username-required-tip').addClass('d-none') ;
                        $('#kf-signin-form-username-unique-tip').addClass('d-none') ;
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
            let pwreg = /([0-9]+[a-z]+[A-Z]+){7}/;
            if(pwreg.test(password))
            {

            }

        });
    });

})(window, $);