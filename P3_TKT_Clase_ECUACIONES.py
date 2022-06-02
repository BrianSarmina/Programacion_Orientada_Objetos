### P3 CLASE ECUACIONES con TKINTER ###
# Fecha: 08 / 04 / 2022
# Autor: M.C.C. Brian García Sarmina

#- Importar paqueterías -#
import numpy as np
import random as r
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Ellipse, Circle


#- Funcion para crear una ventana nueva
#- usando algun widget de boton -#
def nueva_ventana(figura, titulo):
     
    # Se crea un objeto "Toplevel",
    # que sera la nueva ventana, con referencia
    # a al raiz.
    n_ven = Toplevel(root)

    # Titulo de la nueva ventana.
    n_ven.title(titulo)

    #------------- ACTUALIZAR VENTANA GRAFICA ---------------#
    # Variables para graficar.
    bar1 = FigureCanvasTkAgg(figura, n_ven)
    bar1.get_tk_widget().grid(row=0, column=0, columnspan=2)
    #--------------------------------------------------------#

#------------------------------------------------------------#

    
#- CLASE ECUACIONES -#
class Ecuaciones:

    def __init__(self, x_ini=0, x_fin=10, t_ini=0, t_fin=10):
        
        self.x_ini = x_ini # Valor de x inicial.
        self.x_fin = x_fin # Valor de x final.
        self.t_ini = t_ini # Valor de t inicial.
        self.t_fin = t_fin # Valor de t final.

        # Listas de valores para gráficar.
        self.x1 = []
        self.f_x1 = []
        self.t1 = []
        self.f_t1 = []
        

    #---------------------- AMORTIGUADOR ---------------------------#
    def amortiguador(self):

        # Calculo de valores para mostrar la oscilación subamortiguada.
        for i in np.arange(self.t_ini, self.t_fin, 0.05):
            t = i
            self.t1.append(t)
            f_t = np.exp(-t) * np.cos(2*np.pi*t)
            self.f_t1.append(f_t)
            
        # Calculo de valores que muestran la pendiende decreciente a
        # saltos discretos.
        for i in np.arange(self.x_ini, self.x_fin, 1.0):
            x = i
            self.x1.append(x)
            x_t = np.exp(-x) * np.cos(2*np.pi*x)
            self.f_x1.append(x_t)

        # Titulo para grafica y ventana tkinter.
        titulo = 'AMORTIGUADOR SUBAMORTIGUADO'

        #------------- VALORES PARA VENTANA GRAFICA ---------------#
        # Generación de figura y subgrafica.
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot() # Generamos subgrafica.
        self.ax1.grid(linestyle='--')
        self.ax1.set_title(titulo)
        self.ax1.set_xlabel("t")
        self.ax1.set_ylabel("f(t)")
        # Graficar lineas con distintos valores de salto.
        self.ax1.plot(self.t1, self.f_t1, label='Saltos menores')
        self.ax1.plot(self.x1, self.f_x1, 'r', label='Saltos mayores')

        # Generamos la nueva ventana, donde se mostrará la gráfica,
        # pasamos como parámetros la figura generada (contiene la gráfica),
        # y el titulo para colocar en la nueva ventana.
        nueva_ventana(self.fig, titulo)

        # Limpiar datos de atributos.
        self.t1 = []
        self.f_t1 = []
        self.x1 = []
        self.f_x1 = []
    #---------------------------------------------------------------#

    
    #-------------------- ATRACTOR LORENTZ --------------------------#
    def der_parcial_lorentz(self, xyz):
        # Las constantes "s", "r" y "b" se relacionan con parámetros
        # de proporcionalidad relacionados con el NUMERO DE PRANDTL, el
        # NUMERO DE RAYLEIGH y las dimensiones fisicas de la "nivel"
        # o capa de análisis.
        s=10
        r=28
        b=2.667
        x, y, z = xyz # Extracción de variables x, y, z.
        # Derivadas parciales ilustrativas, aqui se puede modificar la
        # derivada calculada para observar distintos fenomenos.
        der_x = s*(y - x)
        der_y = r*x - y - x*z
        der_z = x*y - b*z
        # Guardamos la derivada númerica calculada como un arreglo de numpy.
        der_parcial = np.array([der_x, der_y, der_z])
        
        return der_parcial

    #- Calculo de atractor de Lorentz -#
    def atractor_lorentz(self):

        dt = 0.01 # Valor establecido de "dt".
        numero_pasos = 10000 # Saltos en el tiempo.

        xyzs = np.empty((numero_pasos + 1, 3))  # Agregamos valor extra al numero de pasos.
        xyzs[0] = (0., 1., 1.05)  # Se establece el primer valor del arreglo.

        # Por cada "tiempo" dado por el "numero_pasos" se calculan
        # las derivadas parciales, con lo que se puede estimar la "posición"
        # del siguiente punto.
        for i in range(numero_pasos):
            xyzs[i + 1] = xyzs[i] + self.der_parcial_lorentz(xyzs[i]) * dt

        #------------- VALORES PARA VENTANA GRAFICA ---------------#
        # Titulo para grafica y ventana tkinter.
        titulo = 'ATRACTOR DE LORENTZ'
        # Generación de figura y subgrafica.
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(projection="3d") # Tipo de proyección 3d.
        self.ax1.grid(linestyle='--')
        self.ax1.set_title(titulo)
        self.ax1.set_xlabel("Eje X")
        self.ax1.set_ylabel("Eje Y")
        self.ax1.set_zlabel("Eje Z")
        # Grafica de valores de "Atractor de Lorentz" con lineas y
        # tambien con valores discretos.
        self.ax1.scatter(*xyzs.T, color='red', marker='+', lw=0.3)
        self.ax1.plot(*xyzs.T, lw=0.5)
        #----------------------------------------------------------#

        # Generamos la nueva ventana, donde se mostrará la gráfica,
        # pasamos como parámetros la figura generada (contiene la gráfica),
        # y el titulo para colocar en la nueva ventana.
        nueva_ventana(self.fig, titulo)

        # Limpiar datos de atributos.
        self.t1 = []
        self.f_t1 = []
        self.x1 = []
        self.f_x1 = []
    #---------------------------------------------------------------#


    #------------------ CAMPO MAGNETICO TERRESTRE ------------------#
    # Metodo para calcular el campo vectorial magnetivo para un punto
    # en coordenadas polares (r, theta).
    def campo_mag_rt(self, r, theta):
        fac = self.b0 * np.power((self.r_tierra / r),3)
        # Componente radial.
        r_rad = -2 * fac * np.cos(theta + self.dev_polo)
        # Componente angular.
        r_ang = -fac * np.sin(theta + self.dev_polo)
        return r_rad, r_ang
    # Metodo para simular campo magnetico de la tierra.
    def campo_magnetico(self):
        # Valor promedio del campo magnetico de la Tierra en el ecuador.
        self.b0 = 3.12e-5
        # Radio de la tierra, 6.370x10^6 metros.
        self.r_tierra = 6.370
        # Desviación del polo magnetico del eje, debido a la inclinación de la tierra.
        self.dev_polo = np.radians(9.6)
        # Tamaño de la malla en coordenadas cartesianas "x" y "y".
        nx, ny = 64, 64
        x_max, y_max = 40, 40
        x = np.linspace(-x_max, x_max, nx)
        y = np.linspace(-y_max, y_max, ny)
        X, Y = np.meshgrid(x, y) # Generación de matriz con coordenadas.
        # Transformación a coordendas polares "r" y "theta".
        r, theta = np.hypot(X, Y), np.arctan2(Y, X)
        # Obtención de campo magnetico (Ex, Ey) como elementos individuales.
        Br, Btheta = self.campo_mag_rt(r, theta)
        # Transformación de coordenadas polares a coordenadas cartesianas.
        c, s = np.cos(np.pi/2 + theta), np.sin(np.pi/2 + theta)
        Bx = -Btheta * s + Br * c
        By = Btheta * c + Br * s
        #------------- VALORES PARA VENTANA GRAFICA ---------------#
        # Titulo para grafica y ventana tkinter.
        titulo = 'CAMPO MAGNETICO TERRESTRE'
        # Generación de figura y subgrafica.

        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot()

        # Generación de color, y aplicando el uso de "streamplot" que es un metodo
        # de matplotlib que permite generar una grafica de espacio vectorial con flujo
        # dados los componentes (coo_x, coo_y, Bx, By).
        color1 = 2 * np.log(np.hypot(Bx, By))
        self.ax1.streamplot(x, y, Bx, By, color=color1, linewidth=1, cmap=plt.cm.inferno,
                            density=2, arrowstyle='->', arrowsize=1.5)

        # Generamos una elipse representando a la tierra como centro del campo vectorial
        # de flujo.
        ellipse = Ellipse(xy=(0, 0), width=10.5, height=10, edgecolor='skyblue',
                          fc='darkcyan', lw=2, zorder=100)
        # Polo sur magnético.
        self.ax1.add_patch(Circle((0+np.cos(self.dev_polo),5+np.sin(self.dev_polo)),
                                  0.8, color='r', zorder=101))
        # Polo norte magnético.
        self.ax1.add_patch(Circle((0-np.cos(self.dev_polo),-5-np.sin(self.dev_polo)),
                                  0.8, color='b', zorder=101))
        self.ax1.add_patch(ellipse)
        self.ax1.set_xlabel('$x$')
        self.ax1.set_ylabel('$y$')
        self.ax1.set_xlim(-x_max, x_max)
        self.ax1.set_ylim(-y_max, y_max)
        self.ax1.set_aspect('equal')
        #----------------------------------------------------------#
        # Generamos la nueva ventana, donde se mostrará la gráfica,
        # pasamos como parámetros la figura generada (contiene la gráfica),
        # y el titulo para colocar en la nueva ventana.
        nueva_ventana(self.fig, titulo)
        # Limpiar datos de atributos.
        self.t1 = []
        self.f_t1 = []
        self.x1 = []
        self.f_x1 = []
    #---------------------------------------------------------------#

    #------------------- CAMPO FUERZA 4 VÓRTICES -------------------#
    def campo_magnetico_3d(self):

        # Se realiza la matriz en 3 dimensiones con las coordenadas
        # de cada punto en la matriz.
        i = np.arange(-1, 1, 0.2)
        j = np.arange(-1, 1, 0.2)
        k = np.arange(-1, 1, 0.8)
        x, y, z = np.meshgrid(i, j, k)

        # Calculo de direcciones de los vectores en el espacio 3d.
        u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
        v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
        w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) * np.sin(np.pi * z))

        #------------- VALORES PARA VENTANA GRAFICA ---------------#
        # Titulo para grafica y ventana tkinter.
        titulo = "CAMPO FUERZA 4 VÓRTICES"
        # Generación de figura y subgrafica.
        self.fig = plt.figure()
        self.ax1 = self.fig.gca(projection='3d') # Similar a "subplot" pero "gca" es capaz
                                                 # de agregar un nuevo eje si es necesario.
        self.ax1.grid(linestyle='--')
        self.ax1.set_title(titulo)
        self.ax1.set_xlabel("x")
        self.ax1.set_ylabel("y")
        self.ax1.set_zlabel("z")
        # Grafica de valores de campo de fuerza de 4 vortices usando la
        # función de matplotlib ".quiver(x, y, z, u, v, w)", quiver
        # permite graficar el espacio vectorial con vectores independientes
        # con una magnitud y dirección particular, en el caso anterior con
        # streamplot se graficaba tambien un "flujo" direccional.
        self.ax1.quiver(x, y, z, u, v, w, length=0.15, color = 'black')
        #----------------------------------------------------------#
        # Generamos la nueva ventana, donde se mostrará la gráfica,
        # pasamos como parámetros la figura generada (contiene la gráfica),
        # y el titulo para colocar en la nueva ventana.
        nueva_ventana(self.fig, titulo)

        # Limpiar datos de atributos.
        self.t1 = []
        self.f_t1 = []
        self.x1 = []
        self.f_x1 = []
    #---------------------------------------------------------------#



