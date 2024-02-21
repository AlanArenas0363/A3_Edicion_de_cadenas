import tkinter as tk
from tkinter import filedialog
import pandas as pd

def algoritmo_modificar(Posicion, Referencia, Alteracion, Cadena):
    Lista_Lista_regresar = []
    cadena_actual = list(Cadena)
    x = 0
    y = 9
    while len(cadena_actual) >= y:
        Cadena_G = cadena_actual.copy()
        Lista_L = []
        for j in range(x, y):
            if j in Posicion and Referencia[Posicion.index(j)] == Cadena_G[j]:
                del Cadena_G[j]
                Cadena_G.insert(j, Alteracion[Posicion.index(j)])
                Lista_L.append(j)
                Lista_L.append(Alteracion[Posicion.index(j)])
        if Cadena_G != cadena_actual:
            Lista_L.insert(0,''.join(Cadena_G))
        x += 5
        y += 5
        if Lista_L:
              Lista_Lista_regresar.append(Lista_L)
    return Lista_Lista_regresar

def abrir_archivo():
    def subir():
        archivo = filedialog.askopenfilename()
        if archivo:
            datos = pd.read_csv(archivo)
            global Posicion, Referencia, Alteracion, String_2
            Posicion = datos['posicion'].tolist()
            Referencia = datos['referencia'].tolist()
            Alteracion = datos['alteracion'].tolist()
            String_2 = datos['string_a_modificar'][0]

    winAbrirArchivo = tk.Tk()
    winAbrirArchivo.title("Actividad 3 - Abrir Archivo")
    winAbrirArchivo.geometry('520x300')

    textCadena1 = tk.Label(winAbrirArchivo, text="Elige tu archivo para abrir (QUE SE LLAME dataset.csv)", font="arial 12 bold")
    textCadena1.place(relx=0.5, rely=0.4, anchor="center")
    boton_abrir_archivo = tk.Button(winAbrirArchivo, text="Abrir archivo", command=subir)
    boton_abrir_archivo.place(relx=0.5, rely=0.6, anchor="center")
    winAbrirArchivo.mainloop()

def ver_cadena():
    winCadena = tk.Tk()
    winCadena.title("Actividad 3 - Cadena de Carácteres")
    winCadena.geometry('520x300')

    textMod1 = tk.Label(winCadena, text="Esta es la cadena de carácteres", font="arial 14 bold")
    textMod1.place(relx=0.5, rely=0.4, anchor="center")
    textMod2 = tk.Label(winCadena, text= String_2, font="arial 11")
    textMod2.place(relx=0.5, rely=0.6, anchor="center")
    winCadena.mainloop()

def cadena_final():
    winCadenaFinal = tk.Tk()
    winCadenaFinal.title("Actividad 3 - Cadena Final")
    winCadenaFinal.geometry('520x300')

    Cadena_Guardada = algoritmo_modificar(Posicion, Referencia, Alteracion, String_2)

    txtCadFin1 = tk.Label(winCadenaFinal, text="Esta es la cadena modificada", font="arial 14 bold")
    txtCadFin1.place(relx=0.5, rely=0.4, anchor="center")
    txtCadFin2 = tk.Label(winCadenaFinal, text= Cadena_Guardada[-1][0], font="arial 11")
    txtCadFin2.place(relx=0.5, rely=0.6, anchor="center")
    winCadenaFinal.mainloop()

def main():
    global Posicion, Referencia, Alteracion, String_2
    Posicion, Referencia, Alteracion, String_2 = [], [], [], ''
    
    ventana = tk.Tk()
    ventana.title("Actividad 3 - Edición de cadenas de carácteres")
    ventana.geometry('520x300')

    # Etiqueta inicial
    texto = tk.Label(ventana, text="Edición de cadenas de carácteres", font="arial 14 bold")
    texto.pack(pady=20)

    texto = tk.Label(ventana, text="¿Que quieres hacer?", font="arial 12")
    texto.pack(padx=20, pady=20)

    # Botones
    boton_abrir_archivo = tk.Button(ventana, text="Abrir Archivo", command=abrir_archivo)
    boton_abrir_archivo.pack(pady=5)

    boton_ver_cadena = tk.Button(ventana, text="Ver cadena", command=ver_cadena)
    boton_ver_cadena.pack(pady=5)

    boton_cadena_final = tk.Button(ventana, text="Cadena Final", command=cadena_final)
    boton_cadena_final.pack(pady=5)

    ventana.mainloop()

if __name__ == "__main__":
    main()
