var upd_url = "http://127.0.0.1:8000/api/v1/vacancies/update/"
var release_url = "http://127.0.0.1:8000/api/v1/vacancies/update/"


// получаем куку (используем для получения csrf токена)
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}



var csrftoken = getCookie('csrftoken');


// форма отправки запросов на update вакансии
function ajax_post(url, id, owner) {
        $.ajax({
            headers: { 
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken 
            },
            url: url + id + "/",
            type: 'PATCH',
            dataType: "json",
            contentType: "application/json",
            data: JSON.stringify({owner:Number(owner)}),
            success: function (data) {
                console.log(data)
                window.location.reload();
            },
            error: function (e) {
                console.log(e);
            }      
        });
        return false;
}




 




