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

// $.ajaxSetup({
//     beforeSend: function(xhr, settings) {
    
//             xhr.setRequestHeader("X-CSRFToken", csrftoken);
        
//     }
// });

// форма отправки ПОСТ запросов
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


$.ajax({
    url : "http://127.0.0.1:8000/api/v1/user/vacancies/",
    dataType: "json",
    success : function (data) {
             console.log(data)
  
             var filter_table = document.getElementsByClassName("filter-table")[0]; 
             var vac_url = "http://127.0.0.1:8000/profile/vacancy/"
  
             var child = filter_table.lastElementChild;  
             while (child) { 
                 filter_table.removeChild(child); 
                 child = filter_table.lastElementChild; 
             } 

             for(var i=0; i<data.length; ++i) {
                var filter = document.createElement("tr");  
                filter_table.appendChild(filter);
                var id = document.createElement("td");
                vac_id = data[i].id
                id.innerHTML = vac_id;
                filter.appendChild(id);
                var title = document.createElement("td");
                vac_title = data[i].title;
                title.innerHTML = vac_title;
                filter.appendChild(title);
                var state = document.createElement("td");
                state.innerHTML = data[i].state;
                filter.appendChild(state);
                var owner = document.createElement("td");
                var owner_id = data[i].owner
                owner.innerHTML = owner_id;
                filter.appendChild(owner);

                var forma2 = document.createElement("td");
                forma2.setAttribute('id', 'get')
                filter.appendChild(forma2);                
                var f2 = document.createElement("form")
                f2.setAttribute("method", "PATCH")
                forma2.appendChild(f2);
                f2.innerHTML = '<input class="btn btn-primary btn-sm"\
                                  value="Освободить"\
                                 onclick="ajax_post(\''+release_url+ '\',\'' +vac_id+ '\')"\
                                 ></input>'
                var abs_link = document.createElement("td");
                filter.appendChild(abs_link);
                abs_link.innerHTML = '<a input class="btn btn-primary btn-sm" href="' + vac_url + vac_id + '/">Посмотреть вакансию</form>'                
              }
     
 
              
               
       },
           failure: function(data) { 
               alert('Got an error dude');
           }
        });