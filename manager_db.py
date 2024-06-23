import os, time, datetime
from connect_db import connect,con
"""
ADMINISTRACION DE LAS RESERVACIONES
"""
class reservation_manager:
    def __init__(self,id,name,email,phone,dni,room):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.dni = dni
        self.room = room
        self.date = datetime.datetime.today().strftime('%Y/%m/%d')
    
    def reserve_room(self):
        con.execute("INSERT INTO Reservations(ID_RESERVE,NAME,EMAIL,PHONE,DNI,ROOM,DATE) VALUES(?,?,?,?,?,?)",(self.id,self.name,self.email,self.phone,self.dni,self.room,self.date))
        connect.commit()
        connect.close()
        time.sleep(2)
        os.system("cls")
        print("\tReservacion realizada con exito")
        print(f"Nombre:{self.name}\nCorreo Electronico:{self.email}\nNumero Telefonico:{self.phone}\nDni:{self.dni}\nRoom:{self.room}\nDate:{self.date}")
    
    def delete_reservation(id):
        con.execute("DELETE FROM Reservations WHERE ID_RESERVE=?",(id))
        connect.commit()
        connect.close()
        time.sleep(2)
        os.system("cls")
        print("\tReservacion eliminada con exito")
    
    def update_reservation(id,name,email,phone,dni,room):
        con.execute("UPDATE Reservations SET NAME=?,EMAIL=?,PHONE=?,DNI=?,ROOM=? WHERE ID_RESERVE=?",(name,email,phone,dni,room,id))
        connect.commit()
        connect.close()
        time.sleep(2)
        os.system("cls")
        print("\tReservacion actualizada con exito")
        print(f"Nombre:{name}\nCorreo Electronico:{email}\nNumero Telefonico:{phone}\nDni:{dni}\nRoom:{room}\nDate:{datetime.datetime.today().strftime('%Y/%m/%d')}")
    
    def search_reservation(id):
        con.execute("SELECT * FROM Reservations WHERE ID_RESERVE=?",(id))
        data = con.fetchall()
        for i in data:
            os.system("cls")
            print(f"Nombre:{i[1]}\nCorreo Electronico:{i[2]}\nNumero Telefonico:{i[3]}\nDni:{i[4]}\nRoom:{i[5]}\nDate:{i[6]}")
        connect.commit()
        connect.close()
        time.sleep(2)
        
"""
ADMINISTRACION DE LAS HABITACIONES
"""
class rooms_manager:
    def all_rooms():
        con.execute("SELECT * FROM Rooms")
        data = con.fetchall()
        for i in data:
            print(f"Id:{i[0]}\tPiso:{i[1]}\tHabitacion:{i[2]}\tDisponible:{i[3]}\n")
        connect.commit()
        connect.close()
        time.sleep(2)
    
    def update_room(id,floor,room,available):
        con.execute("UPDATE Rooms SET FLOOR=?,ROOM=?,AVAILABLE=? WHERE ID=?",(floor,room,available,id))
        connect.commit()
        connect.close()
        time.sleep(2)
        os.system("cls")
        print("\tHabitacion actualizada con exito")
