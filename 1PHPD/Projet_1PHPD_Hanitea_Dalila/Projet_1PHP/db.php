<?php
$host = "localhost";
$dbname = "1phpd";
$username = "root";
$password = "";

$con = new mysqli($host, $username, $password, $dbname);

if ($con->connect_error) {
    die("Connexion échouée : " . $con->connect_error);
}
?>
