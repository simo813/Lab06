from database.annoDAO import AnnoDAO
from database.brandDAO import BrandDAO
from database.retailerDAO import RetailerDAO


class Model:
    def __init__(self):
        self.anno = AnnoDAO()
        self.brand = BrandDAO()
        self.retailer = RetailerDAO()

    def listaAnniMO(self):
        self.anno.popolaListaAnniDAO()
        return self.anno.listaAnniDAO

    def listaBrandMO(self):
        self.brand.popolaListaBrandDAO()
        return self.brand.listaBrandDAO

    def listaRetailerMO(self):
        self.retailer.popolaListaRetailerDAO()
        return self.retailer.listaRetailerDAO