import uuid
from datetime import datetime

class Movimiento():
    movimientos_registrados = {} 
    #[]

    def __init__(self,codigo_producto,usuario_responsable,tipo,cantidad,motivo,stock_antes,stock_despues, monto_total):
        self.__id_movimiento = str(uuid.uuid4())
        self.__codigo_producto = codigo_producto
        self.__usuario_responsable = usuario_responsable
        self.__tipo = tipo
        self.__motivo = motivo
        self.__cantidad = cantidad
        self.__fecha = datetime.now()
        self.__stock_antes = stock_antes
        self.__stock_despues = stock_despues
        self.__monto_total = monto_total
        

    def get_id_movimiento(self):
        return self.__id_movimiento
    def get_codigo_producto(self):
        return self.__codigo_producto
    def set_codigo_producto(self,codigo_producto):
        self.__codigo_producto = codigo_producto
    def get_usuario_responsable(self):
        return self.__usuario_responsable
    def set_usuario_responsable(self,usuario_responsable):
        self.__usuario_responsable = usuario_responsable
    def get_tipo(self):
        return self.__tipo
    def set_tipo(self,tipo):
        self.__tipo = tipo
    def get_motivo(self):
        return self.__motivo
    def set_motivo(self,motivo):
        self.__motivo = motivo
    def get_cantidad(self):
        return self.__cantidad
    def set_cantidad(self,cantidad):
        self.__cantidad = cantidad
    def get_fecha(self):
        return self.__fecha
    def set_fecha(self,fecha):
        self.__fecha = fecha
    def get_stock_antes(self):
        return self.__stock_antes
    def get_stock_despues(self):
        return self.__stock_despues
    def get_monto_total(self):
        return self.__monto_total
    def set_monto_total(self,monto_total):
        self.__monto_total = monto_total
 


    def __str__(self):
        return (f"[{self.__fecha}] {self.__tipo} | Codigo Producto: {self.__codigo_producto} | "
                f"Empleado: {self.__usuario_responsable} | Cantidad: {self.__cantidad} | "
                f"Motivo: {self.__motivo} | Stock antes/después: {self.__stock_antes}/{self.__stock_despues} | "
                f"Monto Total: {self.__monto_total}")


  