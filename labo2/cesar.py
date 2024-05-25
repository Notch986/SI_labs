import tkinter as tk
from tkinter import ttk

def cifrado_cesar_personalizado(texto, desplazamiento, alfabeto):
    resultado = ""
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


# def cifrado_total(textaso):

# # Ejemplo de uso
# #texto = "La perfección se logra no cuando no hay nada más que añadir, sino cuando no hay nada más que quitar"
# # textoup=texto.upper
# #desplazamiento = 3
#     alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
#     texto_cifrado = cifrado_cesar_personalizado(textaso,entrada_desplazamiento, alfabeto)
#     print("Texto cifrado:", texto_cifrado)
#     #print(len(alfabeto))
#     return texto_cifrado

# Top level window 
frame = tk.Tk() 
frame.title("Cifrado Cesar") 
frame.geometry('800x400') 
# Function for getting Input 
# from textbox and printing it  
# at label widget 

def printInput(): 
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    desplazamiento=3
    inp = inputtxt.get(1.0, "end-1c") 
    inp2 = cifrado_cesar_personalizado(inp.upper(),desplazamiento,alfabeto)
    lbl.config(text = "Provided Input: "+inp2) 



# TextBox Creation 
inputtxt = tk.Text(frame, 
                   height = 5, 
                   width = 20) 
  
inputtxt.pack() 

# Button Creation 
printButton = tk.Button(frame, 
                        text = "Cifrar",  
                        command = printInput) 
printButton.pack() 

# Label Creation 
lbl = tk.Label(frame, text = "") 
lbl.pack() 

# Ejecutar la aplicación
frame.mainloop()