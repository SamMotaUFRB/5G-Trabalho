import dataclasses
from tkinter import *
import os
from PIL import *
import googlemaps
#from webbrowser import *
#from requests import *

#Configurações Visuais:
app = Tk()
app.title("APP 5G")
app.iconbitmap('F:/Users/SAMUEL/Documents/MeusProjetos/5G/Python Files/radio-tower.ico')
app.geometry("500x500")
app.configure(background="#118")

"""
tkimage = imagetk.PhotoImage(Image.open('F:/Users/SAMUEL/Documents/MeusProjetos/5G/Python Files/5G_background.jpeg'))
tk.Label(app,image=tkimage).pack()
my_label.pack()
"""
"""
#API do Google Maps:
googlemaps = googlemaps.Client(key= "AIzaSyDcz_OKnoD8j0n-a_3AyipLXOb6ZyqFI-0")
geocode_result = googlemaps.geocode(lugar)
"""

#Título de apresentação
txt1 = Label(app, text = "Bem-vindo a interface", background="#ff0", foreground= "#000")
#txt1.grid(row= 5, column= 5) # Colocando o objeto por linhas e colunas.
txt1.place(x=10,y=10,width=150, height=30) #Colocando o objeto por coodernadas

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


def impdados(vf, vp, vlb, lugar, nomeArquivo):
    print(f'O valor {lugar}')

    arquivo=open(nomeArquivo,"a")
    arquivo.write(f"\nFrequência: {vf.get()}")
    arquivo.write( f"\nPotência:   {vp.get()}")
    arquivo.write(f"\nLargura de banda:  {vlb.get()}")
    arquivo.write(f"\n Lugar: {lugar.get()}")
    arquivo.write("\n\n")
    arquivo.close()
    
    print(f"\nFrequência: {vf.get()}")
    print(f"Potência:   {vp.get()}" )
    print(f"Largura de banda:   {vlb.get()}")
    print(f"Lugar: {lugar.get()}" )
   # print("Sua Localização é: %s" %geocode_result))
   
"""
vtxt="Opções"
vbg="#ff0"
vfg="#000"
txt2=Label(app, text=vtxt, bg=vbg, fg=vfg)
txt2.pack(ipadx=10,ipady=10,padx=90,pady=90,side="top",fill=X,expand=True)
"""

#Caixas de Texto e entrada de dados:

Label(app, text="Digite a Frequência (em Hz):",background="#ff0",foreground= "#000", anchor= W).place(x=10,y=50,width=160,height=20)
vf = Entry(app)
vf.place(x=10,y=75,width=110,height=20)


Label(app, text="Digite a Potência (em Watts):",background="#ff0",foreground= "#000", anchor= W).place(x=10,y=100,width=160,height=20)
vp = Entry(app)
vp.place(x=10,y=125,width=110,height=20)


Label(app, text="Digite a Largura de Banda (em Hz):",background="#ff0",foreground= "#000", anchor= W).place(x=10,y=150,width=190,height=20)
vlb= Entry(app)
vlb.place(x=10,y=175,width=110,height=20)


Label(app, text="Digite sua localização: ",background="#ff0",foreground= "#000", anchor= W).place(x=10,y=200,width=120,height=20)
lugar = Entry(app)
lugar.place(x=10,y=225,width=110,height=20)

#Botões:
Button(app, text= "Imprimir", command=lambda:[impdados(vf, vp, vlb, lugar, nomeArquivo)]).place(x =10, y =250, width=110, height=20)
Button(app, text= "Sair",  command= sair).place(x=10,y=300,width=110,height=20)

app.mainloop()