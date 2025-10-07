class Movimiento():
    def __init__(self,codigo_movimiento,producto_codigo,tipo,cantidad,motivo,fecha,usuario_responsable):
        self.__codigo_movimiento = codigo_movimiento
        self.__producto_codigo = producto_codigo
        self.__tipo = tipo
        self.__cantidad = cantidad
        self.__motivo = motivo
        self.__fecha = fecha
        self.__usuario_responsable = usuario_responsable

    def get_codigo_movimiento(self):
        return self.__codigo_movimiento
    def set_codigo_movimiento(self,codigo_movimiento):
        self.__codigo_movimiento = codigo_movimiento
    def get_producto_codigo(self):
        return self.__producto_codigo
    def set_producto_codigo(self,producto_codigo):
        self.__producto_codigo = self.__producto_codigo
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

    def registrar_movimiento():
        pass