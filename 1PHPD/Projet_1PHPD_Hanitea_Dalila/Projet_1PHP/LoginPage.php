<?php
session_start();

require_once 'db.php';

if(isset($_POST['bouton-login'])){
    if (isset($_POST['email'])&& isset($_POST['mdp'])) {
        $email = trim($_POST['email']);
        $mdp = $_POST['mdp'];
        $erreur = " ";
    
        $req = mysqli_query($con , "SELECT * FROM utilisateurs WHERE email='$email' AND mdp='$mdp' ");
        $num_ligne = mysqli_num_rows($req) ;
        if($num_ligne > 0) {

            $user = mysqli_fetch_assoc($req);
            $_SESSION['email'] = $user['email'];
            $_SESSION['username'] = $user['username'];
            $_SESSION['user_id'] = $user['idu'];
            
            header("Location:ProfilPage.php"); 
        } else {
            $erreur = "Adresse mail ou mots de passe incorrect !";
        }
    }    
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Page</title>
    <link rel="stylesheet" href="styles/login.css">
</head>

<body>
    <header>
        <div class="logo">
            <h2><a href="index.php">CinéStore</a></h2>
        </div>
        <nav>
            <ul>
                <li><a data-active="index" href="/index.php">Home</a></li>
                <li><a data-active="about" href="/about.php">About</a></li>
                <li><a data-active="contact" href="/contact.php">Contact</a></li>
                <li><a href="ProfilPage"><img src="ressources/images/account.png" alt="Profil"></a></li>
            </ul>
        </nav>
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
    </header>

    <section>

        <h1>LOGIN</h1>

        <?php
        if(isset($erreur)){
            echo "<p class='Erreur'>".$erreur. "</p>" ; 
        }
        ?>

        <form action="" method="POST">
            <input type="email" name="email" placeholder="exemple@mail.com" required>
            <input type="password" name="mdp" placeholder="Password" required>
            <input type="submit" value="Log in" name="bouton-login">
        </form>

        <p class="signup-link">Pas encore inscrit ? <a href="Register.php">Créer un compte</a></p>
    </section>

</body>

<footer>
<footer>
    <h3>&copy; All Right Reserved</h3>
    
</footer>
</html>
