from database.DB_connect import DBConnect
import mysql


class AnalizzaVenditeDAO:

    def popolaListaAnalizzaVenditeDAO(self, annoFiltro, brandFiltro, retailerCodeFiltro):
        cnx = None
        cursor = None
        try:
            cnx = DBConnect.get_connection()
            if cnx is None:
                raise ConnectionError("Impossibile stabilire la connessione al database.")
            cursor = cnx.cursor()

            analizzaVenditeDB = ("""SELECT 
                                        SUM(gds.Unit_sale_price * gds.Quantity) AS giroAffari,
                                        COUNT(gds.Date) AS numeroVendite,
                                        COUNT(DISTINCT gds.Retailer_code) AS numeroRetailers, 
                                        COUNT(DISTINCT gds.Product_number) AS numeroProdotti
                                    FROM 
                                        go_sales.go_daily_sales gds
                                    JOIN 
                                        go_sales.go_products gp 
                                    ON 
                                        gp.Product_number = gds.Product_number
                                    WHERE 
                                        YEAR(gds.Date) = COALESCE(%s, YEAR(gds.`Date`))
                                        AND gp.Product_brand = COALESCE(%s, gp.Product_brand)
                                        AND gds.Retailer_code = COALESCE(%s, gds.Retailer_code);
                                                                                                """)

            cursor.execute(analizzaVenditeDB, (annoFiltro, brandFiltro, retailerCodeFiltro))
            listaAnalizzaVenditeDB = []
            for row in cursor:
                giroAffariAV = str(row[0])
                numeroVenditeAV = str(row[1])
                numeroRetailersAV = str(row[2])
                numeroProdottiAV = str(row[3])
                listaAnalizzaVenditeDB.append(giroAffariAV) # Assicurati di accedere correttamente al brand
                listaAnalizzaVenditeDB.append(numeroVenditeAV)
                listaAnalizzaVenditeDB.append(numeroRetailersAV)
                listaAnalizzaVenditeDB.append(numeroProdottiAV)

            print(listaAnalizzaVenditeDB)
            return listaAnalizzaVenditeDB

        except (mysql.connector.Error, ConnectionError) as err:
            print(f"Errore: {err}")

        finally:
            if cursor:
                cursor.close()
            if cnx:
                cnx.close()

