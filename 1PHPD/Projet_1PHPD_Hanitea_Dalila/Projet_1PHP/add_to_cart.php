<?php
session_start();
require_once 'db.php';

if (!isset($_SESSION['user_id'])) {
    header('Location: LoginPage.php');
    exit;
}

if (isset($_GET['id'])) {
    $video_id = intval($_GET['id']);
    $user_id = $_SESSION['user_id'];

    $stmt = $con->prepare("SELECT id FROM cart WHERE user_id = ? AND video_id = ?");
    $stmt->bind_param("ii", $user_id, $video_id);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows > 0) {
        $con->query("UPDATE cart SET quantity = quantity + 1 WHERE user_id = $user_id AND video_id = $video_id");
    } else {
        $stmt = $con->prepare("INSERT INTO cart (user_id, video_id) VALUES (?, ?)");
        $stmt->bind_param("ii", $user_id, $video_id);
        $stmt->execute();
    }
}

$redirect_url = $_SERVER['HTTP_REFERER'] ?? 'index.php';
header("Location: $redirect_url");
exit;
?>
