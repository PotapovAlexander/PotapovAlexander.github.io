<?php
if($this->input->post('type_edit')) {
    foreach($this->input->post('type_edit') as $val){
        $data[] = $val;
    }
    var_dump($data); die(); // ничего не выводит

} // не заходит в это условие

$(function(){
	$(".open_category").click(function(){
		var status = $(this).attr("aria-expanded")
		if(status=="false")
		{
			$(this).find("i").attr("class","fa fa-angle-up");
		}
		else
		{
			$(this).find("i").attr("class","fa fa-angle-down");
		}
	})
	
	
	$(".calc").on("change keyup", function(){
		var value = $(this).val();
		var price = $(this).parent().prev().find("input").val();
		price = price.replace(/\s/g, ''); 
		var item_summa = value*price;
		item_summa = item_summa.Crop(2); 
		$(this).parent().next().find("input").val(item_summa);
		
		
		var summa_category = 0; // сюда будем загонять сумму в каждоый категории
		var total_summa = 0; // сюда будем загонять итоговую сумму
		var item_summa_category = $(this).parent().next().find("input");
		$(item_summa_category).each(function(){ // пробегаемся по всем суммам и суммируем
			var k = parseFloat($(this).val());
			if(!k || k==0){k=0;}
			summa_category += k;
		})
		
		
		$(this).parents(".category").find(".summa_category").text(summa_category); 
		$(this).parents(".category").find(".summa_category_input").val(summa_category);
		
		$("big.summa_category").each(function(){ // пробегаемся по всем суммам в категориях и суммируем
			var t = parseFloat($(this).text());
			if(!t || t==0){t=0;}
			total_summa += t; // считаем общую стоимость
			
		})
		
		// выводим итоговую сумму
		$(".total").text(total_summa);
		$(".total_input").val(total_summa);
		
	})
	
})
// функция знаки после запятой
Number.prototype.Crop = function (x){
	var s = this+'', a = s.split('.');
	a[1]=a[1]||'';      
	return parseFloat(a[0]+'.'+a[1].substring(0,x));
}
?>


1.Создать форму -> check
2.Связь БД с веб приложением  ??? заполнить 
3.Заполнение макетов 
4. Шлифуй 
5. Документалка  

ЛОГИКА!!! 
