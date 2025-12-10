# drawer_logic.py
posicion_x = 0  # estado global del módulo

def adelante(pasos): #  función para mover hacia adelante
    global posicion_x
    print(" " * posicion_x + "-" * pasos + ">") # Dibuja la línea hacia adelante con la flecha
    posicion_x += pasos # Actualiza la posición horizontal

def abajo(pasos):  # función para mover hacia abajo
    global posicion_x
    for _ in range(pasos): 
        print(" " * posicion_x + "|") # Dibuja la línea vertical hacia abajo
    print(" " * posicion_x + "v")  # Dibuja la flecha hacia abajo

    
def reiniciar():   # función para reiniciar la posición
    global posicion_x
    posicion_x = 0 # Reinicia la posición a cero