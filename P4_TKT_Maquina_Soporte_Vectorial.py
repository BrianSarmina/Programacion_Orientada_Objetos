### MAQUINAS DE SOPORTE VECTORIAL ###
# Fecha: 20/04/2022
# Autor: M.C.C. Brian García Sarmina

#- TUTORIAL COMPLEMENTARIO -#
""" https://colab.research.google.com/github/gal-a/blog/blob/master/docs/notebooks/sklearn/sklearn_logistic_regression_vs_gbm.ipynb#scrollTo=TYPRYxhH6qJ3 """


#- Importar paqueterías -#
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from tkinter import ttk
import plotly.express as px
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# Nuevas paqueterías
import pandas as pd # Paqueteria para manejar archivos de bases de datos.
from sklearn import datasets, svm
from sklearn.datasets import load_breast_cancer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score




class MaquinaSoporteVectorial:

    def __init__(self, root, df, df_cancer):
        
        # Traemos el "dataframe" creado con la base de datos de cancer de SKLEARN.
        self.root = root
        self.df = df
        self.df_cancer = df_cancer
        self.X = [] # Datos de atributos (altura, peso, forma, etc.).
        self.y = [] # Objetivos (clasificación resultante de los atributos).
        # Separamos los conjuntos de atributos de los de clasificación (objetivos),
        # esto se hace tomando el conjunto de los datos de atributos (tipo forma del
        # tumor, textura, diametro, etc.), y el resultado o target (benigno o maligno)
        # que tuvieron.
        self.X = self.df.drop(columns='Objetivo') # Atributos.
        self.y = self.df['Objetivo'] # Clases (objetivos).


    #- Metodo para "traducir" el kernel seleccionado -#
    def seleccion_kernel(self, seleccion):
        # Se hace la traducción del "kernel elegido" por la aplicación
        # y el que será enviado al modelo de SKLEARN.
        self.kernel = seleccion
        if self.kernel == "Kernel lineal":
            self.kernel = 'linear'
        elif self.kernel == "Kernel polinómico":
            self.kernel = 'poly'
        elif self.kernel == "Kernel Gaussiano (RBF)":
            self.kernel = 'rbf'
        else: # Caso default.
            self.kernel = 'linear'

    #- Selección de grado para Kernel Polinomial -#
    def seleccion_grado(self, seleccion2):
        # Obtenemos el grado del kernel para el caso polinomial.
        self.grado_poli = seleccion2

    #- Graficar la matriz de correlacion TOTAL -#
    def graficar_correlacion_total(self):
        # Esta grafica nos da una idea inicial de como estan correlacionados
        # los datos caracteristicos de la información de la base de datos, posteriormente
        # se pueden realizar procesos de filtrado y PCA para determinar que atributos de
        # los datos son "LOS MAS IMPORTANTES".

        # Usamos metodo ".heatmap" de Seaborn.
        sns.heatmap(self.df.corr(), annot=True)
        plt.show()
                
    #- Graficar la matriz de correlacion 1v1 -#
    def graficar_correlacion_1v1(self):

        # variables posibles = ['mean radius', 'mean texture', 'mean perimeter', 'mean area', 
        #                        'mean smoothness', 'mean compactness', 'mean concavity',
        #                        'mean concave points', 'mean symmetry', 'mean fractal dimension']
        titulo = "Grafica de correlación"
        sns.pairplot(self.df, hue='Objetivo', vars=['mean radius', 'mean texture',
                                                    'mean perimeter', 'mean area'])

        plt.show()

    #- Grafica de Análsis de Componente Principal -#
    def graficar_pca(self):

        # Este metodo busca establecer la correlacion entre los atributos
        # (caractertisticas) con respecto a las etiquetas (objetivos) generados,
        # este metodo se encarga de realizar una reducción dimensional usando "Valor
        # Singular de Descomposición" (SVD en ingles), que consiste en la factorización
        # de una matriz real o compleja que generaliza la "descompisición propia"
        # (eigendecomposition).
        
        # Numero de componentes, representa el numero de variables
        # para realizar la grafica de Análisis de Componente Principal
        n_componentes = 3
        nombres_atributos = list(self.df_cancer.feature_names) # Lista de atributos.
            
        # Generamos un diccionario donde guardamos los atributos permitidos para
        # graficar (dados por el numero de componentes), y la paleta de colores.
        etiquetas = {str(i): nombres_atributos[i] for i in range(n_componentes)}
        etiquetas['color'] = 'Objetivo'

        # Se genera el modelo "Análisis de Componente Principal" (PCA en ingles).
        pca = PCA(n_components=n_componentes)
        # Se utiliza el metodo ".fit_transform" que realiza la reducción de dimensionalidad
        # segun la base de datos dada, en este caso "self.df" que contiene el "dataframe"
        # de los atributos y etiquetas.
        componentes = pca.fit_transform(self.df)
        # La "relación de varianza explicada" (.explained_variance_ratio) es una metodo,
        # que relaciona el radio de cada caracteristica (vista como su eigenvalor) con
        # respecto del resto de las caracteristicas (suma total de eigenvalores).
        total_var = pca.explained_variance_ratio_.sum() * 100
        # Aqui usamos un metodo de la paqueteria PLOTLY (diferente de matplotlib),
        # para graficar diferentes relaciones de atributos (componentes principales)
        # con el modelo de PCA. 
        fig = px.scatter_matrix(componentes,
                color=self.df_cancer.target,
                dimensions=range(n_componentes),
                labels=etiquetas,
                title=f'Varianza total: {total_var:.2f}%', )        
        # Graficar las trazas graficas generadas.
        fig.update_traces(diagonal_visible=True)
        fig.show()

        
    #- Metodo para entrenar modelo -#
    def entrenar_modelo(self): 
        # Se generan 4 conjuntos, 2 conjuntos "X_entrenamiento" y "Y_entrenamiento"
        # (fase de entrenamiento); y 2 conjuntos "x_prueba" y "y_prueba"
        # (fase de prueba). Todo esto se hace con la funcion "train_test_split()" de
        # SKLEARN.
        self.X_entrenamiento, self.x_prueba, self.Y_entrenamiento, self.y_prueba = train_test_split(self.X, self.y,
                                                               test_size=0.3,
                                                               random_state=109)
        # CREAMOS EL MODELO DE "SVC" (Support Vector Classifier), este es un metodo
        # de SKLEARN que recibe ciertos parámetros, siendo el tipo de "kernel" el
        # que vamos a analizar con los diferentes tipos posibles permitidos.
        self.modelo = SVC(C=100, kernel=self.kernel, degree=self.grado_poli, random_state=123)
        # Una vez generado el modelo, se ingresan los datos de entrenamiento (atributos y
        # objetivos) con el metodo "fit(atributos, objetivos)". 
        self.modelo.fit(self.X_entrenamiento, self.Y_entrenamiento)   
        # Imprimir mensaje.
        if self.kernel == 'poly':
            texto = "SVC usando kernel tipo: " + self.kernel +\
                    " , grado polinomial: " + str(self.grado_poli) +\
                    "\n" +\
                    "Modelo entrenado exitosamente."
        else:
            texto = "SVC usando kernel tipo: " + self.kernel +\
                    "\n" +\
                    "Modelo entrenado exitosamente."
        texto_modelo.delete('1.0', tk.END)
        texto_modelo.insert(tk.END, texto)

        # Se genera la predicción usando el modelo entrenado.
        self.prediccion_modelo()

    #- Generar la predicción con respecto del modelo generado-#
    def prediccion_modelo(self):
        # Este metodo ".predict(datos prueba)", genera una serie de respuestas
        # clasificadas segun el modelo usado, es decir, que el metodo recibe una
        # serie de datos "nuevos" de los cuales debe generar una cierta respuesta,
        # la cual debe ser analizada para saber que tan bueno o malo es el modelo entrenado.
        self.y_pred = self.modelo.predict(self.x_prueba)

    #- Metodo para obtener los datos de analsis del modelo -#
    def analisis_modelo(self):
        # La función "accuracy_score(reales, predecidos)" se encarga de comparar,
        # las respuestas generadas de la predicción con respecto de los resultados
        # reales.
        exactitud = accuracy_score(self.y_prueba, self.y_pred)
        # Radio de precision, establece la relación entre "verdaderos positivos" con
        # el "falsos positivos", en otras palabras, es la calidad del modelo para NO
        # clasificar un modelo como positivo (etiqueta que no pertenece) como negativo.
        radio_precision = precision_score(self.y_prueba, self.y_pred)
        # La "recuperación" es la relación entre "verdaderos positivos" y
        # "falsos negativos", es decir, la calidad del modelo para DETECTAR TODAS LAS
        # MUESTRAS POSITIVAS.
        radio_recuperacion = recall_score(self.y_prueba, self.y_pred)
        texto_analisis = "Exactitud: " + str(exactitud) + "\n" +\
                         "Radio precisión: " + str(radio_precision) + "\n" +\
                         "Radio recuperación: " + str(radio_recuperacion)
        texto_modelo.delete('1.0', tk.END)
        texto_modelo.insert(tk.END, texto_analisis)
        # Grafica de matriz de confusión.
        mc = confusion_matrix(self.y_prueba, self.y_pred)
        nombres = ['V-N','F-P','F-N','V-P']
        cuentas = ['{0:0.0f}'.format(valor) for valor in mc.flatten()]
        etiquetas = [f'{v1}\n{v2}' for v1, v2 in zip(nombres, cuentas)]
        etiquetas = np.asarray(etiquetas).reshape(2,2)
        sns.heatmap(mc, annot=etiquetas, fmt='', cmap='Blues')
        plt.show()


