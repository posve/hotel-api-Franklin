from pydantic import BaseModel


class UsuariosIn(BaseModel):
    email: str
    nombres: str
    apellidos: str
    telefono: int
    tipoDocumento: str
    numeroDocumento: int
    pais: str
    ciudad: str
    direccion: str
    clave: str 

class UsuariosOut(BaseModel):
    email: str
    nombres: str
    apellidos: str
    telefono: int
    tipoDocumento: str
    numeroDocumento: int
    pais: str
    ciudad: str
    direccion: str
    clave: str