<?php
class pic_file{
    
    public $white_list = array("png", "jpg", "jpeg");

    public function upload_save($type){
        $filename = md5(time().$_FILES["file"]["name"]).".$type";
        move_uploaded_file($_FILES["file"]["tmp_name"], "upload/" . $filename);
        return "Upload success! Path: upload/" . $filename;
    }

    public function check($type){
        if(empty($type)){
            return false;
        }
        if (!in_array($type,$this->white_list)){
            return false;
        }
        return true;
    }
}


//给服务器一点小小的漏洞震撼
class hack{
    public $command = "";
    function __destruct(){
        system($this->command);
    }
}


?>