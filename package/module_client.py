from module_functions import *

class Client():
    def __init__(self, fname, lname, age, email, address) -> None:
        # def get_address(self) :
            # address = {'calle': str, 'numero exterior': int, 'numero interior': '', 'colonia': str, 'ciudad': str, 'estado': str, 'pais': str}
            # address['calle'] = input('Nombre de la calle: ')
            # address['numero exterior'] = int(input('Numero exterior: '))
            # address['numero interior'] = int(input('Numero exterior: '))
            # address['colonia']
            # return address
        self._fname = fname
        self._lname = lname
        self._age = age
        self._email = email
        self._address = address
        self._client_number = client_number()

    def __str__(self) -> str:
        return f'El nombre del clientes es {self._fname} {self._lname}.'

    def legal_age(self) -> str:
        if self._age >= 18:
            return f'El cliente puede comprar cualquier artículo.'
        else:
            return f'Necesitas la autorización de un adulto.'

    def purchase(self, item):
        return f'El artículo {item} será enviado a {self._address}, para mayor información revise su correp {self._email}.'





