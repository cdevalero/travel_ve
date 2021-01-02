CREATE SEQUENCE cgr_secuencia_bancos
	start with 1
	increment 1
	minvalue 1
	maxvalue 1000
;

CREATE TABLE cgr_bancos
(
	id_banco numeric NOT NULL DEFAULT nextval('cgr_secuencia_bancos'::regclass),
	nombre_banco varchar(75) NOT NULL,
	CONSTRAINT pk_bancos PRIMARY KEY (id_banco)
);

CREATE TABLE cgr_clientes
(
	doc_identidad_o_rif numeric NOT NULL,
	nombre_cliente varchar(75) NOT NULL,
	tipo_cliente varchar(10) NOT NULL,
	primer_apellido varchar(30) DEFAULT '',
	segundo_apellido varchar(30) DEFAULT '',
	CONSTRAINT pk_clientes PRIMARY KEY (doc_identidad_o_rif),
	CONSTRAINT chk_tipo_cliente CHECK(tipo_cliente in ('natural','juridico'))
);

CREATE SEQUENCE cgr_secuencia_areas_de_interes
	start with 1
	increment 1
	minvalue 1
	maxvalue 5000
;

CREATE TABLE cgr_areas_de_interes
(
	id_areas_de_interes numeric NOT NULL DEFAULT nextval('cgr_secuencia_areas_de_interes'::regclass),
	nombre_area_de_interes varchar(75) NOT NULL UNIQUE,
	descripcion_area_de_interes varchar NOT NULL,
	CONSTRAINT pk_areas_de_interes PRIMARY KEY (id_areas_de_interes)
);

CREATE SEQUENCE cgr_secuencia_paises
	start with 1
	increment 1
	minvalue 1
	maxvalue 230
;

CREATE TABLE cgr_paises
(
	id_pais numeric NOT NULL DEFAULT nextval('cgr_secuencia_paises'::regclass),
	nombre_pais varchar(75) NOT NULL UNIQUE,
	region_pais varchar NOT NULL,
	continente_pais varchar(10) NOT NULL,
	nacionalidad varchar NOT NULL UNIQUE,
	descripcion_pais varchar NOT NULL,
	CONSTRAINT pk_paises PRIMARY KEY (id_pais),
	CONSTRAINT chk_region_pais CHECK(region_pais in ('EU', 'AF_MO', 'AU_NZ_PAS','AS','MEX_CEN_SUR','USA_CAN_CAR')),
	CONSTRAINT chk_continente_pais CHECK(continente_pais in ('Asia','Africa','Oceania','Europa','America'))
);

CREATE SEQUENCE cgr_secuencia_rallies
	start with 1
	increment 1
	minvalue 1
	maxvalue 5000
;

CREATE TABLE cgr_rallies
(
	id_rally numeric NOT NULL DEFAULT nextval('cgr_secuencia_rallies'::regclass),
	nombre_rally varchar(30) NOT NULL UNIQUE,
	costo_participante numeric(16,4) NOT NULL,
	f_inicio date NOT NULL,
	f_fin date NOT NULL,
	tipo_rally varchar(15) NOT NULL,
	duracion numeric NOT NULL,
	total_cupo_participante numeric NOT NULL,
	CONSTRAINT pk_rallies PRIMARY KEY (id_rally),
	CONSTRAINT chk_tipo_rally CHECK(tipo_rally in ('individual','pareja'))
);

CREATE SEQUENCE cgr_secuencia_premios
	start with 1
	increment 1
	minvalue 1
	maxvalue 100
;

CREATE TABLE cgr_premios
(
	id_premio numeric NOT NULL DEFAULT nextval('cgr_secuencia_rallies'::regclass),
	id_rally numeric NOT NULL,
	posicion numeric NOT NULL,
	descripcion_premio varchar,
	CONSTRAINT pk_premios PRIMARY KEY (id_premio, id_rally),
	CONSTRAINT fk_id_rally_premio FOREIGN KEY (id_rally) REFERENCES cgr_rallies(id_rally) ON DELETE CASCADE
);

