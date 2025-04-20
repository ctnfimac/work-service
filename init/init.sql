use `work-database`;

CREATE TABLE trabajo_realizado(
	 id INT AUTO_INCREMENT PRIMARY KEY,
	 foto varchar(50) NOT NULL,
	 descripcion TEXT,
	 jardinero_id INT NOT NULL
);


CREATE TABLE tipo_de_servicio(
	id INT AUTO_INCREMENT PRIMARY KEY,
	foto varchar(50) NOT NULL UNIQUE,
	nombre varchar(30)
);

CREATE TABLE servicio(
	id INT AUTO_INCREMENT PRIMARY KEY,
	descripcion varchar(100),
	precio decimal(10,2) NOT NULL,
	jardinero_id INT NOT NULL,
	tipodeservicio_id INT NOT NULL,
	UNIQUE KEY unique_cliente_jardinero(jardinero_id, tipodeservicio_id)
);


/*INSERT INTO trabajo_realizado(foto, descripcion, jardinero_id)
VALUES('/fotos/trabajo1.jpg', 'trabajo de corte de pasto realizado en x lugar', 1),
('/fotos/1/trabajo2.jpg', 'trabajo de Poda realizado para la señora Victoria', 1),
('/fotos/2/trabajo1.jpg', 'trabajo dificil de poda de pino realizado en ramos mejia', 2);


INSERT INTO tipo_de_servicio(foto, nombre)
VALUES('/fotos/corte_de_pasto.jpg', 'Corte de Pasto'),
('/fotos/poda_de_arboles.jpg','Poda de Arboles'),
('/fotos/fertilizar.jpg','Fertilizar'),
('/fotos/proteccion_de_plantas.jpg','Protección de plantas');


INSERT INTO servicio(descripcion, precio, jardinero_id, tipodeservicio_id)
VALUES('Descripcion puesta por el jardinero dando valor a su servicio', 5000.0, 1, 1),
('Descripcion puesta por el jardinero dando valor a su servicio', 6000.0, 2, 1),
('Descripcion puesta por el jardinero dando valor a su servicio', 7000.0, 1, 2),
('Descripcion puesta por el jardinero dando valor a su servicio', 8000.0, 2, 3),
('Descripcion puesta por el jardinero dando valor a su servicio', 9000.0, 2, 2),
('Descripcion puesta por el jardinero dando valor a su servicio', 10000.0, 1, 4),
('Descripcion puesta por el jardinero dando valor a su servicio', 11000.0, 1, 3),
('Descripcion puesta por el jardinero dando valor a su servicio', 12000.0, 2, 4);*/