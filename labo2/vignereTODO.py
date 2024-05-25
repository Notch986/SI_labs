import tkinter as tk
from tkinter import ttk, filedialog

def cifrado_vigenere(texto, clave, alfabeto):
    resultado = ""
    alfabeto = alfabeto.lower()
    texto = texto.lower()
    clave = clave.lower()
    longitud_alfabeto = len(alfabeto)
    longitud_clave = len(clave)
    
    indice_alfabeto = {caracter: indice for indice, caracter in enumerate(alfabeto)}
    
    for i, char in enumerate(texto):
        if char in indice_alfabeto:
            indice_texto = indice_alfabeto[char]
            indice_clave = indice_alfabeto[clave[i % longitud_clave]]
            nuevo_indice = (indice_texto + indice_clave) % longitud_alfabeto
            resultado += alfabeto[nuevo_indice]
        else:
            resultado += char
    
    return resultado

def descifrado_vigenere(texto, clave, alfabeto):
    resultado = ""
    alfabeto = alfabeto.lower()
    texto = texto.lower()
    clave = clave.lower()
    longitud_alfabeto = len(alfabeto)
    longitud_clave = len(clave)
    
    indice_alfabeto = {caracter: indice for indice, caracter in enumerate(alfabeto)}
    
    for i, char in enumerate(texto):
        if char in indice_alfabeto:
            indice_texto = indice_alfabeto[char]
            indice_clave = indice_alfabeto[clave[i % longitud_clave]]
            nuevo_indice = (indice_texto - indice_clave) % longitud_alfabeto
            resultado += alfabeto[nuevo_indice]
        else:
            resultado += char
    
    return resultado

def cargar_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if archivo:
        with open(archivo, "r", encoding="utf-8") as file:
            entrada_texto.delete(1.0, tk.END)
            entrada_texto.insert(tk.END, file.read())

def cifrar_texto():
    texto = entrada_texto.get(1.0, tk.END).strip()
    clave = entrada_clave.get().strip()
    modulo = opcion_modulo.get()
    
    if modulo == "27":
        alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    elif modulo == "191":
        alfabeto = "".join([chr(i) for i in range(32, 223)])  # ASCII del 32 al 222
    
    clave_extendida = (clave * ((len(texto) // len(clave)) + 1))[:len(texto)]
    texto_cifrado = cifrado_vigenere(texto, clave_extendida, alfabeto)
    resultado_var.set(texto_cifrado)

def descifrar_texto():
    texto = entrada_texto.get(1.0, tk.END).strip()
    clave = entrada_clave.get().strip()
    modulo = opcion_modulo.get()
    
    if modulo == "27":
        alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    elif modulo == "191":
        alfabeto = "".join([chr(i) for i in range(32, 223)])  # ASCII del 32 al 222
    
    clave_extendida = (clave * ((len(texto) // len(clave)) + 1))[:len(texto)]
    texto_descifrado = descifrado_vigenere(texto, clave_extendida, alfabeto)
    resultado_var.set(texto_descifrado)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cifrado y Descifrado Vigenère con Módulo Seleccionable")

# Crear y colocar los widgets en la ventana
ttk.Label(ventana, text="Texto:").grid(row=0, column=0, padx=10, pady=10)
entrada_texto = tk.Text(ventana, width=60, height=10)
entrada_texto.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(ventana, text="Clave:").grid(row=1, column=0, padx=10, pady=10)
entrada_clave = ttk.Entry(ventana, width=50)
entrada_clave.grid(row=1, column=1, padx=10, pady=10)

ttk.Label(ventana, text="Módulo:").grid(row=2, column=0, padx=10, pady=10)
opcion_modulo = tk.StringVar(value="27")
modulo_27 = ttk.Radiobutton(ventana, text="Alfabeto 27 caracteres", variable=opcion_modulo, value="27")
modulo_191 = ttk.Radiobutton(ventana, text="ASCII 191 caracteres", variable=opcion_modulo, value="191")
modulo_27.grid(row=2, column=1, padx=10, pady=5, sticky="w")
modulo_191.grid(row=3, column=1, padx=10, pady=5, sticky="w")

boton_cargar_archivo = ttk.Button(ventana, text="Cargar archivo de texto", command=cargar_archivo)
boton_cargar_archivo.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

boton_cifrar = ttk.Button(ventana, text="Cifrar", command=cifrar_texto)
boton_cifrar.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

boton_descifrar = ttk.Button(ventana, text="Descifrar", command=descifrar_texto)
boton_descifrar.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

ttk.Label(ventana, text="Resultado:").grid(row=7, column=0, padx=10, pady=10)
resultado_var = tk.StringVar()
etiqueta_resultado = ttk.Label(ventana, textvariable=resultado_var, wraplength=400)
etiqueta_resultado.grid(row=7, column=1, padx=10, pady=10)

# Ejecutar la aplicación
ventana.mainloop()
