import numpy as np
import matplotlib.pyplot as plt

# Parámetros del proyecto
inversion_inicial:int = 10_000  # Inversión inicial en dólares
tasa_retorno_esperada:float = 0.08  # Tasa de retorno anual esperada 
desviacion_estandar:float = 0.15  # Desviación estándar de la tasa de retorno
num_periodos:int = 8  # Número de períodos (años)
num_simulaciones:int = 10_000  # Número de simulaciones

# Simulaciones de Monte Carlo
valores_finales:list = []

for i in range(num_simulaciones):
    valor:int = inversion_inicial
    for i in range(num_periodos):
        retorno = np.random.normal(tasa_retorno_esperada, desviacion_estandar)
        valor *= (1 + retorno)
    valores_finales.append(valor)

# Análisis de resultados
valores_finales = np.array(valores_finales)
valor_medio = np.mean(valores_finales)
desviacion_estandar_final = np.std(valores_finales)
percentil_5 = np.percentile(valores_finales, 5)
percentil_95 = np.percentile(valores_finales, 95)


def main() -> None:
  print('>>> El programa ha iniciado.')
  print(f"Valor medio final: ${valor_medio:,.2f}")
  print(f"Desviación estándar del valor final: ${desviacion_estandar_final:,.2f}")
  print(f"Percentil 5 del valor final: ${percentil_5:,.2f}")
  print(f"Percentil 95 del valor final: ${percentil_95:,.2f}")
  
  y1,y2,y3,y4 = np.random.randn(100).cumsum(), np.random.randn(100).cumsum(), np.random.randn(100).cumsum(), np.random.randn(100).cumsum()
  lg = plt.subplot()
  lg.plot(y1, label=f"Valor medio final: ${valor_medio:,.2f}", color='r')
  lg.plot(y2, label=f"Desviación estándar del valor final: ${desviacion_estandar_final:,.2f}", color='b')
  lg.plot(y3, label=f"Percentil 5 del valor final: ${percentil_5:,.2f}", color='g') 
  lg.plot(y4, label=f"Percentil 95 del valor final: ${percentil_95:,.2f}", color='y')
  lg.legend(loc='upper right') 
  lg.legend()
  # Graficar los resultados
  plt.hist(valores_finales, bins=50, edgecolor='k', alpha=0.75)
  plt.title('Distribución del Valor Final del Proyecto')
  plt.xlabel('Valor Final ($)')
  plt.ylabel('Frecuencia')
  plt.axvline(valor_medio, color='r', linestyle='dashed', linewidth=1)
  plt.show()
  print('>>> El programa ha finalizado.')
 
if __name__ == '__main__':
  main()
