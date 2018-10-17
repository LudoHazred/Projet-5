
CREATE TABLE Category (
                idCategory INT AUTO_INCREMENT NOT NULL,
                category VARCHAR(1000) NOT NULL,
                PRIMARY KEY (idCategory)
);


CREATE TABLE Substitute (
                id INT AUTO_INCREMENT NOT NULL,
                idCategory INT NOT NULL,
                category VARCHAR(200) NOT NULL,
                subcategory VARCHAR(200),
                ingredient VARCHAR(5000),
                nutriscore CHAR(10),
                label VARCHAR(1000),
                additive VARCHAR(1000),
                nutrient VARCHAR(1000),
                store VARCHAR(1000),
                bar_code BIGINT,
                link VARCHAR(1000),
                PRIMARY KEY (id, idCategory)
);


CREATE TABLE Food (
                id INT AUTO_INCREMENT NOT NULL,
                idCategory INT NOT NULL,
                category VARCHAR(200) NOT NULL,
                food VARCHAR(400) NOT NULL,
                ingredient VARCHAR(5000),
                additive VARCHAR(1000),
                nutriscore CHAR(10),
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

ALTER TABLE Substitute ADD CONSTRAINT category_substitute_fk
FOREIGN KEY (idCategory)
REFERENCES Category (idCategory)
ON DELETE NO ACTION
ON UPDATE NO ACTION;
