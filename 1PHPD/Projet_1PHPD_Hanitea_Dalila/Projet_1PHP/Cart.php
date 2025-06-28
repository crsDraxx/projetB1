<?php
session_start();
require_once 'db.php';

if (!isset($_SESSION['user_id'])) {
    header('Location: LoginPage.php');
    exit;
}

$user_id = $_SESSION['user_id'];
$stmt = $con->prepare("SELECT c.id AS cart_id, v.title, v.price, v.url_image, c.quantity 
                       FROM cart c 
                       JOIN videos v ON c.video_id = v.id 
                       WHERE c.user_id = ?");
$stmt->bind_param("i", $user_id);
$stmt->execute();
$result = $stmt->get_result();
$videos = $result->fetch_all(MYSQLI_ASSOC);

$total = 0;
?>

<!DOCTYPE html>
<html>
<head>
    <title>Votre Panier</title>
    <link rel="stylesheet" href="styles/cart.css">
</head>
<body>
    <nav>
        <div class="brand">CinéStore</div>
        <div class="nav-right">
            <div class="links">
                <a href="index.php">Home</a>
                <a href="about.php">About</a>
                <a href="contact.php">Contact</a>
            </div>
            <div class="auth-cart">
                <?php if (isset($_SESSION['username'])): ?>
                    <span>Salut, <?= htmlspecialchars($_SESSION['username']) ?> !</span>
                    <a href="logout.php">Logout</a>
                <?php else: ?>
                    <a href="LoginPage.php">Login</a>
                <?php endif; ?>
                <div class="cart">
                    <a href="Cart.php">
                        <img src="ressources/images/shopping-cart.png" alt="Cart">
                        <span class="cart-count">
                            <?php
                            if (isset($_SESSION['user_id'])) {
                                $user_id = $_SESSION['user_id'];
                                $stmt = $con->prepare("SELECT SUM(quantity) AS total FROM cart WHERE user_id = ?");
                                $stmt->bind_param("i", $user_id);
                                $stmt->execute();
                                $result = $stmt->get_result();
                                $row = $result->fetch_assoc();
                                echo $row['total'] ?? 0;
                            } else {
                                echo '0';
                            }
                            ?>
                        </span>
                    </a>
                </div>
            </div>
        </div>
    </nav>

    <h1>Votre Panier</h1>

    <?php if (count($videos) > 0): ?>
        <?php foreach ($videos as $video): ?>
            <?php $total += $video['price'] * $video['quantity']; ?>
            <div class="product">
                <img src="<?= htmlspecialchars($video['url_image']) ?>" alt="<?= htmlspecialchars($video['title']) ?>">
                <div class="product-details">
                    <h3><?= htmlspecialchars($video['title']) ?></h3>
                    <p>Prix unitaire : <?= number_format($video['price'], 2) ?> €</p>
                    <p>Quantité : <?= $video['quantity'] ?></p>
                    <a href="remove_from_cart.php?id=<?= $video['cart_id'] ?>" class="remove-btn">Supprimer</a>
                </div>
            </div>
        <?php endforeach; ?>
        
        <div class="total-container">
            <h3>Total : <?= number_format($total, 2) ?> €</h3>
            <a href="clear_cart.php" class="clear-cart-btn">Vider le panier</a>
        </div>
    <?php else: ?>
        <p class="empty-cart-message">Votre panier est vide.</p>
        <div class="cart-links">
            <a href="index.php">Retourner à la boutique</a>
        </div>
    <?php endif; ?>
</body>
</html>
