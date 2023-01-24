import json
import os

folder_data = os.path.join(os.path.abspath('.'), 'data')
clients_db = 'clients_db'


# Carga la base de datos
def load_db(db_file: str = 'clients_db'):
    if db_file and not db_file == '':
        users_db = db_file
    else:
        users_db = 'clients_db'

    users = dict()
    path_to_json = os.path.join(folder_data, users_db + '.json')

    if os.path.exists(path_to_json):
        users = json.load(open(path_to_json, 'r'))
        
    else:
        print('La base de datos no existe.')
        answer = input(f'¿Desear crear la base de datos {users_db} si/no?')
        if answer.lower() == 'si':
            json.dump({}, open(path_to_json, 'w'))
            users = json.load(open(path_to_json, 'r'))
    return users


# Crea un número de usuario
def user_id(db_file: str = 'clients_db'):
    user = load_db(db_file)
    if not user:
        return 1
    else:
        return int(list(user.keys())[-1]) + 1


# Guarda el cliente nuevo en la basae de datos
def save_new_client(new_client, db_file: str = 'clients_db'):
    cliente = new_client.make_client()
    no_id = new_client._client_number
    new_client = {no_id: cliente}

    path_to_json = os.path.join(folder_data, db_file + '.json')

    if new_client:
        json.dump(new_client, open(path_to_json, 'w'), indent=4)
        print('Usuario guardado')
        print('')
    else:
        print('No había que guardar')

# Regresa la edad