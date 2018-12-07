from service import Service
from nail_service import NailService
from salon import Salon


s = Salon("Salon 1", "username", "password")
s.addService()
s.addService()
s.deleteService()
s.sellService()