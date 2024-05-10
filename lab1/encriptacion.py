def eliminar_caracteres(texto):
    caracteres_eliminar = '.,;:!¡¿?"()-[]{}<>_'
    for caracter in caracteres_eliminar:
        texto = texto.replace(caracter, '')
    texto = texto.replace(' ', '')  # Eliminar espacios en blanco
    return texto

def eliminar_tildes(texto):
    tildes = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'}
    for tilde, sin_tilde in tildes.items():
        texto = texto.replace(tilde, sin_tilde)
    return texto

def sustituir_texto(texto):
    texto = texto.replace('a', 'u').replace('A', 'U')
    texto = texto.replace('h', 't').replace('H', 'T')
    texto = texto.replace('ñ', 'e').replace('Ñ', 'E')
    texto = texto.replace('k', 'l').replace('K', 'L')
    texto = texto.replace('v', 'f').replace('V', 'F')
    texto = texto.replace('w', 'b').replace('W', 'B')
    texto = texto.replace('z', 'y').replace('Z', 'Y')
    texto = texto.replace('r', 'p').replace('R', 'P')
    return texto

# Leer el texto desde el archivo texto.txt
with open('silvia.txt', 'r') as archivo:
    texto_original = archivo.read()

# Eliminar tildes
texto_sin_tildes = eliminar_tildes(texto_original)

# Eliminar caracteres especiales y espacios en blanco
texto_limpio = eliminar_caracteres(texto_sin_tildes)

# Realizar las sustituciones en el texto limpio
texto_modificado = sustituir_texto(texto_limpio)

# Convertir todas las letras a mayúsculas
texto_modificado = texto_modificado.upper()

# Guardar el texto modificado en un archivo llamado PRACTICA1_PRE.TXT
with open('practica1_pre.txt', 'w') as archivo_salida:
    archivo_salida.write(texto_modificado)

print("Archivo practica1_pre.txt generado con éxito.")
