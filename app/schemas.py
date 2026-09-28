from decimal import Decimal

from pydantic import BaseModel, Field

class SimulacionIn(BaseModel):
    monto: int = Field(gt=0, description="Monto del credito en CLP")
    tasa_anual: Decimal = Field(ge=0, le=100, description="Tasa anual nominal en %")
    meses: int = Field(gt=0, le=480, description="Plazo en meses")

class Cuota(BaseModel):
    numero: int
    cuota: int
    interes: int
    capital: int
    saldo: int

class SimulacionOut(BaseModel):
    cuota_mensual: int
    total_pagado: int
    total_intereses: int
    tabla: list[Cuota]