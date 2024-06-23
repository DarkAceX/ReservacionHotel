import sqlite3

"""
CONEXION CON LA BASE DE DATOS
"""
connect = sqlite3.connect('Reservacion_db')
con = connect.cursor()
