import funciones_main as h
from inventario import Inventario
from gestor_empleado import GestorEmpleado
from gestor_movimientos import GestorMovimientos
from conexion_bd import ConexionBD


#funcion que ejecuta todo 
def main():
    db = ConexionBD()
    db.conectar()
    
    gestor = GestorEmpleado()#manejo de empleados
    gestor_movimientos = GestorMovimientos()#manejo de movimientos
    inventario = Inventario(gestor,gestor_movimientos,db)# manejo de inventario
    #inventario.generar_movimientos_prueba()
    #inventario.mostrar_movimientos()
    while True:
        try:
            h.menu_principal()
            opcion = input("seleccione una opcion : ").strip()
            if opcion =="1":
                empleado = gestor.login()
                if empleado:
                    #menu inventario
                    while True:
                        try:
                            h.menu_inventario()
                            opcion_inventario=input("seleccione opcion : ")
                            #registrar producto
                            if opcion_inventario=="1":
                                try:
                                    inventario.registrar_producto()
                                except ValueError:
                                    print("error al registrar producto")
                                #movimiento de variables para mejor encapsulamiento
                                #print("producto registrado correctamente")
                            #listar productos
                            elif opcion_inventario=="2":
                                inventario.listar_producto()
                            #aca de igual forma se llama solo a la funcion para mayor encapsulamiento
                            #actualizar stock
                            elif opcion_inventario=="3":
                                try:
                                    inventario.actualizar_stock_con_codigo()
                                except ValueError:
                                    print("error al actualizar stock")
                            #creacion de funcion para resguardar datos en inventario
                            #buscar producto
                            elif opcion_inventario=="4":
                                inventario.buscar_producto()
                            #eliminar producto
                            elif opcion_inventario=="5":
                                try:
                                    inventario.eliminar_producto()
                                except ValueError:
                                    print("error al eliminar el producto")
                            #menu movimientos
                            elif opcion_inventario=="6":
                                #se muestra menu movimientos
                                h.menu_movimientos()
                                opcion = input("Seleccione una opción: ")

                                if opcion == "1":
                                    #muestra todos los movimientos
                                    gestor_movimientos.mostrar_todos(db)
                                elif opcion == "2":
                                    #filtrado de movimientos por tipo
                                    tipo = input("Tipo (Ingreso, Retiro, Eliminación): ")
                                    gestor_movimientos.filtrar_por_tipo(tipo,db)
                                elif opcion == "3":
                                    #filtrado de movimientos por usuario
                                    usuario = input("Nombre del usuario: ")
                                    gestor_movimientos.filtrar_por_usuario(usuario,db)
                                elif opcion == "4":
                                    return
                                else:
                                    print("Opción no válida.")
                            #muestra productos con stock por debajo del minimo
                            elif opcion_inventario=="7":
                                inventario.producto_bajo_stock_minimo()
                            #actualiza los limites de el stock
                            elif opcion_inventario=="8":
                                inventario.actualizar_limite_de_stock()
                            #regresar al menu principal
                            elif opcion_inventario=="9":
                                gestor.cerrar_sesion()
                                break
                      
                            else:
                                print("opcion invalida")
                        except ValueError:
                            print("Error en el menu de inventario")

                input("enter para continuar")
            #registrar nuevo empleado
            elif opcion =="2":
                try:
                    #llamada de metodo para registro
                    gestor.registrar_empleado()
                except ValueError:
                    print("Error al registrar al empleado")
                input("enter para continuar")
            #mostrar empleados registrados
            elif opcion =="3":
                print("Lista de empleados")
                gestor.mostrar_empleados()
                input("enter para continuar")
            #eliminar empleado por 
            elif opcion=="4":
                try:
                    print("Eliminar empleado")
                    gestor.eliminar_empleado()
                except ValueError:
                    print("error al eliminar al empleado")
                input("Enter para continuar..")
            #salir del programa
            elif opcion=="5":
                print("Saliendo del sistema")
                
                break
            else:
                print("Opcion invalida, intentar nuevamente")
        except ValueError:
            print("Ingresar dato valido")
    #al salir se cierra la conexion a la base de datos
    db.cerrar_conexion()
if __name__ =="__main__":
    main()