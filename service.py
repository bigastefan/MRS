from abc import ABC, abstractmethod

# Abstract class Service, has only methods
class Service(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def addService(self):
        pass

    @abstractmethod
    def buyService(self):
        pass

    @abstractmethod
    def deleteService(self):
        pass

    


