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

})(window, $);