import dataclasses
from tkinter import *
from datetime import datetime
import os
from PIL import *
import googlemaps
import requests
from math import pi, log10
import PIL

#from webbrowser import *
#from requests import *


#Configurações Visuais:
app =Tk()
app.title("APP 5G")
app.iconbitmap('F:/Users/SAMUEL/Documents/MeusProjetos/5G/Python Files/radio-tower.ico')
app.geometry("1280x680")
app.configure(background="#118")
lam2 =0
pt2=0
pr2=0
gt2=0
gr2=0
d2=0
pr2=0
pr=0
a= 0
ppr2 = 0
da2= 0
do2= 0
center2=0
lugar2= 0
beta = 2
global r
global f
global imgLogo1
global l_logo1
r = 0
f = 0
imgLogo1 = 0
l_logo1 = 0

#center2 = 'Arena Fonte Nova'    #str(lugar2)
#center2 = str(lugar2)
#print(center2)
        
              
#Background do app:
pastaApp=os.path.dirname(__file__)
imgLogo = PhotoImage(file=pastaApp+"\\5G_background.gif")
l_logo=Label(app,image=imgLogo)
l_logo.place(x=0,y=0)

#Horário:
data = datetime.now()
data = str(data)

# API do Google Maps:
#api_key = "AIzaSyDcz_OKnoD8j0n-a_3AyipLXOb6ZyqFI-0"

# url variable store url
#url = "https://maps.googleapis.com/maps/api/staticmap?"

# zoom defines the zoom
# level of the map

#center ="Arena Fonte Nova, Salvador,Bahia"  #Quero que o valor digitado em center = entry( ), vá para uma variavel x e que center é iguala a x.



"""
class Tela:
    def __init__(self,master):
        self.nossaTela = master
        
        img = Image.open("F:/Users/SAMUEL/Documents/MeusProjetos/5G/Python Files/5G_background.jpeg")
        self.minhaImagem = ImageTk.PhotoImage(img)
        self.lbl = tk.Label (self.nossaTela, image = self.minhaImagem)
        self.lbl.pack()
"""
"""
my_img = Image.open('F:/Users/SAMUEL/Documents/MeusProjetos/5G/Python Files/II.jpeg')
my_label = Label(image = my_img)
my_label.pack()
"""

""""
#API do Google Maps:
googlemaps = googlemaps.Client(key= "AIzaSyDcz_OKnoD8j0n-a_3AyipLXOb6ZyqFI-0")
geocode_result = googlemaps.geocode(lugar)
"""

#Título de apresentação:
txt1 = Label(app, text = "Bem-vindo a interface", background="#ff0", foreground= "#000")
#txt1.grid(row= 5, column= 5) # Colocando o objeto por linhas e colunas.
txt1.place(x=10,y=10,width=150, height=30) #Colocando o objeto por coodernadas
txt2 = Label(app, text = "Calculo da pontência recebida em um ponto de referência:", background="#ff0", foreground= "#000").place(x=10,y=320,width=320, height=30)

#txt2 = Label(app, text = data, background="#ff0", foreground= "#000" )
#txt2.place(x=160,y=10,width=150, height=30)

#Arquivo Criado para escrita dos dados:
c = os.path.dirname(__file__)
nomeArquivo=c+"Dados.txt"


#Definiões:

def get(self):
     """Return the text."""

def sair():
    quit()


