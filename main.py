from package.module_client import Client
from package.module_functions import save_new_client

lh = Client('Laura Carolina', 'Herrera Hernandez', '32', 'lc@gmail.com', 'Caracas', '140', 'Altavista', '64630', 'Monterrey', 'Nuevo Leon', 'Mexico')
save_new_client(lh)
