import numpy as np
import matplotlib.pyplot as plt

class Calculo():   
    def __init__(self) -> None:
          print("objeto gerado !")    
          
    # Dados de exemplo
#     x = np.array([1, 2, 3, 4, 5])
#     y = np.array([2, 3, 5, 4, 5])

    # Função para calcular os coeficientes da reta de melhor ajuste
    @staticmethod
    def calcular_minimos_quadrados(x, y):
            n = len(x)
            soma_x = np.sum(x)
            soma_y = np.sum(y)
            soma_x_squared = np.sum(x**2)
            soma_xy = np.sum(x * y)

            # Calcula os coeficientes da reta de melhor ajuste (a e b)
            a = (n * soma_xy - soma_x * soma_y) / (n * soma_x_squared - soma_x**2)
            b = (soma_y - a * soma_x) / n

            # Cria a reta de melhor ajuste
            coeficientes = [a,b]

            return coeficientes


        