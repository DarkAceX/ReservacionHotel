from manager_db import *
from connect_db import *
import os, time, platform

"""
MENU PRINCIPAL DEL SISTEMA DE RESERVACION
"""
def main_menu():
    clear()
    print("\tHOTEL ORO VERDE")
    print("[1] ADMINISTRAR RESERVACIONES\n[2] ADMINISTRAR HABITACIONES\n[3] SALIR")
    try:
        option = int(input("OPCION: "))
        if option == 1:
            reservation_menu()
        elif option == 2:
            rooms_menu()
        elif option == 3:
            connect.close()
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
    clear()
    print("[1] RESERVAR HABITACION\n[2] ACTUALIZAR RESERVACION\n[3] BORRAR RESERVACION\n[4] BUSCAR RESERVACION")
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
            reserve.reserve_room("NO")
        elif option == 2:
            clear()
            print("\tACTUALIZACION DE DATOS DE RESERVACION")
            id = int(input("ID DE RESERVACION:"))
            name = input("NOMBRE:")
            email = input("CORREO ELECTRONICO:")
            phone = input("TELEFONO:")
            dni = input("DNI:")
            room = input("HABITACION A RESERVAR:")
            reservation_manager.update_reservation(reservation_manager,id,name,email,phone,dni,room)
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
            time.sleep(2)
            reservation_menu()
    except ValueError:
        clear()
        print("[ERROR] Ingreso un digito no valido...")
        time.sleep(2)
        reservation_menu()
    except:
        clear()
        print("[ERROR] Sucedio algo inesperado...")
        time.sleep(2)
        reservation_menu()

def rooms_menu():
    clear()
    print("[1] VER HABITACIONES\n[2] ACTUALIZAR HABITACIONES")
    try:
        option = int(input("OPCION: "))
        if option == 1:
            clear()
            rooms_manager.all_rooms()
        elif option == 2:
            clear()
            print("\tACTUALIZACION DE DATOS DE HABITACION")
            id = int(input("ID DE HABITACION:"))
            floor = input("PISO:")
            room = input("HABITACION:")
            available = input("DISPONIBILIDAD:")
            rooms_manager.update_room(rooms_manager,id,floor,room,available)
        else:
            clear()   
            print("[ERROR] No existe la opcion ingresada...")
            time.sleep(2)
            rooms_menu()
    except ValueError:
        clear()
        print("[ERROR] Ingreso un digito no valido...")
        time.sleep(2)
        rooms_menu
    except:
        clear()
        print("[ERROR] Sucedio algo inesperado...")
        time.sleep(2)
        rooms_menu()

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

if __name__ == '__main__':
    main_menu()