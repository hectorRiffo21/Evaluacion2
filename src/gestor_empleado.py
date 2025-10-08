from empleado import Empleado
import bcrypt

class GestorEmpleado:
    def __init__(self):
        self.__empleados =  {}

    def get_empleado(self):
        return self.__empleados

    def registrar_empleado(self,nombre,apellido,rut, celular,correo_electronico,genero,nombre_usuario,clave,cargo_trabajo):
        if nombre_usuario in self.__empleados:
            print("YA existe este usuario")
            return False
        clave_hash = bcrypt.hashpw(clave.encode('utf-8'), bcrypt.gensalt())
        nuevo = Empleado(nombre,apellido,rut,celular,correo_electronico,genero,nombre_usuario,clave_hash,cargo_trabajo)
        self.__empleados[nombre_usuario] = nuevo
        print("EMpleado registrado correctamente")
        return True
    

    def login(self,nombre_usuario,clave):
        empleado = self.__empleados.get(nombre_usuario)
        if not empleado:
            print("usuarion no encontrado")
            return None
        if empleado.verificar_clave(clave):
            print(f"Bienvenido, {empleado.get_nombre()} {empleado.get_apellido()}.")
            return empleado
        print("contraseña incorrecta")
        return None

    def mostrar_empleados(self):
        if not self.__empleados:
            print("No hay empleados registrados")
            return
        for i, emp in enumerate(self.__empleados.values(), start=1):
            print(f"{i}. Usuario: {emp.get_nombre_usuario()}| Nombre: {emp.get_nombre()} {emp.get_apellido()} | Cargo: {emp.get_cargo_trabajo()}")



    def eliminar_empleado(self, nombre_usuario):
        if nombre_usuario in self.__empleados:
            confirmar = input(f"¿Seguro que desea eliminar al empleado '{nombre_usuario}'? [s/n]: ").lower()
            if confirmar == "s":
                del self.__empleados[nombre_usuario]
                print("Empleado eliminado correctamente.")
            else:
                print("Operación cancelada.")
        else:
            print("Empleado no encontrado.")
 