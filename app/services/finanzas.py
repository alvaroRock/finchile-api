from decimal import Decimal, ROUND_HALF_UP

def redondear(x: Decimal) -> Decimal:
    """CLP no tiene decimales: se redondea al peso."""
    return x.quantize(Decimal("1"), rounding=ROUND_HALF_UP)

def tabla_amortizacion(monto: int, tasa_anual: Decimal, meses: int) -> list[dict]:
    """Sistema frances: cuota fija. Tasa nominal anual dividida en 12."""
    i = tasa_anual / Decimal(1200)
    saldo = Decimal(monto)

    if i == 0:
        cuota = saldo / meses
    else:
        factor = (1 + i) ** meses
        cuota = saldo * i * factor / (factor - 1)
        cuota = redondear(cuota)

        filas = []
        for n in range(1, meses + 1):
            interes = redondear(saldo * i)
            capital = saldo if n == meses else cuota - interes # ajusta la ultima
            pago = capital + interes
            saldo -= capital
            filas.append({
                "numero": n,
                "cuota": int(pago),
                "interes": int(interes),
                "capital": int(capital),
                "saldo": int(saldo),
            })
    return filas