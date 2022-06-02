### T4: Ejemplo básico de TKINTER ###
# Fecha: 30 / 03 / 2022
# Autor: Ing. Brian García Sarmina

#- Importar paqueterias -#
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Función de imprimir nombre.
def nombre():
    print("Ing. Brian García Sarmina")

# Función para graficar.
def grafica():
    t = 50
    t_pasos = []
    x_pasos = []
    for i in np.arange(0, t, 0.3):
        x = np.cos(i)
        t_pasos.append(i)
        x_pasos.append(x)

    plt.grid(linestyle='--')
    plt.plot(t_pasos, x_pasos)
    plt.scatter(t_pasos, x_pasos, color='k')
    plt.show()

### MAIN ###
if __name__ == '__main__':

    # Creamos la ventana "root".
    root = Tk() # Generamos una instancia de la clase Tk().
    root.title("Tkinter Básico") # Generamos titulo de ventana.

    #-------------------------------------------------------#
    # Etiquetas.
    # Generar una etiqueta de texto con el metodo "Label()", recibe como
    # parametros, la ventana donde pertenece, en este caso es "root" (ventana principal),
    # y el "text" que sera el texto que presente la etiqueta.
    texto1 = Label(root, text="Etiqueta de texto")
    texto2 = Label(root, text="Imprimir nombre")
    texto3 = Label(root, text="Generar gráfica")
    et_salto = Label(root, text="\n") # Etiqueta para saltar una linea.
    # Botones.
    # Los botones se generan usando el metodo "Button", que igual reciben la ventana a la
    # pertenecen, en este caso es "root", despues el texto que presenta el boton "text", y
    # "command" es la acción que realiza el boton, esto sirve para llamar a una función
    # o metodo de una clase.
    but_nombre = Button(root, text="Nombre", command=nombre)
    but_grafica = Button(root, text="Graficar", command=grafica)
    # Caso especial para salir del programa.
    but_salir = Button(root, text="SALIR", command=root.destroy) 

    #-------------- AGREGAR WIDGETS CREADOS ---------------#
    # Despues de crear las etiquetas, botones, etcetera; es necesario incorporarlos con
    # alguno de los metodos que posee Tkinter, en este caso usamos "grid" que recibe el
    # número de fila "row" (nivel vertical) y el número de columna "column" (distribución
    # horizontal).
    # Con "columnspan" se distribuye la etiqueta en el número establecido de columnas
    # permitidas.
    texto1.grid(row=0, column=0, columnspan=2)
    texto2.grid(row=1, column=0)
    texto3.grid(row=2, column=0)
    but_nombre.grid(row=1, column=1)
    but_grafica.grid(row=2, column=1)
    but_salir.grid(row=3, column=0, columnspan=2)

    # Loop infinito de TKINTER
    # Este comando genera el ciclo de interacción entre las entradas "clicks" a los botones
    # de la aplicación mientras esta este activa.
    root.mainloop()
