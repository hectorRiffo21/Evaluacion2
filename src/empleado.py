from persona import Persona
import bcrypt
#se usa herencia de persona hacia empleado, heredando atributos y metodos
class Empleado(Persona):
    def __init__(self,nombre,apellido,rut,celular,correo_electronico,genero, nombre_usuario,clave_hash,cargo_trabajo):
        super().__init__(nombre,apellido,rut,celular,correo_electronico,genero)
        self.__nombre_usuario = nombre_usuario
        self.__clave_hash = clave_hash
        self.__cargo_trabajo= cargo_trabajo
    #gets y sets
    def get_nombre_usuario(self):
        return self.__nombre_usuario
    def get_clave_hash(self):
        return self.__clave_hash
    def set_clave_hash(self,clave_hash):
        self.__clave_hash = clave_hash
    def get_cargo_trabajo(self):
        return self.__cargo_trabajo
    def set_cargo_trabajo(self,cargo_trabajo):
        self.__cargo_trabajo = cargo_trabajo
 
    #funcion para verificar clave encryptada
    def verificar_clave(self,clave):
        return bcrypt.checkpw(clave.encode('utf-8'), self.__clave_hash)
    
    #funcion para mostrar la informacion de empleado junto a los datos de persona
    def mostrar_informacion_empleado(self):
        super().mostrar_informacion()
        print(f"Usuario : {self.__nombre_usuario}")
        print(f"Cargo : {self.__cargo_trabajo}")




