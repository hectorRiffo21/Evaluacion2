import bcrypt
from empleado import Empleado

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
        if empleado.verificar_clave(clave,bcrypt):
            print(f"Bienvenido, {empleado.get_nombre()}")
            return empleado
        print("contraseña incorrecta")
        return None



    def iniciar_sesion(self):
        print("INICIO DE SESION")
        usuario = input("nombre de usuario: ")
        clave = input("Contraseña : ")

        for emp in self.__empleados:
            if emp.get_nombre_usuario() == usuario and emp.get_clave() == clave:
                print(f"\n bienvenido {emp.get_nombre()} ({emp.get_cargo_trabajo()})")
                return emp
            
        print("usuario no encontrado.")
        return None
    
    def mostrar_empleados(self):
        print("LIsta empleados")
        if not self.__empleados:
            print("No hay empleados registrados.")
        else:
            for i, emp in enumerate(self.__empleados, start=1):
                print(f"{i}. {emp}")

    def eliminar_empleado(self):
        print("Eliminar empleado")
        usuario= input("Ingresar nombre de usuario del empleado a eliminar : ")

        for emp in self.__empleados:
            if emp.get_nombre_usuario() == usuario:
                confirmar = input(f"seguro que desea eliminar a '{emp.get_nombre()}' (s/n) : ").lower()

                if confirmar == "s":
                    self.__empleados.remove(emp)
                    print("Empleado eliminado correctamente")
                else:
                    print("operacion cancelada")
                return
        print("no se encontro al empleado con ese usuario")

 