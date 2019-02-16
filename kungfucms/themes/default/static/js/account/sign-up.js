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

    function update_submit_button_status()
    {

    }

    function hook_submit_button_onclick()
    {
        let username_field_status = $('#kf-username').attr('status');
        let username = false;

        if(username_field_status === 'true')
        {
            username = true;
        }

        $('#kf-submit-btn').click(function(){

            console.log(username);
        });
    }

    kungfucms.check_username = check_username;
    kungfucms.check_email = check_email;
    kungfucms.check_cellphone = check_cellphone;
    kungfucms.update_submit_button_status = update_submit_button_status;
    kungfucms.hook_submit_button_onclick = hook_submit_button_onclick;


})(window, $);