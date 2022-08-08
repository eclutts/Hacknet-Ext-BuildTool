/* generates a new node */
function addNode() {
    loadNodeForm({node_id: ""})
}

function loadNodeForm(computer) {
    const obj = document.getElementById(computer);
    const elem = document.getElementById('nodeform');
    if (computer.node_id == "") {
        elem.innerHTML = "<p>it works!</p>";
        return;
    } else {
        elem.innerHTML = "<p>" + obj.getAttribute("name") + "</p>";
        return;
    }
    
}

/*
window.addEventListener('load', (event) => {
    const nodelist = document.getElementsByClassName("1");
    const listplace = document.getElementById("btn-group");
    for (let i = 0; i < nodelist.length; i++) {
        listplace.innerHTML += "<a href=/nodes/" + nodelist[i].getAttribute("sql_id") + "/>"
                nodelist[i].getAttribute('nodeid') + "</button>";
    }
    listplace.innerHTML += "<button class='button' onclick='addNode()'>+ Add New Node</button>";
}); */


function getCompForm(id) {
    const form = document.getElementById("form");
    if (id == 0){
        form.innerHTML = "<p>Edit This!</p>";
    } else {
        const obj = document.getElementById(id);
        form.innerHTML = obj.getAttribute('form');
        form.innerHTML += '<input type="submit" value="Save?">'
        /* Add A Submit Button? */
    }
}    
