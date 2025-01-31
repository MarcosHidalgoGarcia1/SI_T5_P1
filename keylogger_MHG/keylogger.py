import keyboard

def imprimir_tecla(tecla): 
    print(tecla.name) #imprime lo escrito
    
    with open('texto escrito.txt', 'a') as file: # crea el .txt en modo de anexado
        if tecla.name == 'space':
            file.write(' ') # si presionas la tecla espacio se genere un espacio
        else:
            file.write(tecla.name) # si no presionas la tecla espacio pues genera la tecla que has generado

keyboard.on_press(imprimir_tecla) # cuando presiones cualquiera tecla se ejecuta en este cado la funcion imprimir_tecla

keyboard.wait() # espera hasta que se presione una tecla