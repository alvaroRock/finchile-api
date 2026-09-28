from decimal import Decimal

from fastapi import APIRouter, Query

from app.services import mindicador

router = APIRouter(prefix="/convertir", tags=["Conversion"])

async def _a_clp(codigo: str) -> Decimal:
    if codigo == "clp":
      return Decimal(1)
    return await mindicador.valor_actual(codigo)

@router.get("")
async def convertir(
    monto: Decimal = Query(gt=0),
    desde: str = "uf",
    hasta: str = "clp",
):
    desde, hasta = desde.lower(), hasta.lower()
    en_clp = monto * await _a_clp(desde)
    resultado = en_clp / await _a_clp(hasta)
    return {
    "monto": monto,
    "desde": desde,
    "hasta": hasta,
    "resultado": round(resultado, 2),
    }