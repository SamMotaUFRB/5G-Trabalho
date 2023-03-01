import dataclasses
from tkinter import *
from datetime import datetime
import os
from PIL import *
import googlemaps
import requests
from math import pi
#from webbrowser import *
#from requests import *


#Configurações Visuais:
app = Tk()
app.title("APP 5G")
app.iconbitmap('F:/Users/SAMUEL/Documents/MeusProjetos/5G/Python Files/radio-tower.ico')
app.geometry("600x600")
app.configure(background="#118")
              
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
#txt2 = Label(app, text = data, background="#ff0", foreground= "#000" )
#txt2.place(x=160,y=10,width=150, height=30)

#Arquivo Criado para escrita dos dados:
c = os.path.dirname(__file__)
nomeArquivo=c+"Dados.txt"
"""

#Calculo do modelo do espaço livre.


float = pr
float = pt, gt, gr, lam, d



pr = (pt*gt*gr*lam*lam)/((4*pi)**2)*(d*d)
"""

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


def impdados(pr,lam, pt, gt, gr,d ,lugar, nomeArquivo):
    #print(f'O valor {lugar}')
    print("Horário: ", data)
    print(f"\nComprimento de Onda: {lam.get()}")
    print(f"Potência da antena:   {pt.get()}" )
    print(f"Ganho da antena de Transmissão:   {gt.get()}")
    print(f"Ganho da antena de Recepção:   {gr.get()}")
    print(f"Lugar: {lugar.get()}" )
    print(lugar.get())
    """
    float = pr, pt, gt, gr, lam, d
    pr = (pt.get()*gt.get()*gr.get()*lam.get()**2)/((4*pi)**2)*(d.get()**2)
    print(pr)

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
    

#Criando Barra de Menus.

barrademenus=Menu(app)
menuprincipal= Menu(barrademenus, tearoff  = 0)
menuprincipal.add_command(label = "Novo", command = semComando)
menuprincipal.add_command(label = "Salvar dados", command = salvardados)
menuprincipal.add_separator()
menuprincipal.add_command(label  = "Fechar",command=app.quit)
barrademenus.add_cascade(label = "Início", menu= menuprincipal)

menusobre = Menu(barrademenus, tearoff = 0)
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


#Botões:
bt = Button(app, text= "OK", command=lambda:[impdados(pr,lam, pt, gt, gr ,d,lugar, nomeArquivo)])
bt.place(x =10, y =230, width=110, height=20)
Button(app, text= "Sair",  command= sair).place(x=130,y=230,width=110,height=20)


#Exibição do Mapa:
pastaApp=os.path.dirname(__file__)
imgLogo1 = PhotoImage(file=pastaApp+"\\II.gif")
l_logo1=Label(app,image=imgLogo1)
l_logo1.place(x=10,y=330)


# zoom defines the zoom
# level of the map

center ="New york"  #Quero que o valor digitado em center = entry( ), vá para uma variavel x e que center é iguala a x.
zoom = 12

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






