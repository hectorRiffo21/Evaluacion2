from producto import Producto
from movimiento import Movimiento
from datetime import datetime

class Inventario:
    def __init__(self):
        self.__productos = {}
        #self.__movimiento ={}

    def get_productos(self):
        return self.__productos
    def set_productos(self,productos):
        self.__productos = productos
    def get_movimiento(self):
        return self.__movimiento
    def set_movimiento(self,movimiento):
        self.__movimiento = movimiento




    def registrar_producto(self, producto):
        print("Registrar nuevo producto")
        codigo=input("Codigo Unico del producto: ")
        if codigo in self.__productos:
            print("el producto ya existe")
            return
        nombre=input("nombre del producto: ")
        categoria=input("Categoria: ")
        stock=int(input("Stock: "))
        stock_minimo=int(input("Stock minimo: "))
        stock_maximo=int(input("stock maximo: "))
        codigo_marca=input("codigo de marca: ")
        codigo_unidad=input("codigo de unidad : ")
        producto = Producto(nombre,codigo_marca,codigo_unidad,codigo,stock,stock_minimo,stock_maximo,categoria)
        self.__productos[codigo] = producto
        print(f"Producto '{nombre}' registrado correctamente.")


    def eliminar_producto(self, codigo):
        codigo=input("codigo del producto: ")
        if codigo in self.__productos:
            del self.__productos[codigo]
            print(f"producto con codigo {codigo} eliminado.")
        else:
            raise ValueError("producto no encontrado")
        
    def buscar_producto(self):
        codigo = input("codigo del producto : ")
        producto = self.__productos.get(codigo)
        if producto:
            print(producto)
        else:
            print("Producto no encontrado")
  
    def listar_producto(self):
        if not self.__productos:
            print("No hay productos en el inventario.")
        else:
            for producto in self.__productos.values():
                print(producto)

    def actualizar_stock_con_codigo(self, usuario_responsable):
        codigo_producto=input("Ingresar codigo producto:")
        cantidad=int(input("ingresar o retirar cantidad"))
        producto = self.buscar_producto(codigo_producto)
        if not producto:
            print("producto no encontrado")
            return
        
        if cantidad>0:
            tipo="ingreso"
        else:
            tipo="retiro"
        motivo=input(f"Motivo del {tipo} del producto : ")
        try:
            producto.actualizar_stock(cantidad)
            movimiento = Movimiento(codigo_producto,tipo,abs(cantidad),motivo,usuario_responsable)
            print(f"stock actualizado correctamente. movimiento registrado: {movimiento}")

        except ValueError as e:
            print(f"Error: {e}")

    
