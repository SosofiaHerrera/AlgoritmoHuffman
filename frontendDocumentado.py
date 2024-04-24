import tkinter as tk  # Importa el módulo tkinter para crear la interfaz gráfica de usuario (GUI)
from tkinter import filedialog  # Importa el submódulo filedialog de tkinter para abrir el cuadro de diálogo de selección de archivos
from collections import Counter  # Importa la clase Counter del módulo collections para contar la frecuencia de caracteres en un texto
from backend import comprimir, descomprimir, construir_arbol_huffman  # Importa las funciones necesarias desde el módulo backend

class HuffmanFrontend:
    def __init__(self, master):
        self.master = master  # Almacena la ventana principal de la aplicación
        self.entradaCadena = entradaCadena  # Almacena la entrada de texto para la cadena
        self.entradaFrecuencia = entradaFrecuencia  # Almacena la entrada de texto para la frecuencia
        self.entradaArbol = entradaArbol  # Almacena la entrada de texto para el árbol
        master.title("Compresor de Archivos")  # Establece el título de la ventana principal

        # Crea un botón para examinar archivos y llama al método examinar_archivo cuando se presiona
        self.examinar_button = tk.Button(master, text="Examinar", command=self.examinar_archivo)
        self.examinar_button.grid(row=4, column=1, padx=(10, 2), pady=20, sticky="ew")

        # Crea un botón para comprimir archivos y llama al método comprimir_archivo cuando se presiona
        self.comprimir_button = tk.Button(master, text="Comprimir", command=self.comprimir_archivo, state=tk.DISABLED)
        self.comprimir_button.grid(row=4, column=2, padx=2, pady=20, sticky="ew")

        # Crea un botón para descomprimir archivos y llama al método descomprimir_archivo cuando se presiona
        self.descomprimir_button = tk.Button(master, text="Descomprimir", command=self.descomprimir_archivo, state=tk.DISABLED)
        self.descomprimir_button.grid(row=4, column=3, padx=2, pady=20, sticky="ew")

    def examinar_archivo(self):
        file_path = filedialog.askopenfilename()  # Abre el cuadro de diálogo para seleccionar un archivo
        if file_path:  # Si se selecciona un archivo
            self.archivo = file_path  # Almacena la ruta del archivo seleccionado
            self.comprimir_button.config(state=tk.NORMAL)  # Habilita el botón de compresión
            self.descomprimir_button.config(state=tk.NORMAL)  # Habilita el botón de descompresión
            with open(self.archivo, 'r') as file:  # Abre el archivo en modo lectura
                contenido = file.read()  # Lee el contenido del archivo
                self.entradaCadena.delete('1.0', tk.END)  # Borra el contenido actual en la entrada de cadena
                self.entradaCadena.insert(tk.END, contenido)  # Inserta el contenido del archivo en la entrada de cadena
            self.calcular_frecuencia()  # Calcula la frecuencia de caracteres en el archivo

    def calcular_frecuencia(self):
        with open(self.archivo, 'r') as file:  # Abre el archivo en modo lectura
            contenido = file.read()  # Lee el contenido del archivo
            self.frecuencias = Counter(contenido)  # Calcula la frecuencia de caracteres en el contenido
            self.entradaFrecuencia.delete('1.0', tk.END)  # Borra el contenido actual en la entrada de frecuencia
            for caracter, frecuencia in self.frecuencias.items():  # Itera sobre los pares caracter-frecuencia
                self.entradaFrecuencia.insert(tk.END, f"{caracter}: {frecuencia}\n")  # Inserta el par en la entrada de frecuencia
        self.mostrar_arbol_huffman()  # Muestra el árbol de Huffman basado en las frecuencias calculadas

    def mostrar_arbol_huffman(self):
        arbol_huffman = construir_arbol_huffman(self.frecuencias)  # Construye el árbol de Huffman
        self.entradaArbol.delete('1.0', tk.END)  # Borra el contenido actual en la entrada de árbol
        self.dibujar_arbol(arbol_huffman)  # Dibuja el árbol de Huffman en la entrada de árbol

    def dibujar_arbol(self, nodo, nivel=0):
        if nodo:  # Si el nodo no es nulo
            self.entradaArbol.insert(tk.END, "    " * nivel)  # Inserta espacios para la indentación
            self.entradaArbol.insert(tk.END, f"({nodo.frecuencia})\n")  # Inserta la frecuencia del nodo
            self.dibujar_arbol(nodo.izquierda, nivel + 1)  # Dibuja el subárbol izquierdo
            self.dibujar_arbol(nodo.derecha, nivel + 1)  # Dibuja el subárbol derecho

    def comprimir_archivo(self):
        output_file = self.archivo + '.huf'  # Establece el nombre del archivo comprimido
        tabla_codigos = comprimir(self.archivo, output_file)  # Comprime el archivo
        print("Archivo comprimido correctamente.")  # Imprime un mensaje de éxito en la consola

    def descomprimir_archivo(self):
        if self.archivo.endswith('.huf'):  # Si el archivo seleccionado es un archivo comprimido
            output_file = self.archivo[:-4]  # Establece el nombre del archivo descomprimido
            descomprimir(self.archivo, output_file)  # Descomprime el archivo
            print("Archivo descomprimido correctamente.")  # Imprime un mensaje de éxito en la consola
        else:
            print("El archivo seleccionado no es un archivo comprimido.")  # Imprime un mensaje de advertencia en la consola

