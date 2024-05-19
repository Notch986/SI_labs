def insertar_cadena(texto, cadena, intervalo):
    resultado = ''
    for i in range(0, len(texto), intervalo):
        resultado += texto[i:i+intervalo] + cadena
    return resultado

def ajustar_multiplo_7(texto):
    longitud_necesaria = (len(texto) + 6) // 7 * 7
    return texto.ljust(longitud_necesaria, 'Z')

# Leer el texto desde el archivo PRACTICA1_PRE.TXT
with open('PRACTICA1_PRE_ALFABETO.TXT', 'r') as archivo:
    texto_preprocesado = archivo.read().upper()

# Insertar "EPIS" cada 15 caracteres
texto_con_epis = insertar_cadena(texto_preprocesado, 'EPIS', 15)

# Ajustar la longitud del texto para que sea múltiplo de 7
texto_ajustado = ajustar_multiplo_7(texto_con_epis)

# Guardar el texto resultante en un nuevo archivo
with open('PRACTICA1_PRE_EPIS.TXT', 'w') as archivo_salida:
    archivo_salida.write(texto_ajustado)

print("\nTexto con inserción de 'EPIS' y ajuste a múltiplo de 7 guardado en PRACTICA1_PRE_EPIS.TXT")
