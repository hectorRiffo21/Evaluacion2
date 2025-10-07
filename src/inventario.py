class Inventario:
    def __init__(self,productos,movimiento):
        self.__productos = productos
        self.__movimiento = movimiento

    def get_productos(self):
        return self.__productos
    def set_productos(self,productos):
        self.__productos = productos
    def get_movimiento(self):
        return self.__movimiento
    def set_movimiento(self,movimiento):
        self.__movimiento = movimiento

