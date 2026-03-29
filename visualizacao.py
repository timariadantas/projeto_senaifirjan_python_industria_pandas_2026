import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="darkgrid")
def generate_graph(df, limite, tendencia=None):
    plt.figure(figsize=(8,5))
    
    sns.lineplot(
        x=range(len(df)),
        y=df["Temperatura"],
        marker="o")
    
    plt.axhline(y=limite,
                color="red", 
                linestyle="--",
                label=f"Limite {limite}°C")
    
       # Título com a tendência
    title = "Monitoramento de Temperatura"
    if tendencia:
        title += f" - Tendência: {tendencia}"
    plt.title(title)
    
    plt.xlabel("Leitura")
    plt.ylabel("Temperatura")
    plt.legend()
    plt.tight_layout()
   
    plt.savefig("grafico.png")
    plt.show()
