<?php

$video_id = $_GET['id'];
$query = "SELECT v.*, d.name AS director_name, d.id AS director_id 
          FROM videos v
          JOIN directors d ON v.director_id = d.id
          WHERE v.id = ?";
$stmt = $pdo->prepare($query);
$stmt->execute([$video_id]);
$video = $stmt->fetch();
?>

<h2><?= htmlspecialchars($video['title']) ?></h2>
<p>Released by : 
   <a href="films_by_director.php?id=<?= $video['director_id'] ?>">
      <?= htmlspecialchars($video['director_name']) ?>
   </a>
</p>
