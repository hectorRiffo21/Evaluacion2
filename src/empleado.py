from persona import Persona

class Empleado(Persona):
    def __init__(self,nombre,apellido,rut,celular,correo_electronico,genero, nombre_usuario,clave,cargo_trabajo):
        super().__init__(nombre,apellido,rut,celular,correo_electronico,genero)
        self.__nombre_usuario = nombre_usuario
        self.__clave = clave
        self.__cargo_trabajo= cargo_trabajo
    def get_nombre_usuario(self):
        return self.__nombre_usuario
    def set_nombre_usuario(self,nombre_usuario):
        self.__nombre_usuario = nombre_usuario
    def get_clave(self):
        return self.__clave
    def set_clave(self,clave):
        self.__clave = clave
    def get_cargo_trabajo(self):
        return self.__cargo_trabajo
    def set_cargo_trabajo(self,cargo_trabajo):
        self.__cargo_trabajo = cargo_trabajo
        ##