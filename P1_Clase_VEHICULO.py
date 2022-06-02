### P1 CLASE VEHICULO ###
# Fecha: 31 / 03 / 2022
# Autor: M.C.C. Brian García Sarmina


#- Importar paqueterías -#
import numpy as np
import random as r
import matplotlib.pyplot as plt

#- Clase VEHICULO -#
class Vehiculo:

    # Definimos constructor.
    def __init__(self, nombre, gasolina, tamaño_tanque, rendimiento=18):
        self.nombre = nombre # Nombre del vehiculo.
        self.gasolina = gasolina # Tipo de combustible que usa.
        self.tamaño_tanque = tamaño_tanque # Tamaño de litros del tanque.
        self.rendimiento = rendimiento # Rendimiento de km por litro.

    # Método "sensores".
    def sensores(self):
        print("---------------------------------------------------------------------")
        print("Los sensores de este vehiculo son: ")
        print(" -sensor gasolina (código 001)")
        print(" -sensor temperatura (código 002)")
        print(" -sensor de puertas (código 003)")
        print(" -sensor ABS (código 004)")
        print(" -sensor de nivel de aceite (código 005)")
        print("---------------------------------------------------------------------")
        print("\n")

    # Método "diag_sensores"
    # simula la falla de uno o varios sensores del sistema.
    def diag_sensores(self):
        # Se genera un cierto número de sensores posibles
        # en falla.
        num_sens_en_falla = r.randrange(0,5)
        sensores_en_falla = []
        for i in range(num_sens_en_falla):
            while True: # Ciclo WHILE INFINITO para elegir numero de sensor, sin repetir.
                # Se elige de forma aleatoria un codigo de falla.
                sensor = r.choice(['001','002', '003', '004','005'])
                if sensor not in sensores_en_falla: # Si "sensor" no esta en la lista.
                    break # Se rompe el WHILE INFINITO (nos llevamos el código elegido
                          # que no se encuentra presente en la lista.
                else:
                    continue # Se continua el WHILE INFINITO.
            # Se agrega el código de falla a la lista de "sensores_en_falla".
            sensores_en_falla.append(sensor)
        if sensores_en_falla == []: # Si no hay sensores en falla.
            print("No hay sensores en falla")
        else: # Se imprimen los sensores en falla.
            print("Los sensores en falla son: ", sensores_en_falla)
            print("\n")
        return sensores_en_falla # Regresamos la lista de "sensores_en_falla".
    
    # Método "reparar_sensores":
    def reparar_sensores(self, sensores_en_falla):
        # Iteramos sobre cada codigo de "sensor" con falla.
        print("---------------------------------------------------------------------")
        print("El vehículo ", self.nombre, " presenta estas fallas: ")
        print("\n")
        for sensor in sensores_en_falla:
            if sensor == '001':
                print("---CÓDIGO 001---")
                print("Pasos para solución: ")
                print(" 1. Verificar nivel de gasolina.")
                print(" 2. Reemplazar sensor AT2209GAS.")
                print(" 3. Oprima boton RESET por 3 segundos, para reiniciar CPU.")
                print("\n")
            elif sensor == '002':
                print("---CÓDIGO 002---")
                print("Pasos para solución: ")
                print(" 1. Apagar vehiculo y esperar que baje temperatura.")
                print(" 2. Reemplazar sensor HG1009TEM.")
                print(" 3. Oprima boton RESET por 3 segundos, para reiniciar CPU.")
                print("\n")
            elif sensor == '003':
                print("---CÓDIGO 003---")
                print("Pasos para solución: ")
                print(" 1. Apagar vehiculo.")
                print(" 2. Reemplazar sensor JL3798PUE.")
                print(" 3. Oprima boton RESET por 3 segundos, para reiniciar CPU.")
                print("\n")
            elif sensor == '004':
                print("---CÓDIGO 004---")
                print("Pasos para solución: ")
                print(" 1. Llevar vehiculo para manteniemto a distruidor autorizado.")
                print("\n")
            elif sensor == '005':
                print("---CÓDIGO 005---")
                print("Pasos para solución: ")
                print(" 1. Llevar vehiculo para manteniemto a distruidor autorizado.")
                print("\n")
            else:
                print("CODIGO NO REGISTRADO")
        print("---------------------------------------------------------------------")
        
    # Método "graf_velocidad"
    def graf_velocidad(self):
        tiempos = []
        velocidades = []
        # Se calcula la "curva teorica" (aproximado) de velocidad.
        for i in range(1, 150, 5):
            t = i
            vel = np.log(t)
            tiempos.append(t/10)
            velocidades.append(vel*10)
        # Se toma el ultimo punto de la curva para simular la
        # velocidad máxima.
        max_vel = np.max(velocidades) + 0.01
        # Constante de velocidad máxima alcanzada.
        for j in range(150, 250, 5):
            t = j
            vel = max_vel
            tiempos.append(t/10)
            velocidades.append(vel)
        # Gráfica de velocidad.
        plt.plot(tiempos, velocidades)
        plt.scatter(tiempos, velocidades)
        plt.grid(linestyle='--')
        plt.title("Grafica de aceleración")
        plt.xlabel("Tiempo (seg)")
        plt.ylabel("Velocidad (km/h)")
        plt.show()


    # Metodo "tiempo_autonomia"
    def autonomia(self):
        # Se calcula la autonomia (en km) del vehiculo,
        # usando el tamaño del tanque (litros) y el
        # rendimiento (km/litro).
        if self.gasolina == 'Gasolina':
            autonomia = self.tamaño_tanque * self.rendimiento
        elif self.gasolina == 'Diesel':
            autonomia = self.tamaño_tanque * self.rendimiento
        else:
            autonomia = self.tamaño_tanque * self.rendimiento
        print("---------------------------------------------------------------------")
        print("La autonomia del vehiculo (en km) ", self.nombre, " es de: ",
              autonomia, "km")
        print("---------------------------------------------------------------------")
        print("\n")
        
    # Método "valvulas"
    def valvulas(self):
        # Se encarga de simular a traves de una gráfica
        # el rendimiento de cada válvula dependiendo el
        # tipo de gasolina usada.
        if self.gasolina == 'Gasolina':
            # Creamos un diccionario con los valores de
            # porcentaje de rendimiento para cada válvula,
            # para el caso de "Gasolina" se suponen 4 valvulas.
            valvulas = {'v1':90, 'v2':80, 'v3':80,
                    'v4':90}
            num_valvula = list(valvulas.keys()) # Identificadores.
            por_rendimiento = list(valvulas.values()) # Valores.
            # Creamos una "gráfica de barras").
            plt.bar(num_valvula, por_rendimiento, color ='maroon', width = 0.4) 
            plt.xlabel("Número de válvula")
            plt.ylabel("Porcentaje de rendimiento")
            plt.title("Rendimiento de válvulas")
            plt.show()
            
        elif self.gasolina == 'Diesel':
            # Se suponen 6 válvulas.
            valvulas = {'v1':85, 'v2':85, 'v3':85,
                        'v4':85, 'v5':85, 'v6':85}
            num_valvula = list(valvulas.keys()) # Identificadores.
            por_rendimiento = list(valvulas.values()) # Valores. 
            # Creamos una "gráfica de barras").
            plt.bar(num_valvula, por_rendimiento, color ='maroon', width = 0.4)
            plt.xlabel("Número de válvula")
            plt.ylabel("Porcentaje de rendimiento")
            plt.title("Rendimiento de válvulas")
            plt.show()
        else:
            # Se suponen 5 válvulas.
            valvulas = {'v1':95, 'v2':90, 'v3':90,
                        'v4':90, 'v5':95}
            num_valvula = list(valvulas.keys()) # Identificadores.
            por_rendimiento = list(valvulas.values()) # Valores. 
            # Creamos una "gráfica de barras").
            plt.bar(num_valvula, por_rendimiento, color ='maroon', width = 0.4)
            plt.xlabel("Número de válvula")
            plt.ylabel("Porcentaje de rendimiento")
            plt.title("Rendimiento de válvulas")
            plt.show()
        
