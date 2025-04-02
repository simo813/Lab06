from database.DB_connect import DBConnect
import mysql

from model.retailer import Retailer


class RetailerDAO:
    def __init__(self):
        self.listaRetailerDAO = []

    def popolaListaRetailerDAO(self):
        cnx = None
        cursor = None
        try:
            cnx = DBConnect.get_connection()
            if cnx is None:
                raise ConnectionError("Impossibile stabilire la connessione al database.")
            cursor = cnx.cursor()

            retailerDB = ("select *  "
                          "from go_sales.go_retailers gr "
                          "order by gr.Retailer_name asc;")

            cursor.execute(retailerDB)
            listaRetailerDB = []
            for row in cursor:
                retailer = Retailer(row[0], row[1], row[2], row[3])
                listaRetailerDB.append(retailer)  # Assicurati di accedere correttamente al brand
            self.listaRetailerDAO = listaRetailerDB
        except (mysql.connector.Error, ConnectionError) as err:
            print(f"Errore: {err}")
            self.listaRetailerDAO = None
        finally:
            if cursor:
                cursor.close()
            if cnx:
                cnx.close()
