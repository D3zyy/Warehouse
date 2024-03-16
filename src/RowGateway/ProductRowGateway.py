from src.RowGateway.RowGateway_polymorphism.RowGateway  import RowGateway 

class ProductRowGateway(RowGateway):
    def __init__(self,database_connector):
        super().__init__(database_connector)
        self.name = None
        self.price = None
        self.qunatity = None
        self.category_id = None


    def create(self):
        print("create")
    def edit(self):
        print("edit")
    def delete(self):
        print("delete")


