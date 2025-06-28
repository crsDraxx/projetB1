#  Projet PHP - Plateforme de Vidéos

Ce projet est une plateforme de vidéos développée en **PHP** et **MySQL**, permettant aux utilisateurs de :

- Rechercher des vidéos
- Voir les détails
- Ajouter au panier
- S'inscrire / se connecter
- Gérer leur profil et voir leurs achats

---

## Comment lancer le projet (avec WampServer 64)

### 1. Démarrer WampServer
- Lance WampServer.
- Attends que l’icône devienne **verte**.

### 2. Copier le dossier du projet
- Place le dossier `Projet_PHP` dans : C:\wamp64\www\projet_PHP\Projet_PHP


### 3. Créer la base de données
- Va sur : [http://localhost/phpmyadmin](http://localhost/phpmyadmin)
- Connecte-toi (user : `root`, mot de passe vide)
- Crée une base appelée : 1phpd

- Importe le fichier SQL fourni (ex : `1phpd.sql`)

### 4. Configuration (fichier `db.php`)
```php
$host = 'localhost';
$dbname = 'video_platform';
$username = 'root';
$password = '';
```
### 5.Lancer le projet
http://localhost/projet_PHP/projet_PHP/Projet_PHP (dossier principal vu sur vscode est Projet_PHP)
