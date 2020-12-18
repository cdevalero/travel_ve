create table departamentos (
	deptno numeric (2) PRIMARY KEY,
	nombre varchar (30) NOT NULL,
	loc varchar (15) NOT NULL
);

create table empleados (
	id numeric (4) NOT NULL,
	cedula numeric (10) NOT NULL UNIQUE,
	nombre varchar (10) NOT NULL,
	apellido varchar (10) NOT NULL,
	id_dept numeric (2) NOT NULL,
	salario numeric (8,2),
	cargo varchar (15),
	comision numeric (4,2),
	id_jefe numeric (4),
	id_ced_jefe numeric (10),
	CONSTRAINT pk_emp PRIMARY KEY (id,cedula),
	CONSTRAINT f_jefe FOREIGN KEY (id_jefe,id_ced_jefe) REFERENCES empleados (id,cedula),
	CONSTRAINT f_departamento FOREIGN KEY (id_dept) REFERENCES departamentos (deptno)
);

create table hijos (
	id_emp numeric (4) NOT NULL,
	ced_emp numeric (10) NOT NULL,
	id numeric (2) NOT NULL,
	nombre varchar (10) NOT NULL,
	apellido varchar (10) NOT NULL,
	CONSTRAINT pk_hijos PRIMARY KEY (id_emp, ced_emp, id),
	CONSTRAINT fk_empleado FOREIGN KEY (id_emp, ced_emp) REFERENCES empleados (id, cedula)
)
