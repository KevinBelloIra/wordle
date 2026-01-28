import random

# Lista de palabras posibles (puedes ampliarla)
palabras = ["perro", "gatos", "nubes", "verde", "carta", "pluma", "salud"]

# Selecciona una palabra al azar
palabra_secreta = random.choice(palabras)
intentos = 6  # número máximo de intentos

print("¡Bienvenido a Wordle en Python!")
print("Adivina la palabra de 5 letras. Tienes", intentos, "intentos.")

for intento in range(intentos):
    guess = input(f"Intento {intento+1}: ").lower()

    if len(guess) != len(palabra_secreta):
        print("La palabra debe tener", len(palabra_secreta), "letras.")
        continue

    # Compara letra por letra
    resultado = ""
    for i in range(len(palabra_secreta)):
        if guess[i] == palabra_secreta[i]:
            resultado += guess[i].upper()  # letra correcta en posición correcta
        elif guess[i] in palabra_secreta:
            resultado += guess[i]  # letra existe pero en otra posición
        else:
            resultado += "-"  # letra incorrecta

    print("Resultado:", resultado)

    if guess == palabra_secreta:
        print("🎉 ¡Correcto! La palabra era:", palabra_secreta)
        break
else:
    print("😢 Se acabaron los intentos. La palabra era:", palabra_secreta)
