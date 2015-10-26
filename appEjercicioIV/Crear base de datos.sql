/**
  Fichero de creación de la base de datos de SMM--
  Uso:
    > mysql -u root -p < DBCreator.sql
  Ejecutado en el mismo directorio que este fichero.

**/
use CALIFICACIONES_DB;

CREATE TABLE EMPRESAS (
	Codigo_empresa int(3) auto_increment, 	
	Nombre varchar(50) not null,
	Ciudad varchar(50) not null,
	PRIMARY KEY (Codigo_empresa)
);

CREATE TABLE USUARIOS (
	Codigo_usuario int(3) auto_increment,
	Nombre varchar(50) not null,
	Ciudad varchar(50) not null,
	PRIMARY KEY (Codigo_usuario)
);

CREATE TABLE CALIFICA(
	Codigo_usuario int,
	Codigo_empresa int,
	Nota int,
	FOREIGN KEY (Codigo_usuario) REFERENCES USUARIOS(Codigo_usuario),
	FOREIGN KEY (Codigo_empresa) REFERENCES EMPRESAS(Codigo_empresa),
	PRIMARY KEY (Codigo_usuario, Codigo_empresa)
);	
