# FinChile API

API REST en Python (FastAPI) con herramientas financieras para Chile: indicadores
(UF, dólar, UTM, IPC), conversor de monedas, simulador de crédito con tabla de
amortización (sistema francés) y validador de RUT.

## Ejecutar

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Documentación interactiva en http://127.0.0.1:8000/docs

## Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | /health | Estado del servicio |
| GET | /indicadores/{codigo} | Último valor (uf, dolar, euro, utm, ipc, tpm) |
| GET | /convertir?monto=2&desde=uf&hasta=clp | Conversión entre monedas |
| POST | /credito/simular | Cuota y tabla de amortización |
| GET | /rut/validar/{rut} | Valida un RUT chileno |

## Tests y Docker

```bash
pytest
docker build -t finchile-api . && docker run -p 8000:8000 finchile-api
```

Fuente de datos: mindicador.cl (con cache de 1 hora).
