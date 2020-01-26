


// фильтр подгрузки всех активных(неархивированных вакансий)        
 $.ajax({
  url : "http://127.0.0.1:8000/api/v1/vacancies/all/",
  dataType: "json",
  success : function (data) {
           console.log(data)

           var filter_table = document.getElementsByClassName("filter-table")[0]; 
           

           for(var i=0; i<data.length; ++i) {
             var filter = document.createElement("tr");  
             filter_table.appendChild(filter);
             var title = document.createElement("td");
             title.innerHTML = data[i].title;
             filter.appendChild(title);
             var state = document.createElement("td");
             state.innerHTML = data[i].state;
             filter.appendChild(state);
             var owner = document.createElement("td");
             owner.innerHTML = data[i].owner;
             filter.appendChild(owner);
          
         }
     },
         failure: function(data) { 
             alert('Got an error dude');
         }
      });

 
// фильтр подгрузки всех архивироанных вакансий по клику
$('#apireq').click( function() {
    
  $.ajax({
      url : "http://127.0.0.1:8000/api/v1/vacancies/archived/",
      dataType: "json",
      success : function (data) {
               console.log(data)

            //    var filter = document.getElementsByClassName("filter")[0];
               var filter_table = document.getElementsByClassName("filter-table")[0]; 
                
               var child = filter_table.lastElementChild;  
               while (child) { 
                   filter_table.removeChild(child); 
                   child = filter_table.lastElementChild; 
               } 
               
               for(var i=0; i<data.length; ++i) {
                 var filter = document.createElement("tr");  
                 filter_table.appendChild(filter);
                 var title = document.createElement("td");
                 title.innerHTML = data[i].title;
                 filter.appendChild(title);
                 var state = document.createElement("td");
                 state.innerHTML = data[i].state;
                 filter.appendChild(state);
                 var owner = document.createElement("td");
                 owner.innerHTML = data[i].owner;
                 filter.appendChild(owner);
              
              }
         },
             failure: function(data) { 
                 alert('Got an error dude');
             }
          });
      });

// фильтр подгрузки вакансий по пользователю

let dropdown_user = $('#user-dropdown');
dropdown_user.empty();

dropdown_user.append('<option selected="true" disabled>Выберете пользователя</option>');
dropdown_user.prop('selectedIndex', 0);

const user_url = 'http://127.0.0.1:8000/api/v1/users/all/';

$.getJSON(user_url, function (data) {
  $.each(data, function (key, value) {
    uname = value.username
    dropdown_user.append(
        $("<option></option>")
            // .attr("value",key)
            .text(uname)
    );  
  })
});


  

$('#userreq').click( function() {
    
    var user = $( "#user-dropdown option:selected" ).text();

    $.ajax({
        url : "http://127.0.0.1:8000/api/v1/vacancies/user/",
        data: {"username":user},
        dataType: "json",
        success : function (data) {
            console.log(data)
            console.log(user)
 
            var filter_table = document.getElementsByClassName("filter-table")[0]; 
                
            var child = filter_table.lastElementChild;  
            while (child) { 
                filter_table.removeChild(child); 
                child = filter_table.lastElementChild; 
            } 
            
            for(var i=0; i<data.length; ++i) {
              var filter = document.createElement("tr");  
              filter_table.appendChild(filter);
              var title = document.createElement("td");
              title.innerHTML = data[i].title;
              filter.appendChild(title);
              var state = document.createElement("td");
              state.innerHTML = data[i].state;
              filter.appendChild(state);
              var owner = document.createElement("td");
              owner.innerHTML = data[i].owner;
              filter.appendChild(owner);
           
          }
      },
          failure: function(data) { 
              alert('Got an error dude');
          }
       });
});

// фильтр подгрузки вакансий по статусу


let dropdown_state = $('#state-dropdown');
dropdown_state.empty();

dropdown_state.append('<option selected="true" disabled>Выберете статус</option>');
dropdown_state.prop('selectedIndex', 0);

const states_url = 'http://127.0.0.1:8000/api/v1/states/all/';

$.getJSON(states_url, function (data) {
    console.log(data) 
    $.each(data, function (key, value) {
      dropdown_state.append(
          $("<option></option>")
              .text(value)
      );  
    })
  });


$('#statereq').click( function() {
    
    var state = $( "#state-dropdown option:selected" ).text();

    $.ajax({
        url : "http://127.0.0.1:8000/api/v1/vacancies/state/",
        data: {"state":state},
        dataType: "json",
        success : function (data) {
            console.log(data)
 
            var filter_table = document.getElementsByClassName("filter-table")[0]; 
                
            var child = filter_table.lastElementChild;  
            while (child) { 
                filter_table.removeChild(child); 
                child = filter_table.lastElementChild; 
            } 
            
            for(var i=0; i<data.length; ++i) {
              var filter = document.createElement("tr");  
              filter_table.appendChild(filter);
              var title = document.createElement("td");
              title.innerHTML = data[i].title;
              filter.appendChild(title);
              var state = document.createElement("td");
              state.innerHTML = data[i].state;
              filter.appendChild(state);
              var owner = document.createElement("td");
              owner.innerHTML = data[i].owner;
              filter.appendChild(owner);
           
          }
      },
          failure: function(data) { 
              alert('Got an error dude');
          }
       });
});

