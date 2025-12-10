# drawer_logic.py
posicion_x = 0  

def adelante(pasos): 
    global posicion_x
    print(" " * posicion_x + "-" * pasos + ">")
    posicion_x += pasos