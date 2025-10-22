from empleado import Empleado
import bcrypt

class GestorEmpleado:
    def __init__(self):
        self.__empleados =  {}
        self.__usuario_actual = None

    def get_empleado(self):
        return self.__empleados
    def get_usuario_actual(self):
        return self.__usuario_actual


    def login(self):
        nombre_usuario = input("Nombre de usuario :")
        clave = input("contraseña :")
        empleado = self.__empleados.get(nombre_usuario)
        if not empleado:
            print("usuarion no encontrado")
            return None
        if empleado.verificar_clave(clave):
            self.__usuario_actual = empleado
            print(f"Bienvenido, {empleado.get_nombre()} {empleado.get_apellido()}.")
            return empleado
        print("contraseña incorrecta")
        return None

    def registrar_empleado(self):
        print("Registrar nuevo empleado")
        nombre= input("Nombre :")
        apellido=input("Apellido :")
        rut=input("Rut :")
        celular=input("Celular :")
        correo_electronico=input("Correo electronico :")
        genero=input("Genero :")
        nombre_usuario=input("Nombre de usuario :")
        clave=input("clave :")
        cargo_trabajo=input("cargo :")
        if nombre_usuario in self.__empleados:
            print("YA existe este usuario")
            return False
        clave_hash = bcrypt.hashpw(clave.encode('utf-8'), bcrypt.gensalt())
        nuevo_empleado = Empleado(nombre,apellido,rut,celular,correo_electronico,genero,nombre_usuario,clave_hash,cargo_trabajo)
        self.__empleados[nombre_usuario] = nuevo_empleado
        print("Empleado registrado correctamente")
        return True
    

    
    
    def cerrar_sesion(self):
        if self.__usuario_actual:
            print(f"Sesion cerrada de {self.__usuario_actual.get_nombre_usuario()}")
            self.__usuario_actual = None
        else:
            print("no hay sesion activa")


    def mostrar_empleados(self):
        if not self.__empleados:
            print("No hay empleados registrados")
            return
        for i, emp in enumerate(self.__empleados.values(), start=1):
            print(f"{i}. Usuario: {emp.get_nombre_usuario()}| Nombre: {emp.get_nombre()} {emp.get_apellido()} | Cargo: {emp.get_cargo_trabajo()}")



    def eliminar_empleado(self):
        nombre_usuario = input("Nombre de usuario del empleado a eliminar : ")
        if nombre_usuario in self.__empleados:
            confirmar = input(f"¿Seguro que desea eliminar al empleado '{nombre_usuario}'? [s/n]: ").lower()
            if confirmar == "s":
                del self.__empleados[nombre_usuario]
                print("Empleado eliminado correctamente.")
            else:
                print("Operación cancelada.")
        else:
            print("Empleado no encontrado.")
 