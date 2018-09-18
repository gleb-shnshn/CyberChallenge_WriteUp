<?php
    error_reporting(0);

    if (!isset($_GET['page'])) {
        header("Location: index.php?page=1");
        exit();
    }

    $page = $_GET['page'];

    if ($page === '/th1s_1s_the_h1dd3n_fl4g.7x7')
        die("Access denied: no flag for you");

    if (strstr($page, '..') !== false) 
        die("Access denied: you little hacker");


?>
<html>
<head>
<style>
body {
    background-color: #fbfbfb;
    font-family: "Courier new", sans-serif;
    font-size: 32px;
}

.content_box {
    background-color: #fff;
    position: absolute;

    width: 33%;
    top: 20%;
    left: 33%;

    min-height: 400px;
    min-width: 500px;
    padding-top: 20px;
    padding-bottom: 40px;

    text-align: center;
    line-height: 200px;

    border: 5px solid #000;
}
</style>
</head>
<body>
<div class="content_box">
<?php
    echo file_get_contents($page);
?>
</div>
</body>
</html>
