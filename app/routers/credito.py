from fastapi import APIRouter

from app.schemas import SimulacionIn, SimulacionOut
from app.services import finanzas

router = APIRouter(prefix="/credito", tags=["Credito"])

@router.post("/simular", response_model=SimulacionOut)
def simular(datos: SimulacionIn):
    filas = finanzas.tabla_amortizacion(datos.monto, datos.tasa_anual, datos.meses)
    total = sum(f["cuota"] for f in filas)
    return SimulacionOut(
        cuota_mensual=filas[0]["cuota"],
        total_pagado=total,
        total_intereses=total - datos.monto,
        tabla=filas,
    )