def impdados(lam, pt, gt, gr,d ,lugar, nomeArquivo):
    #print(f'O valor {lugar}')
    print("Horário: ", data)
    print(f"\nComprimento de Onda: {lam.get()} m")
    print(f"Potência da antena:   {pt.get()} W" )
    print(f"Ganho da antena de Transmissão:   {gt.get()} dBi")
    print(f"Ganho da antena de Recepção:   {gr.get()} dBi")
    print(f"Distância a ser alcançada:   {d.get()} m")
    print(f"Lugar: {lugar.get()}" )
    #print(lugar.get())
    
    
    lam2 = float(lam.get())
    pt2 = float(pt.get())
    gt2 = float(gt.get())
    gr2 = float(gr.get())
    d2 = float(d.get())
    lugar2 = lugar.get()
    center2 = str(lugar.get())
    #print(f"O valor de LUGAR2 é: ",lugar2)
    pr = (pt2*gt2*gr2*lam2**2)/(((4*pi**2))*(d2**2))
    #Atenuação no espaço livre (admensional)
    l = ((4*pi)**2*d2**2)/(lam2**2)
    #Quando em Log(dB)
    lb = log10(l)
    
    
    
    print("Potência recebida: ",pr,"W")
    print("Atenuação no espaço livre (dB): ", lb)
    a = Label(app, text ="Potência recebida(W): ",background="#ff0",foreground= "#000", anchor= W).place(x=10,y=230,width=125,height=20)
    b = Label(app, text = pr,background="white",foreground= "#000", anchor= W).place(x=140,y=230,width=110,height=20)
    c = Label(app, text ="Atenuação no espaço livre (dB): ",background="#ff0",foreground= "#000", anchor= W).place(x=10,y=260,width=170,height=20)
    d = Label(app, text = lb,background="white",foreground= "#000", anchor= W).place(x=185,y=260,width=110,height=20)
    """
    r = requests.get(url + "&size=250x250&center="+str(center2)+
                        "&zoom="+str(zoom)+"&maptype=satellite&key="+api_key)
    print(url + "&size=250x250&center="+str(center2)+
                        "&zoom="+str(zoom)+"&maptype=satellite&key="+api_key)
    
    
    f = open('F:/Users/SAMUEL/Documents/MeusProjetos/5G/Python Files/II.gif', 'wb')
    
    pastaApp=os.path.dirname(__file__)
    imgLogo1 = PhotoImage(file=pastaApp+"\\II.gif")
    l_logo1=Label(app,image=imgLogo1)
    l_logo1.place(x=900,y=400)
    
    f.write(r.content)
    f.close()
    """

    
    
    
 
def calculo_potencia_ponto_referencia(da,do,ppr):
    print("Horário: ", data)
    print(f"Distância almejada: {da.get()} m")
    print(f"Distância do ponto de referência:   {do.get()} m" )
    print(f"Potência no ponto de referência:  {ppr.get()} W")
    da2 = float(da.get())
    do2 = float(do.get())
    ppr2 = float(ppr.get())
    
    pr = (ppr2*pow(do2,beta))/(pow(da2,beta)) #Pontência recebida em um ponto de referencia
    print("A potência do sinal recebido no ponto de referência é: ", pr, "W")
    d1 = da2/do2
    lb = -10*beta*log10(d1) #Convertidas em dB
    print("Medida convertida para dB:", lb, "dB")
    
    #da = Distância almejada
    #do = Distânica do ponto de referência
    #ppr = Potência no ponto de referência 
    
    a = Label(app, text ="Potência recebida no sinal de referência(W): ",background="#ff0",foreground= "#000", anchor= W).place(x=10,y=450,width=240,height=20)
    b = Label(app, text = pr ,background="white",foreground= "#000", anchor= W).place(x=255,y=450,width=110,height=20)
    c = Label(app, text ="Medida convertida para (dB): ",background="#ff0",foreground= "#000", anchor= W).place(x=10,y=480,width=160,height=20)
    d = Label(app, text = lb ,background="white",foreground= "#000", anchor= W).place(x=175,y=480,width=110,height=20)

      
"""
vtxt="Opções"
vbg="#ff0"
vfg="#000"
txt2=Label(app, text=vtxt, bg=vbg, fg=vfg)
txt2.pack(ipadx=10,ipady=10,padx=90,pady=90,side="top",fill=X,expand=True)


"""

