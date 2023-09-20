import numpy as np


votos = np.random.randint(1, 31, 5000)  


votos_unicos, conteo_votos = np.unique(votos, return_counts=True)


resultados = [(candidato, votos) for candidato, votos in zip(votos_unicos, conteo_votos)]


resultados.sort(key=lambda x: x[1], reverse=True)

print("Resultado de la elección del representante:")
for candidato, votos in resultados:
    print(f"Candidato {candidato}: {votos} votos")


estudiantes = np.array([
    [1, 'Juan', 4.5, 1985],
    [2, 'Ana', 3.8, 1992],
    [3, 'Carlos', 4.0, 1988],
    
])


codigo_carrera_a_listar = input("Ingrese el código de la carrera a listar: ")
promedio_minimo = 4.0

carrera_seleccionada = estudiantes[estudiantes[:, 0] == codigo_carrera_a_listar]
estudiantes_aprobados = carrera_seleccionada[carrera_seleccionada[:, 2] >= promedio_minimo]

print(f"Estudiantes de la carrera {codigo_carrera_a_listar} con promedio >= {promedio_minimo}:")
for estudiante in estudiantes_aprobados:
    print(f"Código: {int(estudiante[0])}, Nombre: {estudiante[1]}")

print(f"Total de estudiantes aprobados: {len(estudiantes_aprobados)}")


estudiantes_condicionales = estudiantes[(estudiantes[:, 3] < 1990) & (estudiantes[:, 2] < 3.0)]

print("Estudiantes que ingresaron antes de 1990 y están condicionales:")
for estudiante in estudiantes_condicionales:
    print(f"Código: {int(estudiante[0])}, Nombre: {estudiante[1]}")