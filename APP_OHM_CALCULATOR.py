import tkinter as tk
from tkinter import font

def FIN():
    Ventana1.destroy()
    MainWindow()
    
def CalculoV():
    GUI.destroy()
    global Ventana1
    global textbox1
    global textbox2
    global textbox3
    Ventana1 = tk.Tk()
    Ventana1.title("ProgramacionCreativa en TikTok")
    Ventana1.geometry("500x400")
    Ventana1.config(background="light blue")
    mi_fuente = font.Font(family="Tahoma", size=16, weight="bold")
    titulo = tk.Label(text = "CALCULADORA PYTHON LEY DE OHM",
                    font = mi_fuente, bg = "black", fg = "white",
                    width="38", height="2")
    titulo.place(x=0, y=0)
    etiqueta1 = tk.Label(text = "Resistencia: ", font=("Arial",15) , bg = "orange", 
                         fg = "black", width="10", height="1")
    etiqueta1.place(x=100, y=100)
    textbox1 = tk.Entry(Ventana1, font="Helvetica 11", width=10 )
    textbox1.place(x=230, y=105)
    etiqueta2 = tk.Label(text = "Corriente: ", font=("Arial",15) , bg = "orange", 
                         fg = "black", width="10", height="1")
    etiqueta2.place(x=100, y=150)
    textbox2 = tk.Entry(Ventana1, font="Helvetica 11", width=10 )
    textbox2.place(x=230, y=155)
    calcular = tk.Button(Ventana1,text="Calcular", font="Arial" ,width=12, height=1, 
                       borderwidth=7, command=captura_de_boxtext_1, bg="#F1F55A")
    calcular.place(x=205, y=200)
    salir = tk.Button(Ventana1,text="Salir", font="Arial" ,width=12, height=1, 
                       borderwidth=7,command=FIN, bg="#F1F55A")
    salir.place(x=205, y=310) 
    etiqueta3 = tk.Label(text = "El Voltaje es: ", font=("Arial",14) , bg = "yellow", 
                         fg = "black", width="12", height="1")
    etiqueta3.place(x=80, y=260)
    textbox3 = tk.Entry(Ventana1, font="Helvetica 11", width=10 )
    textbox3.place(x=230, y=265)
    Ventana1.mainloop() 

def CalculoI():
    GUI.destroy()
    global Ventana1
    global textbox1
    global textbox2
    global textbox3
    global textbox4
    Ventana1 = tk.Tk()
    Ventana1.title("ProgramacionCreativa en TikTok")
    Ventana1.geometry("500x400")
    Ventana1.config(background="light blue")
    mi_fuente = font.Font(family="Tahoma", size=16, weight="bold")
    titulo = tk.Label(text = "CALCULADORA PYTHON LEY DE OHM",
                    font = mi_fuente, bg = "black", fg = "white",
                    width="38", height="2")
    titulo.place(x=0, y=0) 
    etiqueta1 = tk.Label(text = "Voltaje: ", font=("Arial",15) , bg = "orange", 
                         fg = "black", width="10", height="1")
    etiqueta1.place(x=100, y=100)
    textbox1 = tk.Entry(Ventana1, font="Helvetica 11", width=10 )
    textbox1.place(x=230, y=105)
    etiqueta2 = tk.Label(text = "Resistencia: ", font=("Arial",15) , bg = "orange", 
                         fg = "black", width="10", height="1")
    etiqueta2.place(x=100, y=150)
    textbox2 = tk.Entry(Ventana1, font="Helvetica 11", width=10 )
    textbox2.place(x=230, y=155)
    calcular = tk.Button(Ventana1,text="Calcular", font="Arial" ,width=12, height=1, 
                       borderwidth=7, command=captura_de_boxtext_2, bg="#4AF50B")
    calcular.place(x=205, y=200)
    salir = tk.Button(Ventana1,text="Salir", font="Arial" ,width=12, height=1, 
                       borderwidth=7,command=FIN, bg="#4AF50B")
    salir.place(x=205, y=310) 
    etiqueta3 = tk.Label(text = "La Corriente es: ", font=("Arial",14) , bg = "yellow", 
                         fg = "black", width="13", height="1")
    etiqueta3.place(x=78, y=260)
    textbox3 = tk.Entry(Ventana1, font="Helvetica 11", width=10 )
    textbox3.place(x=231, y=265)
    textbox4 = tk.Entry(Ventana1, font="Helvetica 11", width=10 )
    textbox4.place(x=321, y=265)
    
