import funciones_main as h
from inventario import Inventario
from gestor_empleado import GestorEmpleado
from gestor_movimientos import GestorMovimientos




def main():
    gestor = GestorEmpleado()
    gestor_movimientos = GestorMovimientos()
    inventario = Inventario(gestor,gestor_movimientos)
    inventario.generar_movimientos_prueba()
    inventario.mostrar_movimientos()
    while True:
        try:
            h.menu_principal()
            opcion = input("seleccione una opcion : ").strip()
            if opcion =="1":
                empleado = gestor.login()
                if empleado:
                    #print("session iniciada")
                    while True:
                        try:
                            h.menu_inventario()
                            opcion_inventario=input("seleccione opcion : ")
                            if opcion_inventario=="1":
                                try:
                                    inventario.registrar_producto()
                                except ValueError:
                                    print("error al registrar producto")
                                #movimiento de variables para mejor encapsulamiento
                                #print("producto registrado correctamente")
            
                            elif opcion_inventario=="2":
                                inventario.listar_producto()
                            #aca de igual forma se llama solo a la funcion para mayor encapsulamiento
                            elif opcion_inventario=="3":
                                try:
                                    inventario.actualizar_stock_con_codigo()
                                except ValueError:
                                    print("error al actualizar stock")
                            #creacion de funcion para resguardar datos en inventario
                   
                            elif opcion_inventario=="4":
                                inventario.buscar_producto()
                      
                            elif opcion_inventario=="5":
                                try:
                                    inventario.eliminar_producto()
                                except ValueError:
                                    print("error al eliminar el producto")

                            elif opcion_inventario=="6":
                                h.menu_movimientos()
                                opcion = input("Seleccione una opción: ")

                                if opcion == "1":
                                    gestor_movimientos.mostrar_todos()
                                elif opcion == "2":
                                    tipo = input("Tipo (Ingreso, Retiro, Eliminación): ")
                                    gestor_movimientos.filtrar_por_tipo(tipo)
                                elif opcion == "3":
                                    usuario = input("Nombre del usuario: ")
                                    gestor_movimientos.filtrar_por_usuario(usuario)
                                elif opcion == "4":
                                    return
                                else:
                                    print("Opción no válida.")
                      
                            elif opcion_inventario=="7":
                                inventario.producto_bajo_stock_minimo()
                            elif opcion_inventario=="8":
                                inventario.actualizar_limite_de_stock()
                            elif opcion_inventario=="9":
                                gestor.cerrar_sesion()
                                break
                      
                            else:
                                print("opcion invalida")
                        except ValueError:
                            print("Error en el menu de inventario")

                input("enter para continuar")

            elif opcion =="2":
                try:
                    gestor.registrar_empleado()
                except ValueError:
                    print("Error al registrar al empleado")
                input("enter para continuar")
            elif opcion =="3":
                print("Lista de empleados")
                gestor.mostrar_empleados()
                input("enter para continuar")
            elif opcion=="4":
                try:
                    print("Eliminar empleado")
                    gestor.eliminar_empleado()
                except ValueError:
                    print("error al eliminar al empleado")
                input("Enter para continuar..")
            elif opcion=="5":
                print("Saliendo del sistema")
                break
            else:
                print("Opcion invalida, intentar nuevamente")
        except ValueError:
            print("Ingresar dato valido")
if __name__ =="__main__":
    main()