CREATE SEQUENCE cgr_secuencia_ciudades
	start with 1
	increment 1
	minvalue 1
	maxvalue 100
;

CREATE TABLE cgr_ciudades
(
	id_ciudad numeric NOT NULL DEFAULT nextval('cgr_secuencia_ciudades'::regclass),
	id_pais numeric NOT NULL,
	nombre_ciudad varchar(60) NOT NULL,
	tipo_ciudad varchar(11) NOT NULL,
	descripcion_ciudad varchar NOT NULL,
	CONSTRAINT pk_ciudades PRIMARY KEY (id_ciudad, id_pais),
	CONSTRAINT chk_tipo_ciudad CHECK(tipo_ciudad in ('localidad','ciudad')),
	CONSTRAINT fk_id_pais_ciudad FOREIGN KEY (id_pais) REFERENCES cgr_paises(id_pais) ON DELETE CASCADE
);

CREATE SEQUENCE cgr_secuencia_atracciones
	start with 1
	increment 1
	minvalue 1
	maxvalue 100
;

CREATE TABLE cgr_atracciones
(
	id_atraccion numeric NOT NULL DEFAULT nextval('cgr_secuencia_atracciones'::regclass),
	id_ciudad numeric NOT NULL,
	id_pais numeric NOT NULL,
	nombre_atraccion varchar(60) NOT NULL,
	descripcion_atraccion varchar NOT NULL,
	CONSTRAINT pk_atracciones PRIMARY KEY (id_atraccion, id_ciudad, id_pais),
	CONSTRAINT fk_id_ciudad_atraccion_id_pais_ciudad_atraccion FOREIGN KEY (id_ciudad, id_pais) REFERENCES cgr_ciudades(id_ciudad,id_pais) ON DELETE CASCADE
);

CREATE TABLE cgr_circuitos
(
	orden_circuito numeric NOT NULL,
	id_rally numeric NOT NULL,
	id_ciudad numeric NOT NULL,
	id_pais numeric NOT NULL,
	maxdias numeric NOT NULL,
	CONSTRAINT pk_circuitos  PRIMARY KEY (orden_circuito, id_rally, id_ciudad,id_pais),
	CONSTRAINT fk1_id_ciudad_id_pais_ciudad_circuito FOREIGN KEY (id_ciudad, id_pais) REFERENCES cgr_ciudades(id_ciudad,id_pais) ON DELETE CASCADE,
	CONSTRAINT fk2_id_rally_circuito FOREIGN KEY (id_rally) REFERENCES cgr_rallies(id_rally) ON DELETE CASCADE
);

CREATE TABLE cgr_atr_cir
(
	id_atraccion numeric NOT NULL,
	id_ciudad_at numeric NOT NULL,
	id_pais_at numeric NOT NULL,
	id_circuito numeric NOT NULL,
	id_rally_cir numeric NOT NULL,
	id_ciudad_cir numeric NOT NULL,
	id_pais_cir numeric NOT NULL,
	orden numeric,
	CONSTRAINT pk_atr_cir  PRIMARY KEY (id_atraccion,id_ciudad_at,id_pais_at,id_circuito,id_rally_cir,id_ciudad_cir,id_pais_cir),
	CONSTRAINT fk1_atracciones FOREIGN KEY (id_atraccion,id_ciudad_at,id_pais_at) REFERENCES cgr_atracciones(id_atraccion,id_ciudad, id_pais) ON DELETE CASCADE,
	CONSTRAINT fk2_circuitos FOREIGN KEY (id_circuito,id_rally_cir,id_ciudad_cir,id_pais_cir) REFERENCES cgr_circuitos(orden_circuito,id_rally,id_ciudad,id_pais) ON DELETE CASCADE
);

CREATE SEQUENCE cgr_secuencia_agencias_de_viajes
	start with 1
	increment 1
	minvalue 1
	maxvalue 100
;

