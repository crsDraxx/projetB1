insert into enseignant values (1, '2020-09-01', 'Dupont', 'Sophie', 'sophie.dupont@email.com');
insert into enseignant values (2, '2018-06-15', 'Martin', 'Paul', 'paul.martin@email.com');

insert into promotion values (1,2025,'Meng2');
insert into promotion values (2,2025,'Meng1');

insert into etudiant values (1,1, 'Durand', 'Alice', 'alice.durand@email.com');
insert into etudiant values (2,2, 'Bernard', 'Hugo', 'hugo.bernard@email.com');
insert into etudiant values (3,2, 'Petit', 'Clara', 'clara.petit@email.com');
insert into etudiant values (4,1, 'Morel', 'Lucas', 'lucas.morel@email.com');
insert into etudiant values (5,1, 'Garcia', 'Emma', 'emma.garcia@email.com');
insert into etudiant values (6,2, 'Lemoine', 'Nathan', 'nathan.lemoine@email.com');
insert into etudiant values (7,2, 'Rousseau', 'Juliette', 'juliette.rousseau@email.com');
insert into etudiant values (8,1, 'Fournier', 'Ethan', 'ethan.fournier@email.com');
insert into etudiant values (9,2, 'Germain', 'Camille', 'camille.germain@email.com');
insert into etudiant values (10,1, 'Leclerc', 'Mathis', 'mathis.leclerc@email.com');

insert into matiere values (1,'Développeur de bases de données');
insert into matiere values (2,'Gestion de travail en équipe');

insert into note values (1,1,1,1,15,'2025/02/20');
insert into note values (2,1,2,2,12,'2025/01/15');
insert into note values (3,2,1,1,18,'2025/02/20');
insert into note values (4,2,2,2,9,'2025/01/15');
insert into note values (5,3,1,1,14,'2025/02/20');
insert into note values (6,3,2,2,7,'2025/01/15');
insert into note values (7,4,1,1,19,'2025/02/20');
insert into note values (8,4,2,2,10,'2025/01/15');
insert into note values (9,5,1,1,13,'2025/02/20');
insert into note values (10,5,2,2,16,'2025/01/15');
insert into note values (11,6,1,1,11,'2025/02/20');
insert into note values (12,6,2,2,8,'2025/01/15');
insert into note values (13,7,1,1,17,'2025/02/20');
insert into note values (14,7,2,2,6,'2025/01/15');
insert into note values (15,8,1,1,14,'2025/02/20');
insert into note values (16,8,2,2,9,'2025/01/15');
insert into note values (17,9,1,1,16,'2025/02/20');
insert into note values (18,9,2,2,7,'2025/01/15');
insert into note values (19,10,1,1,18,'2025/02/20');
insert into note values (20,10,2,2,15,'2025/01/15');

insert into absence values (1,3,'2025/02/20',15,0);
insert into absence values (2,1,'2025/02/21',45,1);
insert into absence values (3,10,'2025/01/20',5,1);
insert into absence values (4,5,'2025/01/20',5,1);
insert into absence values (5,3,'2025/02/02',60,0);
insert into absence values (6,7,'2025/01/13',4,1);
insert into absence values (7,3,'2025/02/01',60,0);
insert into absence values (8,6,'2025/01/04',5,0);
insert into absence values (9,1,'2025/02/17',25,1);
insert into absence values (10,4,'2025/01/20',45,1);