CREATE DATABASE craftsystem;

USE craftsystem;

CREATE TABLE users(
    username varchar(20) NOT NULL PRIMARY KEY,
    password varchar(32) NOT NULL,
    privilege integer NOT NULL DEFAULT -1,
    status integer NOT NULL DEFAULT 1,
    name varchar(150) NOT NULL,
    email varchar(100) NOT NULL,
    other_data varchar(50) NOT NULL,
    user_hash varchar(32) NOT NULL,
    change_pwd integer NOT NULL DEFAULT 1,
    created timestamp NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE sessions(
    session_id char(128) UNIQUE NOT NULL,
    atime timestamp NOT NULL default current_timestamp,
    data text
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE logs( 
    id_log integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username varchar(20) NOT NULL,
    ip varchar(16) NOT NULL,
    access timestamp NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE evento(
    ->     id_evento integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    ->     titulo varchar (30) NOT NULL,
    ->     descripcion varchar (100) NOT NULL,
    ->     fecha varchar(20) NOT NULL,
    ->     hora varchar (15) NOT NULL,
    ->     ubicacion varchar(50) NOT NULL,
    ->     organizador varchar(50) NOT NULL
    -> )ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE organizadores( 
    id_organizador integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre varchar (30) NOT NULL,
    apellido_paterno varchar (100) NOT NULL,
    apellido_materno varchar(20) NOT NULL,
    empresa varchar (15) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE ofertas( 
    id_oferta integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    descripcion varchar (50) NOT NULL,
    puesto varchar (50) NOT NULL,
    evento varchar(50) NOT NULL,
    fecha varchar (50) NOT NULL,
    hora varchar (50) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE ubicacion(
    ->     id_ubicacion integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    ->     latitud varchar (50) NOT NULL,
    ->     longitud varchar (50) NOT NULL,
    ->     evento varchar (50) NOT NULL
    -> )ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO evento(titulo,descripcion,fecha,hora,ubicacion,organizador)VALUES
    -> ('talent land','encuentro de talentos','22 - 26 de abril','10:00 am', 'resinto de expo de jalisco','mario'),
    -> ('feria del libro','encuentro de autores reconocidos de libros','7 - 10 de abril','09:00 am', 'centro cultural de tulancingo','pablo'),
    -> ('proyect','demostracion de proyectos','12 de abril','09:30 am','UTEC Tulancingo','pedro');

INSERT INTO ubicacion(latitud,longitud,evento)VALUES
    -> ('20.083959 ','-98.363538','feria del elote'),
    -> ('20.083959 ','-98.363538','feria del guajolote'),
    -> ('20.083959 ','-98.363538','feria del libro');

INSERT INTO organizadores(nombre,apellido_paterno,apellido_materno,empresa)VALUES
('mario','palomo','suarez','minter'),
('pablo','perez','gil','mjhdh'),
('pedro','aranda','castro','yrfh');

INSERT INTO ofertas(descripcion,puesto,evento,fecha,hora)VALUES
('lleva 2 x 1',5,'latent land','22 al 26 de abril','10:00 - 12:00'),
('lleva 2 x 6',9,'latent land','22 al 26 de abril','10:00 - 10:00'),
('lleva 2 x 3',6,'latent land','22 al 26 de abril','10:00 - 11:00');


INSERT INTO users (username, password, privilege, status, name, email, other_data, user_hash, change_pwd)
VALUES ('admin',MD5(concat('admin', 'kuorra_key')), 0, 1, 'Admin', 'admin@gmail.com','TIC:SI', MD5(concat('admin', 'kuorra_key', '2016/06/04')), 0),
('guess',MD5(concat('guess', 'kuorra_key')), 1, 1, 'Guess', 'guess@gmail.com','TIC:SI', MD5(concat('guess', 'kuorra_key','2016/06/04')), 0);


SELECT * FROM users;
SELECT * FROM sessions;
