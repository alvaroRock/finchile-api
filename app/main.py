from fastapi import FastAPI
from app.routers import convertir, credito, indicadores, rut

app = FastAPI(
    title="FinChile API",
    version="1.0.0",
    description="API financiera chilena: indicadores, conversion, credito y RUT.",
)

app.include_router(indicadores.router)
app.include_router(convertir.router)
app.include_router(credito.router)
app.include_router(rut.router)

@app.get("/health", tags=["Sistema"])
def health():
    return {"status": "ok"}