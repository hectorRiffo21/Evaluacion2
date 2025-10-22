from movimiento import Movimiento

class GestorMovimientos:
    def __init__(self):
        self.__movimientos ={}

    def registrar_movimiento(self, movimiento: Movimiento):
        self.__movimientos[movimiento.get_id_movimiento()] = movimiento

    def mostrar_todos(self):
        """Muestra todos los movimientos registrados."""
        if not self.__movimientos:
            print("No hay movimientos registrados.")
            return
        for mov in self.__movimientos.values():
            print(mov)

    def filtrar_por_tipo(self, tipo):
        """Filtra movimientos por tipo (Ingreso, Retiro, Eliminación, etc)."""
        encontrados = False
        for mov in self.__movimientos.values():
            if mov.get_tipo().lower() == tipo.lower():
                print(mov)
                encontrados = True
        if not encontrados:
            print(f"No se encontraron movimientos del tipo '{tipo}'.")

    def filtrar_por_usuario(self, usuario):
        """Filtra movimientos según el usuario responsable."""
        encontrados = False
        for mov in self.__movimientos.values():
            if mov.get_usuario_responsable().lower() == usuario.lower():
                print(mov)
                encontrados = True
        if not encontrados:
            print(f"No se encontraron movimientos realizados por '{usuario}'.")

    def get_movimientos(self):
        return self.__movimientos



