class Producto():
    def __init__(self, nombre = str,codigo_marca=str,codigo_unidad=str,codigo=str,stock=int,stock_minimo=int,stock_maximo=int,categoria=str,atributos_extra=dict):
        self.__nombre = nombre
        self.__codigo_marca = codigo_marca
        self.__codigo_unidad = codigo_unidad
        self.__codigo = codigo
        self.__stock = stock
        self.__stock_minimo = stock_minimo
        self.__stock_maximo = stock_maximo
        self.__categoria = categoria
        self.__atributos_extra = atributos_extra

    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre):
        self.__nombre = nombre
    def get_codigo_marca(self):
        return self.__codigo_marca
    def set_codigo_marca(self,codigo_marca):
        self.__codigo_marca = codigo_marca
    def get_codigo_unidad(self):
        return self.__codigo_unidad
    def set_codigo_unidad(self,codigo_unidad):
        self.__codigo_unidad = codigo_unidad
    def get_codigo(self):
        return self.__codigo
    def set_codigo(self,codigo):
        self.__codigo = codigo
    def get_stock(self):
        return self.__stock
    def set_stock(self, stock):
        if stock<0:
            raise ValueError("Stock no puede ser negativo")
        self.__stock = stock

    def get_stock_minimo(self):
        return self.__stock_minimo
    def set_stock_minimo(self,stock_minimo):
        if stock_minimo<0:
            raise ValueError("Stock minimo no puede ser negativo")
        self.__stock_minimo = stock_minimo

    def get_stock_maximo(self):
        return self.__stock_maximo
    def set_stock_maximo(self,stock_maximo):
        if stock_maximo<self.__stock_minimo:
            raise ValueError("El Stock Maximo no puede ser Menor que el minimo")
        self.__stock_maximo = stock_maximo

    def get_categoria(self):
        return self.__categoria
    def set_categoria(self,categoria):
        self.__categoria = categoria
    def get_atributos_extra(self):
        return self.__atributos_extra
    def set_atributos_extra(self,atributos_extra):
        self.__atributos_extra = atributos_extra



    def actualizar_stock(self, cantidad):
        nuevo_stock = self.__stock + cantidad
        if nuevo_stock < 0:
            raise ValueError(f"No hay suficiente stock para retirar {abs(cantidad)} unidades.")
        self.__stock = nuevo_stock

    def __str__(self):
        return (f"Producto: {self.__nombre} | Código: {self.__codigo} | "
                f"Stock: {self.__stock} (Min: {self.__stock_minimo}, Max: {self.__stock_maximo}) | "
                f"Categoría: {self.__categoria}")