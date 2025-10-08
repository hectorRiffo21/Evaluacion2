from datetime import datetime

class Movimiento():
    movimientos_registrados = {} 
    contador=0
    #[]

    def __init__(self,producto_codigo,tipo,cantidad,motivo,usuario_responsable):
        Movimiento.contador +=1
        self.__codigo_movimiento = Movimiento.contador 
        self.__producto_codigo = producto_codigo
        self.__tipo = tipo
        self.__cantidad = cantidad
        self.__motivo = motivo
        self.__fecha = datetime.now()
        self.__usuario_responsable = usuario_responsable

        Movimiento.movimientos_registrados[self.__codigo_movimiento]=self

    def get_codigo_movimiento(self):
        return self.__codigo_movimiento
    def set_codigo_movimiento(self,codigo_movimiento):
        self.__codigo_movimiento = codigo_movimiento
    def get_producto_codigo(self):
        return self.__producto_codigo
    def set_producto_codigo(self,producto_codigo):
        self.__producto_codigo = producto_codigo
    def get_tipo(self):
        return self.__tipo
    def set_tipo(self,tipo):
        self.__tipo = tipo
    def get_cantidad(self):
        return self.__cantidad
    def set_cantidad(self,cantidad):
        self.__cantidad = cantidad
    def get_motivo(self):
        return self.__motivo
    def set_motivo(self,motivo):
        self.__motivo = motivo
    def get_fecha(self):
        return self.__fecha
    def set_fecha(self,fecha):
        self.__fecha = fecha
    def get_usuario_responsable(self):
        return self.__usuario_responsable
    def set_usuario_responsable(self,usuario_responsable):
        self.__usuario_responsable = usuario_responsable

    def __str__(self):
        return (f"Movimiento ID: {self.__codigo_movimiento} | Producto: {self.__producto_codigo} |"
                f"Tipo: {self.__tipo} | cantidad: {self.__cantidad} | Motivo: {self.__motivo} | "
                f"Fecha: {self.__fecha.strftime('%Y-%m-%d %H:%M:%S')} | Usuario: {self.__usuario_responsable}")



    def mostrar_movimientos(cls):
        if not cls.movimientos_registrados:
            print("No hay movimientos")
        else:
            for mov in cls.movimientos_registrados.values():
                print(mov)