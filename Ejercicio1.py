estudiantes = [
    ("Ana", 85, 90, 78, 92),
    ("Luis", 88, 76, 95),
    ("Carlos", 100, 98),
    ("María", 70, 80, 75, 85, 90)
]

resultados = {}  

for estudiante in estudiantes:
    
    nombre, *calificaciones = estudiante

    promedio = sum(calificaciones) / len(calificaciones)

    maximo = max(calificaciones)
    minimo = min(calificaciones)

    resultados[nombre] = {
        "promedio": promedio,   
        "max": maximo,
        "min": minimo
    }

print("Diccionario final:")
print(resultados)

mejor_estudiante = max(resultados, key=lambda x: resultados[x]["promedio"])

print("\nEstudiante con el promedio más alto:")
print(mejor_estudiante, "con promedio de", resultados[mejor_estudiante]["promedio"])
