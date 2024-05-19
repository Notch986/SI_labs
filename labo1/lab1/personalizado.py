def cambiar_alfabeto(texto, alfabeto_orig, alfabeto_dest):
    tabla_cambio = str.maketrans(alfabeto_orig, alfabeto_dest)
    return texto.translate(tabla_cambio)

# Definir el alfabeto personalizado (por ejemplo, un desplazamiento de 1)
alfabeto_original = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfabeto_personalizado = 'XZKLMNOPQRTUVWYBCDEFGHIJAS'  # Desplazado en una posición

# Leer el texto desde el archivo PRACTICA1_PRE_UNICODE8.TXT
with open('PRACTICA1_PRE_UNICODE8.TXT', 'r') as archivo:
    texto_unicode_8 = archivo.read()

# Convertir el texto con el alfabeto personalizado
texto_alfabeto_personalizado = cambiar_alfabeto(texto_unicode_8, alfabeto_original, alfabeto_personalizado)

# Guardar el texto convertido en un nuevo archivo
with open('PRACTICA1_PRE_ALFABETO.TXT', 'w') as archivo_salida:
    archivo_salida.write(texto_alfabeto_personalizado)

print("\nTexto con alfabeto personalizado guardado en PRACTICA1_PRE_ALFABETO.TXT")