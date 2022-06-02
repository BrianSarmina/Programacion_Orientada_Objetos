### T1-1: Definir una "clase" ###
# Fecha: 22 / 03 / 2022
# Autor: Ing. Brian García Sarmina


#- Como definir una CLASE -#
class Avion:
    #----------- CUERPO DE LA CLASE -----------#
    # Se utiliza la palabra reservada "class".
    # Por convención se utilizan LetrasMayúsculas para declarar el nombre
    # de la clase: "Avion", "Animal", "AnimalFelino", "TrenBala", etc.

    # ATRIBUTO DE CLASE (constante)
    aerodinamica = "Avion de ala fija" # Para atributos con valor inicial.
    
    #- Las propiedades de los OBJETOS "AVION" -#
    def __init__(self, nombre, tipo, num_motores): # Declara el estado inicial del objeto "Avion".
        # Esta función se encarga de inicializar cada NUEVA INSTANCIA.
        # "self" se encarga de ESCRIBIR los ATRIBUTOS en el NUEVO OBJETO.
        self.nombre = nombre # Crea un atributo llamado "self.nombre" y le asigna el valor de "nombre".
        self.tipo = tipo # Crea un atributo llamado "self.tipo" y le asigna el valor de "tipo".
        self.num_motores = num_motores # Crea un atributo llamado "self.num_motores".
        # Todos los atributos de "self." son ATRIBUTOS DE INSTANCIA (van cambiando).

    pass # Comando para ejecutar "CLASE INCOMPLETA" sin errores. 
    #----------- CUERPO DE LA CLASE -----------#
