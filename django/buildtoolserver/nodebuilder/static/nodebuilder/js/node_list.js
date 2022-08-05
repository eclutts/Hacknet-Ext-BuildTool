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

window.addEventListener('load', (event) => {
    const nodelist = document.getElementsByClassName("1");
    const listplace = document.getElementById("btn-group");
    for (let i = 0; i < nodelist.length; i++) {
        listplace.innerHTML += "<a href=">" + 
                nodelist[i].getAttribute('nodeid') + "</button>";
    }
    listplace.innerHTML += "<button class='button' onclick='addNode()'>+ Add New Node</button>";
});