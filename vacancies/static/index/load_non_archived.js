// фильтр всех активных(неархивированных вакансий) при загрузке страницы 
$.ajax({
    url : "http://127.0.0.1:8000/api/v1/vacancies/all/",
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
                var forma = document.createElement("td");
                forma.setAttribute('id', 'get')
                filter.appendChild(forma);       
                var f = document.createElement("form")
                f.setAttribute("method", "PATCH")
                forma.appendChild(f);
                f.innerHTML = '<input class="btn btn-primary btn-sm"\
                                value="Взять"\
                                onclick="ajax_post(\''+upd_url+ '\',\'' + vac_id + '\',\'' +current_user+ '\')"\
                                ></input>'
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



// загрузить список по клику         
$('#apireq_null').click( function() {
    $.ajax({
        url : "http://127.0.0.1:8000/api/v1/vacancies/all/",
        dataType: "json",
        success : function (data) {
                 console.log(data)
      
                 var filter_table = document.getElementsByClassName("filter-table")[0]; 
                 var upd_url = "http://127.0.0.1:8000/api/v1/vacancies/update/"
                 var release_url = "http://127.0.0.1:8000/api/v1/vacancies/update/"
      
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
                   var forma = document.createElement("td");
                   forma.setAttribute('id', 'get')
                   filter.appendChild(forma);       
                   var f = document.createElement("form")
                   f.setAttribute("method", "PATCH")
                   forma.appendChild(f);
                   f.innerHTML = '<input class="btn btn-primary btn-sm"\
                                   value="add"\
                                   onclick="ajax_post(\''+upd_url+ '\',\'' + vac_id + '\',\'' +current_user+ '\')"\
                                   ></input>'
                   var forma2 = document.createElement("td");
                   forma2.setAttribute('id', 'get')
                   filter.appendChild(forma2);                
                   var f2 = document.createElement("form")
                   f2.setAttribute("method", "PATCH")
                   forma2.appendChild(f2);
                   f2.innerHTML = '<input class="btn btn-primary btn-sm"\
                                     value="release"\
                                    onclick="ajax_post(\''+release_url+ '\',\'' +vac_id+ '\')"\
                                    ></input>'

                  }    
                   
           },
               failure: function(data) { 
                   alert('Got an error dude');
               }
            });
});
    
    