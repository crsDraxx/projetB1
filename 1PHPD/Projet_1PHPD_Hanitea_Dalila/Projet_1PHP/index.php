<?php
session_start();
require_once 'db.php';

$videos = [];
$category_id = isset($_GET['category']) ? (int)$_GET['category'] : 0;

if (isset($_GET['search']) && !empty($_GET['search'])) {
    $search = "%" . $con->real_escape_string($_GET['search']) . "%";
    if ($category_id > 0) {
        $stmt = $con->prepare("SELECT * FROM videos WHERE (title LIKE ? OR director LIKE ?) AND category = ? ORDER BY creation DESC LIMIT 10");
        $stmt->bind_param("ssi", $search, $search, $category_id);
    } else {
        $stmt = $con->prepare("SELECT * FROM videos WHERE title LIKE ? OR director LIKE ? ORDER BY creation DESC LIMIT 10");
        $stmt->bind_param("ss", $search, $search);
    }
    $stmt->execute();
    $result = $stmt->get_result();
} else {
    if ($category_id > 0) {
        $stmt = $con->prepare("SELECT * FROM videos WHERE category = ? ORDER BY creation DESC LIMIT 10");
        $stmt->bind_param("i", $category_id);
    } else {
        $stmt = $con->prepare("SELECT * FROM videos ORDER BY creation DESC LIMIT 10");
    }
    $stmt->execute();
    $result = $stmt->get_result();
}

if ($result) {
    $videos = $result->fetch_all(MYSQLI_ASSOC);
}

$categories_result = $con->query("SELECT * FROM categories");
$categories = $categories_result->fetch_all(MYSQLI_ASSOC);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="We have a wide collection of movies of drama and action">
    <meta name="keywords" content="drama, action">
    <link rel="stylesheet" href="styles/style.css">
    <title>CinéStore</title>
</head>
<body>

    <?php include('navbar.php'); ?>


    <header>
        <h1>Welcome to CinéStore</h1>
        <p class="sub-title">
            Découvrez notre vaste collection de films de tous genres — drame, action, comédie, etc. <br>
            Utilisez la barre de recherche pour trouver votre film préféré.
        </p>
    </header>

    <main>
        <div class="left">
            <div class="section-title">Movie Categories</div>
            <a href="index.php">Toutes les catégories</a>
            <?php foreach ($categories as $category): ?>
                <a href="index.php?category=<?= $category['idc'] ?>"><?= htmlspecialchars($category['name']) ?></a>
            <?php endforeach; ?>
        </div>
        <div class="right">
            <div class="section-title">Films récemment ajoutés</div>

            <form class="search-bar" method="get" action="index.php">
                <input type="text" name="search" placeholder="Rechercher par titre ou réalisateur..." value="<?= htmlspecialchars($_GET['search'] ?? '') ?>">
                <button type="submit">Recherche</button>
            </form>

            <?php if (count($videos) > 0): ?>
                <?php foreach ($videos as $video): ?>
                    <div class="product">
                        <div class="product-left">
                            <img src="<?= htmlspecialchars($video['url_image']) ?>" alt="<?= htmlspecialchars($video['title']) ?>">
                        </div>
                        <div class="product-right">
                            <p class="title">
                                <a href="DetailsMovie.php?id=<?= $video['id'] ?>"><?= htmlspecialchars($video['title']) ?></a>
                            </p>
                            <p class="description"><?= htmlspecialchars($video['description']) ?></p>
                            <p class="price"><?= number_format($video['price'], 2) ?> &euro;</p>
                            <a href="add_to_cart.php?id=<?= $video['id'] ?>" class="add-to-cart-btn">Ajouter au panier</a>
                        </div>
                    </div>
                <?php endforeach; ?>
            <?php else: ?>
                <p>Aucun film trouvé</p>
            <?php endif; ?>
        </div>
    </main>

    <footer>
    <h3>&copy; All Right Reserved</h3>
    </footer>
</body>
</html>
