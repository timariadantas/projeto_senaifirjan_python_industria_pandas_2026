import pandas as pd

def read_temperature():
    entrada = input("Digite as temperaturas: ")
    lista = list(map(float, entrada.split()))
    return pd.DataFrame(lista, columns=["Temperatura"])

def read_limit():
    return float(input("Digite o limite: "))
