from tkinter import *
from Calculo import *
import numpy as np


calculo1 = Calculo()

#cores da aplicação
corRoxa = "#2F0147" 
corBranca = "#fff"

janela1 = Tk()


janela1.title("Geometria analítica e algebra linear !")
janela1.geometry("400x350")
janela1.config(background=corRoxa)

janela1.iconphoto(False, PhotoImage(file="C:\\Users\\luigi\\OneDrive\\Curso_python\\img\\logo.png"))

texto1 = "Digite as respectivas coordenadas x"

texto2 = "Digite as respectivas coordenadas y"



textoNome = Label(janela1, width=50,height=2,text="Usando o método dos mínimos quadrados com Luigi", font=("Arial 15"),fg=corBranca,bg=corRoxa).pack()
textoNome = Label(janela1, width=50,height=2,text=texto1, font=("Arial 15"),fg=corBranca,bg=corRoxa).pack()
coordX = Entry(janela1,width=10,font=("Arial 15"))
coordX.pack()

textoNome = Label(janela1, width=50,height=2,text=texto2, font=("Arial 15"),fg=corBranca,bg=corRoxa).pack()
coordY = Entry(janela1,width=10,font=("Arial 15"))
coordY.pack()
    


    
        
    
def obter_dado_x():
    # Função chamada quando o botão é pressionado
    coordenadas_X =  coordX.get()
    
    listaCoord_x = coordenadas_X.split(" ")
    listaCoord_x = [float(valor) for valor in listaCoord_x]
    return listaCoord_x 

def obter_dado_y():
    # Função chamada quando o botão é pressionado
    coordenadas_Y =  coordY.get() 
    
    listaCoord_y = coordenadas_Y.split(" ")
    listaCoord_y = [float(valor) for valor in listaCoord_y]
    return listaCoord_y 


def obter_pontos():
    lista_x = obter_dado_x()   
    lista_y = obter_dado_y()
    lista_pontos = list(zip(lista_x, lista_y))
    return lista_pontos

       
       
    
def obter_dado_xEy():
    listaCoord_x = obter_dado_x()
    listaCoord_y = obter_dado_y()
     
    x = np.array([listaCoord_x])
    y = np.array([listaCoord_y])
    a_b = Calculo.calcular_minimos_quadrados(x, y)
    textoNome = Label(janela1, width=50,height=2,text=a_b, font=("Arial 15"),fg=corBranca,bg=corRoxa).pack()
    gerar_plano(a_b)

def gerar_plano(a_b):
    # Função para desenhar uma reta y = a * x + b em um plano cartesiano usando Tkinter
    a = a_b[0]
    b = a_b[1]
    
    pontos = obter_pontos()

    # Criação da janela Tkinter
    root = Tk()
    root.title("Plano Cartesiano")
    root.geometry("400x400")

    # Canvas para desenhar
    canvas = Canvas(root, width=300, height=300, bg="white")
    canvas.pack(padx=20, pady=20)

    # Desenha os eixos x e y
    canvas.create_line(0, 150, 300, 150, width=2, fill="black")  # Eixo x
    canvas.create_line(150, 0, 150, 300, width=2, fill="black")  # Eixo y
    
    # Desenha a reta no canvas
    for x in range(-150, 151):
        y = a * x + b  # Calcula o valor y para cada x
        canvas.create_oval(x + 150, 150 - y, x + 151, 151 - y, outline="blue")
    
    # Desenha os valores nos eixos x e y
    for i in range(-150, 151, 50):
        canvas.create_text(i + 150, 160, text=str(i), anchor="n", fill="black")  # Valores no eixo x
        canvas.create_text(160, 150 - i, text=str(i), anchor="w", fill="black")  # Valores no eixo y
    
    pontos = [
    [10, 20],
    [-30, 40],
    [50, -60],
    [70, 80],
    ]
        
    # Desenha os pontos no canvas
    for ponto in pontos:
        x, y = ponto
        canvas.create_oval(x + 150, 150 - y, x + 151, 151 - y, outline="blue")
        
     

        
    # Inicia o loop principal da interface gráfica
    root.mainloop()
    
# Criar um botão que chama a função obter_dado quando pressionado
botao = Button(janela1, text="Calcular reta", font=("Arial 15"), command=obter_dado_xEy)
botao.pack(pady=10)

def center_window(window, width, height):
# Obter as dimensões da tela
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calcular as coordenadas x e y para centralizar a janela
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Configurar a geometria da janela
    window.geometry(f"{width}x{height}+{x}+{y}")

# Definir as dimensões desejadas da janela
window_width = 400
window_height = 300

# Chamar a função para centralizar a janela
center_window(janela1, window_width, window_height)

janela1.mainloop()
    




