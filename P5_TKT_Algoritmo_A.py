### P5: CLASE ALGORITMO A* ###
# Fecha: 03 / 05 / 2022
# Autor: M.C.C. Brian García Sarmina

#- Importar paqueterias -#
from math import sqrt, sin, cos, tan, atan2, pi
import random
import numpy as np
import traceback
from random import randint
import matplotlib.pyplot as plt
import time
from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


###-- CLASE ALGORITMO A* --###
class Algoritmo_A():
    def __init__(self, dimension):
        # Atributos para mapa.
        self.dimension = dimension
        self.contador = 0 # Contador para el numero de objetos.
        self.valor_objeto = 255 # Valor preestablecido de un objeto o pared
                                # (donde '255' representa ocupado).
        # Variables para valores y movimientos permitidos.
        self.s2 = np.sqrt(2)
        self.v_c = 1   
        # Vecinos directos (arriba, abajo, izquierda, derecha).
        # Vecinos diagonales (sup_der, sup_izq, inf_der, inf_izq), estos tienen un
        # costo adicional "s2".
        self.movimientos = [(self.v_c, 0, 1.0), (0, self.v_c, 1.0), (-self.v_c, 0, 1.0), (0, -self.v_c, 1.0),
              (self.v_c, self.v_c, self.s2), (-self.v_c, self.v_c, self.s2),
              (-self.v_c, -self.v_c, self.s2), (self.v_c, -self.v_c, self.s2)]
        
######################################### MAPA ###########################################
    # Obtener dimensiones de mapa, desde el menu. 
    def obtener_dimensiones(self, dimension):
        # Dimension del mapa de exploración.
        self.dimension = dimension
        # Matriz de obstaculos.
        self.obstaculos = np.zeros((self.dimension, self.dimension)) 

    # Obtener el número de obstaculos, desde menu.
    def obtener_num_obstaculos(self, cantidad_obstaculos):
        self.cantidad_obstaculos = cantidad_obstaculos # Cantidad de obstaculos

    #- Metodo para generar los limites de la matriz de exploración -#
    def establecer_limites(self):
        for l in range(self.dimension):
            self.obstaculos[0][l] = self.valor_objeto
            self.obstaculos[l][0] = self.valor_objeto
            self.obstaculos[self.dimension - 1][l] = self.valor_objeto
            self.obstaculos[l][self.dimension - 1] = self.valor_objeto
            
    #- Metodo para generar obstaculos -#
    def establecer_obstaculos(self):
        # Un while infinito para generar los obstaculos.
        while True:
            # Se elige un ancho y alto de obstaculo aleatorio.
            valor_linea_x = randint(0, 10)
            valor_linea_y = randint(0, 10)
            # Se elige una coordenada aleatoria para colocar dicho obstaculo.
            obj_al_y = randint(0, (self.dimension - 1))
            obj_al_x = randint(0, (self.dimension - 1))
            # Se le asigna el valor de objeto a la matriz de obstaculos.
            self.obstaculos[obj_al_x][obj_al_y] = self.valor_objeto
            # Se genera el objeto en eje x.
            for i in range(valor_linea_x):
                # Avanza la linea a la derecha.
                linea_en_x = obj_al_x + i
                # Preguntamos si el elemento generado a la derecha se encuentra dentro
                # de las dimensiones del mapa de exploración.
                if linea_en_x < (self.dimension - 1):
                    self.obstaculos[linea_en_x][obj_al_y] = self.valor_objeto
                # Avanza la linea a la izquierda.
                linea_en_x = obj_al_x - i
                # Preguntamos si el elemento generado a la izquierda se encuentra dentro
                # de las dimensiones del mapa de exploración.
                if 0 < linea_en_x < (self.dimension - 1):
                    self.obstaculos[linea_en_x][obj_al_y] = self.valor_objeto
            # Se repite el proceso anterior para el eje y.
            for i in range(valor_linea_y):
                linea_en_y = obj_al_y + i
                if linea_en_y < (self.dimension - 1):
                    self.obstaculos[obj_al_x][linea_en_y] = self.valor_objeto
                linea_en_y = obj_al_y - i
                if 0 < linea_en_y < (self.dimension - 1):
                    self.obstaculos[obj_al_x][linea_en_y] = self.valor_objeto
            # Contador para la cantidad de obstaculos permitidos por mapa.
            if self.contador == self.cantidad_obstaculos:
                break
            # Aumentamos contador de obstaculos.
            self.contador += 1

        # Vectores correspondientes para las coordenadas de x y y de los objetos del mapa.
        self.x_coo = []
        self.y_coo = []
        self.coordenadas_objetos = []
        # Extraemos las coordenadas de los obstaculos generados.
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.obstaculos[i][j] == 255:
                    self.x_coo.append(i)
                    self.y_coo.append(j)
                    self.coordenadas_objetos.append([i, j])
        # Reiniciar contador.
        self.contador = 0

    #- Metodo para crear un punto de inicio -#
    def establecer_inicio(self):
        # Este punto debe estar dentro del mapa de exploración y no ser o pertenecer
        # a un obstaculo generado.
        while True:
            self.inicio_x = randint(0, self.dimension - 1)
            self.inicio_y = randint(0, self.dimension - 1)
            if self.obstaculos[self.inicio_x][self.inicio_y] != 255:
                break
            
    #- Metodo para crear una meta -#
    def establecer_meta(self):
        # Este punto debe estar dentro del mapa de exploración y no ser o pertenecer
        # a un obstaculo generado.
        while True:
            self.meta_x = randint(0, self.dimension - 1)
            self.meta_y = randint(0, self.dimension - 1)
            if self.obstaculos[self.meta_x][self.meta_y] != 255:
                break
            
