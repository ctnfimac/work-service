use `work-database`;

CREATE TABLE trabajo_realizado(
	id INT AUTO_INCREMENT PRIMARY KEY,
	foto varchar(50) NOT NULL,
	descripcion TEXT,
	jardinero_id INT NOT NULL,
	created_at TIMESTAMP,
	updated_at TIMESTAMP
);


CREATE TABLE tipo_de_servicio(
	id INT AUTO_INCREMENT PRIMARY KEY,
	foto varchar(50) NOT NULL UNIQUE,
	nombre varchar(30) NOT NULL UNIQUE,
	created_at TIMESTAMP,
	updated_at TIMESTAMP
);


CREATE TABLE servicio(
	id INT AUTO_INCREMENT PRIMARY KEY,
	descripcion varchar(100),
	precio decimal(10,2) NOT NULL,
	jardinero_id INT NOT NULL,
	tipodeservicio_id INT NOT NULL,
	created_at TIMESTAMP,
	updated_at TIMESTAMP,
	UNIQUE KEY unique_tipodeservicio_jardinero(jardinero_id, tipodeservicio_id)
);


