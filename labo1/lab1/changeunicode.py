def unicode_8(texto):
    texto_unicode = ''
    for caracter in texto:
        texto_unicode += f'\\u{ord(caracter):04x}'
    return texto_unicode

# Leer el texto desde el archivo PRACTICA1_PRE.TXT
with open('practica1_pre.txt', 'r') as archivo:
    texto_preprocesado = archivo.read()

# Convertir el texto a Unicode-8
texto_unicode_8 = unicode_8(texto_preprocesado)

# Guardar el texto convertido en un nuevo archivo
with open('practica1_pre_UNICODE8.txt', 'w') as archivo_salida:
    archivo_salida.write(texto_unicode_8)

print("\nTexto convertido a Unicode-8 guardado en PRACTICA1_PRE_UNICODE8.TXT")
