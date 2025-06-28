<?php
session_start();
require_once 'db.php';

if (isset($_GET['id']) && isset($_SESSION['user_id'])) {
    $cart_id = intval($_GET['id']);
    $user_id = $_SESSION['user_id'];
    
    $stmt = $con->prepare("DELETE FROM cart WHERE id = ? AND user_id = ?");
    $stmt->bind_param("ii", $cart_id, $user_id);
    $stmt->execute();
}

header("Location: Cart.php");
exit;
?>
