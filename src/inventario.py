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

    def agregar_producto(self, producto):
        codigo = producto.get_codigo()
        if codigo in self.__productos:
            raise ValueError("el producto ya existe")
        self.__productos[codigo] = producto
        print(f"Producto '{producto.get_nombre()}' agregado correctamente.")


    def eliminar_producto(self, codigo):
        if codigo in self.__productos:
            del self.__productos[codigo]
            print(f"producto con codigo {codigo} eliminado.")
        else:
            raise ValueError("producto no encontrado")
        
    def buscar_producto(self,codigo):
        return self.__productos.get(codigo)
  
    def listar_producto(self):
        if not self.__productos:
            print("No hay productos en el inventario.")
        else:
            for producto in self.__productos.values():
                print(producto)

    def actualizar_stock_con_codigo(self,codigo_producto,cantidad,motivo, usuario_responsable):
        producto = self.buscar_producto(codigo_producto)
        if not producto:
            print("producto no encontrado")
            return
        
        if cantidad>0:
            tipo="ingreso"
        else:
            tipo="retiro"
        try:
            producto.actualizar_stock(cantidad)
            movimiento = Movimiento(codigo_producto,tipo,abs(cantidad),motivo,usuario_responsable)
            print(f"stock actualizado correctamente. movimiento registrado: {movimiento}")

        except ValueError as e:
            print(f"Error: {e}")

    
