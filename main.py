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
            reservation_menu()
        elif option == 2:
            clear()
            print("[1] VER HABITACIONES\n[2] ACTUALIZAR HABITACIONES")
        elif option == 3:
            clear()
            print("Saliendo del sistema...")
            time.sleep(2)
            clear()
            exit()
        else:   
            print("[ERROR] No existe la opcion ingresada...")
    except ValueError:
        print("[ERROR] Ingreso un digito no valido...")
    time.sleep(2)
    main_menu()    

def reservation_menu():
    try:
        option = int(input("OPCION: "))
        if option == 1:
            clear()
            print("\tRESERVACION DE HABITACION")
            id = int(input("ID DE RESERVACION:"))
            name = input("NOMBRE:")
            email = input("CORREO ELECTRONICO:")
            phone = input("TELEFONO:")
            dni = input("DNI:")
            room = input("HABITACION A RESERVAR:")
            reserve = reservation_manager(id,name,email,phone,dni,room)
            reserve.reserve_room()
        elif option == 2:
            clear()
            print("\tACTUALIZACION DE DATOS DE RESERVACION")
            id = int(input("ID DE RESERVACION:"))
            name = input("NOMBRE:")
            email = input("CORREO ELECTRONICO:")
            phone = input("TELEFONO:")
            dni = input("DNI:")
            room = input("HABITACION A RESERVAR:")
            reservation_manager.update_reservation(id,name,email,phone,dni,room)
        elif option == 3:
            clear()
            print("\tELIMINACION DE RESERVACION")
            id = int(input("ID DE RESERVACION:"))
            reservation_manager.delete_reservation(reservation_manager,id)
        elif option == 4:
            clear()
            print("\tBUSCAR RESERVACION DE HABITACION")            
            id = input("ID DE RESERVACION:")
            reservation_manager.search_reservation(reservation_manager,id)
        else:
            clear()   
            print("[ERROR] No existe la opcion ingresada...")
    except ValueError:
        clear()
        print("[ERROR] Ingreso un digito no valido...")
        time.sleep(2)
        reservation_menu()

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

if __name__ == '__main__':
    main_menu()