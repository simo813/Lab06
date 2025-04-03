from database.DB_connect import DBConnect
import mysql




class TopVenditeDAO:



    def popolaListaTopVenditeDAO(self, annoFiltro, brandFiltro, retailerCodeFiltro):
        cnx = None
        cursor = None
        try:
            cnx = DBConnect.get_connection()
            if cnx is None:
                raise ConnectionError("Impossibile stabilire la connessione al database.")
            cursor = cnx.cursor()

            topVenditeDB = ("""SELECT 
                                    gds.`Date`,
                                    (gds.Unit_sale_price * gds.Quantity) AS ricavo,
                                    gds.Retailer_code, 
                                    gr.Retailer_name,
                                    gp.Product_number, 
                                    gp.Product_brand 
                                FROM 
                                    go_sales.go_daily_sales gds
                                JOIN 
                                    go_sales.go_products gp 
                                ON 
                                    gp.Product_number = gds.Product_number
                                JOIN
                                    go_sales.go_retailers gr  
                                ON
                                    gds.Retailer_code = gr.Retailer_code 
                                WHERE 
                                    YEAR(gds.`Date`) = COALESCE(%s, YEAR(gds.`Date`))
                                    AND gp.Product_brand = COALESCE(%s, gp.Product_brand)
                                    AND gr.Retailer_code = COALESCE(%s, gr.Retailer_code)
                                    
                                ORDER BY 
                                    ricavo DESC;
                                                                        """)

            cursor.execute(topVenditeDB, (annoFiltro, brandFiltro, retailerCodeFiltro))
            listaTopVenditeDB = []
            for row in cursor:
                annoTV = row[0]
                ricavoTV = row[1]
                retailerTV = row[2]
                prodottoTV = row[4]
                vendita = [annoTV, ricavoTV, retailerTV, prodottoTV]
                listaTopVenditeDB.append(vendita)  # Assicurati di accedere correttamente al brand

            listaFinaleDB = []
            for i in range(len(listaTopVenditeDB)):
                if i >= 5:
                    break
                listaFinaleDB.append(listaTopVenditeDB[i])
            return listaFinaleDB

        except (mysql.connector.Error, ConnectionError) as err:
            print(f"Errore: {err}")

        finally:
            if cursor:
                cursor.close()
            if cnx:
                cnx.close()

