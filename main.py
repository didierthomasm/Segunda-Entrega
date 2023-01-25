from package.module_client import Client
from package.module_functions import save_new_client


cm = Client('Carlo', 'Mendoza', '25', 'cm@gm.cm', 'Principal', '25', 'Colorin', '98741', 'Bogota', 'Puebla', 'Rusia')
vd = Client('Victoria', 'Davaloz', '17', 'vd@hm.mx', 'Juarez', '789-A', 'Margain', '74123', 'San Diego', 'California', 'Republica Checa', '102')
cg = Client('Casimiro', 'Gomez', '45', 'casi@gt.io', 'Su calle', '77', 'Su colonia', '78951', 'Cordoba', 'Mandinga', 'Su pais')

# save_new_client(cm)
print(vd.legal_age())
print(vd.purchase('Laptop Dell'))
print(vd)

# save_new_client(vd)
print(vd.legal_age())
print(vd.purchase('Chicharron de la Ramos'))
print(vd)

# save_new_client(cg)
print(cg.legal_age())
print(cg.purchase('Nescafe'))
print(cg)