from decimal import Decimal

from fastapi.testclient import TestClient

from app.main import app
from app.services import mindicador
from app.services.finanzas import tabla_amortizacion

client = TestClient(app)


def test_health():
    assert client.get("/health").json() == {"status": "ok"}


def test_rut_valido():
    assert client.get("/rut/validar/12.345.678-5").json()["valido"] is True


def test_rut_invalido():
    assert client.get("/rut/validar/12.345.678-9").json()["valido"] is False


def test_amortizacion_cierra_en_cero():
    filas = tabla_amortizacion(1_000_000, Decimal("12"), 12)
    assert len(filas) == 12
    assert filas[-1]["saldo"] == 0


def test_simular_credito():
    r = client.post(
        "/credito/simular",
        json={"monto": 1000000, "tasa_anual": 12, "meses": 12},
    )
    assert r.status_code == 200
    body = r.json()
    assert body["total_intereses"] > 0
    assert len(body["tabla"]) == 12


def test_simular_credito_datos_invalidos():
    r = client.post(
        "/credito/simular",
        json={"monto": -5, "tasa_anual": 12, "meses": 12},
    )
    assert r.status_code == 422


def test_convertir_uf_a_clp(monkeypatch):
    async def falso(codigo):
        return Decimal("39000")

    monkeypatch.setattr(mindicador, "valor_actual", falso)
    r = client.get("/convertir", params={"monto": 2, "desde": "uf", "hasta": "clp"})
    assert r.status_code == 200
    assert float(r.json()["resultado"]) == 78000.0
