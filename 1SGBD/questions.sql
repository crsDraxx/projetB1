-- exercice 1
select nom as first_name, prenom as last_name from etudiant;

-- exercice2
select id_etudiant, date_absence, minutes_retard 
from absence
where justifie = 0 -- non justifie est egale a 0
and minutes_retard > 10
order by minutes_retard desc;

-- exercice 3
select e.nom as last_name, e.prenom as first_name, n.note, n.date_publication, en.email as teacher_emamil
from note n
join etudiant e 
on n.id_etudiant = e.id_etudiant
join enseignant en 
on n.id_enseignant = en.id_enseignant
where n.note between 15 and 20
and YEAR(n.date_publication) = YEAR(CURRENT_DATE);
