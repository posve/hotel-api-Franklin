from datetime import date, datetime
from typing import Dict
from pydantic import BaseModel

class ReservaInDB(BaseModel):
    idReserva: int = 1
    fechaReserva: datetime = datetime.now()
    fechaLlegada: date
    fechaSalida: date
    habitacion: str
    numeroPersonas: int
    nombres: str
    apellidos: str
    email: str
    telefono: int
    tipoDocumento: str
    numeroDocumento: int
    pais: str
    ciudad: str
    direccion: str

database_reservas = Dict[int, ReservaInDB]
database_reservas = {
    1 : ReservaInDB(**{"idReserva":1,
    "fechaReserva":'2020-12-09 21:30:48.620822',
    "fechaLlegada": '2020-12-10',
    "fechaSalida": '2020-12-12',
    "habitacion": "Suit de lujo",
    "numeroPersonas": 2,
    "nombres": "Juan",
    "apellidos": "Rulfo Vizcaíno",
    "email": "juanrulfo@gmail.com",
    "telefono": 3104632378,
    "tipoDocumento": "CC",
    "numeroDocumento": 10227923,
    "pais": "México",
    "ciudad": "San Gabriel",
    "direccion": "Calle 52 #28-20"
    }),

    2 : ReservaInDB(**{"idReserva":2,
    "fechaReserva":'2020-12-09 22:30:48.620822',
    "fechaLlegada": '2020-12-11',
    "fechaSalida": '2020-12-13',
    "habitacion": "Suit de lujo",
    "numeroPersonas": 4,
    "nombres": "Gabriel",
    "apellidos": "García Márquez",
    "email": "gabopremionobel@gmail.com",
    "telefono": 3002025632,
    "tipoDocumento": "CC",
    "numeroDocumento": 9845690,
    "pais": "Colombia",
    "ciudad": "Aracataca",
    "direccion": "Calle 1 #2-20"
    })
}
generator = {"id":1} #Auto-Incremental

def save_reserva(reserva_in_db: ReservaInDB):
    generator["id"] = generator["id"] + 1
    reserva_in_db.idReserva = generator["id"]
    database_reservas[generator["id"]] =  reserva_in_db
    return reserva_in_db

def get_reserva(idReserva: int):
    if idReserva in database_reservas.keys():
        return database_reservas[idReserva]
    else:
        return None