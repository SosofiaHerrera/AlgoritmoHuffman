![This is a alt text.](./banners.png "This is a sample image.")

# Algoritmo de Huffman

## Introducción

En el ámbito digital actual, la compresión de archivos es esencial para optimizar el almacenamiento y la transmisión de datos. Uno de los algoritmos más utilizados para este propósito es el algoritmo de Huffman, desarrollado por David A. Huffman en 1952. Este algoritmo asigna códigos de longitud variable a los caracteres del archivo original, de manera que los caracteres más frecuentes tengan códigos más cortos, lo que resulta en una compresión eficiente.

## Objetivo

El objetivo de este proyecto es desarrollar un compresor de archivos que utilice el algoritmo de Huffman para comprimir y descomprimir archivos de manera eficiente. Se busca proporcionar una interfaz de usuario intuitiva para que los usuarios puedan comprimir y descomprimir archivos de forma sencilla, así como implementar el algoritmo de Huffman en el backend para garantizar una compresión y descompresión precisas.

## Desarrolo

El desarrollo del compresor de archivos con el algoritmo de Huffman consta de dos partes principales: el frontend y el backend.

### Frontend

El frontend del compresor de archivos es responsable de la interfaz de usuario y la interacción con el usuario. Está desarrollado utilizando la biblioteca Tkinter de Python, que proporciona herramientas para crear interfaces gráficas de usuario (GUI). En el frontend, los usuarios pueden seleccionar un archivo para comprimir o descomprimir utilizando un explorador de archivos. Una vez seleccionado el archivo, se muestra la frecuencia de cada carácter en el archivo, así como una representación gráfica del árbol de Huffman correspondiente. Además, los usuarios pueden iniciar el proceso de compresión o descompresión con los botones correspondientes.

### Backend

El backend del compresor de archivos implementa la lógica del algoritmo de Huffman para comprimir y descomprimir archivos. Está desarrollado utilizando funciones y clases de Python. Las operaciones principales del backend incluyen la construcción del árbol de Huffman a partir de las frecuencias de los caracteres, la generación de la tabla de códigos Huffman, la compresión del archivo original utilizando los códigos Huffman generados y la descompresión del archivo comprimido utilizando la tabla de códigos Huffman y el árbol de Huffman.

## Conclusiones

El algoritmo de Huffman y su implementación en un compresor de archivos proporcionan una solución efectiva para la optimización del almacenamiento y la transmisión de datos en aplicaciones informáticas y de comunicación. El compresor de archivos desarrollado en este proyecto ofrece una interfaz gráfica intuitiva para los usuarios, facilitando la compresión y descompresión de archivos de manera rápida y sencilla. Además, la implementación del algoritmo de Huffman en el backend garantiza una compresión eficiente y una descompresión precisa de los archivos.

## Referencias

* Anonimo. (Sin fecha). Algoritmo de Huffman: https://joselu.webs.uvigo.es/material/Algoritmo%20de%20Huffman.pdf
* Sznajdleder, Pablo A. (Sin fecha). Algoritmos a fondo: https://libroweb.alfaomega.com.mx/book/393/free/data/Capitulos/cap16.pdf
