from tkinter import *

app = Tk()
app.title("APP 5G")
app.geometry("500x500")
app.configure(background="#118")

txt1 = Label(app, text = "Bem-vindo a interface", background="#ff0", foreground= "#000")
txt1.place(x=10,y=10,width=150, height=30)

def sair():
    quit()


"""
vtxt="Opções"
vbg="#ff0"
vfg="#000"
txt2=Label(app, text=vtxt, bg=vbg, fg=vfg)
txt2.pack(ipadx=10,ipady=10,padx=90,pady=90,side="top",fill=X,expand=True)
"""

Label(app, text="Digite a Frequência (em Hz):",background="#ff0",foreground= "#000", anchor= W).place(x=10,y=50,width=160,height=20)
vf = Entry(app).place(x=10,y=75,width=110,height=20)

Label(app, text="Digite a Potência (em Watts):",background="#ff0",foreground= "#000", anchor= W).place(x=10,y=100,width=160,height=20)
vp = Entry(app).place(x=10,y=125,width=110,height=20)

Label(app, text="Digite a Largura de Banda (em Hz):",background="#ff0",foreground= "#000", anchor= W).place(x=10,y=150,width=190,height=20)
vlb= Entry(app).place(x=10,y=175,width=110,height=20)


Button(app, text= "Sair",  command= sair).place(x=10,y=235,width=110,height=20)



app.mainloop()