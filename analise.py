import pandas as pd
def calculate_statistics(df: pd.DataFrame):
    media = df["Temperatura"].mean()
    maxima = df["Temperatura"].max()
    minima = df["Temperatura"].min()
    return media, maxima, minima

def analyze_trend(df: pd.DataFrame):
    if df["Temperatura"].iloc[-1] > df["Temperatura"].iloc[0]:
        return "Temperatura Subindo"
    elif df["Temperatura"].iloc[-1] < df["Temperatura"].iloc[0]:
        return "Temperatura Descendo"
    return "Temperatura Estável"

def detect_anomalies(df: pd.DataFrame):
    media = df["Temperatura"].mean()
    desvio = df["Temperatura"].std()
    
    limite_sup = media + 2 * desvio
    limite_inf = media - 2 * desvio
    
    return df [
        (df["Temperatura"] > limite_sup) |
        (df["Temperatura"] < limite_inf)

    ]
    
    