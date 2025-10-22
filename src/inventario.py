from producto import Producto
from movimiento import Movimiento
from gestor_empleado import GestorEmpleado
from conexion_bd import ConexionBD

#clase que maneja el inventario de los productos
class Inventario:
    def __init__(self, gestor_empleado,gestor_movimientos, conexion_db:ConexionBD):
        #diccionario para operaciones en memoria de los productos
        self.__productos = {}
        #self.__productos_por_categoria={}
        self.__gestor_empleado= gestor_empleado
        self.__gestor_movimientos = gestor_movimientos
        self.__db = conexion_db
        #conecta a la base de datos
        self.__db.conectar()
        #carga los productos existentes en la base de datos
        self.cargar_desde_bd()
    #def get_gestor_empleado(self):
    #    return self.__gestor_empleado

    #metodos get y sets
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


    #carga todos los productos activos en la base de datos
    def cargar_desde_bd(self):
        productos = self.__db.ejecutar_consulta("SELECT codigo, nombre, categoria, stock, stock_minimo, stock_maximo, precio FROM productos")
        for p in productos:
            codigo, nombre, categoria, stock, stock_minimo, stock_maximo, precio = p
            self.__productos[codigo] = Producto(nombre, codigo, stock, stock_minimo, stock_maximo, categoria, precio)


    #registra un producto nuevo o reactiva un codigo inactivo
    def registrar_producto(self):
        usuario = self.__gestor_empleado.get_usuario_actual()
        print("Registrar nuevo producto")
        codigo=input("Codigo Unico del producto :")
        existente= self.__db.ejecutar_consulta("SELECT nombre, activo FROM productos WHERE codigo = ?", (codigo,))
        if existente:
            nombre_existente, activo = existente[0]
            if activo == 1:
                print("El producto ya existe en la base de datos")
                return
            else:
                #activar producto inactivo
                print("El producto existe pero está inactivo. Reactivando...")
                nombre = input("nombre del producto :")
                categoria = input("Categoria :")
                stock = int(input("Stock :"))
                stock_minimo = int(input("Stock minimo :"))
                stock_maximo = int(input("stock maximo :"))
                precio = int(input("Precio: "))
                #actualiza datos y activa el codigo de producto
                self.__db.ejecutar_instruccion(
                    "UPDATE productos SET nombre=?, categoria=?, stock=?, stock_minimo=?, stock_maximo=?, precio=?, activo=1 WHERE codigo=?",
                    (nombre, categoria, stock, stock_minimo, stock_maximo, precio, codigo)
                )
                producto = Producto(nombre, codigo, stock, stock_minimo, stock_maximo, categoria, precio)
                self.__productos[codigo] = producto
                # Registrar movimiento de reactivación
                movimiento = Movimiento(
                    codigo_producto=codigo,
                    usuario_responsable=usuario.get_nombre_usuario(),
                    tipo="reactivacion",
                    cantidad=stock,
                    motivo="Reactivación de producto inactivo",
                    stock_antes=0,
                    stock_despues=stock,
                    monto_total=producto.calcular_valor_total()
                )
                self.__gestor_movimientos.registrar_movimiento_sql(movimiento, self.__db)
                print(f"Producto '{nombre}' reactivado y movimiento registrado.")
                return
        #registrar un producto nuevo
        nombre=input("nombre del producto :")
        categoria=input("Categoria :")
        stock=int(input("Stock :"))
        stock_minimo=int(input("Stock minimo :"))
        stock_maximo=int(input("stock maximo :"))
        precio=int(input("Precio: "))
        registrar= self.__db.ejecutar_instruccion(
            "INSERT INTO productos (codigo, nombre, categoria, stock, stock_minimo, stock_maximo, precio) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (codigo, nombre, categoria, stock, stock_minimo, stock_maximo, precio)
        )
        if registrar:
            print(f"Producto '{nombre}' registrado correctamente.")
        producto = Producto(nombre,codigo,stock,stock_minimo,stock_maximo,categoria,precio)
        monto_total = producto.calcular_valor_total()
        self.__productos[codigo] = producto
        #registro de movimiento
        movimiento = Movimiento(codigo_producto=codigo,usuario_responsable=usuario.get_nombre_usuario(),tipo="registro",cantidad=stock,motivo="Ingreso inicial de producto",stock_antes=0,stock_despues=stock,monto_total=monto_total)
        self.__gestor_movimientos.registrar_movimiento_sql(movimiento, self.__db)
        print(f"Producto '{nombre}' registrado correctamente en la base de datos.")
        print(f" movimiento registrado: {movimiento}")

    #listar productos segun la opcion escogida
    def listar_producto(self):
        print("\nOpciones de listado:")
        print("1. Mostrar todos los productos")
        print("2. Mostrar productos por categoria")
        opcion= input("Seleccione una opcion: ").strip()
        if opcion == "1":
            #consulta todos los productos
            print("Lista de todos los productos")
            productos = self.__db.ejecutar_consulta("SELECT * FROM productos WHERE activo = 1")
        elif opcion == "2":
            #filtrado por categoria elegida
            categoria = input("Ingrese la categoria: ").strip().lower()
            productos = self.__db.ejecutar_consulta(
            "SELECT * FROM productos WHERE LOWER(categoria) = LOWER(?) AND activo = 1",(categoria,))
        else:
            print("Opción inválida.")
            return
        #se muestran los productos encontrados
        if not productos:
            print("No se encontraron productos.")
        else:
            print("\n--- Lista de productos ---")
            for p in productos:
                print(f"Código: {p[0]} | Nombre: {p[1]} | Categoría: {p[2]} | Stock: {p[3]} | Mínimo: {p[4]} | Máximo: {p[5]} | Precio: {p[6]}")
                
                
    #actualiza el stock de un producto mediante el codigo unico que tiene
    def actualizar_stock_con_codigo(self):
        usuario = self.__gestor_empleado.get_usuario_actual()
        codigo_producto=input("Ingresar codigo producto:")
        #consulta stock actual y limites de stock
        producto_bd = self.__db.ejecutar_consulta("SELECT stock, stock_minimo, stock_maximo, precio FROM productos WHERE codigo = ?", (codigo_producto,))
        if not producto_bd:
            print("producto no encontrado")
            return
        stock_actual, stock_minimo, stock_maximo, precio = producto_bd[0]
        print("\n1.Ingresar\n2.Retirar")
        #determina el tipo de movimiento y calcula el nuevo stock
        opcion=input("Ingresar opcion : ")
        if opcion =="1":
            tipo="ingreso"
            cantidad=int(input("cantidad a ingresar : "))
            nuevo_stock =stock_actual+cantidad
            if nuevo_stock> stock_maximo:
                print(f"No se puede ingresar más de la cantidad máxima ({stock_maximo}).")
                return
        elif opcion=="2":
            tipo="retiro"
            cantidad=int(input("cantidad a retirar : "))
            nuevo_stock =stock_actual-cantidad
            if nuevo_stock < 0:
                print("No se puede retirar más del stock disponible.")
                return
        else:
            print("Opcion invalida")
            return

        motivo=input(f"Motivo del {tipo} del producto : ")
        try:
            stock_antes= stock_actual
            #actualizacion de stock en la base de datos
            self.__db.ejecutar_instruccion(
            "UPDATE productos SET stock = ? WHERE codigo = ?",
            (nuevo_stock, codigo_producto)
            )
            monto_total = nuevo_stock * precio
            #crea y registra movimiento
            movimiento = Movimiento(codigo_producto=codigo_producto,usuario_responsable=usuario.get_nombre_usuario(),tipo=tipo,cantidad=abs(cantidad),motivo=motivo,stock_antes=stock_antes,stock_despues=nuevo_stock,monto_total=monto_total)
            self.__gestor_movimientos.registrar_movimiento_sql(movimiento,self.__db)
            print(f"stock actualizado correctamente. movimiento registrado: {movimiento}")

        except ValueError as e:
            print(f"Error: {e}")

    #buscar producto por codigo unico mostrando la informacion
    def buscar_producto(self):
        codigo=(input("Ingresar codigo del producto: "))
        producto = self.__db.ejecutar_consulta(
        "SELECT codigo, nombre, categoria, stock, stock_minimo, stock_maximo, precio FROM productos WHERE codigo = ?",
        (codigo,)
    )
        if producto:
            p = producto[0]
            print(f"""
        Producto encontrado:
        - Código: {p[0]}
        - Nombre: {p[1]}
        - Categoría: {p[2]}
        - Stock actual: {p[3]}
        - Stock mínimo: {p[4]}
        - Stock máximo: {p[5]}
        - Precio: ${p[6]}
        """)
        else:
                 print("Producto no encontrado")
     
        

    #elimina producto y registra el movimiento
    def eliminar_producto(self):
        codigo=input("codigo del producto: ")
        usuario=self.__gestor_empleado.get_usuario_actual()
        producto =self.__db.ejecutar_consulta("SELECT nombre, categoria, stock, stock_minimo, stock_maximo, precio, activo FROM productos WHERE codigo = ?",(codigo,))
        if not producto or producto[0][6] == 0:
            print("Producto no encontrado o ya inactivo.")
            return
        nombre, categoria, stock_actual, stock_minimo, stock_maximo, precio, activo = producto[0]
        confirmacion=input(f"¿Seguro que desea eliminar el producto '{nombre}'? [s/n]: ").lower()
        if confirmacion!="s":
            print("operacion cancelada.")
            return
        try:
            #marca el producto
            self.__db.ejecutar_instruccion(
            "UPDATE productos SET activo=0 WHERE codigo=?", (codigo,)
            )
            stock_antes = stock_actual
            monto_total = stock_actual * precio
            #registra movimiento de la eliminacion
            movimiento = Movimiento(codigo_producto=codigo,usuario_responsable=usuario.get_nombre_usuario(),tipo="eliminacion",cantidad=0,motivo="eliminacion de producto de sistema",stock_antes=stock_antes,stock_despues=0, monto_total=monto_total)
            self.__gestor_movimientos.registrar_movimiento_sql(movimiento,self.__db)
            print(f"Producto '{nombre}' | Categoría: '{categoria}' eliminado correctamente. "
              f"Detalles guardados en movimiento.")
        except Exception as e:
            print(f"error al eliminar el producto {e}")
        
    #muestra stock de productos que esten por debajo del minimo registrado
    def producto_bajo_stock_minimo(self):
        print("Productos por debajo del stock minimo : ")
        try:
            productos = self.__db.ejecutar_consulta(
            "SELECT codigo, nombre, categoria, stock, stock_minimo, stock_maximo, precio "
            "FROM productos WHERE stock < stock_minimo"
        )
            if not productos:
                print("No hay productos por debajo del stock minimo.")
                return
            for codigo, nombre, categoria, stock, stock_minimo, stock_maximo, precio in productos:
                print(f"Código: {codigo} | Nombre: {nombre} | Categoría: {categoria} | "
                  f"Stock: {stock} | Stock Mínimo: {stock_minimo} | Stock Máximo: {stock_maximo} | "
                  f"Precio: {precio}")
        except Exception as e:
            print(f"Error al obtener productos por debajo del stock mínimo: {e}")


    #actualiza los limites de stock minimo y maximo de un producto por medio de su codigo unico
    def actualizar_limite_de_stock(self):
        codigo=input("codigo del producto: ")
        producto = self.__db.ejecutar_consulta(
        "SELECT stock_minimo, stock_maximo FROM productos WHERE codigo = ?", (codigo,)
    )
        if not producto:
            print("producto no encontrado.")
            return
        stock_minimo_actual, stock_maximo_actual = producto[0]
        try:
            nuevo_stock_minimo = int(input(f"Ingresar nuevo stock mínimo (stock minimo actual: {stock_minimo_actual}): "))
            nuevo_stock_maximo = int(input(f"Ingresar nuevo stock máximo (stock maximo actual: {stock_maximo_actual}): "))
            if nuevo_stock_minimo > nuevo_stock_maximo:
                print("El stock mínimo no puede ser mayor que el máximo.")
                return
            #actualiza datos den la base de datos
            self.__db.ejecutar_instruccion(
            "UPDATE productos SET stock_minimo = ?, stock_maximo = ? WHERE codigo = ?",
            (nuevo_stock_minimo, nuevo_stock_maximo, codigo)
        )
            print("Límites de stock actualizados correctamente.")
        except ValueError:
            print("Debe ingresar un número válido.")