CREATE TABLE cgr_agencias_de_viajes
(
	id_agencia numeric NOT NULL DEFAULT nextval('cgr_secuencia_agencias_de_viajes'::regclass),
	nombre varchar(50) NOT NULL,
	tipo_de_operacion varchar(3) NOT NULL,
	alcance_geografico varchar(3) NOT NULL,
	web varchar,
	telefono numeric,
	calle_av varchar,
	id_ciudad numeric,
	id_pais numeric,
	descripcion varchar,
	CONSTRAINT pk_agencias PRIMARY KEY (id_agencia),
	CONSTRAINT chk_tipo_de_operacion CHECK(tipo_de_operacion in ('T','W','R','M')),
	CONSTRAINT chk_alcance_geografico CHECK(alcance_geografico in ('I','N','L')),
	CONSTRAINT fk_id_ciudad_agencia_id_pais_agencia FOREIGN KEY (id_ciudad,id_pais) REFERENCES cgr_ciudades(id_ciudad,id_pais) ON DELETE CASCADE
);

CREATE TABLE cgr_age_age
(
	id_agencia numeric NOT NULL,
	id_socio numeric NOT NULL,
	f_inicio date NOT NULL,
	f_fin date,
	CONSTRAINT pk_age_age PRIMARY KEY (id_agencia,id_socio),
	CONSTRAINT fk1_id_agencia_age_age FOREIGN KEY (id_agencia) REFERENCES cgr_agencias_de_viajes(id_agencia) ON DELETE CASCADE,
	CONSTRAINT fk2_id_socio_age_age FOREIGN KEY (id_socio) REFERENCES cgr_agencias_de_viajes(id_agencia) ON DELETE CASCADE
);

CREATE TABLE cgr_cupos
(
	id_agencia numeric NOT NULL,
	id_rally numeric NOT NULL,
	cantidad numeric,
	CONSTRAINT pk_cupos PRIMARY KEY (id_agencia,id_rally),
	CONSTRAINT fk_id_agencia_cupo FOREIGN KEY (id_agencia) REFERENCES cgr_agencias_de_viajes(id_agencia) ON DELETE CASCADE,
	CONSTRAINT fk_id_rally_cupo FOREIGN KEY (id_rally) REFERENCES cgr_rallies(id_rally) ON DELETE CASCADE
);

CREATE TABLE cgr_registro_clientes
(
	id_cliente numeric NOT NULL,
	id_agencia numeric NOT NULL,
	f_registro date NOT NULL,
	numero_registro numeric NOT NULL,
	CONSTRAINT pk_registros_clientes PRIMARY KEY (id_cliente,id_agencia),
	CONSTRAINT fk1_id_cliente_registro_clientes FOREIGN KEY (id_cliente) REFERENCES cgr_clientes(doc_identidad_o_rif) ON DELETE CASCADE,
	CONSTRAINT fk2_id_agencia_registro_clientes FOREIGN KEY (id_agencia) REFERENCES cgr_agencias_de_viajes(id_agencia) ON DELETE CASCADE
);

CREATE SEQUENCE cgr_secuencia_alojamientos 
	start with 1
	increment 1
	minvalue 1
	maxvalue 100
;

CREATE TABLE cgr_alojamientos
(
	id_alojamiento numeric NOT NULL DEFAULT nextval('cgr_secuencia_alojamientos'::regclass),
	id_ciudad numeric NOT NULL,
	id_pais numeric NOT NULL,
	nombre varchar NOT NULL,
	CONSTRAINT pk_alojamientos PRIMARY KEY (id_alojamiento),
	CONSTRAINT fk_id_ciudad_id_pais_alojamientos FOREIGN KEY (id_ciudad,id_pais) REFERENCES cgr_ciudades(id_ciudad,id_pais) ON DELETE CASCADE
);

CREATE SEQUENCE cgr_secuencia_proveedores
	start with 1
	increment 1
	minvalue 1
	maxvalue 100
;

