function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
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

buildList();

function buildList(){
    var url = "http://127.0.0.1:8000/api/task-list/";
    var wrapper = document.getElementById('list-wrapper');
    wrapper.innerHTML = "";

    fetch(url)
    .then((response) => response.json())
    .then(function(data){

        var list = data;
        
        for (var i in list) {
            var item = `
                <div id="data-row-${i}" class="task-wrapper flex-wrapper">
                    <div style="flex:7">
                        <span class="title">${list[i].title}</span>
                    </div>
                    <div style="flex:1">
                        <button class="btn btn-sm btn-outline-dark delete">Delete </button>
                    </div>
                </div>
            `

            wrapper.innerHTML += item;
        }

        for (var i in list) {
            var deleteBtn = document.getElementsByClassName('delete')[i];

            deleteBtn.addEventListener('click', (function(item) {
                return function() {
                    deleteItem(item)
                }
            })(list[i]))
        }
    })
}


var form = document.getElementById('form-wrapper');

form.addEventListener('submit', function(e){
    e.preventDefault()
    var title = document.getElementById('title').value;
    var form = document.getElementById('form');
    var url = 'http://127.0.0.1:8000/api/task-create/';
    // console.log("Form Submitted!")

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'title': title})
    })
    .then(function(response){
        buildList()
        form.reset()
    })
})


function deleteItem(item){
    var url = `http://127.0.0.1:8000/api/task-delete/${item.id}`;
    // console.log(item)

    fetch(url, {
        method: 'DELETE', 
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        }
    })
    .then(response=>buildList())
}