function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        var csrftoken = getCookie('csrftoken');
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


$(document).ready(function () {

    var options = {
        url: "/send_data/",
        beforeSubmit: function () {
            document.getElementById("status_msg").innerHTML = 'Status: saving data....';
            $("#personal_data_form").find(":input").attr("disabled", true);
            alert('Debug message: before ajax submit');
        },
        success: function (data) {
            alert('Debug message: request done');
            $("#personal_data_form").find(":input").attr("disabled", false);
            if (data == 'error') {
                document.getElementById("reset_form").click();
                document.getElementById("status_msg").innerHTML = 'Status: Data error';
                alert('Debug message: incorrect data');
            }
            else document.getElementById("status_msg").innerHTML = 'Status: success, data saved';
        },
        error: function (data) {
            document.getElementById("status_msg").innerHTML = 'Status: Ajax error';
            $("#personal_data_form").find(":input").attr("disabled", false);
            alert('Debug message: ajax error');
        }
    };

    $("#personal_data_form").submit(function () {
        $(this).ajaxSubmit(options);
        return false;
    });

});