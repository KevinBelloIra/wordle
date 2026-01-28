# wordle
# este juego costo 1 millon de dolares 
Claro, aquí tienes un ejemplo de **README.md** para tu proyecto de Wordle en Python. Está estructurado como se suele hacer en repositorios de GitHub:

---

# Wordle en Python 🎮

## 📖 Descripción
Este proyecto es una versión sencilla del famoso juego **Wordle**, implementada en Python para jugar directamente en la terminal.  
El objetivo es adivinar una palabra secreta de 5 letras en un máximo de 6 intentos.

## 🚀 Características
- Selección aleatoria de palabras desde una lista predefinida.  
- Comparación letra por letra:  
  - ✅ Letra correcta en posición correcta → se muestra en **mayúscula**.  
  - 🔄 Letra correcta en posición incorrecta → se muestra en minúscula.  
  - ❌ Letra incorrecta → se muestra como `-`.  
- Número limitado de intentos (6 por defecto).  
- Mensajes de victoria o derrota al finalizar la partida.  

## 🛠️ Requisitos
- Python 3.x instalado en tu sistema.  
- No requiere librerías externas (solo `random`).  

## ▶️ Cómo jugar
1. Clona este repositorio o descarga el archivo `.py`.  
2. Ejecuta el programa en la terminal:  

```bash
python wordle.py
```

3. Ingresa tus intentos de palabras de 5 letras.  
4. Observa el resultado y ajusta tu siguiente intento.  

## 📌 Ejemplo de salida
```
¡Bienvenido a Wordle en Python!
Adivina la palabra de 5 letras. Tienes 6 intentos.
Intento 1: perro
Resultado: P---o
Intento 2: carta
Resultado: CAr--
🎉 ¡Correcto! La palabra era: carta
```

## 💡 Mejoras futuras
- Colorear las letras en la terminal (usando `colorama`).  
- Ampliar el diccionario de palabras.  
- Crear una interfaz gráfica con `tkinter` o `pygame`.  
- Guardar estadísticas de partidas ganadas/perdidas.  

---

¿Quieres que te lo prepare en formato **Markdown real con encabezados y listas** listo para pegar en tu repositorio, o prefieres que lo adapte a un estilo más **documentación técnica** con secciones como *Instalación*, *Uso* y *Contribución*?