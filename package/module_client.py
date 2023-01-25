from package.module_functions import user_id


class Address:
    def __init__(self, calle, nexterior, colonia, cpostal, ciudad, estado, pais, ninterior=None) -> None:
        self.calle = calle
        self.nexterior = nexterior
        self.ninterior = ninterior
        self.colonia = colonia
        self.cpostal = cpostal
        self.ciudad = ciudad
        self.estado = estado
        self.pais = pais

    def __str__(self):
        return f'Calle {self.calle} #{self.nexterior}, #int{self.ninterior}, colonia {self.colonia}, estado {self.estado}, pais {self.pais}'

    def make_address(self) -> dict:
        address = {
            'calle': self.calle,
            'numero exterior': self.nexterior,
            'numero interior': self.ninterior,
            'colonia': self.colonia,
            'codigo postal': self.cpostal,
            'ciudad': self.ciudad,
            'estado': self.estado,
            'pais': self.pais
        }
        return address


class Client:
    def __init__(self, fname, lname, age, email, calle, nexterior, colonia, cpostal, ciudad, estado, pais,
                 ninterior=None) -> None:
        self._fname = fname
        self._lname = lname
        self._age = age
        self._email = email
        self._address = Address(calle, nexterior, colonia, cpostal, ciudad, estado, pais, ninterior)
        self._client_number = str(user_id())

    def __str__(self) -> str:
        return f'El nombre del clientes es {self._fname} {self._lname}.'

    def make_client(self) -> dict:
        name = {
            'nombre': self._fname,
            'apellido': self._lname,
            'edad': self._age,
            'e-mail': self._email,
            'direccion': self._address.make_address()
        }
        return name

    def legal_age(self) -> str:
        if int(self._age) >= 18:
            return f'El cliente puede comprar cualquier artículo.'
        else:
            return f'Necesitas la autorización de un adulto.'

    def purchase(self, item):
        return f'El artículo {item} será enviado a {self._address}, para mayor información revise su correo {self._email}.'
