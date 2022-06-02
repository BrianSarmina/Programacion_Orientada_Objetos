### T1-2: Clase e Instancia ###
# Fecha: 22 / 03 / 2022
# Autor: Ing. Brian García Sarmina


#- Como definir una CLASE -#
class Avion:

    # ATRIBUTO DE CLASE (constante)
    aerodinamica = "Avion de ala fija" # Para atributos con valor inicial.
    
    #- Las propiedades de los OBJETOS "Avion" -#
    def __init__(self, nombre, tipo, num_motores): 
        # Esta función se encarga de inicializar cada NUEVA INSTANCIA.
        # "self" se encarga de ESCRIBIR los ATRIBUTOS en el NUEVO OBJETO.
        self.nombre = nombre # Crea un atributo llamado "self.nombre" y
                             # le asigna el valor de "nombre".
        self.tipo = tipo 
        self.num_motores = num_motores # Todos los atributos de "self."
                                       # son ATRIBUTOS DE INSTANCIA (van cambiando).


### MAIN ###
if __name__ == '__main__':

    # Generar INSTANCIAS (objetos).
    avion1 = Avion("Boing 777", "Pasajeros", 2) # "avion1" (objeto) es la INSTANCIA de la clase.
    avion2 = Avion("Boing 797", "Carga", 4) # "avion2" (objeto) es un segunda INSTANCIA.
    print("\n")
    print("Objeto 1 de clase Avion: ", avion1) # Nos imprime el objeto creado y
                                               # su dirección de memoria.
    print("Objeto 2 de clase Avion: ", avion2)
    print("\n")
    
    
