def frecuencias(archivo):
    with open(archivo, 'r') as file:
        texto = file.read().upper()  # Leer el texto y convertir a mayúsculas
        tabla_frecuencias = {}

        # Calcular frecuencias para cada letra de la 'A' a la 'Z'
        for letra in range(ord('A'), ord('Z')+1):
            letra = chr(letra)
            frecuencia = texto.count(letra)
            tabla_frecuencias[letra] = frecuencia

        return tabla_frecuencias

archivo_generado = 'practica1_pre.txt'
frecuencias_letras = frecuencias(archivo_generado)
print("Tabla de frecuencias de letras:")
print(frecuencias_letras)

# Obtener los cinco caracteres de mayor frecuencia
cinco_mas_frecuentes = sorted(frecuencias_letras.items(), key=lambda x: x[1], reverse=True)[:5]
print("\nCinco caracteres más frecuentes:")
print(cinco_mas_frecuentes)
