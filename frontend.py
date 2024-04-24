import tkinter as tk
from tkinter import filedialog
from collections import Counter
from backend import comprimir, descomprimir, construir_arbol_huffman

class HuffmanFrontend:
    def __init__(self, master):
        self.master = master
        self.entradaCadena = entradaCadena
        self.entradaFrecuencia = entradaFrecuencia
        self.entradaArbol = entradaArbol
        master.title("Compresor de Archivos")

        self.examinar_button = tk.Button(master, text="Examinar", command=self.examinar_archivo)
        self.examinar_button.grid(row=4, column=1, padx=(10, 2), pady=20, sticky="ew")


        self.comprimir_button = tk.Button(master, text="Comprimir", command=self.comprimir_archivo, state=tk.DISABLED)
        self.comprimir_button.grid(row=4, column=2, padx=2, pady=20, sticky="ew")

        self.descomprimir_button = tk.Button(master, text="Descomprimir", command=self.descomprimir_archivo, state=tk.DISABLED)
        self.descomprimir_button.grid(row=4, column=3, padx=2, pady=20, sticky="ew")

    def examinar_archivo(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.archivo = file_path
            self.comprimir_button.config(state=tk.NORMAL)
            self.descomprimir_button.config(state=tk.NORMAL)
            with open(self.archivo, 'r') as file:
                contenido = file.read()
                self.entradaCadena.delete('1.0', tk.END)  # Limpiar el campo de entrada
                self.entradaCadena.insert(tk.END, contenido)  # Insertar contenido del archivo
            self.calcular_frecuencia()


    def calcular_frecuencia(self):
        with open(self.archivo, 'r') as file:
            contenido = file.read()
            self.frecuencias = Counter(contenido)
            self.entradaFrecuencia.delete('1.0', tk.END)  # Limpiar el campo de entrada
            for caracter, frecuencia in self.frecuencias.items():
                self.entradaFrecuencia.insert(tk.END, f"{caracter}: {frecuencia}\n")  # Insertar frecuencia
        self.mostrar_arbol_huffman()


    def mostrar_arbol_huffman(self):
        arbol_huffman = construir_arbol_huffman(self.frecuencias)
        self.entradaArbol.delete('1.0', tk.END)  # Limpiar el campo de entrada
        self.dibujar_arbol(arbol_huffman)


    def dibujar_arbol(self, nodo, nivel=0):
        if nodo:
            self.entradaArbol.insert(tk.END, "    " * nivel)
            self.entradaArbol.insert(tk.END, f"({nodo.frecuencia})\n")
            self.dibujar_arbol(nodo.izquierda, nivel + 1)
            self.dibujar_arbol(nodo.derecha, nivel + 1)

    def comprimir_archivo(self):
        output_file = self.archivo + '.huf'
        tabla_codigos = comprimir(self.archivo, output_file)
        print("Archivo comprimido correctamente.")

    def descomprimir_archivo(self):
        if self.archivo.endswith('.huf'):
            output_file = self.archivo[:-4]  # Eliminar la extensión .huf
            descomprimir(self.archivo, output_file)
            print("Archivo descomprimido correctamente.")
        else:
            print("El archivo seleccionado no es un archivo comprimido.")

root = tk.Tk()
root.title("Algoritmo de Huffman")
root.geometry("800x550")
root.resizable(0, 0)

Titulo = tk.Label(root, text="ALGORITMO DE HUFFMAN")
Titulo.grid(row=0, column=0, columnspan=6, padx=30, pady=20, sticky="nsew")

cadena = tk.Label(root, text="   Cadena: ")
cadena.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entradaCadena = tk.Text(root, width=80, height=3, wrap=tk.WORD)  # Ajustar el ancho y alto del widget entradaCadena
entradaCadena.grid(row=1, column=1, columnspan=5, padx=5, pady=10, sticky="w")

frecuencia = tk.Label(root, text="   Frecuencia: ")
frecuencia.grid(row=2, column=0, padx=10, pady=10, sticky="w")
entradaFrecuencia = tk.Text(root, width=80, height=8, wrap=tk.WORD)  # Ajustar el ancho y alto del widget entradaCadena
entradaFrecuencia.grid(row=2, column=1, columnspan=5, padx=5, pady=10, sticky="w")

arbol = tk.Label(root, text="   Arbol: ")
arbol.grid(row=3, column=0, padx=10, pady=10, sticky="w")
entradaArbol = tk.Text(root, width=80, height=11, wrap=tk.WORD)  # Ajustar el ancho y alto del widget entradaCadena
entradaArbol.grid(row=3, column=1, columnspan=5, padx=5, pady=10, sticky="w")


app = HuffmanFrontend(root)
root.mainloop()
