class Producto():
    def __init__(self, nombre,codigo,stock,stock_minimo,stock_maximo,categoria,precio):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__stock = stock
        self.__stock_minimo = stock_minimo
        self.__stock_maximo = stock_maximo
        self.__categoria = categoria
        self.__precio = precio
        self.__valor_total = self.calcular_valor_total()

    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre):
        self.__nombre = nombre
    def get_codigo(self):
        return self.__codigo
    def set_codigo(self,codigo):
        self.__codigo = codigo
    def get_stock(self):
        return self.__stock
    def set_stock(self, nuevo_stock):
        self.__stock = nuevo_stock
        self.__valor_total = self.calcular_valor_total()
    def get_stock_minimo(self):
        return self.__stock_minimo
    def set_stock_minimo(self,stock_minimo):
        self.__stock_minimo = stock_minimo
    def get_stock_maximo(self):
        return self.__stock_maximo
    def set_stock_maximo(self,stock_maximo):
        self.__stock_maximo = stock_maximo
    def get_categoria(self):
        return self.__categoria
    def set_categoria(self,categoria):
        self.__categoria = categoria
    def get_precio(self):
        return self.__precio
    def set_precio(self,nuevo_precio):
        self.__precio = nuevo_precio
        self.__valor_total = self.calcular_valor_total()

    def get_valor_total(self):
        return self.__valor_total
    def calcular_valor_total(self):
        return self.__precio*self.__stock

    def actualizar_stock(self, cantidad, tipo):
        if tipo=="ingreso":
            if self.__stock + cantidad > self.__stock_maximo:
                raise ValueError(f"No se puede ingresar {cantidad}. Stock máximo permitido: {self.__stock_maximo}. Stock actual: {self.__stock}")
            self.__stock += cantidad
        elif tipo=="retiro":
            if cantidad>self.__stock:
                raise ValueError(f"No hay suficiente stock para retirar {cantidad}. Stock actual: {self.__stock}")
            self.__stock -= cantidad

        else:
            raise ValueError("Tipo de operación inválido. Use 'ingreso' o 'retiro'.")
        self.__valor_total = self.calcular_valor_total()

    def datos_diccionario(self):
         return {
        "nombre": self.__nombre,
        "codigo": self.__codigo,
        "categoria": self.__categoria,
        "stock": self.__stock,
        "stock_minimo": self.__stock_minimo,
        "stock_maximo": self.__stock_maximo,
        "precio":self.__precio
    }

    def __str__(self):
        return (f"Producto: {self.__nombre} | Código: {self.__codigo} | "
                f"Stock: {self.__stock} (Min: {self.__stock_minimo}, Max: {self.__stock_maximo}) | "
                f"Categoría: {self.__categoria} | "
                f"Precio: {self.__precio}")