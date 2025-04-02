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
        self._view.dropdownAnnoValue = e.control.value

    def handleDropdownBrand(self):
        listaBrandCO = self._model.listaBrandMO()
        for i in listaBrandCO:
            self._view.dropdownBrand.options.append(ft.dropdown.Option (key=i, text=i))
        self._view.update_page()


    def dropdownBrandChanged(self, e):
        #gestisce l'assegnazione del valore della dropdown dei brand
        self._view.dropdownBrandValue = e.control.value

    def handleDropdownRetailer(self):
        listaRetailerCO = self._model.listaRetailerMO()
        for i in listaRetailerCO:
            self._view.dropdownRetailer.options.append(ft.dropdown.Option (key = i.code, text = i.name))
        self._view.update_page()


    def dropdownRetailerChanged(self, e):
        #gestisce l'assegnazione del valore della dropdown dei brand
        self._view.dropdownRetailerValue = e.control.value
