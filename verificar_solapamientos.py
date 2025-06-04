import json
from datetime import datetime, time

def parse_hora(hora_str):
    # Convierte string "HH:MM:SS" a objeto time
    return datetime.strptime(hora_str, "%H:%M:%S").time()

def hay_solapamiento(horarios, inicio_nuevo, fin_nuevo):
    if inicio_nuevo == fin_nuevo == time(0,0,0):
        # bloque vacío, no hay solapamiento posible
        return False
    for inicio, fin in horarios:
        if not (fin_nuevo <= inicio or inicio_nuevo >= fin):
            return True
    return False

def verificar_solapamientos(data):
    horarios_profesor = {}
    horarios_curso = {}
    errores = []

    for asignacion in data:
        profesor_id = asignacion['profesor']
        curso_id = asignacion['curso']
        dia = asignacion['dia']  # Nuevo

        bloques = [
            (asignacion['bloque_1_inicio'], asignacion['bloque_1_fin']),
            (asignacion['bloque_2_inicio'], asignacion['bloque_2_fin']),
        ]

        for inicio_str, fin_str in bloques:
            inicio = parse_hora(inicio_str)
            fin = parse_hora(fin_str)

            if inicio == fin == time(0,0,0):
                continue  # bloque vacío, omitir

            clave_profesor = (profesor_id, dia)  # Se agrega día
            clave_curso = (curso_id, dia)        # Se agrega día

            if clave_profesor not in horarios_profesor:
                horarios_profesor[clave_profesor] = []
            if clave_curso not in horarios_curso:
                horarios_curso[clave_curso] = []

            if hay_solapamiento(horarios_profesor[clave_profesor], inicio, fin):
                errores.append(f"Solapamiento para profesor {profesor_id} en {dia} {inicio}-{fin}")
            else:
                horarios_profesor[clave_profesor].append((inicio, fin))

            if hay_solapamiento(horarios_curso[clave_curso], inicio, fin):
                errores.append(f"Solapamiento para curso {curso_id} en {dia} {inicio}-{fin}")
            else:
                horarios_curso[clave_curso].append((inicio, fin))

    return errores


# Cargar JSON desde archivo (o pegar el JSON directamente en la variable 'data')
# con open('asignaciones.json') as f:
#    data = json.load(f)

# Ejemplo con variable (puedes reemplazar por lectura archivo)
data = [
    {
        "id": 876,
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 171,
        "materia": 611,
        "profesor": 522
    },
    {
        "id": 877,
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 171,
        "materia": 612,
        "profesor": 522
    },
    {
        "id": 878,
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 171,
        "materia": 613,
        "profesor": 522
    }
]

errores = verificar_solapamientos(data)
if errores:
    print("Se encontraron solapamientos:")
    for error in errores:
        print(" -", error)
else:
    print("No se encontraron solapamientos.")
