from database.DB_connect import DBConnect
import mysql

class AnnoDAO:
    def __init__(self):
        self.listaAnniDAO = []

    def popolaListaAnniDAO(self):
        cnx = None
        cursor = None
        try:
            cnx = DBConnect.get_connection()
            cursor = cnx.cursor()

            anniDB = "SELECT distinct YEAR(gds.`Date`) FROM go_daily_sales gds;"
            cursor.execute(anniDB)
            listaAnniDB = []
            for row in cursor:
                listaAnniDB.append(str(row[0]))
                  # Assicurati di accedere alla data correttamente
            self.listaAnniDAO = listaAnniDB
        except mysql.connector.Error as err:
            print(f"Errore: {err}")
            self.listaAnniDAO = None
        finally:
            if cursor:
                cursor.close()
            if cnx:
                cnx.close()
