### T3-2: Transmisión de Funcionalidad ###
# Fecha: 30 / 03 / 2022
# Autor: Ing. Brian García Sarmina


#- CLASE PADRE -#
class Animales:

    tipos_animales = "Animales varios"

    # CONSTRUCTOR de clase padre, que genera
    # asignación para atributos de instancia.
    def __init__(self, nombre, familia, alimento, ambiente = 'Desconocido'):
        self.nombre = nombre
        self.familia = familia
        self.alimento = alimento
        self.ambiente = ambiente

    # Metodo de clase "Padre".
    def enemigosNaturales(self, animal1, animal2):
        if animal1 != animal2:
            print("El animal ", animal1.nombre, " y el animal ",
                  animal2.nombre, " son enemigos naturales.")
        else:
            print("El animal ", animal1.nombre, " y el animal ",
                  animal2.nombre, " son animales compatibles.")


#- CLASE HIJO 1 -#
class Savana(Animales):

    # Expansión de "Atributo de Clase (Hijo)".
    tipos_animales_savana = "Leones, Hienas, Cebras, Elefantes"

    # Sobreescibir constructor "__init__" para clase hijo.
    def __init__(self, nombre, familia, alimento, ambiente = 'Savana'):
        self.nombre = nombre
        self.familia = familia
        self.alimento = alimento
        self.ambiente = ambiente # Atributo de instancia, sobreescrito.
    
    def viven_en(self): # Metodo de clase hijo.
        viven = "Su ambiente natural en exterior"
        return viven

#- CLASE HIJO 2 -#
class Domesticos(Animales):

    # Sobreescibir constructor.
    def __init__(self, nombre, familia, alimento, ambiente = 'Urbano'):
        self.nombre = nombre
        self.familia = familia
        self.alimento = alimento
        self.ambiente = ambiente # Atributo de instancia, sobreescrito.

    def viven_en(self): # Metodo de clase hijo.
        viven = "Su ambiente natural en la casa"
        return viven


### MAIN ###
if __name__ == '__main__':
    
    leon = Animales('Leon', 'Felinos', 'Carne')
    cebra = Animales('Cebra', 'Equinos', 'Plantas')
    print("Clase PADRE")
    leon.enemigosNaturales(leon, cebra)
    print("\n")
    perro = Domesticos('Perro', 'Caninos', 'Procesado')
    hiena = Savana('Hiena', 'Felinos', 'Carne')
    print("Clase HIJO")
    perro.enemigosNaturales(perro, hiena)

    # Además, de los métodos del padre, los hijos pueden
    # contener sus propios metodos, con lo que logran EXPANDIR
    # su funcionalidad.
    viven = perro.viven_en()
    viven2 = hiena.viven_en()
    print("\n")
    print("EXPANDIR FUNCIONALIDAD")
    print("El ", perro.nombre, " tiene: ", viven)
    print("El ", hiena.nombre, " tiene: ", viven2)

    # Atributos de clase para hijo "Savana".
    print("\n")
    print("ATRIBUTOS CLASE PADRE, CLASE HIJO")
    print("Los tipos de animales para clase padre ANIMALES son: ", hiena.tipos_animales)
    print("Los tipos de animales para clase SAVANA son: ", hiena.tipos_animales_savana)

    # Los hijos al igual que los padres, son capaces de SOBRESCRIBIR
    # los atributos de clase.
    print("\n")
    print("SOBREESCIBIR")
    # Atributo de clase original (padre).
    print("El ", perro.nombre, " se consideran como: ", perro.tipos_animales)
    # Atributo de clase modificado (hijo).
    perro.tipos_animales = "Animales domesticos"
    print("El ", perro.nombre, " se consideran como: ", perro.tipos_animales)
    # Atributo de instancia "ambiente" original (padre).
    print("En un inicio los animales se consideran de ambiente: ", leon.ambiente)
    # Atributo de instancia "ambiente" modificado (hijo), se modifica el
    # CONSTRUCTOR de la clase hijo.
    print("La ", hiena.nombre, " se vive en: ", hiena.ambiente)
    print("El ", perro.nombre, " se vive en: ", perro.ambiente)
    