CREATE TABLE cgr_proveedores
(
	id_proveedor numeric NOT NULL DEFAULT nextval('cgr_secuencia_proveedores'::regclass),
	id_alojamiento numeric NOT NULL,
	nombre_proveedor varchar(30) NOT NULL,
	tipo_proveedor varchar(20) NOT NULL,
	CONSTRAINT pk_proveedores PRIMARY KEY (id_proveedor),
	CONSTRAINT chk_tipo_proveedor CHECK(tipo_proveedor in ('exclusivo','multiagencias')),
	CONSTRAINT fk_id_alojamiento FOREIGN KEY (id_alojamiento) REFERENCES cgr_alojamientos(id_alojamiento) ON DELETE CASCADE
);

CREATE TABLE cgr_pro_age
(
	id_agencia numeric NOT NULL,
	id_proveedor numeric NOT NULL,
	f_inicio date NOT NULL,
	f_fin date,
	CONSTRAINT pk_pro_age PRIMARY KEY (id_agencia,id_proveedor),
	CONSTRAINT fk_id_agencia FOREIGN KEY (id_agencia) REFERENCES cgr_agencias_de_viajes(id_agencia) ON DELETE CASCADE,
	CONSTRAINT fk_id_proovedor FOREIGN KEY (id_proveedor) REFERENCES cgr_proveedores(id_proveedor) ON DELETE CASCADE
);

CREATE SEQUENCE cgr_secuencia_asesores_de_viajes
	start with 1
	increment 1
	minvalue 1
	maxvalue 100
;


CREATE TABLE cgr_asesores_de_viajes
(
	id_asesor numeric NOT NULL DEFAULT nextval('cgr_secuencia_asesores_de_viajes'::regclass),
	primer_nombre varchar(20) NOT NULL,
	primer_apellido varchar(20) NOT NULL,
	segundo_apellido varchar(20) NOT NULL,
	telefono numeric NOT NULL,
	segundo_nombre varchar(20),
	CONSTRAINT pk_asesores_de_viajes PRIMARY KEY (id_asesor)
);

CREATE SEQUENCE cgr_secuencia_paquetes
	start with 1
	increment 1
	minvalue 1
	maxvalue 100
;


CREATE TABLE cgr_paquetes
(
	id_paquete numeric NOT NULL DEFAULT nextval('cgr_secuencia_paquetes'::regclass),
	id_agencia numeric NOT NULL,
	nombre_paquete varchar(30) NOT NULL,
	duracion_dias numeric NOT NULL,
	descripcion_turistica varchar NOT NULL,
	disponible boolean,
	numero_personas numeric,
	CONSTRAINT pk_paquetes PRIMARY KEY (id_paquete,id_agencia),
	CONSTRAINT fk_id_agencia FOREIGN KEY (id_agencia) REFERENCES cgr_agencias_de_viajes(id_agencia) ON DELETE CASCADE
);

CREATE SEQUENCE cgr_secuencia_especializaciones
	start with 1
	increment 1
	minvalue 1
	maxvalue 100
;


CREATE TABLE cgr_especializaciones
(
	id_especializacion numeric NOT NULL DEFAULT nextval('cgr_secuencia_especializaciones'::regclass),
	id_areas_de_interes numeric NOT NULL,
	id_atraccion numeric ,
	id_ciudad numeric ,
	id_pais numeric ,
	id_agencia numeric ,
	id_paquete numeric ,
	id_agencia_paquete numeric ,
	id_asesor numeric ,
	comentarios varchar ,
	CONSTRAINT pk_especializaciones PRIMARY KEY (id_especializacion,id_areas_de_interes),
	CONSTRAINT fk1_areas_de_interes FOREIGN KEY (id_areas_de_interes) REFERENCES cgr_areas_de_interes(id_areas_de_interes) ON DELETE CASCADE,
	CONSTRAINT fk2_atracciones FOREIGN KEY (id_atraccion,id_ciudad,id_pais) REFERENCES cgr_atracciones(id_atraccion,id_ciudad,id_pais) ON DELETE CASCADE,
	CONSTRAINT fk3_agencias_de_viajes FOREIGN KEY (id_agencia) REFERENCES cgr_agencias_de_viajes(id_agencia) ON DELETE CASCADE,
	CONSTRAINT fk4_paquetes FOREIGN KEY (id_paquete,id_agencia_paquete) REFERENCES cgr_paquetes(id_paquete,id_agencia) ON DELETE CASCADE,
	CONSTRAINT fk5_asesores_de_viajes FOREIGN KEY (id_asesor) REFERENCES cgr_asesores_de_viajes(id_asesor) ON DELETE CASCADE
);

