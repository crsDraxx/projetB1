<?php
session_start();
require_once 'db.php';

if (isset($_GET['id'])) {
    $video_id = intval($_GET['id']);
    $stmt = $con->prepare("SELECT v.id, v.title, v.description, v.price, v.url_image
                           FROM videos v
                           WHERE v.id = ?");
    $stmt->bind_param("i", $video_id);
    $stmt->execute();
    $result = $stmt->get_result();
    $video = $result->fetch_assoc();
}
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Détails de la vidéo</title>
    <link rel="stylesheet" href="styles/style.css">
    <link rel="stylesheet" href="styles/details_movie.css">
</head>
<body>
    
    <?php include('navbar.php'); ?>

    <main class="video-details">
        <div class="video-left">
            <img src="<?= htmlspecialchars($video['url_image']) ?>" alt="<?= htmlspecialchars($video['title']) ?>">
        </div>
        <div class="video-right">
            <h1><?= htmlspecialchars($video['title']) ?></h1>
            <p class="description"><?= nl2br(htmlspecialchars($video['description'])) ?></p>
            <p class="price"><?= number_format($video['price'], 2) ?> €</p>
            <a href="add_to_cart.php?id=<?= $video['id'] ?>" class="add-to-cart-btn">Ajouter au panier</a>
        </div>
    </main>

    <footer>
        <h3>&copy; All Right Reserved</h3>
    </footer>
</body>
</html>
