
CREATE TABLE Category (
                idCategory INT AUTO_INCREMENT NOT NULL,
                category VARCHAR(1000) NOT NULL,
                PRIMARY KEY (idCategory)
);


CREATE TABLE History (
                id_research INT AUTO_INCREMENT NOT NULL,
                foodStart VARCHAR(1000) NOT NULL,
                substitute VARCHAR(1000) NOT NULL,
                PRIMARY KEY (id_research)
);


CREATE TABLE Substitute (
                id INT AUTO_INCREMENT NOT NULL,
                id_research INT NOT NULL,
                category VARCHAR(200) NOT NULL,
                subcategory VARCHAR(200),
                ingredient VARCHAR(1000) NOT NULL,
                nutriscore CHAR(1),
                label VARCHAR(1000),
                additive VARCHAR(1000),
                nutrient VARCHAR(1000),
                store VARCHAR(1000),
                bar_code BIGINT NOT NULL,
                link VARCHAR(1000),
                PRIMARY KEY (id, id_research)
);


CREATE TABLE FoodStart (
                id INT AUTO_INCREMENT NOT NULL,
                id_research INT NOT NULL,
                category VARCHAR(200) NOT NULL,
                subcategory VARCHAR(200),
                ingredient VARCHAR(1000) NOT NULL,
                nutriscore CHAR(1),
                additive VARCHAR(1000),
                label VARCHAR(1000),
                nutrient VARCHAR(1000),
                store VARCHAR(1000),
                bar_code BIGINT NOT NULL,
                PRIMARY KEY (id, id_research)
);


CREATE TABLE Food (
                id INT AUTO_INCREMENT NOT NULL,
                idCategory INT NOT NULL,
                category VARCHAR(200) NOT NULL,
                subcategory VARCHAR(200),
                food VARCHAR(400) NOT NULL,
                ingredient VARCHAR(1000) NOT NULL,
                additive VARCHAR(1000),
                nutriscore CHAR(1) NOT NULL,
                nutrient VARCHAR(1000),
                label VARCHAR(1000),
                store VARCHAR(1000),
                bar_code BIGINT,
                PRIMARY KEY (id, idCategory)
);


ALTER TABLE Food ADD CONSTRAINT category_food_fk
FOREIGN KEY (idCategory)
REFERENCES Category (idCategory)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE FoodStart ADD CONSTRAINT history_foodstart_fk
FOREIGN KEY (id_research)
REFERENCES History (id_research)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE Substitute ADD CONSTRAINT history_substitute_fk
FOREIGN KEY (id_research)
REFERENCES History (id_research)
ON DELETE NO ACTION
ON UPDATE NO ACTION;
