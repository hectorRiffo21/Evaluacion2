from producto import Producto
from movimiento import Movimiento
from gestor_empleado import GestorEmpleado
from datetime import datetime, timedelta

class Inventario:
    def __init__(self, gestor_empleado,gestor_movimientos):
        self.__productos = {}
        #self.__productos_por_categoria={}
        self.__gestor_empleado= gestor_empleado
        self.__gestor_movimientos = gestor_movimientos

    #def get_gestor_empleado(self):
    #    return self.__gestor_empleado

    def get_productos(self):
        return self.__productos
    def set_productos(self,productos):
        self.__productos = productos
    def get_producto_por_categoria(self):
        return self.__productos_por_categoria
    def get_movimientos(self):
        return self.__movimientos
    def set_movimientos(self,movimientos):
        self.__movimientos = movimientos




    def registrar_producto(self):
        usuario = self.__gestor_empleado.get_usuario_actual()
        print("Registrar nuevo producto")
        codigo=input("Codigo Unico del producto :")
        if codigo in self.__productos:
            print("el producto ya existe")
            return
        nombre=input("nombre del producto :")
        categoria=input("Categoria :")
        stock=int(input("Stock :"))
        stock_minimo=int(input("Stock minimo :"))
        stock_maximo=int(input("stock maximo :"))
        precio=int(input("Precio: "))
        producto = Producto(nombre,codigo,stock,stock_minimo,stock_maximo,categoria,precio)
        monto_total = producto.calcular_valor_total()
        self.__productos[codigo] = producto
        movimiento = Movimiento(codigo_producto=codigo,usuario_responsable=usuario.get_nombre_usuario(),tipo="registro",cantidad=stock,motivo="Ingreso inicial de producto",stock_antes=0,stock_despues=stock,monto_total=monto_total)
        self.__gestor_movimientos.registrar_movimiento(movimiento)
        print(f"Producto '{nombre}' registrado correctamente.")
        print(f" movimiento registrado: {movimiento}")

    def listar_producto(self):
        if not self.__productos:
            print("No hay productos en el inventario.")
            return
        print("\nOpciones de listado:")
        print("1. Mostrar todos los productos")
        print("2. Mostrar productos por categoria")
        opcion= input("Seleccione una opcion: ").strip()
        if opcion == "1":
            print("Lista de todos los productos")
            for producto in self.__productos.values():
                print(producto)
        elif opcion == "2":
            categoria = input("Ingrese la categoria: ").strip().lower()
            encontrados = [
            p for p in self.__productos.values()
            if p.get_categoria().lower() == categoria
            ]
            if encontrados:
                print(f"\n--- Productos en la categoria '{categoria}' ---")
                for prod in encontrados:
                    print(prod)
                print(f"Total de productos en esta categoria: {len(encontrados)}")
            else:
                print("No hay productos registrados en esa categoria.")
        else:
            print("OPcion invalida, intentar nuevamente.")
                

    def actualizar_stock_con_codigo(self):
        usuario = self.__gestor_empleado.get_usuario_actual()
        codigo_producto=input("Ingresar codigo producto:")
        producto = self.__productos.get(codigo_producto)
        if not producto:
            print("producto no encontrado")
            return
        print("\n1.Ingresar\n2.Retirar")
        opcion=input("Ingresar opcion : ")
        if opcion =="1":
            tipo="ingreso"
            cantidad=int(input("cantidad a ingresar : "))
        elif opcion=="2":
            tipo="retiro"
            cantidad=int(input("cantidad a retirar : "))

        motivo=input(f"Motivo del {tipo} del producto : ")
        try:
            stock_antes= producto.get_stock()
            producto.actualizar_stock(cantidad,tipo)
            stock_despues = producto.get_stock()
            monto_total = producto.calcular_valor_total()
            movimiento = Movimiento(codigo_producto=codigo_producto,usuario_responsable=usuario.get_nombre_usuario(),tipo=tipo,cantidad=abs(cantidad),motivo=motivo,stock_antes=stock_antes,stock_despues=stock_despues,monto_total=monto_total)
            self.__gestor_movimientos.registrar_movimiento(movimiento)
            print(f"stock actualizado correctamente. movimiento registrado: {movimiento}")

        except ValueError as e:
            print(f"Error: {e}")

    def buscar_producto(self):
        codigo=(input("Ingresar codigo del producto: "))
        producto = self.__productos.get(codigo)
        if producto:
                print(producto)
        else:
                 print("Producto no encontrado")
     
        


    def eliminar_producto(self):
        codigo=input("codigo del producto: ")
        usuario=self.__gestor_empleado.get_usuario_actual()
        if codigo in self.__productos:
            producto =self.__productos[codigo]
            stock_antes = producto.get_stock()
            nombre = producto.get_nombre()
            categoria = producto.get_categoria()
            stock_minimo= producto.get_stock_minimo()
            stock_maximo = producto.get_stock_maximo()
            confirmacion=input(f"¿Seguro que desea eliminar el producto '{nombre}'? [s/n]: ").lower()
            if confirmacion!="s":
                print("operacion cancelada.")
                return
            
            print(f"producto con codigo {codigo} eliminado.")
            monto_total = producto.calcular_valor_total()
            movimiento = Movimiento(codigo_producto=codigo,usuario_responsable=usuario.get_nombre_usuario(),tipo="eliminacion",cantidad=0,motivo="eliminaacion de producto de sistema",stock_antes=stock_antes,stock_despues=0, monto_total=monto_total)
            self.__gestor_movimientos.registrar_movimiento(movimiento)
            del self.__productos[codigo]
            print(f"Producto : '{nombre}' | Categoria : '{categoria}' | Eliminado Correctamente. detalles guardados en movimiento")
        else:
            raise ValueError("producto no encontrado")
        

    def producto_bajo_stock_minimo(self):
        print("Productos por debajo del stock minimo : ")
        encontrados = False
        for producto in self.__productos.values():
            if producto.get_stock() < producto.get_stock_minimo():
                print(producto)
                encontrados = True
        if not encontrados:
            print("No hay productos por debajo del stock minimo.")

    def actualizar_limite_de_stock(self):
        codigo=input("codigo del producto: ")
        producto= self.__productos.get(codigo)
        if not producto:
            print("producto no encontrado.")
            return
        try:
            nuevo_stock_minimo = int(input(f"Ingresar nuevo stock mínimo (stock minimo actual: {producto.get_stock_minimo()}): "))
            nuevo_stock_maximo = int(input(f"Ingresar nuevo stock máximo (stock maximo actual: {producto.get_stock_maximo()}): "))
            if nuevo_stock_minimo > nuevo_stock_maximo:
                print("El stock mínimo no puede ser mayor que el máximo.")
                return
            producto.set_stock_minimo(nuevo_stock_minimo)
            producto.set_stock_maximo(nuevo_stock_maximo)
            print("Límites de stock actualizados correctamente.")
        except ValueError:
            print("Debe ingresar un número válido.")



    def generar_movimientos_prueba(self):
    # Movimiento reciente (hoy)
        mov1 = Movimiento(
            codigo_producto="P001",
            usuario_responsable="hector",
            tipo="ingreso",
            cantidad=10,
            motivo="Ingreso inicial de stock",
            stock_antes=0,
            stock_despues=10,
            monto_total= 100000
        )
        self.__gestor_movimientos.registrar_movimiento(mov1)

    # Movimiento de hace 5 días
        mov2 = Movimiento(
            codigo_producto="P002",
            usuario_responsable="sofia",
            tipo="retiro",
            cantidad=3,
            motivo="Venta al cliente",
            stock_antes=15,
            stock_despues=12,
            monto_total= 200000
        )
        mov2._Movimiento__fecha = datetime.now() - timedelta(days=5)
        self.__gestor_movimientos.registrar_movimiento(mov2)

    # Movimiento de hace 25 días
        mov3 = Movimiento(
            codigo_producto="P003",
            usuario_responsable="admin",
            tipo="ingreso",
            cantidad=20,
            motivo="Reposición mensual",
            stock_antes=10,
            stock_despues=30,
            monto_total= 15000
        )
        mov3._Movimiento__fecha = datetime.now() - timedelta(days=25)
        self.__gestor_movimientos.registrar_movimiento(mov3)


        print("Movimientos de prueba creados correctamente.")

    def mostrar_movimientos(self):
        if not Movimiento.movimientos_registrados:
            print("No hay movimientos registrados.")
            return
        opcion = input("Ingrese opción: ")
        ahora = datetime.now()

        if opcion == "1":
            fecha_str = input("Ingrese la fecha (formato YYYY-MM-DD): ")
            try:
                fecha_obj = datetime.strptime(fecha_str, "%Y-%m-%d")
                movimientos_filtrados = [
                    m for m in Movimiento.movimientos_registrados.values()
                    if m.get_fecha().date() == fecha_obj.date()
                ]
            except ValueError:
                print("Formato de fecha incorrecto.")
                return

        elif opcion == "2":
            hace_una_semana = ahora - timedelta(days=7)
            movimientos_filtrados = [
                m for m in Movimiento.movimientos_registrados.values()
                if m.get_fecha() >= hace_una_semana
            ]

        elif opcion == "3":
            hace_un_mes = ahora - timedelta(days=30)
            movimientos_filtrados = [
                m for m in Movimiento.movimientos_registrados.values()
                if m.get_fecha() >= hace_un_mes
            ]

        elif opcion == "4":
            movimientos_filtrados = Movimiento.movimientos_registrados.values()
        else:
            print("Opción inválida.")
            return

        if movimientos_filtrados:
            print("\n--- Historial de movimientos ---")
            for m in movimientos_filtrados:
                print(m)
        else:
            print("No se encontraron movimientos en ese rango.")