CREATE TABLE cgr_precios_paquetes
(
	f_inicio  timestamp NOT NULL DEFAULT LOCALTIMESTAMP,
	id_paquete numeric NOT NULL,
	id_agencia numeric NOT NULL,
	f_fin timestamp, 
	valor numeric,
	CONSTRAINT pk_precios_paquetes PRIMARY KEY (f_inicio,id_paquete,id_agencia),
	CONSTRAINT fk_paquetes FOREIGN KEY (id_paquete,id_agencia) REFERENCES cgr_paquetes(id_paquete,id_agencia) ON DELETE CASCADE
);

CREATE TABLE cgr_calendarios_anuales
(
	f_salida  timestamp NOT NULL DEFAULT LOCALTIMESTAMP,
	id_paquete numeric NOT NULL,
	id_agencia numeric NOT NULL,
	descripcion varchar,
	CONSTRAINT pk_calendarios_anuales PRIMARY KEY (f_salida,id_paquete,id_agencia),
	CONSTRAINT fk_paquetes FOREIGN KEY (id_paquete,id_agencia) REFERENCES cgr_paquetes(id_paquete,id_agencia) ON DELETE CASCADE
);

CREATE SEQUENCE cgr_secuencia_descuentos
	start with 1
	increment 1
	minvalue 1
	maxvalue 100
;

CREATE TABLE cgr_descuentos
(
	id_descuento numeric NOT NULL DEFAULT nextval('cgr_secuencia_descuentos'::regclass),
	id_agencia numeric NOT NULL,
	f_inicio  date NOT NULL,
	tipo_descuento varchar(20) NOT NULL,
	f_fin  date,
	cant_per_gratis numeric,
	porcentaje numeric,
	CONSTRAINT pk_descuentos PRIMARY KEY (id_descuento,id_agencia),
	CONSTRAINT chk_tipo_descuento CHECK(tipo_descuento in ('desnino','adultos','general','viajerosgratis','otros')),
	CONSTRAINT fk_agencias_de_viajes FOREIGN KEY (id_agencia) REFERENCES cgr_agencias_de_viajes(id_agencia) ON DELETE CASCADE
);

CREATE TABLE cgr_itinerarios
(
	orden numeric NOT NULL,
	id_paquete numeric NOT NULL,
	id_agencia numeric NOT NULL,
	id_ciudad numeric NOT NULL,
	id_pais numeric NOT NULL,
	tiempo_estadia numeric,
	CONSTRAINT pk_itinerarios PRIMARY KEY (orden,id_paquete,id_agencia,id_ciudad,id_pais),
	CONSTRAINT fk1_paquetes FOREIGN KEY (id_paquete,id_agencia) REFERENCES cgr_paquetes(id_paquete,id_agencia) ON DELETE CASCADE,
	CONSTRAINT fk2_ciudades FOREIGN KEY (id_ciudad,id_pais) REFERENCES cgr_ciudades(id_ciudad,id_pais) ON DELETE CASCADE
);

CREATE TABLE cgr_itn_atr
(
	id_itinerario numeric NOT NULL,
	id_paquete numeric NOT NULL,
	id_agencia numeric NOT NULL,
	id_ciudad numeric NOT NULL,
	id_pais numeric NOT NULL,
	id_atraccion numeric NOT NULL,
	id_ciudad_at numeric NOT NULL,
	id_pais_at numeric NOT NULL,
	orden_visita numeric NOT NULL,
	CONSTRAINT pk_itn_atr PRIMARY KEY (id_itinerario,id_paquete ,id_agencia ,id_ciudad ,id_pais ,id_atraccion,id_ciudad_at ,id_pais_at ),
	CONSTRAINT fk1_itinerarios FOREIGN KEY (id_itinerario,id_paquete ,id_agencia ,id_ciudad ,id_pais) REFERENCES cgr_itinerarios(orden,id_paquete ,id_agencia ,id_ciudad ,id_pais) ON DELETE CASCADE,
	CONSTRAINT fk2_atracciones FOREIGN KEY (id_atraccion,id_ciudad_at ,id_pais_at) REFERENCES cgr_atracciones(id_atraccion,id_ciudad,id_pais) ON DELETE CASCADE
);

