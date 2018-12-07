from nail_service import NailService


class Salon:
    def __init__(self, name, username, password):
        self.allServices = []
        self.name = name
        self.__username = username
        self.__password = password

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    # def salonLogin(self):
    #     pass
    #
    # def changeService(self):
    #     pass

    def addService(self):
        name = input("Insert service name: ")
        price = input("Insert service price: ")
        service = NailService(name, price)
        self.allServices.append(service)
        print(service.name, " has been successfully added !")
        return service

    def deleteService(self):
        name = input("Insert service Name you want to delete: ")
        for i in self.allServices:
            if i.name == name:
                self.allServices.remove(i)
                print(i.name,  " has been successfully deleted !")
        return True

    def sellService(self):
        name = input("Insert service Name you want to sell: ")
        counter = 0
        for i in self.allServices:
            if i.name != name:
                counter += 1
                if counter == len(self.allServices):
                    print("There is no service, try again")
                    self.sellService()
            else:
                print("Your bill is: ", i.price)
                return True
