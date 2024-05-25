import tkinter as tk
from tkinter import ttk

def cifrado_cesar_personalizado(texto, desplazamiento, alfabeto):
    resultado = ""
    alfabeto = alfabeto.lower()  # Convertir el alfabeto a minúsculas
    texto = texto.lower()  # Convertir el texto a minúsculas
    longitud_alfabeto = len(alfabeto)
    
    # Crear un diccionario para acceder rápidamente al índice de cada carácter
    indice_alfabeto = {caracter: indice for indice, caracter in enumerate(alfabeto)}
    
    # Iterar sobre cada carácter en el texto
    for char in texto:
        if char in indice_alfabeto:
            # Obtener el índice del carácter en el alfabeto
            indice_actual = indice_alfabeto[char]
            # Calcular el nuevo índice con el desplazamiento
            nuevo_indice = (indice_actual + desplazamiento) % longitud_alfabeto
            # Agregar el carácter cifrado al resultado
            resultado += alfabeto[nuevo_indice]
        else:
            # Si el carácter no está en el alfabeto, dejarlo como está
            resultado += char

    return resultado

def descifrado_fuerza_bruta(texto_cifrado, alfabeto):
    longitud_alfabeto = len(alfabeto)
    posibles_resultados = []
    
    for desplazamiento in range(longitud_alfabeto):
        # Usar un desplazamiento negativo para descifrar
        texto_descifrado = cifrado_cesar_personalizado(texto_cifrado, -desplazamiento, alfabeto)
        posibles_resultados.append(f"Desplazamiento {desplazamiento}: {texto_descifrado}")
    
    return posibles_resultados

def mostrar_descifrados():
    texto_cifrado = entrada_texto.get()
    alfabeto = entrada_alfabeto.get()
    resultados = descifrado_fuerza_bruta(texto_cifrado, alfabeto)
    resultado_var.set("\n".join(resultados))

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Descifrado César por Fuerza Bruta")

# Crear y colocar los widgets en la ventana
ttk.Label(ventana, text="Texto cifrado:").grid(row=0, column=0, padx=10, pady=10)
entrada_texto = ttk.Entry(ventana, width=50)
entrada_texto.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(ventana, text="Alfabeto:").grid(row=1, column=0, padx=10, pady=10)
entrada_alfabeto = ttk.Entry(ventana, width=50)
entrada_alfabeto.grid(row=1, column=1, padx=10, pady=10)

boton_descifrar = ttk.Button(ventana, text="Descifrar", command=mostrar_descifrados)
boton_descifrar.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

ttk.Label(ventana, text="Posibles descifrados:").grid(row=3, column=0, padx=10, pady=10)
resultado_var = tk.StringVar()
etiqueta_resultado = ttk.Label(ventana, textvariable=resultado_var, wraplength=400)
etiqueta_resultado.grid(row=3, column=1, padx=10, pady=10)

# Ejecutar la aplicación
ventana.mainloop()
