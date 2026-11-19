# cuentas.csv = 1001,Lucas,50000; 1002,Ana,82000; 1003,Pedro,30000; 1004,Sofia,100000
# Formato = nro_cuenta, titular, saldo
# movimientos.csv = 1001,5000; 1001,2000; 1003,1500; 1004,10000; 1004,5000; 1004,2000
# Formato = nro_cuenta, monto_retirado
# Se pide generas cuentas_actualizadas.csv restando todos los movimientos al saldo
# Ademas informar cuenta con mayor cantidad de dinero retirado.
# ej: titulas: sofia, retirado: 17000

def leer_cuentas(cuentas):
    linea = cuentas.readline()
    if linea:
        nro_cuenta, titular, saldo = linea.strip().split(",")
        nro_cuenta = int(nro_cuenta)
        saldo = int(saldo)
    else:
        nro_cuenta = titular = saldo = None
    return nro_cuenta, titular, saldo

def leer_movimientos(movimientos):
    linea = movimientos.readline()
    if linea:
        nro_cuenta, monto_retirado = linea.strip().split(",")
        nro_cuenta = int(nro_cuenta)
        monto_retirado = int(monto_retirado)
    else:
        nro_cuenta = monto_retirado = None
    return nro_cuenta, monto_retirado

def procesar_archivos(cuentas, movimientos, cuentas_actualizadas):
    nro_cuenta_c, titular, saldo = leer_cuentas(cuentas)
    nro_cuenta_m, monto_retirado = leer_movimientos(movimientos)
    mayor_dinero_retirado = 0
    titular_max = []
    while nro_cuenta_c != None:
        if nro_cuenta_c == nro_cuenta_m:
            titular_actual = titular
            total_retirado = 0
            while nro_cuenta_m is not None and nro_cuenta_m == nro_cuenta_c:
                total_retirado += monto_retirado
                nro_cuenta_m, monto_retirado = leer_movimientos(movimientos)
            saldo -= total_retirado
            if total_retirado > mayor_dinero_retirado:
                mayor_dinero_retirado = total_retirado
                titular_max = [titular_actual]
            elif total_retirado == mayor_dinero_retirado:
                titular_max.append(titular_actual)
        cuentas_actualizadas.write(str(nro_cuenta_c)+","+titular+","+str(saldo)+"\n")
        nro_cuenta_c, titular, saldo = leer_cuentas(cuentas)
    print("Cuenta con mayor dinero retirado:")
    for titul in titular_max:
        print(f"Titular: {titul}")
    print(f"Retirado: {mayor_dinero_retirado}")

def main():
    cuentas = open("ejercicios-campus/2do-parcial/practica/csv-ejercicos/ejercicio-11-cuentas.csv")
    movimientos = open("ejercicios-campus/2do-parcial/practica/csv-ejercicos/ejercicio-11-movimientos.csv")
    cuentas_actualizadas = open("ejercicios-campus/2do-parcial/practica/csv-ejercicos/ejercicio-11-cuentas_actualizadas.csv", "w")
    procesar_archivos(cuentas, movimientos, cuentas_actualizadas)
    cuentas.close()
    movimientos.close()
    cuentas_actualizadas.close()

main()