# Mini-Turtle (Versión Funcional – Modularidad)

Este proyecto es una simulación simple del movimiento de una "tortuga" dibujando figuras simples usando texto en la terminal.  
Forma parte de la práctica sobre **modularidad** y diseño de una interfaz limpia en Python.

El objetivo es separar correctamente:
- La **lógica interna** del dibujo  
- La **interfaz pública** que utiliza el usuario  

## Estructura del Paquete

<img width="819" height="247" alt="image" src="https://github.com/user-attachments/assets/9b811998-9160-4064-a042-d70980808a2d" />


## 🔧 Funcionalidades

- `adelante(n)`: Dibuja un movimiento horizontal hacia la derecha con `-` y `>`.
- `abajo(n)`: Dibuja un movimiento vertical hacia abajo respetando la posición acumulada.
- `reiniciar()`: Restablece la posición horizontal a cero.

Los usuarios pueden importar estas funciones así:

```python
from mini_turtle import adelante, abajo, reiniciar
