Create database if not exists client;
Use client;

-- Création de la table ENSEIGNANT
CREATE TABLE if not exists Enseignants(
    id_enseignants integer(20),
    date_entree DATE NOT NULL,
    nom VARCHAR(30) NOT NULL,
    prenom VARCHAR(30),
    adresse_mail VARCHAR(100),
    CONSTRAINT pk_enseignant PRIMARY KEY (id_enseignant),
    CONSTRAINT uq_enseignant_email UNIQUE (email)
);
DESCRIBE Enseignants;

-- Création de la table PROMOTION
CREATE TABLE if not exists Promotion (
    id_promotion integer(20),
    annee_promotion integer(4) NOT NULL,
    classe VARCHAR(30) NOT NULL,
    CONSTRAINT pk_promotion PRIMARY KEY (id_promotion),
    CONSTRAINT uq_promotion_annee UNIQUE (annee)
);
DESCRIBE Promotion;

-- Création de la table ETUDIANT
CREATE TABLE if not exists Etudiants(
	id_etudiant integer(20),
    id_promotion integer(20),
    nom VARCHAR(30) NOT NULL,
    prenom VARCHAR(30),
    adresse_mail VARCHAR(100),
    CONSTRAINT pk_etudiant PRIMARY KEY(id_etudiant),
    CONSTRAINT uq_etudiant_email UNIQUE (email),
    CONSTRAINT fk_etudiant foreign key(id_promotion) references promotion(id_promotion)
);
DESCRIBE Etudiants;

-- Création de la table MATIERE
CREATE TABLE if not exists Matieres (
    id_matiere integer(20),
    nom_matiere VARCHAR(100) NOT NULL,
    CONSTRAINT pk_matiere PRIMARY KEY (id_matiere),
    CONSTRAINT uq_matiere_nom UNIQUE (nom)
);
DESCRIBE Matieres;

-- Création de la table NOTE
CREATE TABLE if not exists Notes (
    id_note integer(20),
    id_etudiant integer(20),
    id_matiere integer(20),
    id_enseignant integer(20),
    note integer(2) CHECK (note BETWEEN 0 AND 20),
    date_publication DATE NOT NULL,
    CONSTRAINT pk_note PRIMARY KEY (id_note),
    CONSTRAINT uq_note UNIQUE (id_etudiant, id_matiere),
    CONSTRAINT fk_note_etudiant FOREIGN KEY (id_etudiant) REFERENCES ETUDIANT(id_etudiant) ON DELETE CASCADE,
    CONSTRAINT fk_note_matiere FOREIGN KEY (id_matiere) REFERENCES MATIERE(id_matiere) ON DELETE CASCADE,
    CONSTRAINT fk_note_enseignant FOREIGN KEY (id_enseignant) REFERENCES ENSEIGNANT(id_enseignant) ON DELETE CASCADE
);
DESCRIBE Notes;

-- Création de la table ABSENCE
CREATE TABLE if not exists Absences (
    id_absence integer(20),
    id_etudiant integer(20),
    date DATE NOT NULL,
    minutes_retard integer(4) CHECK (minutes_retard >= 0),
    justifications boolean,
    CONSTRAINT pk_absence PRIMARY KEY (id_absence),
    CONSTRAINT fk_absence_etudiant FOREIGN KEY (id_etudiant) REFERENCES ETUDIANT(id_etudiant) ON DELETE CASCADE
);

DESCRIBE Absences;