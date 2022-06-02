### P2 CLASE VEHICULO con TKINTER ###
# Fecha: 06 / 04 / 2022
# Autor: M.C.C. Brian García Sarmina


#- Importar paqueterías -#
import numpy as np
import random as r
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import * # Importa toda la paquetería de tkinter.
# Metodo para gráfica usando Tkinter.
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 


#- Clase VEHICULO -#
class Vehiculo:

    # Definimos constructor.
    def __init__(self, nombre, gasolina, tamaño_tanque, rendimiento=18):
        self.nombre = nombre # Nombre del vehiculo.
        self.gasolina = gasolina # Tipo de combustible que usa.
        self.tamaño_tanque = tamaño_tanque # Tamaño de litros del tanque.
        self.rendimiento = rendimiento # Rendimiento de km por litro.
        # Agregamos un nuevo atributo "SENSORES EN FALLA", esto se hace
        # debido al funcionamiento de Tkinter, el cual no permite regresar
        # valores explicitos de metodos (como variables), pero podemos utilizar
        # la idea de POO, donde podemos modificar un atributo usando un metodo
        # al interior de la clase y ACTUALIZARLO.
        self.sensores_en_falla = [] 

    # Método "sensores".
    def sensores(self):
        texto_sensores = """\n   Los sensores que este vehiculo tiene son: 
        -sensor gasolina (código 001).
        -sensor temperatura (código 002).
        -sensor de puertas (código 003).
        -sensor ABS (código 004).
        -sensor de nivel de aceite (código 005).
            """
        # Insertar el texto generado, dentro de la ventana de texto.
        texto.delete('1.0', END) # Comando para borrar elementos de cuadro de texto.
        texto.insert(tk.END, texto_sensores)

    # Método "diag_sensores"
    # simula la falla de uno o varios sensores del sistema.
    def diag_sensores(self):
        # Se genera un cierto número de sensores posibles
        # en falla.
        num_sens_en_falla = r.randrange(0,4)
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
            texto_sen_falla = "\n No hay sensores en falla \n"
            #print(texto_sen_falla)
            # Insertar el texto generado, dentro de la ventana de texto.
            texto.delete('1.0', END) # Comando para borrar elementos de cuadro de texto.
            texto.insert(END, texto_sen_falla)
        else: # Se imprimen los sensores en falla.
            texto_sen_falla = "\n Los sensores en falla son: \n \n" + "    "\
                              + str(sensores_en_falla) + "\n"
            #print(texto_sen_falla)
            # Insertar el texto generado, dentro de la ventana de texto.
            texto.delete('1.0', END) # Comando para borrar elementos de cuadro de texto.
            texto.insert(END, texto_sen_falla)

        # Se actualiza el valor del atributo "self.sensores_en_falla".
        self.sensores_en_falla = sensores_en_falla
        
        return self.sensores_en_falla # Regresamos la lista de "sensores_en_falla".
    
    # Método "reparar_sensores"
    # Ya no es necesario enviar la lista de "sensores en falla", porque se cuenta
    # con el atributo "self.sensores_en_falla" el cual contempla la lista de sensores
    # simulados en falla.
    def reparar_sensores(self):
        # Presentar texto inicial de mensaje.
        texto_rep = "\n El vehículo " + self.nombre + " presenta estas fallas: \n"
        texto.delete('1.0', END)
        texto.insert(tk.END, texto_rep)
        # Iteramos sobre cada codigo de "sensor" con falla.
        for sensor in self.sensores_en_falla: # Modificación por "self.sensores_en_falla".
            if sensor == '001':
                texto_falla = "\n  ---CÓDIGO 001---" + "\n Pasos para solución: \n" +\
                              " 1. Verificar nivel de gasolina. \n" +\
                              " 2. Reemplazar sensor AT2209GAS. \n" +\
                              " 3. Oprima boton RESET por 3 segundos, para reiniciar CPU. \n"
                texto.insert(tk.END, texto_falla)
            elif sensor == '002':
                texto_falla = "\n  ---CÓDIGO 002---" + "\n Pasos para solución: \n" +\
                              " 1. Apagar vehiculo y esperar que baje temperatura. \n" +\
                              " 2. Reemplazar sensor HG1009TEM. \n" +\
                              " 3. Oprima boton RESET por 3 segundos, para reiniciar CPU. \n"
                texto.insert(tk.END, texto_falla)
            elif sensor == '003':
                texto_falla = "\n  ---CÓDIGO 003---" + "\n Pasos para solución: \n" +\
                              " 1. Apagar vehiculo. \n" +\
                              " 2. Reemplazar sensor JL3798PUE. \n" +\
                              " 3. Oprima boton RESET por 3 segundos, para reiniciar CPU. \n"
                texto.insert(tk.END, texto_falla)
            elif sensor == '004':
                texto_falla = "\n  ---CÓDIGO 004---" + "\n Pasos para solución: \n" +\
                              " 1. Llevar vehiculo para manteniemto a distruidor autorizado. \n"
                texto.insert(tk.END, texto_falla)
            elif sensor == '005':
                texto_falla = "\n  ---CÓDIGO 005---" + "\n Pasos para solución: \n" +\
                              " 1. Llevar vehiculo para manteniemto a distruidor autorizado. \n"
                texto.insert(tk.END, texto_falla)


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

        #------------- ACTUALIZAR VENTANA GRAFICA ---------------#
        figura = plt.Figure(figsize=(5,4), dpi=100)
        ax1 = figura.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figura, root)
        bar1.get_tk_widget().grid(row=9, column=1)
        #--------------------------------------------------------#
        # Gráfica de velocidad.
        ax1.plot(tiempos, velocidades)
        ax1.scatter(tiempos, velocidades)
        ax1.grid(linestyle='--')
        ax1.set_title("Gráfica de velocidad")
        ax1.set_xlabel("Tiempo (seg)")
        ax1.set_ylabel("Velocidad (km/h)")


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
        # Presentar texto inicial de mensaje.
        texto_autonomia = "\n \n La autonomia del vehiculo (en km) " + self.nombre +\
                          " es de: " + str(autonomia) + "km \n"
        texto.delete('1.0', END)
        texto.insert(tk.END, texto_autonomia)

        
    # Método "valvulas"
    def valvulas(self):
        #------------- ACTUALIZAR VENTANA GRAFICA ---------------#
        figura = plt.Figure(figsize=(5,4), dpi=100)
        ax1 = figura.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figura, root)
        bar1.get_tk_widget().grid(row=9, column=1)
        #--------------------------------------------------------#
        # Se encarga de simular a traves de una gráfica
        # el rendimiento de cada válvula dependiendo el
        # tipo de gasolina usada.
        if self.gasolina == 'Gasolina':
            # Creamos un diccionario con los valores de
            # porcentaje de rendimiento para cada válvula,
            # para el caso de "Gasolina" se suponen 4 valvulas.
            valvulas = {'v1':90, 'v2':80, 'v3':80, 'v4':90}
            num_valvula = list(valvulas.keys()) # Identificadores.
            por_rendimiento = list(valvulas.values()) # Valores.
            # Creamos una "gráfica de barras" (ACTUALIZADA).
            ax1.bar(num_valvula, por_rendimiento, color ='maroon', width = 0.4) 
            ax1.set_xlabel("Número de válvula")
            ax1.set_ylabel("Porcentaje de rendimiento")
            ax1.set_title("Rendimiento de válvulas")
            
        elif self.gasolina == 'Diesel':
            # Se suponen 6 válvulas.
            valvulas = {'v1':85, 'v2':85, 'v3':85,
                        'v4':85, 'v5':85, 'v6':85}
            num_valvula = list(valvulas.keys()) # Identificadores.
            por_rendimiento = list(valvulas.values()) # Valores. 
            # Creamos una "gráfica de barras" (ACTUALIZADA).
            ax1.bar(num_valvula, por_rendimiento, color ='maroon', width = 0.4) 
            ax1.set_xlabel("Número de válvula")
            ax1.set_ylabel("Porcentaje de rendimiento")
            ax1.set_title("Rendimiento de válvulas")
        else:
            # Se suponen 5 válvulas.
            valvulas = {'v1':95, 'v2':90, 'v3':90,
                        'v4':90, 'v5':95}
            num_valvula = list(valvulas.keys()) # Identificadores.
            por_rendimiento = list(valvulas.values()) # Valores. 
            # Creamos una "gráfica de barras" (ACTUALIZADA).
            ax1.bar(num_valvula, por_rendimiento, color ='maroon', width = 0.4) 
            ax1.set_xlabel("Número de válvula")
            ax1.set_ylabel("Porcentaje de rendimiento")
            ax1.set_title("Rendimiento de válvulas")


