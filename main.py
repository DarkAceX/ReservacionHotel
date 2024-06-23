from manager_db import *
import os, time, platform

"""
MENU PRINCIPAL DEL SISTEMA DE RESERVACION
"""
def main_menu():
    clear()
    print("\tHOTEL ORO VERDE")
    print("[1] ADMINISTRAR HABITACIONES\n[2] ADMINISTRAR RESERVACIONES\n[3] SALIR")
    try:
        option = int(input("OPCION: "))
        if option == 1:
            clear()
            print("[1] RESERVAR HABITACION\n[2] ACTUALIZAR RESERVACION\n[3] BORRAR RESERVACION\n[4] BUSCAR RESERVACION")
        elif option == 2:
            clear()
            print("[1] VER HABITACIONES\n[2] ACTUALIZAR HABITACIONES")
        elif option == 3:
            clear()
            print("Saliendo del sistema...")
            time.sleep(2)
            clear()
            exit()
        print("[ERROR] No existe la opcion ingresada...")
    except ValueError:
        print("[ERROR] Ingreso un digito no valido...")
    time.sleep(2)
    main_menu()    

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

if __name__ == '__main__':
    main_menu()