####################################### ALGORITMO A* #######################################        
    #- Metodo para calcular distancia euclididana en 2d -#  
    def distancia(self, p, q):
        return np.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)

    #- Implementación de Algoritmo A* en 2d -#
    def A_estrella(self):
        # Variables generales para explorar mapa.
        valor_celda = 1
        valor_objeto = 255
        # Conversión de inicio y meta a una lista.
        inicio = list(self.inicio)
        meta = list(self.meta)
        # Los limites se establecen como la forma de la matriz de obstaculos.
        limites = self.obstaculos.shape
        # La matriz de nodos visitados se inicia a ceros.
        self.visitados = np.zeros(limites, dtype=np.float32)    
        # Camino ordenado.
        camino_reversa = {}
        # Vector de frente, que contiene el (inicio + distancia hacia la meta),
        # un valor de costo inicial "0.001", las coordenadas (en primera iteración
        # es el punto de incio) van cambiando con cada iteración, y finalmente se tiene
        # la posición previa (que en primera iteración es "None").
        frente = [((inicio + self.distancia(inicio, meta)), 0.001, inicio, None)]
        # Generamos un while mientras existan elementos en el vector FRENTE.
        while frente:
            # Obtenemos el elemento con valor "minimo" del vecto de FRENTE, respecto a su
            # posición y distancia.
            minimo = min(frente)
            # Obtenemos el indice del elemento con valor minimo del vector de FRENTE.
            indice_min = frente.index(minimo)
            # Eliminamos el elemento elegido del vector de FRENTE.
            del frente[indice_min]
            # Extraemos los datos del elemento elegido, costo total = posición + distancia
            # hacia la meta, costo = costo acumulado, pos = posición actual y
            # pose_previa = posición anterior.
            costo_total, costo, pos, pose_previa = minimo
            # Extraemos las coordenadas "x" y "y" de la posición actual.
            x, y = pos
            # Si la ubicación actual es mayor que "0", ese nodo no se explora y se salta
            # a la siguiente iteración.
            if self.visitados[int(x),int(y)] > 0:
                continue
            # En caso contrario, es decir, que el nodo actual no esta dentro de la matriz
            # de nodos visitados con valor mayor que "0", entonces agregamos ese elemento
            # a la matriz de nodos visitados con el "costo" que posee.
            self.visitados[int(x),int(y)] = costo
            # Agregamos el nodo anterior, el nodo previo al que se esta explorando
            # actualmente, ese nodo resulta ser el elemento con el valor minimo anterior.
            camino_reversa[int(x),int(y)] = pose_previa
            # Verificamos si el nodo que estamos explorando es la META, si esto es correcto
            # salimos del while infinito, sino seguimos explorando.
            if (pos[0] == meta[0] and pos[1] == meta[1]):
                break
            # Exploramos sobre cada movimiento en el vector de MOVIMIENTOS.
            for dx, dy, deltacosto in self.movimientos:
                # Generamos la nueva posición de "x" y "y" segun el movimiento elegido.
                nueva_x = x + dx
                nueva_y = y + dy
                # Preguntamos si esta nueva "x" y nueva "y" se encuentran dentro de los
                # limites de exploración.
                if 0.0 <= nueva_x < limites[0] or 0.0 <= nueva_y < limites[1]:
                    # Guardamos la nueva posición generada.
                    nueva_pose = [nueva_x, nueva_y]
                    # Actualizacion del costo, contemplando el costo del camino hasta el
                    # momento ("costo") y el costo del movimiento ("deltacosto").
                    nuevo_costo = costo + deltacosto
                    # Entonces, nuevo_costo_total es la suma de nuevo_costo más el valor
                    # calculado de distancia euclididan entre la nueva posición y la meta.
                    nuevo_costo_total = nuevo_costo + self.distancia(nueva_pose, meta)
                    # Si la nueva posición no esta dentro de la matriz de nodos visitados
                    # y no esta considerado como un obstaculo del mapa.
                    if self.visitados[int(nueva_x), int(nueva_y)] == 0 and not self.obstaculos[int(nueva_x), int(nueva_y)] == 255:
                        # Se agrega el nuevo nodo al vector de FRENTE.
                        frente.append((nuevo_costo_total, nuevo_costo, nueva_pose, pos))
                # Si no se cumple la condición dentro de los limites, se continua con
                # otro movimiento.
                else:
                    continue
        # Generamos el camino minimo.
        camino = []
        # Si la posición alcanzada es la meta.
        if (pos[0] == meta[0] and pos[1] == meta[1]):
            # Mientras existan elementos en "pos".
            while pos:
                # Agregamos el camino a "camino_reversa".
                camino.append(pos)
                x_p, y_p = pos
                pos = camino_reversa[int(x_p), int(y_p)]
            # Invertimos el orden de la lista de camino.
            camino.reverse()
            self.camino_fin = camino
        
        return self.camino_fin, self.visitados

    #- Metodo para graficar mapa, obstaculos y camino elegido -#
    def graficar_camino(self):
        # Extraemos las coordenadas de la matriz de nodos visitados.
        coo_visitados = []
        for x in range(len(self.visitados)):
            for y in range(len(self.visitados)):
                if self.visitados[x][y] != 0.0:
                    coo_visitados.append([x, y])
                else:
                    continue

        inicio = list(self.inicio)
        meta = list(self.meta)
        #------------- ACTUALIZAR VENTANA GRAFICA ---------------#
        # Generación de figura y subgrafica.
        figura = plt.figure()
        ax1 = figura.add_subplot()
        ax1.grid(linestyle='--')
        ax1.set_title("Mapa de exploración")
        ax1.set_xlabel("Coordenada x")
        ax1.set_ylabel("Coordenada y")
        ax1.scatter([vis[0] for vis in coo_visitados], [vis[1] for vis in coo_visitados], color='yellow')
        ax1.scatter([obj[0] for obj in self.objetos], [obj[1] for obj in self.objetos])
        ax1.scatter(inicio[0], inicio[1], color='k')
        ax1.scatter(meta[0], meta[1], color='r')
        ax1.plot([cam[0] for cam in self.camino_fin], [cam[1] for cam in self.camino_fin])
        # Variables para graficar.
        bar1 = FigureCanvasTkAgg(figura, root)
        bar1.get_tk_widget().grid(row=5, column=0, columnspan=2)
        #--------------------------------------------------------#
        
