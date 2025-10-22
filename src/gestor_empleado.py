from empleado import Empleado
import bcrypt
from conexion_bd import ConexionBD

#clase que administra las operaciones de empleado
class GestorEmpleado:
    def __init__(self):
        #diccionario para operaciones en memoria
        self.__empleados =  {}
        #usuario actual para obtener la persona que realiza las operaciones
        self.__usuario_actual = None
        #instancia de conexion a base de datos
        self.__db = ConexionBD()
        #inicializador de la conexion de base de datos
        self.__db.conectar()
    
    #Gets
    def get_empleado(self):
        return self.__empleados
    def get_usuario_actual(self):
        return self.__usuario_actual

    #Funcion para poder iniciar sesion y tener acceso al menu de inventario
    def login(self):
        nombre_usuario = input("Nombre de usuario :")
        clave = input("contraseña :")
        consulta= """SELECT nombre, apellido, rut, celular, correo_electronico, genero, nombre_usuario, clave, cargo_trabajo FROM empleados WHERE nombre_usuario = ? """
        resultado = self.__db.ejecutar_consulta(consulta,(nombre_usuario,))
        if not resultado:
            print("usuarion no encontrado")
            return None
        datos = resultado[0]
        nombre, apellido, rut, celular, correo, genero, nombre_usuario_db, clave_hash, cargo = datos
        #se crea el objeto empleado con los datos
        empleado = Empleado(nombre, apellido, rut, celular, correo, genero, nombre_usuario_db, clave_hash.encode('utf-8') if isinstance(clave_hash, str) else clave_hash, cargo)
        #se valida la contraseña
        if bcrypt.checkpw(clave.encode('utf-8'), empleado.get_clave_hash()):
            self.__usuario_actual = empleado
            print(f"Bienvenido, {empleado.get_nombre()} {empleado.get_apellido()}.")
            return empleado
        else:
            print("Contraseña incorrecta.")
            return None


    #registrar un nuevo empleado en la base de datos
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
        existe = self.__db.ejecutar_consulta("SELECT COUNT(*) FROM empleados WHERE nombre_usuario = ?", (nombre_usuario,))
        #se verifica si existe el empleado ya en la base de datos
        if existe and existe[0][0] > 0:
            print("YA existe este usuario")
            return False
        #contraseña hasheada
        clave_hash = bcrypt.hashpw(clave.encode('utf-8'), bcrypt.gensalt())

        consulta = """
            INSERT INTO empleados (nombre, apellido, rut, celular, correo_electronico, genero, nombre_usuario, clave, cargo_trabajo)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        try:
            self.__db.ejecutar_instruccion(consulta, (nombre, apellido, rut, celular, correo_electronico, genero, nombre_usuario, clave_hash, cargo_trabajo))
            print("Empleado registrado correctamente en la base de datos.")
            return True
        except Exception as e:
            print("Error al registrar el empleado:", e)
            return False


    #cerrar sesion de el usuario actual, de esa forma al iniciar con otro usuario los movimientos quedan
    #asociados a el
    def cerrar_sesion(self):
        if self.__usuario_actual:
            print(f"Sesion cerrada de {self.__usuario_actual.get_nombre_usuario()}")
            self.__usuario_actual = None
        else:
            print("no hay sesion activa")

    #mostrar todos los empleados en la base de datos
    def mostrar_empleados(self):
        consulta = "SELECT nombre_usuario, nombre, apellido, cargo_trabajo FROM empleados"
        empleados = self.__db.ejecutar_consulta(consulta)
        if not empleados:
            print("No hay empleados registrados")
            return
        for i, emp in enumerate(empleados, start=1):
            nombre_usuario, nombre, apellido, cargo = emp
            print(f"{i}. Usuario: {nombre_usuario} | Nombre: {nombre} {apellido} | Cargo: {cargo}")


    #eliminar un empleado de la base de datos
    def eliminar_empleado(self):
        nombre_usuario = input("Nombre de usuario del empleado a eliminar : ")
        resultado = self.__db.ejecutar_consulta("SELECT * FROM empleados WHERE nombre_usuario = ?", (nombre_usuario,))
        if not resultado:
            print("Empleado no encontrado.")
            return

        confirmar = input(f"¿Seguro que desea eliminar al empleado '{nombre_usuario}'? [s/n]: ").lower()
        if confirmar !="s":
            print("Operación cancelada.")
            return

        try:
            self.__db.ejecutar_instruccion("DELETE FROM empleados WHERE nombre_usuario = ?", (nombre_usuario,))
            print("Empleado eliminado correctamente de la base de datos.")
        except Exception as e:
            print("Error al eliminar empleado:", e)
 