### MAIN ###
if __name__ == "__main__":

    # Creamos la ventana "root".
    root = Tk()
    root.title("SVC")
    # Importar datos de base de cancer de SKLEARN.
    cancer = datasets.load_breast_cancer()
    # Convertir base de datos en "Dataframe" de Pandas,
    # tomamos los datos usando "data=cancer.data" y los
    # nombres de las columnas con "columns=cancer.feature_names".
    df = pd.DataFrame(data=cancer.data, columns=cancer.feature_names)
    # Agregamos las clasificaciones obtenidas para los datos de cancer,
    # normalmente se clasifican como "benigno" o "maligno".
    df['Objetivo'] = cancer.target

    # Creamos una instancia de la clase MaquinaSoporteVectorial.
    svm1 = MaquinaSoporteVectorial(root, df, cancer)

    #----------- CREAR MENU DE ENTRENAMIENTO --------------#
    tipos_kernel = ["Kernel lineal", "Kernel polinómico", "Kernel Gaussiano (RBF)"]
    grados_poli = [2, 3 , 4, 5]
    var = StringVar() # Variable tipo TKINTER, que permite mantener monitorización de valor
                      # elegido por el menu de tipos de kernel.
    var.set(tipos_kernel[0])
    var2 = IntVar()
    var2.set(grados_poli[0])
    menu_kernel = OptionMenu(root, var, *tipos_kernel, command=svm1.seleccion_kernel)
    menu_grados = OptionMenu(root, var2, *grados_poli, command=svm1.seleccion_grado)

    #------------------ CREAR WIDGETS ---------------------#
    # Cuadros visuales.
    ventana_sep = ttk.Panedwindow(root, orient=HORIZONTAL)
    ventana_sep2 = ttk.Panedwindow(root, orient=HORIZONTAL)
    ventana_sep.grid(row=6, column=0, columnspan=2)
    ventana_sep2.grid(row=7, column=0, columnspan=2)
    #ventana_sep.pack(fill=BOTH, expand=True)
    fram1=ttk.Frame(ventana_sep, width=400, height=120, relief=SUNKEN)
    fram2=ttk.Frame(ventana_sep2, width=400, height=80, relief=SUNKEN)
    ventana_sep.add(fram1, weight=1)
    ventana_sep2.add(fram2, weight=1)
    fram1.grid_propagate(0)
    fram2.grid_propagate(0)
    # Etiquetas.
    et_salto = Label(root, text="\n")
    et_titulo = Label(root, text="  Aplicación de Maquinas de Soporte Vectorial  ",
                      font='Helvetica 18 bold')
    texto1 = Label(root, text="Base de datos de cancer de mama de SKLEARN",
                   font='Helvetica 15')
    texto2 = Label(root, text="Selección tipo de KERNEL: ")
    texto3 = Label(root, text="Para caso de Kernel Polinomial, elegir el grado: ")
    texto4 = Label(fram1, text="Graficar")
    texto5 = Label(fram2, text="Entrenar modelo")
    # Ventana de texto para presentar datos del modelo.
    texto_modelo = Text(root, height=5, width=50)
    # Botones.
    boton_graficar_cor_1v1 = Button(fram1, text="Graf Cor 1v1", command=svm1.graficar_correlacion_1v1)
    boton_graficar_cor_total = Button(fram1, text="Graf Cor TOTAL", command=svm1.graficar_correlacion_total)
    boton_graficar_pca = Button(fram1, text="Graf PCA", command=svm1.graficar_pca)
    boton_ent = Button(fram2, text="Entrenar", command=svm1.entrenar_modelo)
    boton_analisis = Button(fram2, text="Análisis modelo", command=svm1.analisis_modelo)
    boton_salir = Button(root, text="SALIR", command=root.destroy)
    #---------------------------------------------------------------#
    
    #-------------- AGREGAR WIDGETS CREADOS ---------------#
    et_titulo.grid(row=0, column=0, columnspan=2)
    et_salto.grid(row=1, column=0)
    texto1.grid(row=2, column=0, columnspan=2)
    et_salto.grid(row=3, column=0)
    # Elección de KERNEL
    texto2.grid(row=4, column=0)
    menu_kernel.grid(row=4, column=1)
    # Elección de grado polinomial.
    texto3.grid(row=5, column=0)
    menu_grados.grid(row=5, column=1)
    ##-- SUBVENTANA 1 --##
    # Graficas.
    texto4.grid(row=0, column=0)
    # Se usa el metodo ".place(x, y)" para ubicar libremente el boton
    # dentro del cuadro generado.
    boton_graficar_cor_total.place(x=200, y=10)
    boton_graficar_cor_1v1.place(x=200, y=40)
    boton_graficar_pca.place(x=200, y=70)
    ##-- SUBVENTANA 2 --##
    # Entrenamiento.
    texto5.grid(row=8, column=0)
    boton_ent.place(x=200, y=10)
    # Análisis de modelo.
    boton_analisis.place(x=200, y=40)
    # Cuadro de texto.
    texto_modelo.grid(row=11, column=0, columnspan=2)
    boton_salir.grid(row=12, column=0, columnspan=2)
    #-------------------------------------------------------#

    # Loop infinito de TKINTER
    root.mainloop()