################################# Metodos para simular ###################################
    # Generación de mapa.
    def generar_mapa(self):
        # Generamos el mapa con limites, obstaculos y punto de inicio.
        self.establecer_limites()
        self.establecer_obstaculos()
        self.establecer_inicio()
        self.establecer_meta()
        self.inicio = (self.inicio_x, self.inicio_y)
        self.meta = (self.meta_x, self.meta_y)
        self.objetos = self.coordenadas_objetos

        #------------- ACTUALIZAR VENTANA GRAFICA ---------------#
        # Generación de figura y subgrafica.
        figura = plt.figure()
        ax1 = figura.add_subplot()
        ax1.grid(linestyle='--')
        ax1.set_title("Mapa de exploración")
        ax1.set_xlabel("Coordenada x")
        ax1.set_ylabel("Coordenada y")
        ax1.scatter([obj[0] for obj in self.objetos], [obj[1] for obj in self.objetos])
        ax1.scatter(self.inicio[0], self.inicio[1], color='k')
        ax1.scatter(self.meta[0], self.meta[1], color='r')
        # Variables para graficar.
        bar1 = FigureCanvasTkAgg(figura, root)
        bar1.get_tk_widget().grid(row=5, column=0, columnspan=2)
        #--------------------------------------------------------#
    # Aplicación de algoritmo A*.
    def simular(self):
        # Algoritmo A*.
        self.A_estrella()
        self.graficar_camino()


