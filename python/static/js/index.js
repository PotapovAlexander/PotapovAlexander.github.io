$(document).ready(function () {
    let table = document.getElementById('rofl-table');
    let selector = document.getElementById("courses-select");
    let load_button = document.getElementById("load-button");
    let check_box = table.getElementsByTagName("input");
    let calc_button = document.getElementById('calc-button');
    let output_span = document.getElementById('output-span');
    let save_button = document.getElementById('save-button');

    load_button.onclick = function () {//выполняем запрос GET запрос на адресс get-course

        let url = "/get-course?" + $.param({id: selector.value});
        fetch(url, {
            method: 'GET',
        })
            .then(responce => responce.json())
            .then(answer => {
                let data = answer['result'];
                console.log(data);

                table.innerHTML = "<tr><th><input type='checkbox' value='0' checked></th></tr>";
                for (let j = 0; j < data[0].length; j++) {
                    table.getElementsByTagName('tr')[0].innerHTML += "<th>" + data[0][j] + "</th>";
                }
                for (let i = 1; i < data.length; i++) {
                    table.innerHTML += "<tr><td><input type='checkbox' value='"+data[i][3]+"' checked></td></tr>";
                    for (let j = 0; j < data[i].length; j++) {
                        table.getElementsByTagName('tr')[i].innerHTML += "<td>" + data[i][j] + "</td>";
                    }
                }
                check_box[0].onclick = function () {
                    let row_count = table.rows.length;
                    if (check_box[0].checked) {//Выделить все чекбоксы
                        for (let i = 1; i < row_count; i++) {
                            check_box[i].checked = true;
                        }
                    } else {//Убиравем все выделенные чекбоксы
                        for (let i = 1; i < row_count; i++) {
                            check_box[i].checked = false;
                        }
                    }
                }

                for (let i = 1; i < table.rows.length; i++) {//убирвем Верхний чекбокс если есть изменения в других
                    check_box[i].onclick = function () {
                        if (!check_box[i].checked) {
                            check_box[0].checked = false;
                        }
                    }
                }
            })
    }

     save_button.onclick = function () {//функция сохранение выделенных курсов
       let table_arr = [];//создаем массив для хранения
       let rows = table.rows;//строка
       for (let i = 1; i < rows.length; i++) {
           if (check_box[i].checked  === true ) {
               table_arr.push(rows[i].cells[1].innerText);
           }
       }
       let json_data = {"list":table_arr};//
       console.log(json_data);

        let url = "/save_excel_course";
        fetch(url, {//отправляем POST запрос
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(json_data)
        })
            .then(responce => responce.blob())//ожидание json
            .then(blob => {
                var url = window.URL.createObjectURL(blob);
                var a = document.createElement('a');
                a.href = url;
                a.download = "tmp.xlsx";
                document.body.appendChild(a); // we need to append the element to the dom -> otherwise it will not work in firefox
                a.click();
                a.remove();
            })
    }
    calc_button.onclick = function calc() {//читаем данные с сформированной таблицы
        console.log('click');
        let rows = table.rows;
        let sum = 0;

        for (let i = 0; i < rows.length; i++) {//расчет суммы
            if (check_box[i].checked === true) {
                let row_value = rows[i].getElementsByTagName('input')[0].value;//берем из input value
                sum += parseInt(row_value);//суммирование
                console.log("значение строки = " + row_value);
            }
        }

        output_span.innerText = sum.toString();// передаем значение суммы на страницу
    }
});