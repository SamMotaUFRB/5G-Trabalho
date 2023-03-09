import dataclasses
from tkinter import *
from datetime import datetime
import os
from PIL import *
import googlemaps
import requests
from math import pi, log10
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
lugar2=0
beta = 2

              
              
#Background do app:
pastaApp=os.path.dirname(__file__)
imgLogo = PhotoImage(file=pastaApp+"\\5G_background.gif")
l_logo=Label(app,image=imgLogo)
l_logo.place(x=0,y=0)

#Horário:
data = datetime.now()
data = str(data)

# API do Google Maps:
api_key = "AIzaSyDcz_OKnoD8j0n-a_3AyipLXOb6ZyqFI-0"

# url variable store url
url = "https://maps.googleapis.com/maps/api/staticmap?"

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


class Pack:
    """Geometry manager Pack.

    Base class to use the methods pack_* in every widget."""
    def pack_configure(self, cnf={}, **kw):
        """Pack a widget in the parent widget. Use as options:
        after=widget - pack it after you have packed widget
        anchor=NSEW (or subset) - position widget according to
                                  given direction
        before=widget - pack it before you will pack widget
        expand=bool - expand widget if parent size grows
        fill=NONE or X or Y or BOTH - fill widget if widget grows
        in=master - use master to contain this widget
        in_=master - see 'in' option description
        ipadx=amount - add internal padding in x direction
        ipady=amount - add internal padding in y direction
        padx=amount - add padding in x direction
        pady=amount - add padding in y direction
        side=TOP or BOTTOM or LEFT or RIGHT -  where to add this widget.
        """
        self.tk.call(
              ('pack', 'configure', self._w)
              + self._options(cnf, kw))
    pack = configure = config = pack_configure
    def pack_forget(self):
        """Unmap this widget and do not use it for the packing order."""
        self.tk.call('pack', 'forget', self._w)
    forget = pack_forget
    def pack_info(self):
        """Return information about the packing options
        for this widget."""
        d = _splitdict(self.tk, self.tk.call('pack', 'info', self._w))
        if 'in' in d:
            d['in'] = self.nametowidget(d['in'])
        return d
    info = pack_info
    propagate = pack_propagate = Misc.pack_propagate
    slaves = pack_slaves = Misc.pack_slaves
   


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

"""  
def on_submit(lam, pt, gt, gr,d):
        #To be run when the user submits the form
    lam = lam_var.get()
    pt = pt_var.get()
    gt = gt_var.get()
    gr = gr_var.get()
"""   
    
   # NameError: name 'pr' is not defined

    
   # print("Sua Localização é: %s" %geocode_result))
   
#def bt_onclick():
      
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
    #photo= PhotoImage(file=pastaApp+"\\teabla.png")
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
             

#Botões:
bt = Button(app, text= "OK", command=lambda:[impdados(lam, pt, gt, gr ,d,lugar, nomeArquivo)])
bt.place(x =10, y =290, width=110, height=20)
bt1= Button(app, text= "OK", command =lambda:[calculo_potencia_ponto_referencia(da,do,ppr)])
bt1.place(x =240, y =450, width=110, height=20)
#bt2 = Button(app, text= "OK", command=lambda:[impdados(lam, pt, gt, gr ,d,lugar, nomeArquivo)])
#bt2.place(x =10, y =290, width=110, height=20)
Button(app, text= "Sair",  command= sair).place(x=130,y=290,width=110,height=20)

#print("Valor de x",x)

#Exibição do Mapa:
pastaApp=os.path.dirname(__file__)
imgLogo1 = PhotoImage(file=pastaApp+"\\II.gif")
l_logo1=Label(app,image=imgLogo1)
l_logo1.place(x=900,y=400)


center = 'Brasil'    #str(lugar2)
zoom = 3

# get method of requests module
# return response object
r = requests.get(url + "&size=250x250&center="+str(center)+
                        "&zoom="+str(zoom)+"&maptype=satellite&key="+api_key)
print(url + "&size=250x250&center="+str(center)+
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



app.mainloop()



# center defines the center of the map,
# equidistant from all edges of the map. 






