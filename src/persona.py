class Persona():
    def __init__(self,nombre,apellido,rut,celular,correo_electronico,genero):
        self.__nombre=nombre
        self.__apellido = apellido
        self.__rut = rut
        self.__celular = celular
        self.__correo_electronico = correo_electronico
        self.__genero = genero

    #metodos gets y sets
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre):
        self.__nombre = nombre
    def get_apellido(self):
        return self.__apellido
    def set_apellido(self,apellido):
        self.__apellido = apellido
    def get_rut(self):
        return self.__rut
    def set_rut(self, rut):
        self.__rut = rut
    def get_celular(self):
        return self.__celular
    def set_celular(self,celular):
        self.__celular = celular
    def get_correo_electronico(self):
        return self.__correo_electronico
    def set_correo_electronico(self,correo_electronico):
        self.__correo_electronico = correo_electronico
    def get_genero(self):
        return self.__genero
    def set_genero(self,genero):
        self.__genero = genero
        
    #metodo para mostrar informacion en consola
    def mostrar_informacion(self):
        print(f"Nombre : {self.__nombre} {self.__apellido}")
        print(f"Rut: {self.__rut}")
        print(f"Celular : {self.__celular}")
        print(f"correo : {self.__correo_electronico}")
        print(f"Genero : {self.__genero}")