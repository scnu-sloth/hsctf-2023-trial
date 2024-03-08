<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>show</title>
</head>
<body>
    <form method="GET" action="show.php">
        <input type="text" name="filename" placeholder="Search...">
        <input type="submit" />
    </form>
<?php
error_reporting(0);
include("config_file.php");
if(isset($_GET['filename']) && $_GET['filename']!=''){
    $filename = $_GET['filename'];
    echo '<img src="data:image/png;base64,'.base64_encode(file_get_contents($filename)).'" />';
}
?>
</body>
</html>