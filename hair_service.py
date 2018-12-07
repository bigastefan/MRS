from service import Service


class HairService(Service):
    def __init__(self, name, price):
        self.data = []
        self.name = name
        self.price = price
        return super().__init__()

    def buyService(self):
        super().buyService()
        print("Hair treatmant bought !")

    def addService(self, service):
        super().addService()
        self.createService(service)

    def deleteService(self):
        super().deleteService()
        print("Hair service had been successfully deleted !")

    def createService(self, service):
        name = input("Insert service name: ")
        price = input("Insert service price: ")
        service = HairService(name, price)
        self.data.append(service)
        print("Hair service have been added to the sistem !")
        print(self.data[-1].name, self.data[-1].price)
