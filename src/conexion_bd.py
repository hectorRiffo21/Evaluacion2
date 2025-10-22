import pyodbc
from dotenv import load_dotenv
import os

#conexion a la bae de datos sql
class ConexionBD:
    def __init__(self):
        load_dotenv()# aqui se cargan las credenciales de el archivo .env
        self.servidor = os.getenv("DB_SERVER")
        self.base_datos = os.getenv("DB_NAME")
        self.usuario = os.getenv("DB_USER")
        self.contrasena = os.getenv("DB_PASSWORD")
        self.conexion = None 

    #metodo para comenzar conexion a base de datos
    def conectar(self):
        try:
            self.conexion = pyodbc.connect(
                f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                f'SERVER={self.servidor};'
                f'DATABASE={self.base_datos};'
                f'UID={self.usuario};'
                f'PWD={self.contrasena}'
            )
            print("Conexión exitosa a Base De datos.")
        except Exception as e:
            print("Error al conectar a la base de datos:", e)

    #metodo para finalizar la conexion a la base de datos
    def cerrar_conexion(self):
        if self.conexion:
            self.conexion.close()
            print("Conexión cerrada")

    #funcion que ejecuta las consultas con SELECT y devuelve los resultados
    #se solicitan en la funcion la consulta y el parametro buscado
    def ejecutar_consulta(self, consulta, parametros=()):
        if self.conexion is None:
            print("No hay conexión activa")
            return []
        try:
            cursor = self.conexion.cursor()
            cursor.execute(consulta, parametros)
            return cursor.fetchall()
        except Exception as e:
            print("Error al ejecutar la consulta : ", e)
            return []

    #funcion para realizar modificaciones en la base de datos 
    #como INSERT, UPDATE, DELETE
    def ejecutar_instruccion(self, consulta, parametros=()):
        if self.conexion is None:
            print("No hay conexión activa")
            return False
        try:
            cursor = self.conexion.cursor()
            cursor.execute(consulta, parametros)
            self.conexion.commit()# aqui se confirman los cambios efectuados
            return True
        except Exception as e:
            print("Error al ejecutar la instrucción : ", e)
            self.conexion.rollback()#en caso de algun error no se realiza el cambio
            return False
