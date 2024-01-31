from .entities.elector import Elector


class ModeloElector():


    @classmethod
    def login(self, conexion, elector):
        try:
            cursor = conexion.connection.cursor()
            sql = """SELECT nombre, ci, fecha_nacimiento, estado_habilitado, genero 
                    FROM ELECTOR WHERE ci = '{}' and fecha_nacimiento = '{}'""".format(elector.ci, elector.fecha_nacimiento)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                elector = Elector(row[0], row[1], row[2], row[3], row[4]) # (opcional) despues usar metodo para hash ci aumentar row[2] fechanac
                return elector
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
        
    @classmethod
    def get_by_id(self, conexion, ci):
        try:
            cursor = conexion.connection.cursor()
            sql = "SELECT nombre, ci, fecha_nacimiento, estado_habilitado, genero FROM ELECTOR WHERE ci = {}".format(ci)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return Elector(row[0], row[1], row[2], row[3], row[4])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def votar(self, conexion, elector):
        try:
            cursor = conexion.connection.cursor()
            sql = "UPDATE ELECTOR set estado_habilitado={} where ci={};".format(0, elector.ci)
            print(elector.ci)
            cursor.execute(sql) 
            conexion.connection.commit()       
            return None
        except Exception as ex:
            raise Exception(ex)