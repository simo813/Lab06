import flet as ft

from model import retailer


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.retailer = retailer

    def handleDropdownAnno(self):
        listaAnniCO = self._model.listaAnniMO()
        for i in listaAnniCO:
            self._view.dropdownAnno.options.append(ft.dropdown.Option (key=i, text=i))
        self._view.update_page()

    def dropdownAnnoChanged(self, e):
        #gestisce l'assegnazione del valore della dropdown degli anni
        if e.control.value == "Nessun valore":
            self._view.dropdownAnnoValue = None
        else:
            self._view.dropdownAnnoValue = e.control.value

    def handleDropdownBrand(self):
        listaBrandCO = self._model.listaBrandMO()
        for i in listaBrandCO:
            self._view.dropdownBrand.options.append(ft.dropdown.Option (key=i, text=i))
        self._view.update_page()


    def dropdownBrandChanged(self, e):
        #gestisce l'assegnazione del valore della dropdown dei brand
        if e.control.value == "Nessun valore":
            self._view.dropdownBrandValue = None
        else:
            self._view.dropdownBrandValue = e.control.value

    def handleDropdownRetailer(self):
        listaRetailerCO = self._model.listaRetailerMO()
        for i in listaRetailerCO:
            self._view.dropdownRetailer.options.append(ft.dropdown.Option (key = i.code, text = i.name))
        self._view.update_page()


    def dropdownRetailerChanged(self, e):
        #gestisce l'assegnazione del valore della dropdown dei brand
        if e.control.value == "Nessun valore":
            self._view.dropdownRetailerValue = None
        else:
            self._view.dropdownRetailerValue = e.control.value

    def handleTopVendite(self,e):
        """
        metodo che passa i valori delle dropdown a model
        """
        self._view.txt_result.controls = []
        self._view.update_page()
        annoTV = self._view.dropdownAnnoValue
        brandTV = self._view.dropdownBrandValue
        retailerTV = self._view.dropdownRetailerValue
        filtriTV = [annoTV, brandTV, retailerTV]
        self._model.filtriTV =filtriTV
        listaTopVenditeCO = self._model.listaTopVenditeMO()
        self._view.txt_result.controls.append(ft.Text(value=f"Top vendite dell' anno {annoTV} del brand {brandTV} e del retailer {retailerTV}\n", color="black",
                                                      text_align=ft.TextAlign.LEFT, width=300, weight=ft.FontWeight.BOLD ))
        stampa = ""
        for i in listaTopVenditeCO:
            stampa += "Anno: " + str(i[0]) + ", " + "Ricavo: " + str(i[1]) + ", " + "Retailer: " + str(i[2]) + ", " + "Prodotto: " + str(i[3]) + "\n"
        self._view.txt_result.controls.append(ft.Text(value=f"{stampa}", color="black",
                            text_align=ft.TextAlign.LEFT, width=300))
        self._view.update_page()

    def handleAnalizzaVendite(self,e):
        """
        metodo che passa i valori delle dropdown a model
        """
        self._view.txt_result.controls = []
        self._view.update_page()
        annoTV = self._view.dropdownAnnoValue
        brandTV = self._view.dropdownBrandValue
        retailerTV = self._view.dropdownRetailerValue
        filtriTV = [annoTV, brandTV, retailerTV]
        self._model.filtriTV = filtriTV
        analizzaVenditeCO = self._model.listaAnalizzaVenditeMO()
        self._view.txt_result.controls.append(
            ft.Text(value=f"Analisi vendite dell' anno {annoTV} del brand {brandTV} e del retailer {retailerTV}\n",
                    color="black",
                    text_align=ft.TextAlign.LEFT, width=300, weight=ft.FontWeight.BOLD))
        stampa = ""
        stampa = "Giro d'affari: " + str(analizzaVenditeCO[0]) + "\n" + "Numero vendite: " + str(analizzaVenditeCO[1]) + "\n" + "Numero retailers coinvolti: " + str(
            analizzaVenditeCO[2]) + "\n" + "Numero prodotti coinvolti: " + str(analizzaVenditeCO[3]) + "\n"
        self._view.txt_result.controls.append(ft.Text(value=f"{stampa}", color="black",
                                                      text_align=ft.TextAlign.LEFT, width=300))
        self._view.update_page()