### MAIN ###
if __name__ == '__main__':

    # Creamos unas instacias de la clase VEHICULO,
    # es decir, un objetos de la clase.
    solaris = Vehiculo('Solaris', 'Gasolina', 105)
    gran_spartan = Vehiculo('Gran Spartan', 'Diesel', 150, 14)
    varage = Vehiculo('Varage', 'Gas', 100, 17)

    print("---------------------------------------------------------------------")
    print("Programa de información y diagnostico de vehículos")
    print("La lista de funciones disponibles son: ")
    print(" - .sensores(): Imprime la lista de sensores y sus códigos de falla.")
    print(" - .diag_sensores(): Simula e imprime una secuencia de sensores posibles en falla.")
    print(" - .reparar_sensores(sensores en falla)**: Da las indicaciones para reparación de códigos de falla.")
    print(" - .graf_velocidad(): Imprime una gráfica de velocidad IMAGINARIA del vehículo.")
    print(" - .autonomia(): Calcula la autonomía del vehículo en kilometros.")
    print(" - .valvulas(): Imprime una gráfica del porcentaje de rendimiento de las válvulas del vehículo.")
    print(" - SALIR: Salir del programa.")
    print("Los vehiculos disponibles son: Solaris, Gran Spartan y Varage.")
    print("---------------------------------------------------------------------")
    print("\n")
    
    while True: # Se crea el menu con un WHILE INFINITO.
        funcion = input("¿Qué función desea ejectuar? ")
        print("\n")    
        if funcion == '.sensores()':
            solaris.sensores()
            gran_spartan.sensores()
            varage.sensores()
        elif funcion == '.diag_sensores()':
            # Esta método se necesita ejecutar antes de la reparación de sensores,
            # para poder transmitir la lista de códigos de sensores en falla.
            sen_falla_sol = solaris.diag_sensores()
            sen_falla_spa = gran_spartan.diag_sensores()
            sen_falla_var = varage.diag_sensores()
        elif funcion == '.reparar_sensores()':
            # Necesita la lista de sensores en falla del método ".diag_sensores()".
            solaris.reparar_sensores(sen_falla_sol)
            gran_spartan.reparar_sensores(sen_falla_spa)
            varage.reparar_sensores(sen_falla_var)
        elif funcion == '.graf_velocidad()':
            # Solo se imprime una gráfica, ya que solo existe una para
            # todos los vehículos.
            solaris.graf_velocidad()
        elif funcion == '.autonomia()':
            solaris.autonomia()
            gran_spartan.autonomia()
            varage.autonomia()
        elif funcion == '.valvulas()':
            solaris.valvulas()
            gran_spartan.valvulas()
            varage.valvulas()
        elif funcion == 'SALIR':
            print("Saliendo del programa...")
            break
        else:
            print("No se ha encontrado la función, favor de reescribirla.")
    
        
        
