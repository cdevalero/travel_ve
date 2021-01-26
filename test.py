from datetime import datetime
from datetime import date

def calcular_edad_agnios(fecha_nacimiento):
    fecha_nacimiento = datetime.strptime(fecha_nacimiento,'%Y-%m-%d')
    fecha_actual = date.today()
    resultado = fecha_actual.year - fecha_nacimiento.year
    resultado -= ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return resultado


fecha_nacimiento_turing = '1998-06-14'

edad = calcular_edad_agnios(fecha_nacimiento_turing)

print(edad)