CREATE SEQUENCE cgr_secuencia_detalles_servicios
	start with 1
	increment 1
	minvalue 1
	maxvalue 100
;

CREATE TABLE cgr_detalles_servicios
(
	id_detalle_servicio numeric NOT NULL DEFAULT nextval('cgr_secuencia_detalles_servicios'::regclass),
	id_itinerario numeric NOT NULL,
	id_paquete numeric NOT NULL,
	id_agencia numeric NOT NULL,
	id_ciudad numeric NOT NULL,
	id_pais numeric NOT NULL,
	tipo_detalle varchar(30) NOT NULL,
	descripcion varchar NOT NULL,
	comida boolean,
	CONSTRAINT pk_detalles_servicios PRIMARY KEY (id_detalle_servicio, id_itinerario, id_paquete, id_agencia, id_ciudad, id_pais),
	CONSTRAINT chk_tipo_detalle CHECK(tipo_detalle in ('boleto_avion', 'boleto_tren', 'boleto_autobus','cama_alq','alojamiento','otro')),
	CONSTRAINT fk1_itinerarios FOREIGN KEY (id_itinerario,id_paquete ,id_agencia ,id_ciudad ,id_pais) REFERENCES cgr_itinerarios(orden,id_paquete ,id_agencia ,id_ciudad ,id_pais) ON DELETE CASCADE
);

CREATE TABLE cgr_alo_det
(
	id_detalle_servicio numeric NOT NULL ,
	id_itinerario numeric NOT NULL,
	id_paquete numeric NOT NULL,
	id_agencia numeric NOT NULL,
	id_ciudad numeric NOT NULL,
	id_pais numeric NOT NULL,
	id_alojamiento numeric NOT NULL,
	CONSTRAINT pk_alo_detalle PRIMARY KEY (id_detalle_servicio,id_itinerario,id_paquete,id_agencia,id_ciudad,id_pais,id_alojamiento),
	CONSTRAINT fk1_detalles_servicios FOREIGN KEY (id_detalle_servicio,id_itinerario,id_paquete,id_agencia,id_ciudad,id_pais) REFERENCES cgr_detalles_servicios(id_detalle_servicio,id_itinerario,id_paquete,id_agencia,id_ciudad,id_pais) ON DELETE CASCADE,
	CONSTRAINT fk2_alojamientos FOREIGN KEY (id_alojamiento) REFERENCES cgr_alojamientos(id_alojamiento) ON DELETE CASCADE
);

CREATE SEQUENCE cgr_secuencia_instrumentos_de_pago
	start with 1
	increment 1
	minvalue 1
	maxvalue 100
;

CREATE TABLE cgr_instrumentos_de_pago
(
	id_instrumento numeric NOT NULL DEFAULT nextval('cgr_secuencia_instrumentos_de_pago'::regclass),
	doc_identidad_cliente numeric NOT NULL,
	monto numeric NOT NULL,
	tipo_instrumento varchar NOT NULL,
	id_banco numeric,
	numero_zelle numeric,
	email_zelle varchar,
	CONSTRAINT pk_instrumentos_de_pago PRIMARY KEY (id_instrumento,doc_identidad_cliente),
	CONSTRAINT chk_tipo_instrumento CHECK(tipo_instrumento in ('TDC','TDD','ctabanco','zelle')),
	CONSTRAINT fk_clientes FOREIGN KEY (doc_identidad_cliente) REFERENCES cgr_clientes(doc_identidad_o_rif) ON DELETE CASCADE,
	CONSTRAINT fk_bancos FOREIGN KEY (id_banco) REFERENCES cgr_bancos(id_banco) ON DELETE CASCADE
);

