import funciones_main as h
from empleado import Empleado
from producto import Producto
from inventario import Inventario
from gestor_empleado import GestorEmpleado




def main():
    gestor = GestorEmpleado()
    inventario = Inventario()
    while True:
        h.menu_principal()
        opcion = input("seleccione una opcion : ").strip()
        if opcion =="1":
            usuario = input("Nombre de usuario : ")
            clave = input("contraseña : ")
            empleado = gestor.login(usuario,clave)
            if empleado:
                print("session iniciada")
                print(f"\nBienvenido {empleado.get_nombre()} ({empleado.get_cargo_trabajo()})")
                empleado.mostrar_informacion_empleado()
                while True:
                    h.menu_inventario()
                    opcion_inventario=input("seleccione opcion : ")
                    if opcion_inventario=="1":
                        nombre=input("nombre del producto: ")
                        codigo=input("Codigo Unico del producto: ")
                        categoria=input("Categoria: ")
                        stock=int(input("Stock: "))
                        stock_minimo=int(input("Stock minimo: "))
                        stock_maximo=int(input("stock maximo: "))
                        codigo_marca=input("codigo de marca: ")
                        codigo_unidad=input("codigo de unidad : ")
                        producto = Producto(nombre,codigo_marca,codigo_unidad,codigo,stock,stock_minimo,stock_maximo,categoria)
                        try:
                            inventario.agregar_producto(producto)
                            print("producto registrado correctamente")
                        except ValueError as e:
                            print("error : ", e)
                    elif opcion_inventario=="2":
                        productos=inventario.listar_producto()
                        if not productos:
                            print("no hay productos registrados.")
                        else:
                            for prod in productos:
                                print(prod)

                    elif opcion_inventario=="3":
                        codigo = input("codigo del producto: ")
                        prod=inventario.buscar_producto(codigo)
                        if prod:
                            cantidad=int(input("cantidad a agregar (+) o retirar (-):"))
                            try:
                                prod.actualizar_stock(cantidad)
                                print(f"stock actualizado. nuevo stock: {prod.get_stock()}")
                            except ValueError as e:
                                print("error: ", e)
                        else:
                            print("producto no encontrado")
                    elif opcion_inventario=="4":
                        codigo = input("codigo del producto : ")
                        prod = inventario.buscar_producto(codigo)
                        if prod:
                            print(prod)
                        else:
                            print("producto no encontrado")
                    elif opcion_inventario=="5":
                        codigo=input("codigo del producto: ")
                        try:
                            inventario.eliminar_producto(codigo)
                            print("producto eliminado correctamente.")
                        except ValueError as e:
                            print("Error:",e)

                    elif opcion_inventario=="6":
                        break

                    else:
                        print("opcion invalida")

            input("enter para continuar")

        elif opcion =="2":
            print("Registrar nuevo empleado")
            nombre= input("Nombre:")
            apellido=input("Apellido:")
            rut=input("Rut:")
            celular=input("Celular:")
            correo_electronico=input("Correo electronico:")
            genero=input("Genero:")
            nombre_usuario=input("Nombre de usuario: ")
            clave=input("clave:")
            cargo_trabajo=input("cargo:")

            gestor.registrar_empleado(nombre,apellido,rut,celular,correo_electronico,genero,nombre_usuario,clave,cargo_trabajo)
            pasar=input("presionar enter para continuar...")
        elif opcion =="3":
            print("Lista de empleados")
            gestor.mostrar_empleados()
            pasar=input("enter para continuar")
        elif opcion=="4":
            print("Eliminar empleado")
            nombre_usuario = input("Nombre de usuario del empleado a eliminar : ")
            gestor.eliminar_empleado(nombre_usuario)
            pasar=input("Enter para continuar..")
        elif opcion=="5":
            print("Salienod del sistema")
            break
        else:
            print("Opcion invalida, reintentar")

if __name__ =="__main__":
    main()