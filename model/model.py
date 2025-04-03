from database.analizzaVenditeDAO import AnalizzaVenditeDAO
from database.annoDAO import AnnoDAO
from database.brandDAO import BrandDAO
from database.retailerDAO import RetailerDAO
from database.topVenditeDAO import TopVenditeDAO



class Model:
    def __init__(self):
        self.analizzaVenditeDAO = AnalizzaVenditeDAO()
        self.anno = AnnoDAO()
        self.brand = BrandDAO()
        self.retailer = RetailerDAO()
        self.topVendite = TopVenditeDAO()
        self.filtriTV = []


    def listaAnniMO(self):
        self.anno.popolaListaAnniDAO()
        return self.anno.listaAnniDAO

    def listaBrandMO(self):
        self.brand.popolaListaBrandDAO()
        return self.brand.listaBrandDAO

    def listaRetailerMO(self):
        self.retailer.popolaListaRetailerDAO()
        return self.retailer.listaRetailerDAO

    def listaTopVenditeMO(self):
        listaTopVenditeMO = self.topVendite.popolaListaTopVenditeDAO(self.filtriTV[0], self.filtriTV[1], self.filtriTV[2])
        return listaTopVenditeMO
    
    def listaAnalizzaVenditeMO(self):
        listaAnalizzaVenditeMO = self.analizzaVenditeDAO.popolaListaAnalizzaVenditeDAO(self.filtriTV[0], self.filtriTV[1], self.filtriTV[2])
        return listaAnalizzaVenditeMO


