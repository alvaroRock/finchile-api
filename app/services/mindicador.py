import time
from decimal import Decimal

import httpx
from fastapi import HTTPException

BASE_URL = "https://mindicador.cl/api"
TTL_SEGUNDOS = 3600
CODIGOS = {"uf", "dolar", "euro", "utm", "ipc", "tpm"}

_cache: dict[str, tuple[float, dict]] = {}

async def obtener_indicador(codigo: str) -> dict:
    codigo = codigo.lower()
    if codigo not in CODIGOS:
        raise HTTPException(404, f"Indicador '{codigo}' no soportado")
    ahora = time.time()
    if codigo in _cache and ahora - _cache[codigo][0] < TTL_SEGUNDOS:
        return _cache[codigo][1]
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            resp = await client.get(f"{BASE_URL}/{codigo}")
            resp.raise_for_status()
    except httpx.HTTPError:
        raise HTTPException(502, "No se pudo consultar la fuente de datos")

    data = resp.json()
    _cache[codigo] = (ahora, data)
    return data

async def valor_actual(codigo: str) -> Decimal:
    data = await obtener_indicador(codigo)
    return Decimal(str(data["serie"][0]["valor"]))