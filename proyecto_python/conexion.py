import sqlite3

class Conexion():
    def __init__(self):
        try:
            self.con = sqlite3.connect("banco.db", timeout=10)
            self.crearTablas()
              
        except Exception as ex:
                print(ex)
            
    def crearTablas(self):
        sql_create_table_uno = """CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        usuario TEXT UNIQUE,
        clave TEXT)"""
        cur = self.con.cursor()
        cur.execute(sql_create_table_uno)
        cur.close()
        self.crearAdmin()

    def crearAdmin(self):
        try:
            sql_insert = """INSERT INTO usuarios values(null, '{}', '{}', '{}')""".format("Administrador", "admin", "admin1337")
            cur = self.con.cursor()
            cur.execute(sql_insert)
            self.con.commit()
            
        except Exception as ex:
             print('Ya se creó el usuario admin', ex)
    
    def conectar(self):
        return self.con

# con = Conexion();