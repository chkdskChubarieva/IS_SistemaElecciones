import mysql.connector
from mysql.connector import errorcode

print("Conectando...")
try:
    conn = mysql.connector.connect(
           host='chkdsk7.mysql.pythonanywhere-services.com',
           user='chkdsk7',
           password='mundolibre'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe un error en el nombre de usuario o en la clave')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `chkdsk7$sistemaElecciones`;")

cursor.execute("CREATE DATABASE `chkdsk7$sistemaElecciones`;")

cursor.execute("USE `chkdsk7$sistemaElecciones`;")

# creando las tablas
TABLES = {}

TABLES['Elector'] = ('''
      create table ELECTOR
(
   ID_ELECTOR           int auto_increment,
   NOMBRE               varchar(30),
   CI                   char(10),
   FECHA_NACIMIENTO     date,
   GENERO               varchar(15),
   ESTADO_HABILITADO    int not null,
   PRIMARY KEY (ID_ELECTOR)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')


TABLES['Comite'] = ('''
      CREATE TABLE `COMITE` (
      ID_COMITE int NOT NULL AUTO_INCREMENT,
      NOMBRE               varchar(30),
      CI                   char(10),
      FECHA_NACIMIENTO     date,
      GENERO               varchar(15),
      ROL varchar(15) NOT NULL,
      CODIGO varchar(15),
      PRIMARY KEY (ID_COMITE)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Candidato'] = ('''
      CREATE TABLE `CANDIDATO` (
      ID_CANDIDATO int NOT NULL AUTO_INCREMENT,
      NOMBRE               varchar(30),
      CI                   char(10),
      FECHA_NACIMIENTO     date,
      GENERO               varchar(15),
      votos                int,
      FOTO varchar(50) NOT NULL,
      PARTIDO varchar(20) NOT NULL,
      PRIMARY KEY (ID_CANDIDATO)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')


TABLES['Admin'] = ('''
      CREATE TABLE `ADMINISTRADOR` (
      ID_ADMIN int NOT NULL AUTO_INCREMENT,
      NOMBRE               varchar(30),
      CI                   char(10),
      FECHA_NACIMIENTO     date,
      GENERO               varchar(15),
      USUARIO varchar(20) NOT NULL,
      CONTRASENIA varchar(30) NOT NULL,
      PRIMARY KEY (ID_ADMIN)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')


for tabla_nombre in TABLES:
      tabla_sql = TABLES[tabla_nombre]
      try:
            print('Creando tabla {}:'.format(tabla_nombre), end=' ')
            cursor.execute(tabla_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Ya existe la tabla')
            else:
                  print(err.msg)
      else:
            print('OK')





# commitando si no hay nada que tenga efecto
conn.commit()

cursor.close()
conn.close()