(function (window, $) {

    let kungfucms = window.kungfucms;

    function check_username(username) {
        kungfucms.ajax({
            'url': '/account/check-username',
            'method': 'post',
            'data': {
                'username': username
            },
            'success': function (data) {
                console.log(data);
            },
            'error': function (data) {
                console.log(data);
            }
        });
    }

    function check_email(email) {
        kungfucms.ajax({
            'url': '/account/check-email',
            'method': 'post',
            'data': {
                'email': email
            },
            'success': function (data) {
                console.log(data);
            },
            'error': function (data) {
                console.log(data);
            }
        });
    }


    function check_cellphone(cellphone) {
        kungfucms.ajax({
            'url': '/account/check-cellphone',
            'method': 'post',
            'data': {
                'cellphone': cellphone
            },
            'success': function (data) {
                console.log(data);
            },
            'error': function (data) {
                console.log(data);
            }
        });
    }

    kungfucms.check_username = check_username;
    kungfucms.check_email = check_email;
    kungfucms.check_cellphone = check_cellphone;

})(window, $);