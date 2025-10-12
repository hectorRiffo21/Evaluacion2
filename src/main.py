import funciones_main as h
from empleado import Empleado

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
                        try:
                            inventario.registrar_producto()
                            #movimiento de variables para mejor encapsulamiento
                            #print("producto registrado correctamente")
                        except ValueError as e:
                            print("error : ", e)
                    elif opcion_inventario=="2":
                        inventario.listar_producto()
                        #aca de igual forma se llama solo a la funcion para mayor encapsulamiento
                    elif opcion_inventario=="3":
                        inventario.actualizar_stock_con_codigo()
                        #creacion de funcion para resguardar datos en inventario
                   
                    elif opcion_inventario=="4":
                        inventario.buscar_producto()
                      
                    elif opcion_inventario=="5":
                        inventario.eliminar_producto()

                    elif opcion_inventario=="6":
                        break

                    else:
                        print("opcion invalida")

            input("enter para continuar")

        elif opcion =="2":
            gestor.registrar_empleado()
            pasar=input("presionar enter para continuar...")
        elif opcion =="3":
            print("Lista de empleados")
            gestor.mostrar_empleados()
            pasar=input("enter para continuar")
        elif opcion=="4":
            print("Eliminar empleado")
            gestor.eliminar_empleado()
            pasar=input("Enter para continuar..")
        elif opcion=="5":
            print("Salienod del sistema")
            break
        else:
            print("Opcion invalida, reintentar")

if __name__ =="__main__":
    main()