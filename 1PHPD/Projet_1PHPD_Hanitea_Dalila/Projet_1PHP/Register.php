<?php
session_start();
$erreurs = [];

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_POST['email']) && isset($_POST['mdp']) && isset($_POST['username'])) {
        $email = trim($_POST['email']);
        $mdp = $_POST['mdp'];
        $username = $_POST['username'];

        if (empty($username)) {
            $erreurs[] = "Nom d'utilisateur requis.";
        }

        if (strlen($mdp) < 4) {
            $erreurs[] = "Le mot de passe doit contenir au moins 4 caractères.";
        }

        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            $erreurs[] = "Email invalide.";
        }

        if (empty($erreurs)) {
            $host = "localhost";
            $dbname = "1phpd";
            $user = "root";
            $password = "";

            try {
                $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $user, $password);
                $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            } catch (PDOException $e) {
                die("Erreur de connexion à la base de données : " . $e->getMessage());
            }

            $sql = "INSERT INTO utilisateurs (username, email, mdp) VALUES (?, ?, ?)";
            $stmt = $pdo->prepare($sql);
            $stmt->execute([$username, $email, $mdp]);

            $successMessage = "Inscription réussie ! <br> <a href='LoginPage.php'>Se connecter maintenant</a>";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Créer un compte</title>
    <link rel="stylesheet" href="styles/register.css">
</head>
<body>

    <header>
        <div class="logo">
            <h2><a href="index.php">Our Store</a></h2>
        </div>
        <nav>
            <ul>
                <li><a href="index.php">Home</a></li>
                <li><a href="about.php">About</a></li>
                <li><a href="contact.php">Contact</a></li>
                <li><a href="LoginPage.php">Login</a></li>
            </ul>
        </nav>
        <div class="cart">
            <a href="Cart.php">
                <img src="ressources/images/shopping-cart.png" alt="Cart">
                <span class="cart-count">
                    <?php 
                    echo isset($_SESSION['cart']) ? count($_SESSION['cart']) : '0'; ?>
                </span>
            </a>
        </div>
    </header>

    <section>
        <h1>Créer un compte</h1>

        <?php
        if (!empty($erreurs)) {
            foreach ($erreurs as $erreur) {
                echo "<p class='Erreur'>$erreur</p>";
            }
        }

        if (isset($successMessage)) {
            echo "<div class='success-message'>$successMessage</div>";
        } else {
            echo '
            <form action="" method="POST">
                <input type="text" name="username" placeholder="Nom d\'utilisateur" required>
                <input type="email" name="email" placeholder="Email" required>
                <input type="password" name="mdp" placeholder="Mot de passe" required>
                <button type="submit">S\'inscrire</button>
            </form>';
        }
        ?>

        <p class="signup-link">
            Déjà inscrit ? <a href="LoginPage.php">Se connecter</a>
        </p>
    </section>

    <footer>
        <h3>&copy; Tous droits réservés</h3>
    </footer>

</body>
</html>
