import matplotlib.pyplot as plt
from collections import Counter

def vigenere_cipher(text, key):
    text = text.upper()
    key = key.upper()
    key_len = len(key)
    encrypted_text = []
    
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(key[i % key_len]) - ord('A')
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)
    
    return ''.join(encrypted_text)

def letter_frequencies(text):
    text = text.upper()
    frequencies = Counter(char for char in text if char.isalpha())
    return frequencies

def plot_frequencies(frequencies, title, ax):
    labels, values = zip(*sorted(frequencies.items()))
    ax.bar(labels, values)
    ax.set_title(title)

# Mensaje original y claves
message = "La perfección se logra no cuando no hay nada más que añadir, sino cuando no hay nada más que quitar"
keys = ["MEZCLADOR", "MALEFICIO", "HUMOR", "MAR"]

# Cifrar el mensaje con la clave "MEZCLADOR"
encrypted_message = vigenere_cipher(message, keys[0])
print(f"Encrypted Message with 'MEZCLADOR': {encrypted_message}")

# Calcular las frecuencias del mensaje original
original_frequencies = letter_frequencies(message)
print(f"Original Frequencies: {original_frequencies}")

# Calcular las frecuencias de cada letra usando las claves "MALEFICIO", "HUMOR" y "MAR"
frequencies = {}

for key in keys[1:]:
    encrypted_text = vigenere_cipher(message, key)
    frequencies[key] = letter_frequencies(encrypted_text)
    print(f"Encrypted Message with '{key}': {encrypted_text}")

# Crear subplots para las frecuencias
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Graficar las frecuencias
plot_frequencies(original_frequencies, "Original Frequencies", axes[0, 0])

for i, key in enumerate(keys[1:], start=1):
    plot_frequencies(frequencies[key], f"Frequencies with key '{key}'", axes[i // 2, i % 2])

plt.tight_layout()
plt.show()

# Comentarios sobre la variación de las frecuencias
print("\nComentarios sobre la variación de las frecuencias:")
print("1. Frecuencias Originales: Las frecuencias de las letras en el texto original reflejan la distribución típica del idioma español.")
print("2. Frecuencias con Clave 'MALEFICIO' (8 caracteres): Esta clave más larga introduce una mayor variabilidad en la distribución de frecuencias de las letras cifradas, reduciendo patrones evidentes.")
print("3. Frecuencias con Clave 'HUMOR' (5 caracteres): Una clave intermedia que proporciona un balance entre variabilidad y repetición.")
print("4. Frecuencias con Clave 'MAR' (3 caracteres): Esta clave más corta puede resultar en patrones más repetitivos, haciendo el cifrado menos seguro frente al análisis de frecuencias.")
print("Comparando las frecuencias, se observa que las claves más largas tienden a distribuir las frecuencias de las letras de manera más uniforme en el texto cifrado, dificultando el análisis de frecuencias. Las claves más cortas, por otro lado, muestran más regularidad y patrones repetitivos, lo que puede facilitar el criptoanálisis.")
