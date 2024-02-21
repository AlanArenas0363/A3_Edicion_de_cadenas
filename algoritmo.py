import pandas as pd

datos = pd.read_csv('dataset.csv')

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


Posicion = datos['posicion'].tolist()
Referencia = datos['referencia'].tolist()
Alteracion = datos['alteracion'].tolist()
String = datos['string_a_modificar']

String_2 = String[0]

Cadena_Guardada = algoritmo_modificar(Posicion, Referencia, Alteracion, String_2)

df = pd.DataFrame({'Cadena_Modificada': Cadena_Guardada})

df.to_csv('cadenas_modificadas.csv', index=False)