### MAIN ###
if __name__ == '__main__':

    # Creamos unas instacias de la clase VEHICULO,
    # es decir, un objetos de la clase.
    solaris = Vehiculo('Solaris', 'Gasolina', 105)
    #gran_spartan = Vehiculo('Gran Spartan', 'Diesel', 150, 14)
    #varage = Vehiculo('Varage', 'Gas', 100, 17)
    
    # Crea la "ventana" raiz, en TKINTER se llama "widget".
    root = Tk()

    # Cambiar titulo de ventana principal.
    root.title("Programa de información y diagnostico de vehículos")

    # Agregamos el logo del canal de YT.
    img = Image('photo', file="/home/brian/Desktop/PROYECTOS/Clases_YT/Logo_CANAL.png")
    root.tk.call('wm', 'iconphoto', root._w, img)

    #------------------ CREAR WIDGETS --------------------#
    # Creamos una "etiqueta ventana", o
    # "label widget".
    # Crea una objeto etiqueta usando en método "Label(donde, texto)" y se agrega a raíz.
    et_salto = Label(root, text="\n")
    et_sensores = Label(root, text="- .sensores(): Imprime la lista de sensores y sus códigos de falla.")
    et_diag_sensores = Label(root, text="- .diag_sensores(): Simula e imprime una secuencia de sensores posibles en falla.")
    et_rep_sensores = Label(root, text="- .reparar_sensores(sensores en falla)**: Da las indicaciones para reparación de códigos de falla.")
    et_graf_vel = Label(root, text="- .graf_velocidad(): Imprime una gráfica de velocidad IMAGINARIA del vehículo.")
    et_autonomia = Label(root, text="- .autonomia(): Calcula la autonomía del vehículo en kilometros.")
    et_valvulas = Label(root, text="- .valvulas(): Imprime una gráfica del porcentaje de rendimiento de las válvulas del vehículo.")
    et_salir = Label(root, text="- SALIR: Salir del programa.")

    # Crear una ventana de texto, con ciertos valores de alto y ancho.
    texto = Text(root, height=23.3, width=65)
    
    # Para crear un BOTON se usa lo siguiente:
    # Se especifica ("donde" y "que dirá") tambien puede tener estado "state" (hab o desh),
    # se usa "padx=int" o "pady=int" para modificar tamaño.
    # Se usa COMMAND para asignar "acción" al boton, no necesita "()".
    boton_sen = Button(root, text='Sensores', padx=50, command=solaris.sensores)
    boton_diag_sen = Button(root, text="Diagnostico sensores", command=solaris.diag_sensores)
    boton_rep_sen = Button(root, text='Reparación', command=solaris.reparar_sensores)
    boton_graf_vel = Button(root, text="Gráfica velocidad", command=solaris.graf_velocidad)
    boton_autonomia = Button(root, text='Autonomia', command=solaris.autonomia)
    boton_valvulas = Button(root, text='Valvulas', command=solaris.valvulas)
    # El comando "root.destroy" destruye la ventana raiz del programa.
    boton_salir = Button(root, text='SALIR', command=root.destroy)
    #-----------------------------------------------------------------------#

    #------------- AGREGAR WIDGETS CREADOS ---------------#
    # Se agrega el "widget" usando el método ".pack()" (acomoda automático) o "grid()".
    et_salto.grid(row=0, column=0) # Con ".grid()" se puede acomodar especificamente la posición.
    et_salto.grid(row=1, column=0) # los elementos ".grid()" estan relacionados entre si.
    et_sensores.grid(row=2, column=0) # Etiqueta sensores.
    boton_sen.grid(row=2, column=1) # Boton sensores.
    et_diag_sensores.grid(row=3, column=0) # Etiqueta diagnostico de sensores.
    boton_diag_sen.grid(row=3, column=1) # Boton diagnostico de sensores.
    et_rep_sensores.grid(row=4, column=0) # Etiqueta reparación de fallas.
    boton_rep_sen.grid(row=4, column=1) # Boton reparación de fallas.
    et_graf_vel.grid(row=5, column=0) # Etiqueta gráfica de velocidad.
    boton_graf_vel.grid(row=5, column=1) # Boton gráfica de velocidad.
    et_autonomia.grid(row=6, column=0) # Etiqueta autonomia.
    boton_autonomia.grid(row=6, column=1) # Boton autonomia.
    et_valvulas.grid(row=7, column=0) # Etiqueta de rendimiento de válvulas.
    boton_valvulas.grid(row=7, column=1) # Boton de rendimiento de válvulas.
    et_salto.grid(row=8, column=0) # Salto.
    texto.grid(row=9, column=0)
    et_salir.grid(row=10, column=0) # Etiqueta para salir.
    boton_salir.grid(row=10, column=1) # Boton para salir.
    #-----------------------------------------------------#

    #------------- AGREGAR VENTANA GRAFICA ---------------#
    figura = plt.Figure(figsize=(5,4), dpi=100) # Generamos la figura.
    ax1 = figura.add_subplot(111) # Agregamos una subgrafica a la figura.
    bar1 = FigureCanvasTkAgg(figura, root) # Genera la ventana gráfica en widget root.
    bar1.get_tk_widget().grid(row=9, column=1) # Colocamos en alguna posición la ventana.
    ax1.grid(linestyle='--')
    ax1.set_title("Titulo de gráfica")
    ax1.set_xlabel("Eje X")
    ax1.set_ylabel("Eje Y")
    #-----------------------------------------------------#
    
    # Se genera el "CICLO INFINITO" que se encarga de "actualizar" el widget del "root".
    root.mainloop()

    
        
        
