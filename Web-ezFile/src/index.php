<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload</title>
</head>
<style type="text/css">
  body {
    margin: 0;
  }
  .ui_ {
    width: 100%;
    height: 100px;
    background-color: #f08994;
    text-align: center;
    line-height: 100px;
    font-size: 30px;
  }
  .filepath {
    width: 100%;
    height: 30px;
  }
</style>
<body>
  <div class="ui_">假装这是好看的前端!</div>
  <form action="index.php" method="post" enctype="multipart/form-data" >
  <input type="file" name="file">
  <button class="" ><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">提交</font></font></button>
</form>
<div class="filepath"></div>
<input type="button" value="show pic" onclick="javascript:window.location.href='show.php'">
<?php
error_reporting(0);
include "config_file.php";
if(!empty($_FILES)){
  $file = new pic_file();
  $type = end(explode(".", $_FILES['file']['name']));
  if(!$file->check($type)){
    echo "哎~~哟~~，你~~在~~~嘛!";
  }else {
    echo $file->upload_save($type);
  }
}
?>
</body>
</html>