### MAIN ###    
if __name__ == '__main__':

    # Creamos la ventana "root".
    root = Tk()
    root.title("Algoritmo A*")

    # Instancia de clase Algoritmo A*.
    alg_a1 = Algoritmo_A(dimension=100)
    
    #------------------ CREAR WIDGETS ---------------------#
    # Cuadros visuales.
    ventana_sep = ttk.Panedwindow(root, orient=HORIZONTAL)
    ventana_sep.grid(row=2, column=0, columnspan=2)
    fram1=ttk.Frame(ventana_sep, width=250, height=130, relief=SUNKEN)
    ventana_sep.add(fram1, weight=1)
    fram1.grid_propagate(0)
    #----------- CREAR MENU DE ENTRENAMIENTO --------------#
    dimensiones_mapa = [100, 200, 300, 400]
    numero_obstaculos = [10, 20, 30, 40]
    var = IntVar()
    var2 = IntVar()
    var.set(dimensiones_mapa[0])
    var2.set(numero_obstaculos[0])
    menu_dimension = OptionMenu(fram1, var, *dimensiones_mapa,
                             command=alg_a1.obtener_dimensiones)
    menu_obstaculos = OptionMenu(fram1, var2, *numero_obstaculos,
                             command=alg_a1.obtener_num_obstaculos)
    #-------------------------------------------------------#
    # Etiquetas.
    et_titulo = Label(root, text="  Algoritmo de A*  ",
                      font='Helvetica 15 bold')
    texto1 = Label(fram1, text="Atributos para Mapa")
    texto2 = Label(fram1, text="Dimensiones (nxn): ")
    texto3 = Label(fram1, text="Obstaculos: ")
    et_salto = Label(root, text="\n")
    # Botones.
    but_mapa = Button(fram1, text="Generar mapa", command=alg_a1.generar_mapa)
    but_correr = Button(fram1, text="Simular", command=alg_a1.simular)
    but_salir = Button(root, text="SALIR", command=root.destroy)
    #-------------- AGREGAR WIDGETS CREADOS ---------------#
    et_titulo.grid(row=0, column=0, columnspan=2)
    texto1.grid(row=1, column=0, columnspan=2)
    # Elección de dimensión.
    texto2.place(x=20, y=25)
    menu_dimension.place(x=160, y=20)
    # Elección de obstaculos.
    texto3.place(x=35, y=60)
    menu_obstaculos.place(x=160, y=55)
    but_mapa.place(x=20, y=90)
    but_correr.place(x=150, y=90)
    et_salto.grid(row=4, column=0)
    #------------- ACTUALIZAR VENTANA GRAFICA ---------------#
    # Generación de figura y subgrafica.
    figura = plt.figure()
    ax1 = figura.add_subplot()
    ax1.grid(linestyle='--')
    ax1.set_title("Mapa de exploración")
    ax1.set_xlabel("Coordenada x")
    ax1.set_ylabel("Coordenada y")
    # Variables para graficar.
    bar1 = FigureCanvasTkAgg(figura, root)
    bar1.get_tk_widget().grid(row=5, column=0, columnspan=2)
    #--------------------------------------------------------#
    # Agregar boton de salida.
    but_salir.grid(row=6, column=0, columnspan=2)
        
    # Loop infinito de TKINTER
    root.mainloop()
        
