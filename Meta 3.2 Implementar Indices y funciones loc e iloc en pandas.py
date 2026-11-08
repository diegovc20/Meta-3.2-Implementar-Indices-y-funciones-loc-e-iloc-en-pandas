# Meta 3.2 Implementar índices y funciones loc e iloc en pandas
# Diego Valle Cuevas
# Grupo: 952
# 07-Noviembre-2026
# Descripción: Seleccionar y modificar ventas usando índices, loc e iloc.

import pandas as pd
import numpy as np


# Crear el DataFrame de ventas de enero, febrero y marzo.
datos = np.random.randint(100, 1001, size=(3, 3))

ventas = pd.DataFrame(
    datos,
    index=["Enero", "Febrero", "Marzo"],
    columns=["A", "B", "C"]
)


# 1. Función para seleccionar ventas usando loc y los nombres de los índices.
def seleccionar_loc(df:pd.DataFrame, meses, productos=None):
    if productos is None:
        seleccion = df.loc[meses, :]
    else:
        seleccion = df.loc[meses, productos]

    return seleccion


# 2. Función para seleccionar ventas usando iloc y las posiciones.
def seleccionar_iloc(df:pd.DataFrame, filas=None, columnas=None):
    if filas is None and columnas is None:
        seleccion = df
    elif filas is None:
        seleccion = df.iloc[:, columnas]
    elif columnas is None:
        seleccion = df.iloc[filas, :]
    else:
        seleccion = df.iloc[filas, columnas]

    return seleccion


# 3. Función para cambiar las ventas de un producto en un mes.
def cambiar_venta(df:pd.DataFrame, mes, producto, nuevo_valor):
    df.loc[mes, producto] = nuevo_valor
    return df


if __name__ == "__main__":
    print("DataFrame original:")
    print(ventas)
    print("=" * 100)

    print("Ventas del producto A en enero:")
    print(seleccionar_loc(ventas, "Enero", "A"))
    print("=" * 100)

    print("Ventas de todos los productos en febrero:")
    print(seleccionar_loc(ventas, "Febrero"))
    print("=" * 100)

    print("Ventas de todos los productos en enero y marzo:")
    print(seleccionar_loc(ventas, ["Enero", "Marzo"]))
    print("=" * 100)

    print("Ventas del primer mes para todos los productos:")
    print(seleccionar_iloc(ventas, filas=0))
    print("=" * 100)

    print("Ventas del segundo producto en todos los meses:")
    print(seleccionar_iloc(ventas, columnas=1))
    print("=" * 100)

    print("Ventas del segundo y tercer mes para el primer producto:")
    print(seleccionar_iloc(ventas, filas=[1, 2], columnas=0))
    print("=" * 100)

    print("Ventas después de cambiar el producto B en marzo a 1200:")
    print(cambiar_venta(ventas, "Marzo", "B", 1200))
