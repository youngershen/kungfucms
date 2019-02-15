(function(window, $){

    function check_username(username)
    {
        kungfucms.ajax({
            'url': '/account/check-username',
            'method': 'post',
            'data': {
                'username': username
            },
            'success': function(data){
                console.log(data);
            },
            'error': function(data){
                console.log(data);
            }
        });
    }

    kungfucms.check_username = check_username;

})(window, $);