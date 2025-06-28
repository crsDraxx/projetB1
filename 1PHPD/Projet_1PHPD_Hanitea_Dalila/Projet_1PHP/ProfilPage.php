<?php
session_start();

if (!isset($_SESSION['email'])) {
    header("Location: LoginPage.php");
    exit();
}

$error_message = "";
$success_message = "";

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $current_password = $_POST['current_password'];
    $new_password = $_POST['new_password'];
    $confirm_password = $_POST['confirm_password'];

    require_once 'db.php';

    $stmt = $con->prepare("SELECT mdp FROM utilisateurs WHERE email = ?");
    $stmt->bind_param("s", $email);
    $stmt->execute();
    $stmt->store_result();
    $stmt->bind_result($stored_password);
    $stmt->fetch();


    if ($current_password !== $stored_password) {
        $error_message = "Le mot de passe actuel est incorrect.";
    } elseif ($new_password !== $confirm_password) {
        $error_message = "Les mots de passe ne correspondent pas.";        
    } else {
        $update_stmt = $con->prepare("UPDATE utilisateurs SET mdp = ? WHERE email = ?");
        $update_stmt->bind_param("ss", $new_password, $email);
        $update_stmt->execute();

        $success_message = "Mot de passe modifié avec succès.";
        
    }
}

$email = $_SESSION['email'];
$username = $_SESSION['username'];

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profil Page</title>
    <link rel="stylesheet" href="styles/profile.css">
</head>
<body>

    <header>
        <div class="logo">
            <h2><a href="index.php">CinéStore</a></h2>
        </div>
        <nav>
            <ul>
                <li><a href="index.php">Home</a></li>
                <li><a href="about.php">About</a></li>
                <li><a href="contact.php">Contact</a></li>
                <li><a href="ProfilPage.php">Profile</a></li>
                <li><a href="logout.php">Logout</a></li>
            </ul>
        </nav>
    </header>

    <section class="profile-section">
        <h1>Welcome to your profile!</h1>
        
        <div class="profile-info">
            <p><strong>Username:</strong> <?php echo htmlspecialchars($username); ?></p>
            <p><strong>Email:</strong> <?php echo htmlspecialchars($email); ?></p>
        </div>

        <!-- Affiche le message d'erreur si présent -->
        <?php if (!empty($error_message)): ?>
            <div class="error-message"><?php echo $error_message; ?></div>
        <?php endif; ?>

        <?php if (!empty($success_message)): ?>
            <div class="success-message"><?php echo $success_message; ?></div>
        <?php endif; ?>

        <div class="change-password-section">
            <h2>Modifier le mot de passe</h2>
            <form method="POST">
                <div class="form-group">
                    <label for="current_password">Mot de passe actuel</label>
                    <input type="password" id="current_password" name="current_password" required>
                </div>
                <div class="form-group">
                    <label for="new_password">Nouveau mot de passe</label>
                    <input type="password" id="new_password" name="new_password" required>
                </div>
                <div class="form-group">
                    <label for="confirm_password">Confirmer le mot de passe</label>
                    <input type="password" id="confirm_password" name="confirm_password" required>
                </div>
                <button type="submit">Modifier le mot de passe</button>
            </form>
        </div>
        <div class="logout-section">
            <a href="logout.php" class="logout-button">Logout</a>
        </div>
    </section>

</body>
    <footer>
    <h3>&copy; All Right Reserved</h3>
    </footer>
</html>