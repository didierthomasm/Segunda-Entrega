from package.module_client import *


#Didier = Client('Didier', 'Thomas', 33, 'didierthomas.m@gmail.com', {'calle': 'Juan Zuazua', 'numero exterior': 524, 'numero interior': 5, 'colonia': 'Centro', 'código postal': 64000, 'ciudad': 'Monterrey', 'estado': 'Nuevo León', 'país': 'México'})

#direccion = Didier._address
#print(Didier._address)
#print(Didier._address['colonia'])
#print(Didier._client_number)

Lingo = Client('Lingo', 'Dingo', 25, 'lingodingo@mail.io', '1° street #10, Python, 41789, USA')

print(Lingo._client_number)
print(Lingo.legal_age())
print(Lingo._address)