import pandas as pd
import numpy as np

serie_amigos = ["Ramses", "Arthur", "Sebastian", "El Luis", "Eliseo", "Iram", "Alonso"]
print("--- Serie listado de amigos NC = 0079 ---")
amigos = pd.Series(serie_amigos)
print(amigos)

serie_billetes = [20, 50, 100, 200, 500, 1000]
print("--- Serie listado de billetes MX NC = 0079 ---")
billetes = pd.Series(serie_billetes)
print(billetes)

serie_billetes = [20, 50, 100, 200, 500, 1000]
serie_letras = ["Veinte", "Cincuenta", "Cien", "Doscientos", "Quinientos", "Mil"]
print("--- Serie listado, nombre y valor de billetes MX NC = 0079 ---")
tablabilletes = pd.Series(serie_billetes, serie_letras)
print(tablabilletes)
# Diccionario DataFrame
#Diccionario monedas valor y nombre
print("--- Datos de diccionario a Data Frame en Pandas ---")
dicc_monedas = {
    "serie_billetes" : [20, 50, 100, 200, 500, 1000],
    "serie_letras" : ["Veinte", "Cincuenta", "Cien", "Doscientos", "Quinientos", "Mil"]
}
tablabilletes = pd.DataFrame(dicc_monedas, index = ["A", "B", "C", "D", "E", "F"])
print(tablabilletes)
print("Casa de cambio de Iram Jimenez NC = 0079")