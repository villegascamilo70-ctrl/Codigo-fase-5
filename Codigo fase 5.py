#funcion para calcular las horas trabajadas por cada recurso
def calcular_horas(equipo, limite=40):
    lista_resultados = []
    for recurso in equipo:
        nombre = recurso [0]
        horas_semana = recurso [1:]
        suma_horas = sum(horas_semana)
        if suma_horas > limite:
            estado = "sobretiempo"
        else:
            estado = "horario estandar"
        lista_resultados.append((nombre,suma_horas, estado))
    return lista_resultados
# funcion para mostrar el reporte
def mostrar_reporte(datos):
    print("reporte semanal de horas")
    print("------------")
    for nombre, total, estado in datos:
        print("recurso:", nombre)
        print("horas trabajadas:", total)
        print("estado de jornada:", estado)
        print("----------")
# Programa principal
equipo_trabajo = [
    ["Ana", 8, 9, 8, 8, 7],
    ["Carlos", 10, 9, 9, 8, 7],
    ["Beatriz", 8, 8, 8, 8, 8],
    ["Diego", 9, 10, 9, 8, 8],
]
resultado_final = calcular_horas(equipo_trabajo)
mostrar_reporte(resultado_final)