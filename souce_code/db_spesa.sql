-- 1) Tabella UTENTI
CREATE TABLE utenti (
    id   INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);

-- 2) Tabella LISTE
CREATE TABLE liste (
    id         INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome       VARCHAR(100) NOT NULL,
    id_utente  INT UNSIGNED NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_liste_utenti
      FOREIGN KEY (id_utente)
      REFERENCES utenti(id)
      ON DELETE CASCADE
);

-- 3) Tabella OGGETTI
CREATE TABLE oggetti (
    id       INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome     VARCHAR(100) NOT NULL,
    id_lista INT UNSIGNED NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_oggetti_liste
      FOREIGN KEY (id_lista)
      REFERENCES liste(id)
      ON DELETE CASCADE
);

-- 4) Constraints
ALTER TABLE utenti ADD CONSTRAINT UNIQUE(nome)
ALTER TABLE liste ADD CONSTRAINT UNIQUE(nome, id_utente)
ALTER TABLE oggetti ADD CONSTRAINT UNIQUE(nome, id_lista)