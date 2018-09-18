<?php
session_start();
$validUser = $_SESSION["login"] === true;
if(!$validUser) {
   header("Location: /"); 
   die();
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Flag</title>
</head>
<body>
    <p>flag() is not implemented</p>
</body>
</html>
