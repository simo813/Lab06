from database.DB_connect import DBConnect
import mysql

class BrandDAO:
    def __init__(self):
        self.listaBrandDAO = []

    def popolaListaBrandDAO(self):
        cnx = None
        cursor = None
        try:
            cnx = DBConnect.get_connection()
            if cnx is None:
                raise ConnectionError("Impossibile stabilire la connessione al database.")
            cursor = cnx.cursor()

            brandDB = ("SELECT DISTINCT gp.Product_brand "
                       "FROM go_sales.go_products gp "
                       "ORDER BY gp.Product_brand ASC;")

            cursor.execute(brandDB)
            listaBrandDB = []
            for row in cursor:
                listaBrandDB.append(str(row[0]))  # Assicurati di accedere correttamente al brand
            self.listaBrandDAO = listaBrandDB
        except (mysql.connector.Error, ConnectionError) as err:
            print(f"Errore: {err}")
            self.listaBrandDAO = None
        finally:
            if cursor:
                cursor.close()
            if cnx:
                cnx.close()
