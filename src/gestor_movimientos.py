from movimiento import Movimiento
from conexion_bd import ConexionBD

#clase para gestionar los movimientos de los productos en el inventario
class GestorMovimientos:
    def __init__(self):
        #diccionario para operaciones en memoria
        self.__movimientos ={}

    #registra los movimientos en el diccionario
    def registrar_movimiento(self, movimiento: Movimiento):
        self.__movimientos[movimiento.get_id_movimiento()] = movimiento

    def get_movimientos(self):
        return self.__movimientos
    

    #mostrar todos los movimientos de la base de datos
    def mostrar_todos(self, db:ConexionBD):
        consulta = "SELECT * FROM movimientos ORDER BY id ASC"
        movimientos = db.ejecutar_consulta(consulta)
        if not movimientos:
            print("No hay movimientos registrados.")
            return
        print("\n--- Lista de Movimientos ---")
        for m in movimientos:
            print(f"ID: {m[0]} | Producto: {m[1]} | Usuario: {m[2]} | Tipo: {m[3]} | Cantidad: {m[4]} | Motivo: {m[5]} | Stock Antes: {m[6]} | Stock Después: {m[7]} | Monto: {m[8]}")

    #filtrado de movimientos por tipo
    #ingreso, retiro o eliminacion de los productos
    def filtrar_por_tipo(self, tipo, db:ConexionBD):
        """Filtra movimientos por tipo (Ingreso, Retiro, Eliminación, etc)."""
        consulta = "SELECT * FROM movimientos WHERE tipo = ? ORDER BY id ASC"
        movimientos = db.ejecutar_consulta(consulta, (tipo,))
        if not movimientos:
            print(f"No hay movimientos de tipo '{tipo}'.")
            return
        print(f"\n--- Movimientos de tipo '{tipo}' ---")
        for m in movimientos:
            print(f"ID: {m[0]} | Producto: {m[1]} | Usuario: {m[2]} | Cantidad: {m[4]} | Motivo: {m[5]} | Stock Antes: {m[6]} | Stock Después: {m[7]} | Monto: {m[8]}")


    #filtrado de movimientos por el usuario responsable
    def filtrar_por_usuario(self, usuario, db:ConexionBD):
        """Filtra movimientos según el usuario responsable."""
        consulta = "SELECT * FROM movimientos WHERE usuario_responsable = ? ORDER BY id ASC"
        movimientos = db.ejecutar_consulta(consulta, (usuario,))
        if not movimientos:
            print(f"No hay movimientos registrados por el usuario '{usuario}'.")
            return
        print(f"\n--- Movimientos realizados por '{usuario}' ---")
        for m in movimientos:
            print(f"ID: {m[0]} | Producto: {m[1]} | Tipo: {m[3]} | Cantidad: {m[4]} | Motivo: {m[5]} | Stock Antes: {m[6]} | Stock Después: {m[7]} | Monto: {m[8]}")


    #registra los movimientos directamente en la base de datos
    def registrar_movimiento_sql(self, movimiento: Movimiento, db: ConexionBD):
        """
        Registra un movimiento en la base de datos.
        """
        consulta = """
        INSERT INTO movimientos (
            codigo_producto, usuario_responsable, tipo, cantidad, motivo, stock_antes, stock_despues, monto_total
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        parametros = (
            movimiento.get_codigo_producto(),
            movimiento.get_usuario_responsable(),
            movimiento.get_tipo(),
            movimiento.get_cantidad(),
            movimiento.get_motivo(),
            movimiento.get_stock_antes(),
            movimiento.get_stock_despues(),
            movimiento.get_monto_total()
        )
        exito = db.ejecutar_instruccion(consulta, parametros)
        if exito:
            print(f"Movimiento registrado correctamente: {movimiento}")
        else:
            print("Error al registrar movimiento en la base de datos.")