-- -----------------------------------------------------
-- Schema feelback
-- -----------------------------------------------------
DROP DATABASE IF EXISTS feelback;
-- -----------------------------------------------------
--
-- -----------------------------------------------------
CREATE DATABASE feelback;
-- -----------------------------------------------------
-- 
-- -----------------------------------------------------
USE `feelback` ;

-- -----------------------------------------------------
-- Table `feelback`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `feelback`.`users` (
  `id_users` INT NOT NULL AUTO_INCREMENT,
  `email_users` VARCHAR(255) NOT NULL,
  `password_users` VARCHAR(255) NOT NULL,
  `create_at_users` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at_users` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `delete_at_users` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_users`));

-- -----------------------------------------------------
-- Table `feelback`.`forms`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `feelback`.`forms` (
  `id_forms` INT NOT NULL AUTO_INCREMENT,
  `name_forms` VARCHAR(45) NOT NULL,
  `created_at_forms` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at_forms` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `delete_at_forms` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `users_id` INT NOT NULL,
  PRIMARY KEY (`id_forms`),
  INDEX `FK_users_id_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `FK_users_id_forms`
    FOREIGN KEY (`users_id`)
    REFERENCES `feelback`.`users` (`id_users`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `feelback`.`packages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `feelback`.`packages` (
  `id_packages` INT NOT NULL AUTO_INCREMENT,
  `create_at_packages` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `delete_at_packages` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `forms_id` INT NOT NULL,
  `users_id` INT NOT NULL,
  PRIMARY KEY (`id_packages`),
  INDEX `FK_forms_id_idx` (`forms_id` ASC) VISIBLE,
  INDEX `FK_users_id_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `FK_forms_id_packages`
    FOREIGN KEY (`forms_id`)
    REFERENCES `feelback`.`forms` (`id_forms`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `FK_users_id_packages`
    FOREIGN KEY (`users_id`)
    REFERENCES `feelback`.`users` (`id_users`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `feelback`.`questions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `feelback`.`questions` (
  `id_questions` INT NOT NULL AUTO_INCREMENT,
  `title_questions` VARCHAR(150) NOT NULL,
  `created_at_questions` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at_questions` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `delete_at_questions` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `forms_id` INT NOT NULL,
  PRIMARY KEY (`id_questions`),
  INDEX `FK_forms_id_idx` (`forms_id` ASC) VISIBLE,
  CONSTRAINT `FK_forms_id_questions`
    FOREIGN KEY (`forms_id`)
    REFERENCES `feelback`.`forms` (`id_forms`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `feelback`.`answers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `feelback`.`answers` (
  `id_answers` INT NOT NULL AUTO_INCREMENT,
  `value_answers` TINYINT NOT NULL,
  `created_at_answers` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at_answers` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `delete_at_answers` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `questions_id` INT NOT NULL,
  `users_id` INT NOT NULL,
  PRIMARY KEY (`id_answers`),
  INDEX `FK_questions_id_idx` (`questions_id` ASC) VISIBLE,
  INDEX `FK_users_id_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `FK_questions_id`
    FOREIGN KEY (`questions_id`)
    REFERENCES `feelback`.`questions` (`id_questions`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `FK_users_id`
    FOREIGN KEY (`users_id`)
    REFERENCES `feelback`.`users` (`id_users`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
KEY_BLOCK_SIZE = 1;



-- -----------------------------------------------------
-- Donnée à rentrer
-- -----------------------------------------------------
INSERT INTO users (email_users,password_users) VALUES ('user1@user', 'user1');
INSERT INTO forms (name_forms, users_id) VALUES ('Le questionnaire de satisfaction',1);
INSERT INTO questions (title_questions, forms_id) 
VALUES ('Évaluer de 1 à 5 le respect du délai de livraison',1),
      ('Évaluer de 1 à 5 l\'état de votre colis à sa réception',1),
      ('Évaluer de 1 à 5 le comportement du livreur',1);







