from entrada import read_temperature, read_limit
from analise import calculate_statistics, analyze_trend, detect_anomalies
from visualizacao import generate_graph


def main():
    df = read_temperature()
    limite = read_limit()
    
    media, maxima, minima = calculate_statistics(df)
    
    print(f"Media: {media:.2f}")
    print(f"Maxima: {maxima:.2f}")
    print(f"Minima: {minima:.2f}")
    
    if maxima > limite:
        print("ALERTA: risco de superaquecimento!")
    else:
        print("Status: Operação Normal.")
        print("Tendência:", analyze_trend(df))
    
    anomalias = detect_anomalies(df)
    print("Anomalias:\n", anomalias if not anomalias.empty else "Nenhuma")
    
    
    generate_graph(df, limite)
    
if __name__ == "__main__":
    main()
