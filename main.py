from db.reservas_db import ReservaInDB
from db.reservas_db import save_reserva, get_reserva

from db.usuarios_db import UsuariosInDB
from db.usuarios_db import get_usuarios, update_usuarios 

from models.reservas_models import ReservaOut, ReservaIn
from models.usuarios_models import UsuariosIn, UsuariosOut 

from datetime import datetime, date
from fastapi import FastAPI, HTTPException
api = FastAPI()

# SECCIÓN RESERVAS # 

@api.get("/reserva/{idReserva}")
async def view_reserva(idReserva: int):
    reserva_in_db = get_reserva(idReserva)
    if reserva_in_db == None:
        raise HTTPException(status_code=404,
                            detail = "La reserva no existe")
    reserva_out = ReservaOut(**reserva_in_db.dict())
    return reserva_out

@api.post("/reserva/reservar/")
async def make_reserva(reserva_in: ReservaIn):
    new_reserva = save_reserva(reserva_in)
    return new_reserva

  #SECCIÓN USUARIOS #
  
@api.get("/usuarios/{email}")
async def view_usuarios(email: str):
    usuarios_in_db = get_usuarios(email)
    if usuarios_in_db == None:
        raise HTTPException(status_code=404,
                            detail = "Usuario no existe")
    usuarios_out = UsuariosOut(**usuarios_in_db.dict())
    return usuarios_out

@api.post("/usuarios/auth/")
async def auth_user(usuarios_in: UsuariosIn):

    usuarios_in_db = get_usuarios(usuarios_in.email)

    if usuarios_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    if usuarios_in_db.clave != usuarios_in.clave:
        return  {"Autenticado": False}

    return  {"Autenticado": True}