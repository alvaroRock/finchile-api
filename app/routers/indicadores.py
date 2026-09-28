from fastapi import APIRouter

from app.services import mindicador

router = APIRouter(prefix="/indicadores", tags=["Indicadores"])

@router.get("/{codigo}")
async def obtener(codigo: str):
    data = await mindicador.obtener_indicador(codigo)
    ultimo = data["serie"][0]
    return {
        "codigo": data["codigo"],
        "nombre": data["nombre"],
        "unidad": data["unidad_medida"],
        "fecha": ultimo["fecha"],
        "valor": ultimo["valor"],
    }