function makeList() {
    let listData = [
        'Blue',
        'Red',
        'White',
        'Green',
        'Black',
        'Orange'
    ],

    listContainer = document.createElement('div'),
    listElement = document.createElement('ul'),

    numberOfListItems = listData.length,
    listItem,
    i;

    document.getElementsByTagName('body')[0].appendChild(listContainer);
    listContainer.appendChild(listElement);

    for (i = 0; i < numberOfListItems; ++i) {
        listItem = document.createElement('li');
        listItem.innerHTML = listData[i];
        listElement.appendChild(listItem);
    }
}

function makeForm() {
    // <label for=[0]>[1]</label>
    // <input type=[2] id=[0] name=[3], value=[4]><br>
    let form = [
        ["id", "id", "text", "node_id", ""],
        ["name", "name", "text", "node_name", ""],
        ["ip", "ip", "text", "node_ip", ""]
        
    ],
    listContainer = document.createElement('div'),
    listContainer2 = document.createElement('form'),
    formLength = form.length,
    formLabel,
    formItem,
    i;

    document.getElementsByTagName('body')[0].appendChild(listContainer);
    listContainer.appendChild(listContainer2);

    for (i = 0; i < formLength; ++i){
        formLabel = document.createElement('label');
        formLabel.for = form[i][0];
        formLabel.innerHTML = form[i][1];
        formItem = document.createElement('input');
        formItem.type = form[i][2];
        formItem.id = form[i][0];
        formItem.name = form[i][3];
        if (form[i][4] != "") {
            formItem.value = form[i][4];
        }
        listContainer2.appendChild(formLabel);
        listContainer2.appendChild(formItem);
    }
}