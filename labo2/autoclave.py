def autoclave_cifrado(texto, clave, alfabeto):
    resultado = ""
    alfabeto = alfabeto.lower()
    texto = texto.lower()
    clave = clave.lower()
    longitud_alfabeto = len(alfabeto)
    longitud_texto = len(texto)
    
    for i, char in enumerate(texto):
        if char in alfabeto:
            indice_texto = alfabeto.index(char)
            indice_clave = alfabeto.index(clave[i % longitud_texto])
            nuevo_indice = (indice_texto + indice_clave) % longitud_alfabeto
            resultado += alfabeto[nuevo_indice]
        else:
            resultado += char
    
    return resultado

def autoclave_descifrado(texto, clave, alfabeto):
    resultado = ""
    alfabeto = alfabeto.lower()
    texto = texto.lower()
    clave = clave.lower()
    longitud_alfabeto = len(alfabeto)
    longitud_texto = len(texto)
    
    for i, char in enumerate(texto):
        if char in alfabeto:
            indice_texto = alfabeto.index(char)
            indice_clave = alfabeto.index(clave[i % longitud_texto])
            nuevo_indice = (indice_texto - indice_clave) % longitud_alfabeto
            resultado += alfabeto[nuevo_indice]
        else:
            resultado += char
    
    return resultado

# Ejemplo de uso
texto_original = "QUISIERAESTATARDEDIVINADEOCTUBREPASEARPORLAORILLALEJANADELMARQUELAARENADEOROYLASAGUASVERDESYLOSCIELOSPUROSMEVIERANPASAR"
clave = "UNODELOSMASGRANDESCRIPTOGRAFOS"
alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

#texto_cifrado = autoclave_cifrado(texto_original, clave, alfabeto)
texto_cifrado2="XHGDQESDMPKÑDEEDKNGJZPFJSUIFZOLFCINFJCESVZTGBFXCIUDAYNUUDIZYWWZBEYNVQWIVUNKZEPHDODQUZZLBDNDRWTHQSERÑIVMLERCMGIFLSORZXTSDIGLOXQSDJHWVCIWQXQJCKMBPOKMPSKMUVIMNJDNBLCSZHXHNYYUIXDBSOXHZLXWVGDJGXHWLTDWKÑSAQIMZLNBVMLXHUOQQXIQGWGUFTWKZKMOKUDNINSIFJDUOZIJBSVVOWFAIEÑGYOWPSOAP"
texto_descifrado = autoclave_descifrado(texto_cifrado2, clave, alfabeto)

#print("Texto Original:", texto_original)
#print("Texto Cifrado:", texto_cifrado)
print("Texto Descifrado:", texto_descifrado)
