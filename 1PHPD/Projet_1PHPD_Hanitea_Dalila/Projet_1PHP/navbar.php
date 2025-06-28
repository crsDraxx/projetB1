<nav>
    <div class="brand">CinéStore</div>

    <div class="links">
        <a href="index.php">Home</a>
        <a href="about.php">About</a>
        <a href="contact.php">Contact</a>
    </div>

    <div class="auth">
        <?php if (isset($_SESSION['username'])): ?>
            <span>Salut, <?= htmlspecialchars($_SESSION['username']) ?> !</span>
            <a href="ProfilPage.php">Profile</a>
            <a href="logout.php">Logout</a>
        <?php else: ?>
            <a href="LoginPage.php">Login</a>
        <?php endif; ?>
    </div>

    <div class="cart">
        <a href="Cart.php">
            <img src="ressources/images/shopping-cart.png" alt="Cart">
            <span class="cart-count">
                <?php
                require_once 'db.php';
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
</nav>