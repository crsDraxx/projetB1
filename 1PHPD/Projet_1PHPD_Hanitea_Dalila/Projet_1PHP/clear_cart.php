<?php
session_start();
require_once 'db.php';

if (isset($_SESSION['user_id'])) {
    $stmt = $con->prepare("DELETE FROM cart WHERE user_id = ?");
    $stmt->bind_param("i", $_SESSION['user_id']);
    $stmt->execute();
}
header("Location: Cart.php");
