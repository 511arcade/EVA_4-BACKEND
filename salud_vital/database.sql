-- DDL PostgreSQL del esquema Salud Vital (incluye segmento 8: Cita)

create table if not exists "Especialidad" (
   id     serial primary key,
   nombre varchar(100) unique not null
);

create table if not exists "Paciente" (
   id               serial primary key,
   "RUT"            varchar(12) unique not null,
   nombre           varchar(100) not null,
   fecha_nacimiento date not null,
   sexo             varchar(1) not null check ( sexo in ( 'M',
                                              'F',
                                              'O' ) )
);

create table if not exists "Medico" (
   id              serial primary key,
   "RUT"           varchar(12) unique not null,
   nombre          varchar(100) not null,
   especialidad_id integer not null
);

create table if not exists "Tratamiento" (
   id          serial primary key,
   nombre      varchar(100) not null,
   descripcion text
);

create table if not exists "Medicamento" (
   id          serial primary key,
   nombre      varchar(100) not null,
   descripcion text
);

create table if not exists "ConsultaMedica" (
   id             serial primary key,
   paciente_id    integer not null,
   medico_id      integer not null,
   fecha          timestamp with time zone not null,
   motivo         varchar(200) not null,
   diagnostico    text,
   tratamiento_id integer
);

create table if not exists "RecetaMedica" (
   id           serial primary key,
   consulta_id  integer unique not null,
   indicaciones text
);

create table if not exists "RecetaItem" (
   id             serial primary key,
   receta_id      integer not null,
   medicamento_id integer not null,
   dosis          varchar(100) not null,
   frecuencia     varchar(100) not null,
   duracion_dias  integer not null check ( duracion_dias >= 0 )
);

-- Segmento 8: Cita
create table if not exists "Cita" (
   id          serial primary key,
   paciente_id integer not null,
   medico_id   integer not null,
   fecha_hora  timestamp with time zone not null,
   estado      varchar(10) not null check ( estado in ( 'programada',
                                                   'atendida',
                                                   'cancelada' ) ),
   consulta_id integer unique
);

-- Índices sugeridos
create index if not exists idx_cita_medico on
   "Cita" (
      medico_id,
      fecha_hora
   );
create index if not exists idx_cita_paciente on
   "Cita" (
      paciente_id,
      fecha_hora
   );

-- Nota: Si ejecutas este DDL manualmente, recuerda crear primero el esquema base
-- y asignar permisos al rol correspondiente (por ejemplo, "Felipe").

-- Claves foráneas (definidas aparte para mayor compatibilidad de parsers)
alter table "Medico"
   add constraint fk_medico_especialidad foreign key ( especialidad_id )
      references "Especialidad" ( id );

alter table "ConsultaMedica"
   add constraint fk_consulta_paciente foreign key ( paciente_id )
      references "Paciente" ( id );

alter table "ConsultaMedica"
   add constraint fk_consulta_medico foreign key ( medico_id )
      references "Medico" ( id );

alter table "ConsultaMedica"
   add constraint fk_consulta_tratamiento foreign key ( tratamiento_id )
      references "Tratamiento" ( id );

alter table "RecetaMedica"
   add constraint fk_receta_consulta foreign key ( consulta_id )
      references "ConsultaMedica" ( id );

alter table "RecetaItem"
   add constraint fk_recetaitem_receta foreign key ( receta_id )
      references "RecetaMedica" ( id );

alter table "RecetaItem"
   add constraint fk_recetaitem_medicamento foreign key ( medicamento_id )
      references "Medicamento" ( id );

alter table "Cita"
   add constraint fk_cita_paciente foreign key ( paciente_id )
      references "Paciente" ( id );

alter table "Cita"
   add constraint fk_cita_medico foreign key ( medico_id )
      references "Medico" ( id );

alter table "Cita"
   add constraint fk_cita_consulta foreign key ( consulta_id )
      references "ConsultaMedica" ( id );