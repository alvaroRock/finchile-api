from fastapi import APIRouter

from app.services import rut_utils

router = APIRouter(prefix="/rut", tags=["RUT"])

@router.get("/validar/{rut}")
def validar(rut: str):
    return {"rut": rut, "valido": rut_utils.validar_rut(rut)}