def salvardados():
    arquivo=open(nomeArquivo,"a")
    arquivo.write(data)
    arquivo.write(f"\nFrequência: {vf.get()}")
    arquivo.write( f"\nPotência:   {vp.get()}")
    arquivo.write(f"\nLargura de banda:  {vlb.get()}")
    arquivo.write(f"\n Lugar: {lugar.get()}")
    arquivo.write("\n\n")
    arquivo.close()
    

def semComando():
    print(" ")
   
"""
def abrir_tabelas():
    nova_janela = tk.Toplevel()
    nova_janela.title("Tabela fator de atenuação")
    nova_janela.geometry("800x600")
    #pastaApp=os.path.dirname(__file__)
    #photo= PhotoImage(file=pastaApp+"\\tabela.png")
    #photo = PhotoImage(file = "tabela.png" )
    #img = Image.open("tabela.png")
    #label = Label(nova_janela, image = img)
    #label.pack()
    #img.show()
    
 """   
"""    
def modelo_espaco_livre():
    nova_janela1 = tk.Toplevel(app)
    nova_janela1.title("Tabela fator de atenuação")
    nova_janela1.geometry("800x600")
    label = tk.label(nova_janela1, text = "Calculo")
    label.pack(pady=20)
    
"""

#Criando Barra de Menus.

barrademenus=Menu(app)
menuprincipal= Menu(barrademenus, tearoff  = 0)
menuprincipal.add_command(label = "Novo", command = semComando)
menuprincipal.add_command(label = "Salvar dados", command = salvardados)
menuprincipal.add_separator()
menuprincipal.add_command(label  = "Fechar",command=app.quit)
barrademenus.add_cascade(label = "Início", menu= menuprincipal)

menusobre = Menu(barrademenus, tearoff = 0)
#menusobre.add_command(label = "Tabelas", command = abrir_tabelas)
menusobre.add_separator()
menusobre.add_command(label = "Sobre", command = semComando)
barrademenus.add_cascade(label = "Informações", menu= menusobre)
app.config(menu=barrademenus)


#Caixas de Texto e entrada de dados:

Label(app, text="Digite a Comprimento de onda (em m):",background="#ff0",foreground= "#000", anchor= W).place(x=10,y=50,width=215,height=20)
lam = Entry(app)
lam.place(x=230,y=50,width=110,height=20)


Label(app, text="Digite a Potência da antena (em Watts):",background="#ff0",foreground= "#000", anchor= W).place(x=10,y=80,width=215,height=20)
pt = Entry(app)
pt.place(x=230,y=80,width=110,height=20)


Label(app, text="Digite o Ganho da antena de Transmissão (em dBi):",background="#ff0",foreground= "#000", anchor= W).place(x=10,y=110,width=275,height=20)
gt= Entry(app)
gt.place(x=290,y=110,width=110,height=20)

Label(app, text="Digite o Ganho da antena de Recepção (em dBi):",background="#ff0",foreground= "#000", anchor= W).place(x=10,y=140,width=260,height=20)
gr= Entry(app)
gr.place(x=275,y=140,width=110,height=20)


Label(app, text="Digite a distância a ser alcançada: ",background="#ff0",foreground= "#000", anchor= W).place(x=10,y=170,width=180,height=20)
d= Entry(app)
d.place(x=195,y=170,width=110,height=20)


Label(app, text="Digite sua localização: ",background="#ff0",foreground= "#000", anchor= W).place(x=10,y=200,width=120,height=20)
lugar = Entry(app)
lugar.place(x=135,y=200,width=110,height=20)

# Para o calculo da pontência recebida em um ponto de referencia:

Label(app, text="Digite o distância almejada (em m):  ",background="#ff0",foreground= "#000", anchor= W).place(x=10,y=360,width=150,height=20)
da = Entry(app)
da.place(x=165,y=360,width=110,height=20)

Label(app, text="Digite o distância do ponto de referência (em m):  ",background="#ff0",foreground= "#000", anchor= W).place(x=10,y=390,width=225,height=20)
do = Entry(app)       
do.place(x=240,y=390,width=110,height=20)

