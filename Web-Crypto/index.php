<?php
error_reporting(0);
highlight_file(__FILE__);

if($_GET['a'] != $_GET['b'] && md5($_GET['a']) == md5($_GET['b'])) {
    if((string)$_POST['c'] != (string)$_POST['d'] && sha1($_POST['c']) === sha1($_POST['d'])) {
        $cmd = $_POST['cmd'];
        if(preg_match('/f|l|a|g/i',$cmd)||$cmd=='') {
            die("need a weber's help?");
        }
        eval($cmd);
    }else{
        die("you need another Crypto's help!");
    }
}else{
    die("you need a Crypto's help!");
}