CREATE SEQUENCE cgr_secuencia_paquetes_contrato
	start with 1
	increment 1
	minvalue 1
	maxvalue 100
;

CREATE TABLE cgr_paquetes_contrato
(
	numero_factura numeric NOT NULL DEFAULT nextval('cgr_secuencia_paquetes_contrato'::regclass),
	id_paquete numeric NOT NULL,
	id_agencia numeric NOT NULL,
	id_reg_cliente numeric NOT NULL,
	id_reg_agencia numeric NOT NULL,
	presupuesto numeric NOT NULL,
	f_aprobacion date NOT NULL,
	f_emision date NOT NULL,
	email_validacion varchar NOT NULL,
	total_costo_calculado numeric NOT NULL,
	numer_de_viajeros numeric NOT NULL,
	f_viaje date NOT NULL,
	id_asesor numeric,
	CONSTRAINT pk_paquetes_contrato PRIMARY KEY (numero_factura),
	CONSTRAINT fk1_paquetes FOREIGN KEY (id_paquete,id_agencia) REFERENCES cgr_paquetes(id_paquete,id_agencia) ON DELETE CASCADE,
	CONSTRAINT fk2_registro_clientes FOREIGN KEY (id_reg_cliente,id_reg_agencia) REFERENCES cgr_registro_clientes(id_cliente,id_agencia) ON DELETE CASCADE,
	CONSTRAINT fk3_asesores_de_viajes FOREIGN KEY (id_asesor) REFERENCES cgr_asesores_de_viajes(id_asesor) ON DELETE CASCADE
);

CREATE TABLE cgr_formas_de_pago
(
	id_instrumento numeric NOT NULL,
	id_cliente numeric NOT NULL,
	id_paquete_contrato numeric NOT NULL,
	tipo_forma_de_pago varchar,
	CONSTRAINT pk_forma_de_pago PRIMARY KEY (id_instrumento,id_cliente,id_paquete_contrato),
	CONSTRAINT chk_tipo_forma_de_pago CHECK(tipo_forma_de_pago in ('parcial','cuotas')),
	CONSTRAINT fk1_instrumentos_de_pago FOREIGN KEY (id_instrumento,id_cliente) REFERENCES cgr_instrumentos_de_pago(id_instrumento,doc_identidad_cliente) ON DELETE CASCADE,
	CONSTRAINT fk2_paquetes_contrato FOREIGN KEY (id_paquete_contrato) REFERENCES cgr_paquetes_contrato(numero_factura) ON DELETE CASCADE
);

CREATE SEQUENCE cgr_secuencia_viajero
	start with 1
	increment 1
	minvalue 1
	maxvalue 100
;

CREATE TABLE cgr_viajeros
(
	id_de_identidad numeric NOT NULL DEFAULT nextval('cgr_secuencia_viajero'::regclass),
	id_ciudad numeric NOT NULL,
	id_pais numeric NOT NULL,
	id_paquete_contrato numeric NOT NULL,
	primer_nombre varchar NOT NULL,
	primer_apellido varchar NOT NULL,
	segundo_apellido varchar NOT NULL,
	sexo varchar NOT NULL,
	f_nacimiento date NOT NULL,
	segundo_nombre varchar,
	CONSTRAINT pk_viajero PRIMARY KEY (id_de_identidad),
	CONSTRAINT chk_sexo CHECK(sexo in ('M','F')),
	CONSTRAINT fk_ciudades FOREIGN KEY (id_ciudad,id_pais) REFERENCES cgr_ciudades(id_ciudad,id_pais) ON DELETE CASCADE,
	CONSTRAINT fk_paquetes_contrato FOREIGN KEY (id_paquete_contrato) REFERENCES cgr_paquetes_contrato(numero_factura) ON DELETE CASCADE
);

CREATE TABLE cgr_pai_via
(
	id_viajero numeric NOT NULL,
	id_pais numeric NOT NULL,
	nro_de_pasaporte numeric NOT NULL,
	CONSTRAINT pk_pai_via PRIMARY KEY (id_viajero,id_pais),
	CONSTRAINT fk1_viajero FOREIGN KEY (id_viajero) REFERENCES cgr_viajeros(id_de_identidad) ON DELETE CASCADE,
	CONSTRAINT fk2_paises FOREIGN KEY (id_pais) REFERENCES cgr_paises(id_pais) ON DELETE CASCADE
);

