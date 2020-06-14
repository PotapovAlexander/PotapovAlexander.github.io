$(document).ready(function () {
    let table = document.getElementById('rofl-table');
    let selector = document.getElementById("courses-select");
    let load_button = document.getElementById("load-button");

    load_button.onclick = function () {
        let url = "/get-course?" + $.param({id: selector.value});
        fetch(url, {
            method: 'GET',
        })
            .then(responce => responce.json())
            .then(answer => {
                let data = answer['result'];
                console.log(data);

                table.innerHTML = "<tr></tr>";
                for (let j = 0; j < data[0].length; j++) {
                    table.getElementsByTagName('tr')[0].innerHTML += "<th>" + data[0][j] + "</th>";
                }
                for (let i = 1; i < data.length; i++) {
                    table.innerHTML += "<tr></tr>";
                    for (let j = 0; j < data[i].length; j++) {
                        table.getElementsByTagName('tr')[i].innerHTML += "<td>" + data[i][j] + "</td>";
                    }
                }
            })
    }
});