import pandas as pd
import matplotlib.pyplot as plt
import os

# Definición de rutas relativas para garantizar la reproducibilidad
DATA_PATH = "datos/dataset.csv"
OUTPUT_PATH = "resultados/grafico_resultados.png"

def procesar_datos():
    # Cargar datos meteorológicos
    if not os.path.exists(DATA_PATH):
        print(f"Error: No se encuentra el archivo en {DATA_PATH}")
        return
        
    df = pd.read_csv(DATA_PATH)
    
    # Calcular métricas e indicadores requeridos
    # Asumiendo columnas estándar del dataset de DataHub ('Mean')
    temp_promedio = df['Mean'].mean()
    temp_maxima = df['Mean'].max()
    temp_minima = df['Mean'].min()
    
    print(f"--- Indicadores Climáticos Calculados ---")
    print(f"Temperatura Promedio Historica: {temp_promedio:.2f}")
    print(f"Temperatura Maxima Registrada: {temp_maxima:.2f}")
    print(f"Temperatura Minima Registrada: {temp_minima:.2f}")
    
    # Generar gráfico evolutivo de la temperatura
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df['Mean'], color='orange', label='Anomalia de Temp')
    plt.title("Evolucion de la Temperatura en el Tiempo")
    plt.xlabel("Registros Historicos (Mensuales/Anuales)")
    plt.ylabel("Desviacion de Temperatura")
    plt.legend()
    plt.grid(True)
    
    # Guardar productos en la carpeta resultados
    plt.savefig(OUTPUT_PATH)
    plt.close()
    print(f"Grafico guardado exitosamente en: {OUTPUT_PATH}")

if __name__ == "__main__":
    procesar_datos()
