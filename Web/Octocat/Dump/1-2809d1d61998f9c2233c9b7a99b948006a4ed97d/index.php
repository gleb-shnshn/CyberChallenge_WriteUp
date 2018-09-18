<?php
session_start();
$errorMsg = "";
$validUser = $_SESSION["login"] === true;
$validUser = $validUser || $_POST["username"] == "admin" && $_POST["password"] == "password";
if(!$validUser) {
    $errorMsg = "Invalid username or password.";
} else {
    $_SESSION["login"] = true;
}
if($validUser) {
   header("Location: /flag.php"); 
   die();
}
?>
<!doctype html>
<html lang="en">

    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <title>Signin</title>

        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO"
            crossorigin="anonymous">
        <!-- Custom styles for this template -->
        <link href="/public/signin.css" rel="stylesheet">
    </head>

    <body>
        <div class="text-center">
            <form class="form-signin" method="POST" action="/">
            <h1 class="h3 mb-3 font-weight-normal">Please sign in</h1>
            <label for="inputEmail" class="sr-only">Email address</label>
            <input name="username" type="email" id="inputEmail" class="form-control" placeholder="Email address" required autofocus>
            <label for="inputPassword" class="sr-only">Password</label>
            <input name="password" type="password" id="inputPassword" class="form-control" placeholder="Password" required>
            <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
            <p class="mt-5 mb-3 text-muted">&copy; 2017-2018</p>
            </form>
        </div>
    </body>

</html>