Label(app, text="Digite a potência no ponto de referência (em Watts):  ",background="#ff0",foreground= "#000", anchor= W).place(x=10,y=420,width=225,height=20)
ppr = Entry(app)
ppr.place(x=240,y=420,width=110,height=20)

zoom2 = 0
zoom = 0

zoom = Scale(app,from_=10, to=20, orient = HORIZONTAL) 
zoom.set(13)
zoom.place(x = 420 , y = 268)
print(str(zoom.get()))
             

#Botões:
bt = Button(app, text= "OK", command=lambda:[impdados(lam, pt, gt, gr ,d,lugar, nomeArquivo)])
bt.place(x =10, y =290, width=110, height=20)
bt1= Button(app, text= "OK", command =lambda:[calculo_potencia_ponto_referencia(da,do,ppr)])
bt1.place(x =10, y =510, width=110, height=20)
Button(app, text= "Sair",  command= sair).place(x=130,y=290,width=110,height=20)
bt3 = Button(app, text= "Mapa", command=lambda:[mapa(lugar,center2,r,f,imgLogo1,l_logo1, pastaApp)])
bt3.place(x =300, y =290, width=110, height=20)




"""
#Exibição do Mapa:
pastaApp=os.path.dirname(__file__)
imgLogo1 = PhotoImage(file=pastaApp+"\\II.gif")
l_logo1=Label(app,image=imgLogo1)
l_logo1.place(x=900,y=400)




# get method of requests module
# return response object
r = requests.get(url + "&size=250x250&center="+str(center2)+
                        "&zoom="+str(zoom)+"&maptype=satellite&key="+api_key)
print(center2)
print(url + "&size=250x250&center="+str(center2)+
                        "&zoom="+str(zoom)+"&maptype=satellite&key="+api_key)
#https://maps.googleapis.com/maps/api/staticmap?&size=400x400&center=Tokyo&zoom=10&maptype=satellite&key=AIzaSyDcz_OKnoD8j0n-a_3AyipLXOb6ZyqFI-0
# wb mode is stand for write binary mode
f = open('F:/Users/SAMUEL/Documents/MeusProjetos/5G/Python Files/II.gif', 'wb')
  
# r.content gives content,
# in this case gives image
f.write(r.content)
  
# close method of file object
# save and close the file
f.close()

"""


def mapa(lugar,center2,r,f,imgLogo1,l_logo1,pastaApp):
    api_key = "AIzaSyDcz_OKnoD8j0n-a_3AyipLXOb6ZyqFI-0"
    url = "https://maps.googleapis.com/maps/api/staticmap?"
    zoom2= str(zoom.get())
    print(zoom2)
    center2 = str(lugar.get())
    print(lugar.get())
    print(center2)
    
    r = requests.get(url + "&size=250x250&center="+str(center2)+
                        "&zoom="+str(zoom2)+"&maptype=satellite&key="+api_key)
    print(url + "&size=250x250&center="+str(center2)+
                        "&zoom="+str(zoom2)+"&maptype=satellite&key="+api_key)
    f = open('F:/Users/SAMUEL/Documents/MeusProjetos/5G/Python Files/II.png', 'wb')
    f.write(r.content)
    f.close()
    
    pastaApp=os.path.dirname(__file__)
    imgLogo1 = PhotoImage(file=pastaApp+"\\II.png")
    l_logo1=Label(app,image=imgLogo1)
    l_logo1.place(x=900,y=200)
    
    """
    
    img = Image.open("II.gif")
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    label = Label(app, image=img)
    label.pack()
    
    """
    """
    canvas = Canvas(app, width=250, height=250)
    canvas.pack()

    img = Image.open("II.gif")
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    canvas.create_image(0, 0, anchor=NW, image=img)
    """
    
    text = Text(app)
    text.pack()

    img = Image.open("II.png")
    img = img.resize((200, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    text.image_create(END, image=img)
    
    
app.mainloop()




# center defines the center of the map,
# equidistant from all edges of the map. 