def CalculoR():
    GUI.destroy()
    global Ventana1
    global textbox1
    global textbox2
    global textbox3
    global textbox4
    global textbox5
    global textbox6
    global textbox7
    Ventana1 = tk.Tk()
    Ventana1.title("ProgramacionCreativa en TikTok")
    Ventana1.geometry("500x450")
    Ventana1.config(background="light blue")
    mi_fuente = font.Font(family="Tahoma", size=16, weight="bold")
    titulo = tk.Label(text = "CALCULADORA PYTHON LEY DE OHM",
                    font = mi_fuente, bg = "black", fg = "white",
                    width="38", height="2")
    titulo.place(x=0, y=0)  
    etiqueta1 = tk.Label(text = "Voltaje: ", font=("Arial",15) , bg = "orange", 
                         fg = "black", width="10", height="1")
    etiqueta1.place(x=100, y=100)
    textbox1 = tk.Entry(Ventana1, font="Helvetica 11", width=10 )
    textbox1.place(x=230, y=105)
    etiqueta2 = tk.Label(text = "Corriente: ", font=("Arial",15) , bg = "orange", 
                         fg = "black", width="10", height="1")
    etiqueta2.place(x=100, y=150)
    textbox2 = tk.Entry(Ventana1, font="Helvetica 11", width=10 )
    textbox2.place(x=230, y=155)
    calcular = tk.Button(Ventana1,text="Calcular", font="Arial" ,width=12, height=1, 
                       borderwidth=7, command=captura_de_boxtext_3, bg="#0BF5B9")
    calcular.place(x=205, y=200)
    etiqueta3 = tk.Label(text = "La Resistencia es: ", font=("Arial",14) , bg = "yellow", 
                         fg = "black", width="14", height="1")
    etiqueta3.place(x=67, y=260)
    textbox3 = tk.Entry(Ventana1, font="Helvetica 11", width=10 )
    textbox3.place(x=230, y=265) 
    textbox4 = tk.Entry(Ventana1, font="Helvetica 11", width=10 )
    textbox4.place(x=320, y=265) 
    etiqueta4 = tk.Label(text = "La Potencia Disipada en R: ", font=("Arial",14) , bg = "yellow", 
                         fg = "black", width="21", height="1")
    etiqueta4.place(x=30, y=305)
    textbox5 = tk.Entry(Ventana1, font="Helvetica 11", width=10 )
    textbox5.place(x=271, y=310) 
    textbox6 = tk.Entry(Ventana1, font="Helvetica 11", width=10 )
    textbox6.place(x=360, y=310) 
    etiqueta5 = tk.Label(text = "Debes Usar una Resistencia De: ", font=("Arial",14) , bg = "yellow", 
                         fg = "black", width="25", height="1")
    etiqueta5.place(x=30, y=350)
    textbox7 = tk.Entry(Ventana1, font="Helvetica 11", width=10 )
    textbox7.place(x=315, y=354) 
    salir = tk.Button(Ventana1,text="Salir", font="Arial" ,width=12, height=1, 
                       borderwidth=7,command=FIN, bg="#0BF5B9")
    salir.place(x=205, y=400) 
    
def CalculoP():
    GUI.destroy()
    global Ventana1
    global textbox1
    global textbox2
    global textbox3
    global textbox4
    Ventana1 = tk.Tk()
    Ventana1.title("ProgramacionCreativa en TikTok")
    Ventana1.geometry("500x400")
    Ventana1.config(background="light blue")
    mi_fuente = font.Font(family="Tahoma", size=16, weight="bold")
    titulo = tk.Label(text = "CALCULADORA PYTHON LEY DE OHM",
                    font = mi_fuente, bg = "black", fg = "white",
                    width="38", height="2")
    titulo.place(x=0, y=0) 
    etiqueta1 = tk.Label(text = "Voltaje: ", font=("Arial",15) , bg = "orange", 
                         fg = "black", width="10", height="1")
    etiqueta1.place(x=100, y=100)
    textbox1 = tk.Entry(Ventana1, font="Helvetica 11", width=10 )
    textbox1.place(x=230, y=105)
    etiqueta2 = tk.Label(text = "Corriente: ", font=("Arial",15) , bg = "orange", 
                         fg = "black", width="10", height="1")
    etiqueta2.place(x=100, y=150)
    textbox2 = tk.Entry(Ventana1, font="Helvetica 11", width=10 )
    textbox2.place(x=230, y=155)
    calcular = tk.Button(Ventana1,text="Calcular", font="Arial" ,width=12, height=1, 
                       borderwidth=7, command=captura_de_boxtext_4, bg="#EA7171")
    calcular.place(x=205, y=200)
    salir = tk.Button(Ventana1,text="Salir", font="Arial" ,width=12, height=1, 
                       borderwidth=7,command=FIN, bg="#EA7171")
    salir.place(x=205, y=310) 
    etiqueta3 = tk.Label(text = "La Potencia es: ", font=("Arial",14) , bg = "yellow", 
                         fg = "black", width="12", height="1")
    etiqueta3.place(x=80, y=260)
    textbox3 = tk.Entry(Ventana1, font="Helvetica 11", width=10 )
    textbox3.place(x=230, y=265)
    textbox4 = tk.Entry(Ventana1, font="Helvetica 11", width=10 )
    textbox4.place(x=320, y=265)

