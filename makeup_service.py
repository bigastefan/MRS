from service import Service


class MakeupService(Service):
    def __init__(self, name, price):
        self.data = []
        self.name = name
        self.price = price
        return super().__init__()

    def buyService(self):
        super().buyService()
        print("Makeup treatmant bought !")

    def addService(self, service):
        super().addService()
        self.createService(service)

    def deleteService(self):
        super().deleteService()
        print("Makeup had been successfully deleted !")

    def createService(self, service):
        name = input("Insert service name: ")
        price = input("Insert service price: ")
        service = MakeupService(name, price)
        self.data.append(service)
        print("Makeup have been added to the sistem !")
        print(self.data[-1].name, self.data[-1].price)



