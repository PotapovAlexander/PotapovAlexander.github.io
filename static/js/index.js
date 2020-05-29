$(document).ready(function () {
    let calc_button = document.getElementById('calc-button');

    let output_span = document.getElementById('output-span');

    let table = document.getElementById('my-rofl-table');

    let check_box = table.getElementsByTagName("input");

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