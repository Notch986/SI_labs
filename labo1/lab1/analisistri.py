def obtener_trigramas(texto):
    trigramas = {}
    for i in range(len(texto)-2):
        trigrama = texto[i:i+3]
        if trigrama in trigramas:
            trigramas[trigrama].append(i)
        else:
            trigramas[trigrama] = [i]
    return trigramas

def obtener_distancias(trigramas):
    distancias = {}
    for trigrama, posiciones in trigramas.items():
        if len(posiciones) > 1:
            distancias[trigrama] = [posiciones[i+1] - posiciones[i] for i in range(len(posiciones)-1)]
    return distancias

archivo_generado = 'practica1_pre.txt'
with open(archivo_generado, 'r') as file:
    texto_preprocesado = file.read().upper()

trigramas = obtener_trigramas(texto_preprocesado)
distancias_trigramas = obtener_distancias(trigramas)

print("\nTrigramas encontrados:")
print(trigramas)
print("\nDistancias entre trigramas iguales:")
print(distancias_trigramas)