root = tk.Tk()  # Crea la ventana principal de la aplicación
root.title("Algoritmo de Huffman")  # Establece el título de la ventana
root.geometry("800x550")  # Establece las dimensiones de la ventana
root.resizable(0, 0)  # Hace que la ventana no sea redimensionable

Titulo = tk.Label(root, text="ALGORITMO DE HUFFMAN")  # Crea una etiqueta para el título
Titulo.grid(row=0, column=0, columnspan=6, padx=30, pady=20, sticky="nsew")  # Coloca la etiqueta en la ventana

cadena = tk.Label(root, text="   Cadena: ")  # Crea una etiqueta para la entrada de cadena
cadena.grid(row=1, column=0, padx=10, pady=10, sticky="w")  # Coloca la etiqueta en la ventana
entradaCadena = tk.Text(root, width=80, height=3, wrap=tk.WORD)  # Crea una entrada de texto para la cadena
entradaCadena.grid(row=1, column=1, columnspan=5, padx=5, pady=10, sticky="w")  # Coloca la entrada de texto en la ventana

frecuencia = tk.Label(root, text="   Frecuencia: ")  # Crea una etiqueta para la entrada de frecuencia
frecuencia.grid(row=2, column=0, padx=10, pady=10, sticky="w")  # Coloca la etiqueta en la ventana
entradaFrecuencia = tk.Text(root, width=80, height=8, wrap=tk.WORD)  # Crea una entrada de texto para la frecuencia
entradaFrecuencia.grid(row=2, column=1, columnspan=5, padx=5, pady=10, sticky="w")  # Coloca la entrada de texto en la ventana

arbol = tk.Label(root, text="   Arbol: ")  # Crea una etiqueta para la entrada de árbol
arbol.grid(row=3, column=0, padx=10, pady=10, sticky="w")  # Coloca la etiqueta en la ventana
entradaArbol = tk.Text(root, width=80, height=11, wrap=tk.WORD)  # Crea una entrada de texto para el árbol
entradaArbol.grid(row=3, column=1, columnspan=5, padx=5, pady=10, sticky="w")  # Coloca la entrada de texto en la ventana

app = HuffmanFrontend(root)  # Crea una instancia de la clase HuffmanFrontend
root.mainloop()  # Ejecuta el bucle principal de la aplicación
