# Implementar una funcion llamada calcular_recaudacion_socios, que reciba movimientos, socios_club, cuota_normal y devuelva
#el monto total recaudado. La lista movimientos es una lista de listas donde cada elemento tiene la forma:
#[numero_socio, actividad], por ej: [[101,"pileta"],[205,"tenis"],[101,"gimnasio"],[300,"pileta"]].La lista fue creada
# en orden cronologico. La lista socios_club contiene unicamente los numeros de socio habilitados para recibir
# beneficios. Restricciones: si el numero de socio no pertenece a socios_club, no se cobra nada. Cada actividad realizada
# por un socio habilitado cuesta cuota_normal. Las primeras 5 actividades realizadas por socios habilitados se cobran a precio
# completo. A partir de la sexta actividad de socios habilitados inclusive se aplica un descuento del 20%.
#Si ningun socio habilitado realizo actividades, la funcion debe devolver 0.

def calcular_recaudacion_socios(movimientos, socios_club, cuota_normal):
    total_recaudado = 0
    cantidad_actividades = 0
    
    for socio, actividad in movimientos:
        if socio in socios_club:
            cantidad_actividades += 1
            
            precio_actividad = cuota_normal
            
            if cantidad_actividades >= 6:
                precio_actividad = precio_actividad * 0.8
            
            total_recaudado += precio_actividad
    return total_recaudado