(function (window, $) {

    let kungfucms = window.kungfucms;

    function check_username(username, success_callback, error_callback) {
        kungfucms.ajax({
            'url': '/account/check-username',
            'method': 'post',
            'data': {
                'username': username
            },
            'success': success_callback(data),
            'error': error_callback(data)
        });
    }

    function check_email(email, success_callback, error_callback) {
        kungfucms.ajax({
            'url': '/account/check-email',
            'method': 'post',
            'data': {
                'email': email
            },
            'success': success_callback(data),
            'error': error_callback(data)
        });
    }


    function check_cellphone(cellphone, success_callback, error_callback) {
        kungfucms.ajax({
            'url': '/account/check-cellphone',
            'method': 'post',
            'data': {
                'cellphone': cellphone
            },
            'success': success_callback(data),
            'error': error_callback(data)
        });
    }

    function update_submit_button_status() {

    }

    function hook_submit_button_onclick() {
        let username_field_status = $('#kf-username').attr('status');
        let username = false;

        if (username_field_status === 'true') {
            username = true;
        }

        $('#kf-submit-btn').click(function () {

            console.log(username);
        });
    }

    function captcha_onclick() {
        $('#kf-captcha-box').click(function (e) {
            let url = kungfucms.get_meta_content('CAPTCHA_URL');
            let rand = Math.random();

            $('#kf-captcha-image').attr('src', url + '?rand=' + rand);
            console.log(e);
        })
    }

    function username_onchange() {
        $('#kf-username').change(function (e) {

            let username = $('#kf-username').val();
            let url = kungfucms.get_meta_content('CHECKUSERNAME_URL');

            kungfucms.ajax({
                'url': url,
                'method': 'POST',
                'data': {
                    'username': username
                },
                'success': function (d) {

                    if(d.status === 0)
                    {
                        $('#kf-username-warning-messsage-box').addClass('d-none');
                    }
                    else
                    {
                        let message = d.message.username['min_length'] || d.message.username['required'] || d.message.username['unique'];
                        $('#kf-username-warning-messsage-box').removeClass('d-none');
                        $('#kf-username-warning-messsage').html(message);
                    }

                },
                'error': function (d) {
                    $('#kf-username-warning-messsage-box').removeClass('d-none');
                    $('#kf-username-warning-messsage').html('something is went wrong, try again later.');
                }
            })

        });
    }

    kungfucms.check_username = check_username;
    kungfucms.check_email = check_email;
    kungfucms.check_cellphone = check_cellphone;
    kungfucms.update_submit_button_status = update_submit_button_status;
    kungfucms.hook_submit_button_onclick = hook_submit_button_onclick;
    kungfucms.captcha_onclick = captcha_onclick;
    kungfucms.username_onchange = username_onchange;

})(window, $);