### MAIN ###
if __name__ == '__main__':

    # Crea la "ventana" raiz.
    root = Tk()
    root.title("Gráfica de ecuaciones")
     # Agregamos el logo del canal de YT.
    img = Image('photo', file="/home/brian/Desktop/PROYECTOS/Clases_YT/Logo_CANAL.png")
    root.tk.call('wm', 'iconphoto', root._w, img)

    #- Se crean las instacias de la clase "Ecuaciones" -#
    ecuacion_amortiguador = Ecuaciones(-5, 5, -5, 5)
    ecuacion_oscilador = Ecuaciones()
    ecuacion_magnetica = Ecuaciones()
    ecuacion_magnetica2 = Ecuaciones()
    
    #------------------ CREAR WIDGETS ---------------------#
    et_salto = Label(root, text="\n")
    et_titulo = Label(root, text="Seleccione el tipo de ecuacion para visualizar")
    texto1 = Label(root, text="Amortiguador")
    texto2 = Label(root, text="Atractor de Lorentz")
    texto3 = Label(root, text="Campo magnético terrestre")
    texto4 = Label(root, text="Campo de fuerza de 4 vórtices")

    #- Crear botones -#
    boton1 = Button(root, text="Graficar", command=ecuacion_amortiguador.amortiguador)
    boton2 = Button(root, text="Graficar", command=ecuacion_oscilador.atractor_lorentz)
    boton3 = Button(root, text="Graficar", command=ecuacion_magnetica.campo_magnetico)
    boton4 = Button(root, text="Graficar", command=ecuacion_magnetica2.campo_magnetico_3d)
    boton_salir = Button(root, text="SALIR", command=root.destroy)
    #------------------------------------------------------#

    
    #-------------- AGREGAR WIDGETS CREADOS ---------------#
    et_titulo.grid(row=0, column=0)
    et_salto.grid(row=1, column=1)
    et_salto.grid(row=2, column=0)
    texto1.grid(row=3, column=0) # Amortiguador.
    boton1.grid(row=3, column=1)
    et_salto.grid(row=4, column=0)
    texto2.grid(row=5, column=0) # Atractor de Lorentz.
    boton2.grid(row=5, column=1)
    et_salto.grid(row=6, column=0)
    texto3.grid(row=7, column=0) # Campo magnético.
    boton3.grid(row=7, column=1)
    et_salto.grid(row=8, column=0)
    texto4.grid(row=9, column=0) # Campo magnético 3D.
    boton4.grid(row=9, column=1)
    et_salto.grid(row=10, column=0)
    boton_salir.grid(row=11, column=0, columnspan=2)
    #------------------------------------------------------#

    
    # Se genera el "CICLO INFINITO" que se encarga de "actualizar" el widget del "root".
    root.mainloop()
    
