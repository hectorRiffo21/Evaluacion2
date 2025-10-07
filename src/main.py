import funciones_main as h

def main():
    while True:
        h.menu_Usuarios()
        try:
            opcion_usuario = int(input("INGRESE OPCIÓN: "))
            if opcion_usuario== 1:
                #user = input("Ingrese nombre de usuario: ")
                #clave = input("Ingrese password: ")
                while True:
                            h.menu_Principal()
                            try:
                                op = int(input("INGRESE OPCIÓN: "))
                                if op == 1:
                                    print("1")
                                elif op == 2:
                                    print("2")
                                elif op == 3:
                                  print("3")
                                elif op == 4:
                                   print("4")
                                elif op == 5:
                                    if input("¿DESEA SALIR [SI/NO]: ").lower() == "si":
                                        break
                                else:
                                    print("OPCION FUERA DE RANGO !!!")
                            except ValueError:
                                print("INGRESE OPCION DENTRO DE RANGO!!")
                    
        
            elif opcion_usuario == 2:
                print("2")
            elif opcion_usuario == 3:
                if input("¿DESEA SALIR [SI/NO]: ").lower() == "si":
                    break
            else:
                print("OPCION FUERA DE RANGO!!")
        except ValueError:
            print("INGRESE OPCION DENTRO DE RANGO!!")


if __name__ == "__main__":
    main()