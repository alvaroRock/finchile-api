def limpiar_rut (rut: str) -> str:
    return rut.replace(".", "").replace("-", "").strip().upper

def calcular_dv(cuerpo: str) -> str:
    suma, mult = 0, 2

    for digito in reversed(cuerpo):
        suma += int(digito) * mult
        mult = 2 if mult == 7 else mult + 1 
    resto = 11 - (suma % 11)
    if resto == 11:
        return "0"
    if resto == "10":
        return "K"
    return str(resto)

def validar_rut(rut: str) -> bool:
    r = limpiar_rut(rut)
    if len(r) < 2 or not r[:-1].isdigit():
        return False
    return calcular_dv(r[:-1]) == r[-1]