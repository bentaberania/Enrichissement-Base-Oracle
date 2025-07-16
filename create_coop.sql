  CREATE TABLE vinR (
    Nvin integer,
    Cru VARCHAR(30),
    Degre real NOT NULL CHECK (Degre BETWEEN 5 AND 15),
    CONSTRAINT k_vin primary key(nvin)
    );
    
  CREATE TABLE producteurR (
    Nprod integer,
    Nom VARCHAR(30),
    Prenom VARCHAR(30),
    Region VARCHAR(20),
    CONSTRAINT k_prod primary key(nprod)
    );
    
  CREATE TABLE recolteR (
    Nprod integer,
    Nvin integer,
    Annee INTEGER,
    Qte real,
    constraint k_recolte PRIMARY KEY(Nprod, Nvin, Annee),
    CONSTRAINT vin_fk FOREIGN KEY (Nvin) REFERENCES vinR,
    CONSTRAINT prod_fk FOREIGN KEY (Nprod) REFERENCES producteurR
    );