def captura_de_boxtext_1():
    box_1 = textbox1.get()
    box_2 = textbox2.get()
    if 'k' in box_1:
        R_con_K = box_1.replace('k', '')
        R_int = float(R_con_K)
        R_int = R_int*1000
    else:
        R_int = int(box_1)
    if 'm' in box_2:
        I_con_m = box_2.replace('m','')
        I_int = float(I_con_m)
        I_int = I_int/1000
    else:
        I_int = float(box_2)
    V = R_int * I_int
    #salida
    textbox3.delete(0,tk.END)
    textbox3.insert(0,round(V,3))
    textbox3.insert(7,"V")
    
def captura_de_boxtext_2():
    box_1 = textbox1.get()
    box_2 = textbox2.get()
    if 'k' in box_2:
        R_con_K = box_2.replace('k', '')
        R_int = float(R_con_K)
        R_int = R_int*1000
    else:
        R_int = int(box_2)
    V = int(box_1)
    I = V / R_int
    #Output
    textbox3.delete(0,tk.END)
    textbox3.insert(0,round(I,3))
    textbox3.insert(7,"A")
    I = I*1000
    textbox4.delete(0,tk.END)
    textbox4.insert(0,round(I,3))
    textbox4.insert(7,"mA")

def captura_de_boxtext_3():
    box_1 = textbox1.get()
    box_2 = textbox2.get()
    if 'm' in box_2:
        I_con_m = box_2.replace('m','')
        I_int = float(I_con_m)
        I_int = I_int/1000
    else:
        I_int = float(box_2)
    V = float(box_1)
    R = V / I_int
    R_aux = R
    #salida
    textbox3.delete(0,tk.END)
    textbox3.insert(0,round(R,3))
    textbox3.insert(7,"Ω")
    R = R/1000 
    textbox4.delete(0,tk.END)
    textbox4.insert(0,round(R,3))
    textbox4.insert(7,"KΩ")
    P = (I_int**2)*R_aux
    if P <= 0.125:
        P_int = P
        vatios = "1/8"
    elif P <= 0.25:
        P_int = P
        vatios = "1/4"
    elif P <= 0.5:
        P_int = P
        vatios = "1/2"
    elif P <= 1:
        P_int = P
        vatios = "1"
    print("-----------------------------------")
    print(f"La Potencia en la Resistencia es de ==> {round(P_int,2)} W") 
    textbox5.delete(0,tk.END)
    textbox5.insert(0,round(P_int,3))
    textbox5.insert(7,"W")
    P = P*1000
    print(f"La Potencia es ==> {round(P,3)} mW")
    print("...................................")
    textbox6.delete(0,tk.END)
    textbox6.insert(0,round(P,3))
    textbox6.insert(7,"mW")
    print(f"Debes de usar una Resistencia de *{vatios}* de vatio") 
    print("-----------------------------------")
    if(vatios=="1/4" or vatios=="1/8"):
        textbox7.delete(0,tk.END)
        textbox7.insert(0,vatios)
        textbox7.insert(5," de Vatio")
    else:
        textbox7.delete(0,tk.END)
        textbox7.insert(0,vatios)
        textbox7.insert(5," Vatio")

def captura_de_boxtext_4():
    box_1 = textbox1.get()
    box_2 = textbox2.get()
    if 'm' in box_2:
        I_con_m = box_2.replace('m','')
        I_int = float(I_con_m)
        I_int = I_int/1000
    else:
        I_int = float(box_2)
    V = float(box_1)
    P = V * I_int
    #salida
    textbox3.delete(0,tk.END)
    textbox3.insert(0,round(P,3))
    textbox3.insert(7,"W")
    P = P*1000
    textbox4.delete(0,tk.END)
    textbox4.insert(0,round(P,3))
    textbox4.insert(7,"mW")

def MainWindow():
    global GUI 
    GUI = tk.Tk() 
    GUI.title("ProgramacionCreativa en TikTok")
    GUI.geometry("500x400")
    GUI.config(background="light blue")
    mi_fuente = font.Font(family="Tahoma", size=16, weight="bold")
    titulo = tk.Label(text = "CALCULADORA PYTHON LEY DE OHM",
                    font = mi_fuente, bg = "black", fg = "white",
                    width="38", height="2")
    titulo.place(x=0, y=0)
    boton1 = tk.Button(GUI,text="VOLTAJE", font="Arial" ,width=15, height=2, 
                       command=CalculoV, borderwidth=6, bg="#F1F55A")
    boton1.place(x=190, y=90)
    boton2 = tk.Button(GUI,text="CORRIENTE", font="Arial" ,width=15, height=2, 
                       command=CalculoI, borderwidth=6, bg="#4AF50B")
    boton2.place(x=190, y=160)
    boton3 = tk.Button(GUI,text="RESISTENCIA", font="Arial", width=15, height=2, 
                       command=CalculoR, borderwidth=6, bg="#0BF5B9")
    boton3.place(x=190, y=230)
    boton3 = tk.Button(GUI,text="POTENCIA", font="Arial", width=15, height=2, 
                       command=CalculoP, borderwidth=6, bg="#EA7171") 
    boton3.place(x=190, y=300)
    
MainWindow()
GUI.mainloop()