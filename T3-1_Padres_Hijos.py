### T3-1: Padres e Hijos ###
# Fecha: 25 / 03 / 2022
# Autor: Ing. Brian García Sarmina


#- CLASE PADRE -#
class Animales:

    def __init__(self, nombre, familia, alimento):
        self.nombre = nombre
        self.familia = familia
        self.alimento = alimento

    def enemigosNaturales(self, animal1, animal2):
        if animal1 != animal2:
            print("Son enemigos naturales")
        else:
            print("Son animales compatibles")

#- CLASE HIJO 1 -#
class Savana(Animales):
    pass

#- CLASE HIJO 2 -#
class Domesticos(Animales):
    pass


### MAIN ###
if __name__ == '__main__':

    leon = Animales('Leon', 'Felinos', 'Carne') # Instancias de clase Animales.
    cebra = Animales('Cebra', 'Equinos', 'Plantas')
    # Llamar al método de la clase Animales.
    print("Clase PADRE")
    leon.enemigosNaturales(leon.alimento, cebra.alimento)
    print("\n")
    # Generar "hijos".
    perro = Domesticos('Perro', 'Caninos', 'Procesado')
    hiena = Savana('Hiena', 'Felinos', 'Carne')
    # Llamar al método de clase padre.
    print("Clase HIJO")
    perro.enemigosNaturales(perro.alimento, hiena.alimento)
    
