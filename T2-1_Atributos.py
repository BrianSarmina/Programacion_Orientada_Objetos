### T2-1: Atributos ###
# Fecha: 24 / 03 / 2022
# Autor: Ing. Brian García Sarmina


#- CLASE "Avion" -#
class Avion:

    # ATRIBUTO DE CLASE (constante)
    aerodinamica = "Avion de ala fija" # Para atributos con valor inicial.
    
    #- Las propiedades de los OBJETOS "Avion" -#
    def __init__(self, nombre, tipo, num_motores): 
        # Todos los atributos de "self." son ATRIBUTOS DE INSTANCIA (pueden cambiar de
        # instancia en instancia).
        self.nombre = nombre 
        self.tipo = tipo 
        self.num_motores = num_motores 

### MAIN ###
if __name__ == '__main__':

    avion1 = Avion("Boing 777", "Pasajeros", 2) # Recibe ATRIBUTOS DE INSTANCIA:
                                                # nombre, tipo, num_motores.
    avion2 = Avion("Boing 797", "Carga", 4)
    print("\n")
    print("Objeto 1 de clase Avion: ", avion1) 
    print("Objeto 2 de clase Avion: ", avion2)
    print("\n")
    
    # Aqui ocupamos la notación ".", lo que permite en este caso es solicitar
    # los atributos de clase o de instancia (avion1 o avion2) para los objetos
    # generados de la clase Avion. 
    print("Atributo de clase Avion: ", avion1.aerodinamica) # Atributo de clase.
    print("Atributo de instancia 1: ", avion1.nombre) # Atributo de instacia ".nombre".
    print("Atributo de instancia 2: ", avion1.tipo) # Atributo de instancia ".tipo".
    print("Atributo de instancia 3: ", avion1.num_motores) # Atributo de instancia ".num_motores".
    print("\n")
    
    # Los atributos de clase o de instancia (objetos) son MUTABLES por default, es decir,
    # que son MODIFICABLES similares a las listas y diccionarios.
    avion2.aerodinamica = "Ala movil" # Modificamos atributo de clase para "avion2".
    avion1.num_motores = 6 # Modificamos el atributo de instancia "num_motores".
    print("Atributo de clase avion1: ", avion1.aerodinamica) # Atributo de clase (avion1).
    print("Nuevo atributo de clase avion2: ", avion2.aerodinamica) # Atributo de clase (avion2).
    print("Nuevo atributo de instancia 3: ", avion1.num_motores) # Atributo modificado.