CREATE TABLE cgr_registro_viajeros
(
	id_agencia numeric NOT NULL,
	id_viajero numeric NOT NULL,
	f_registro date NOT NULL,
	nro_registro numeric NOT NULL,
	CONSTRAINT pk_registro_viajeros PRIMARY KEY (id_agencia,id_viajero),
	CONSTRAINT fk1_agencias_de_viajes FOREIGN KEY (id_agencia) REFERENCES cgr_agencias_de_viajes(id_agencia) ON DELETE CASCADE,
	CONSTRAINT fk2_viajero FOREIGN KEY (id_viajero) REFERENCES cgr_viajeros(id_de_identidad) ON DELETE CASCADE
);

CREATE TABLE cgr_detalle_viajeros
(
	id_viajero numeric NOT NULL,
	id_agencia numeric NOT NULL,
	id_paquete_contrato numeric NOT NULL,
	CONSTRAINT pk_detalle_viajeros PRIMARY KEY (id_viajero,id_agencia,id_paquete_contrato),
	CONSTRAINT fk1_registro_viajeros FOREIGN KEY (id_viajero,id_agencia) REFERENCES cgr_registro_viajeros(id_viajero,id_agencia) ON DELETE CASCADE,
	CONSTRAINT fk2_paquetes_contrato FOREIGN KEY (id_paquete_contrato) REFERENCES cgr_paquetes_contrato(numero_factura) ON DELETE CASCADE
);

CREATE SEQUENCE cgr_secuencia_participantes
	start with 1
	increment 1
	minvalue 1
	maxvalue 100
;

CREATE TABLE cgr_participantes
(
	id_partipante numeric NOT NULL DEFAULT nextval('cgr_secuencia_participantes'::regclass),
	id_rally numeric NOT NULL,
	id_via_agencia numeric ,
	id_via_viajero numeric ,
	id_cli_agencia numeric ,
	id_cli_cliente numeric ,
	equipo boolean ,
	posicion numeric ,
	CONSTRAINT pk_participantes PRIMARY KEY (id_partipante,id_rally),
	CONSTRAINT fk1_rallies FOREIGN KEY (id_rally) REFERENCES cgr_rallies(id_rally) ON DELETE CASCADE,
	CONSTRAINT fk2_registro_viajeros FOREIGN KEY (id_via_agencia,id_via_viajero ) REFERENCES cgr_registro_viajeros(id_agencia,id_viajero) ON DELETE CASCADE,
	CONSTRAINT fk3_registro_clientes FOREIGN KEY (id_cli_agencia,id_cli_cliente) REFERENCES cgr_registro_clientes(id_agencia,id_cliente) ON DELETE CASCADE
);

CREATE SEQUENCE cgr_secuencia_puntuacion
	start with 1
	increment 1
	minvalue 1
	maxvalue 100
;

CREATE TABLE cgr_puntuaciones
(
	id_puntuacion numeric NOT NULL DEFAULT nextval('cgr_secuencia_puntuacion'::regclass),
	id_rally numeric,
	id_pais numeric,
	id_ciudad numeric,
	id_atraccion numeric,
	id_paquete_contrato numeric,
	CONSTRAINT pk_puntuacion PRIMARY KEY (id_puntuacion),
	CONSTRAINT fk1_rallies FOREIGN KEY (id_rally) REFERENCES cgr_rallies(id_rally) ON DELETE CASCADE,
	CONSTRAINT fk2_atracciones FOREIGN KEY (id_pais,id_ciudad,id_atraccion) REFERENCES cgr_atracciones(id_pais,id_ciudad,id_atraccion) ON DELETE CASCADE,
	CONSTRAINT fk3_paquetes_contrato FOREIGN KEY (id_paquete_contrato) REFERENCES cgr_paquetes_contrato(numero_factura) ON DELETE CASCADE
);