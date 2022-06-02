### T2-2: Metodos ###
# Fecha: 24 / 03 / 2022
# Autor: Ing. Brian García Sarmina


#- CLASE "Avion" -#
class Avion:
    
    def __init__(self, nombre, tipo, num_motores, velocidad_crucero): # PRIMER METODO de clase.
        self.nombre = nombre 
        self.tipo = tipo 
        self.num_motores = num_motores
        self.velocidad_crucero = velocidad_crucero

    def potenciaReal(self, num_pasajeros): # METODO calculo de potencia.
        peso_pasajero = 80 # Peso supuesto por pasajero.
        arrastre = peso_pasajero * num_pasajeros # Peso total de pasajeros.
        por_arrastre = (arrastre / (5000*self.num_motores)) + 0.05 # Porcentaje de arrastre.
        return por_arrastre

    def velocidadReal(self, por_arrastre): # METODO calculo de velocidad crucero real.
        velocidad_real = self.velocidad_crucero * por_arrastre # Velocidad real crucero de avion.
        return velocidad_real


### MAIN ###
if __name__ == '__main__':

    avion1 = Avion("Boing 777", "Pasajeros", 2, 650)
    avion2 = Avion("Boing 797", "Pasajeros", 2, 525)

    num_pasajeros1 = 100 # Número de pasajeros para INSTANCIA "avion1".
    num_pasajeros2 = 125 # Número de pasajeros para INSTANCIA "avion2".
    
    por_arrastre1 = avion1.potenciaReal(num_pasajeros1) # Llamamos al primer METODO de la
                                                        # primera INSTANCIA (objeto) de la
                                                        # clase "Avion" llamado "avion1".
    por_arrastre2 = avion2.potenciaReal(num_pasajeros2)

    velocidad_real1 = avion1.velocidadReal(por_arrastre1) # Segundo METODO de la clase
                                                          # "Avion".
    velocidad_real2 = avion2.velocidadReal(por_arrastre2)

    print("La velocidad sin carga del avion1 ", avion1.nombre, " es de: ",
          avion1.velocidad_crucero)
    print("La velocidad con carga de ", num_pasajeros1, " pasajeros del avion1 ",
          avion1.nombre, " es de: ", velocidad_real1)
