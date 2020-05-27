<?php
if($this->input->post('type_edit')) {
    foreach($this->input->post('type_edit') as $val){
        $data[] = $val;
    }
    var_dump($data); die(); // ничего не выводит

} // не заходит в это условие
?>