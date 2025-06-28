-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Apr 15, 2025 at 08:55 PM
-- Server version: 9.1.0
-- PHP Version: 8.3.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `1phpd`
--

-- --------------------------------------------------------

--
-- Table structure for table `actors`
--

DROP TABLE IF EXISTS `actors`;
CREATE TABLE IF NOT EXISTS `actors` (
  `ida` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`ida`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

DROP TABLE IF EXISTS `cart`;
CREATE TABLE IF NOT EXISTS `cart` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `video_id` int NOT NULL,
  `quantity` int NOT NULL DEFAULT '1',
  `added_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
CREATE TABLE IF NOT EXISTS `categories` (
  `idc` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`idc`)
) ENGINE=MyISAM AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`idc`, `name`) VALUES
(1, 'Science-fiction'),
(2, 'Drame'),
(3, 'Thriller'),
(4, 'Action'),
(5, 'Comédie'),
(6, 'Suspense'),
(7, 'Aventure'),
(8, 'Animation'),
(9, 'Horreur'),
(10, 'Romance'),
(11, 'Science-fiction'),
(12, 'Drame'),
(13, 'Thriller'),
(14, 'Action'),
(15, 'Comédie'),
(16, 'Suspense'),
(17, 'Aventure'),
(18, 'Animation'),
(19, 'Horreur'),
(20, 'Romance'),
(21, 'Science-fiction'),
(22, 'Drame'),
(23, 'Thriller'),
(24, 'Action'),
(25, 'Comédie'),
(26, 'Suspense'),
(27, 'Aventure'),
(28, 'Animation'),
(29, 'Horreur'),
(30, 'Romance');

-- --------------------------------------------------------

--
-- Table structure for table `directors`
--

DROP TABLE IF EXISTS `directors`;
CREATE TABLE IF NOT EXISTS `directors` (
  `idd` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`idd`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
CREATE TABLE IF NOT EXISTS `orders` (
  `id` int NOT NULL AUTO_INCREMENT,
  `utilisateur_id` int NOT NULL,
  `total` decimal(10,0) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `order_items`
--

DROP TABLE IF EXISTS `order_items`;
CREATE TABLE IF NOT EXISTS `order_items` (
  `id` int NOT NULL AUTO_INCREMENT,
  `order_id` int NOT NULL,
  `video_id` int NOT NULL,
  `price` decimal(6,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `utilisateurs`
--

DROP TABLE IF EXISTS `utilisateurs`;
CREATE TABLE IF NOT EXISTS `utilisateurs` (
  `idu` int NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `mdp` varchar(255) NOT NULL,
  `username` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `date_creation` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`idu`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `utilisateurs`
--

INSERT INTO `utilisateurs` (`idu`, `email`, `mdp`, `username`, `date_creation`, `update_at`) VALUES
(1, 'test@gmail.com', 'test', 'premier test', '2025-04-13 19:58:21', '2025-04-13 21:42:25');

-- --------------------------------------------------------

--
-- Table structure for table `videos`
--

DROP TABLE IF EXISTS `videos`;
CREATE TABLE IF NOT EXISTS `videos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `director` varchar(255) NOT NULL,
  `actors` text NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `category` varchar(100) NOT NULL,
  `description` text NOT NULL,
  `url_image` varchar(255) NOT NULL,
  `creation` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `videos`
--

INSERT INTO `videos` (`id`, `title`, `director`, `actors`, `price`, `category`, `description`, `url_image`, `creation`, `updated`) VALUES
(1, 'Inception', 'Christopher Nolan', '', 14.99, '1', 'Un voleur s’infiltre dans les rêves pour voler des informations.', 'ressources/images/inception.jpg', '2025-04-14 08:58:07', '2025-04-14 18:20:32'),
(2, 'The Matrix', 'Lana Wachowski', '', 12.99, '1', 'Un hacker découvre la vraie nature de la réalité.', 'ressources/images/matrix.jpg', '2025-04-14 08:58:07', '2025-04-14 18:20:32'),
(3, 'The Godfather', 'Francis Ford Coppola', '', 11.50, '2', 'L’histoire de la famille mafieuse Corleone.', 'ressources/images/godfather.jpg', '2025-04-14 08:58:07', '2025-04-14 18:20:32'),
(4, 'Interstellar', 'Christopher Nolan', '', 15.00, '1', 'Une équipe d’explorateurs voyage au-delà de notre galaxie pour sauver l’humanité.', 'ressources/images/interstellar.jpg', '2025-04-14 08:58:07', '2025-04-14 18:20:32'),
(5, 'Parasite', 'Bong Joon-ho', '', 10.99, '2', 'Une famille pauvre s’infiltre chez des riches pour améliorer sa situation.', 'ressources/images/parasite.jpg', '2025-04-14 08:58:07', '2025-04-14 18:20:32'),
(6, 'Forrest Gump', 'Robert Zemeckis', '', 12.00, '2', 'L’histoire bouleversante d’un homme simple d’esprit dont la vie traverse des decennies d’histoire américaine.', 'ressources/images/forrestGump.jpg', '1994-04-14 08:58:07', '2025-04-14 21:30:55'),
(7, 'Les evadés', 'Frank Darabont', '', 10.99, '2', 'Un homme injustement emprisonné se lie d’amitié avec un codétenu.', 'ressources/images/lesEvades.jpg', '2025-04-14 08:58:07', '2025-04-14 21:30:55'),
(12, 'Kandahar', 'Ric Roman Waugh', '', 17.50, '4', 'Un agent de la CIA (Gerard Butler) est pris en chasse en Afghanistan après une mission secrète révélée au grand jour.', 'ressources/images/kandahar.jpg', '2023-04-14 08:58:07', '2025-04-15 19:38:13'),
(13, 'Room', 'Lenny Abrahamson', '', 11.99, '2', 'Une femme et son fils vivent reclus dans une pièce depuis des années avant de tenter une évasion.', 'ressources/images/room.jpg', '2025-04-15 08:58:07', '2025-04-15 19:38:13'),
(8, ' Million Dollar Baby', 'Clint Eastwood', '', 10.99, '2', 'Une jeune boxeuse persévérante veut atteindre le sommet avec l’aide d’un entraîneur désabusé.', 'ressources/images/millionDollarBaby.jpg', '2025-04-14 08:58:07', '2025-04-15 15:41:05'),
(9, 'Requiem for a Dream', ' Darren Aronofsky', '', 12.99, '2', 'Une descente aux enfers de quatre personnages confrontés à leurs addictions et illusions.', 'ressources/images/requiem.jpg', '1994-04-14 08:58:07', '2025-04-15 15:43:47'),
(14, ' A Beautiful Mind', 'Ron Howard', '', 12.99, '2', 'Biographie poignante du mathématicien John Nash, aux prises avec la schizophrénie.', 'ressources/images/beautifulMind.jpg', '2025-04-15 08:58:07', '2025-04-15 19:38:13'),
(10, 'La Vie est belle', 'Roberto Benigni', '', 13.99, '2', ' Un père juif italien protège son fils de l’horreur d’un camp de concentration en transformant tout en jeu.', 'ressources/images/lavieEstBelle.jpg', '2025-04-15 08:58:07', '2025-04-15 15:52:10'),
(11, '12 Years a Slave', 'Steve McQueen', '', 7.99, '2', ' L’histoire vraie de Solomon Northup, un homme noir libre kidnappé et vendu comme esclave pendant 12 ans', 'ressources/images/12yearsaslave.jpg', '2025-04-15 08:58:07', '2025-04-15 15:52:10'),
(15, 'Mayday', 'Jean-François Richet', '', 18.00, '4', 'Un pilote de ligne (Gerard Butler) doit poser son avion en urgence sur une île contrôlée par des rebelles, mettant en péril la vie de ses passagers.', 'ressources/images/mayday.jpg', '2025-04-14 08:58:07', '2025-04-15 19:38:13'),
(16, 'Silent Night', ' John Woo', '', 15.00, '4', 'Un père endeuillé (Joel Kinnaman) se lance dans une quête de vengeance sans prononcer un mot, dans ce film d action muet.', 'ressources/images/silentNight.jpg', '2025-04-14 08:58:07', '2025-04-15 19:38:13'),
(17, 'Retribution', 'Francis Ford Coppola', '', 11.50, '4', ' Un homme (Liam Neeson) découvre une bombe sous son siège de voiture et doit suivre les instructions d un inconnu pour sauver sa famille.', 'ressources/images/retribution.jpg', '2025-04-14 08:58:07', '2025-04-15 19:38:13'),
(18, 'The A-Team', 'Roar Uthaug', '', 14.00, '4', ' Une équipe d anciens soldats accusés à tort cherche à blanchir leur nom tout en accomplissant des missions périlleuses.', 'ressources/images/ateam.jpg', '2025-04-14 08:58:07', '2025-04-15 19:38:13'),
(19, 'Tomb Raider', 'Bong Joon-ho', '', 10.99, '4', 'Lara Croft (Alicia Vikander) part à la recherche de son père disparu sur une île mystérieuse.', 'ressources/images/tombraider.jpg', '2025-04-14 08:58:07', '2025-04-15 19:38:13'),
(20, 'Overdrive', 'Antonio Negret', '', 13.50, '4', 'Deux frères voleurs de voitures de luxe se retrouvent impliqués dans un conflit entre criminels à Marseille.', 'ressources/images/overdrive.jpg', '2025-04-14 08:58:07', '2025-04-15 19:38:13'),
(21, 'Security', 'Alain Desrochers', '', 12.00, '4', 'Un ex-soldat devenu agent de sécurité protège une fillette traquée par des tueurs dans un centre commercial.', 'ressources/images/security.jpg', '2025-04-14 08:58:07', '2025-04-15 19:38:13'),
(22, 'Extraction', 'Sam Hargrave', '', 17.00, '4', 'Un mercenaire sauve un enfant dans une ville ennemie.', 'ressources/images/extraction.jpg', '2025-04-14 08:58:07', '2025-04-15 19:38:13'),
(23, 'John Wick', 'Chad Stahelski', '', 13.99, '4', 'Un tueur à gages venge son chien tué', 'ressources/images/johnWick.jpg', '2025-04-14 08:58:07', '2025-04-15 19:38:13'),
(24, 'Gone Girl', 'David Fincher', '', 12.00, '3', 'Un homme est suspecté après la disparition de sa femme.', 'ressources/images/goneGirl.jpg', '2025-04-14 08:58:07', '2025-04-15 20:16:29'),
(25, 'The Hangover ', 'Todd Phillips', '', 11.50, '5', 'Trois amis se réveillent après une soirée chaotique à Vegas.', 'ressources/images/hangover.jpg', '2025-04-14 08:58:07', '2025-04-15 20:16:29'),
(26, ' Prisoners', 'Denis Villeneuve', '', 13.99, '6', 'Un père enquête après la disparition de sa fille', 'ressources/images/prisoners.jpg', '2025-04-14 08:58:07', '2025-04-15 20:16:29'),
(27, 'Jurassic World', 'Colin Trevorrow', '', 12.00, '7', 'Des dinosaures s’échappent dans un parc à thème.', 'ressources/images/jurassic.jpg', '2025-04-14 08:58:07', '2025-04-15 20:16:29'),
(28, ' Coco', 'Lee Unkrich', '', 14.50, '8', 'Un jeune garçon explore le monde des morts pour découvrir ses origines', 'ressources/images/coco.jpg', '2025-04-14 08:58:07', '2025-04-15 20:16:29'),
(29, 'The Conjuring', 'James Wan', '', 12.00, '9', ': Des enquêteurs du paranormal affrontent une entité maléfique.', 'ressources/images/conjuring.jpg', '2025-04-14 08:58:07', '2025-04-15 20:16:29'),
(30, 'The Notebook', ' Nick Cassavetes', '', 11.99, '210', ' Une histoire d’amour poignante entre deux jeunes gens issus de milieux différents.', 'ressources/images/notebook.jpg', '2025-04-14 08:58:07', '2025-04-15 20:16:29');

-- --------------------------------------------------------

--
-- Table structure for table `video_actors`
--

DROP TABLE IF EXISTS `video_actors`;
CREATE TABLE IF NOT EXISTS `video_actors` (
  `video_id` int NOT NULL,
  `actor_id` int NOT NULL,
  `video_id, actor_id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`video_id, actor_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
