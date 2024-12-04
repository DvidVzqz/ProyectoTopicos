import pymysql

def conectar():
    mydb = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="laboratorio_clinico"
    )
    return mydb
if __name__ == "__main__":
    conectar()