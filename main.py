from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

import requests
import json

co0 = "#444466"
co1 = "#feffff"
co2 = "#6f9fbd"
fundo = "#484f60"

# Criando janela #
janela = Tk()
janela.title("")
janela.geometry('320x350')
janela.configure(bg=fundo)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

frame_top = Frame(janela, width=320, height=50, bg=co1, pady=0, padx=0, relief='flat')
frame_top.grid(row=1, column=0)

frame_bottom = Frame(janela, width=320, height=300, bg=fundo, pady=0, padx=0, relief='flat')
frame_bottom.grid(row=2, column=0, sticky=NW)

def info():
    ai_link_dolar = "https://api.coinbase.com/v2/prices/BTC-USD/spot"
    ai_link_euro = "https://api.coinbase.com/v2/prices/BTC-EUR/spot"
    ai_link_reais = "https://api.coinbase.com/v2/prices/BTC-BRL/spot"
    ai_link_kwz = " https://api.coinbase.com/v2/prices/BTC-GBP/spot"

    response = requests.get(ai_link_dolar)
    response2 = requests.get(ai_link_reais)
    response3 = requests.get(ai_link_kwz)
    response4 = requests.get(ai_link_euro)

    dados1 = response.json()
    dados2 = response2.json()
    dados3 = response3.json()
    dados4 = response4.json()

    valor_usd = float(dados1['data']['amount'])
    valor_fromatado_usd = "${:,.3f}".format(valor_usd)
    l_p_usd['text'] = valor_fromatado_usd

    valor_euro = float(dados4['data']['amount'])
    valor_fromatado_euro = "{:,.3f}".format(valor_euro)
    l_p_euro['text'] ='Em Euro é: €' + valor_fromatado_euro

    valor_reais = float(dados2['data']['amount'])
    valor_fromatado_reais = "{:,.3f}".format(valor_reais)
    l_p_reais['text'] ='Em Reais é: R$' + valor_fromatado_reais

    valor_kwz = float(dados3['data']['amount'])
    valor_fromatado_kwz = "{:,.3f}".format(valor_kwz)
    l_p_kwz['text'] ='Em Kwanzas é: AOA' + valor_fromatado_kwz

    frame_bottom.after(1000, info)




image = Image.open('images/icons8-bitcoin-48(1).png')
image = image.resize((30, 30), Image.ADAPTIVE)
image = ImageTk.PhotoImage(image)

l_icon = Label(frame_top, image=image, compound=LEFT, bg=co1, relief='flat')
l_icon.place(x=10, y=10)

l_nome = Label(frame_top, text='Bitcoin Price tracker',  bg=co1, fg=co2, relief='flat', anchor='center', font=('Arial 20'))
l_nome.place(x=50, y=5)

l_p_usd = Label(frame_bottom, text='', width=14, bg=fundo, fg=co1, relief='flat', anchor='center', font=('Arial 20'))
l_p_usd.place(x=-10, y=50)

l_p_euro = Label(frame_bottom, text='', bg=fundo, fg=co1, relief='flat', anchor='center', font=('Arial 12'))
l_p_euro.place(x=10, y=130)

l_p_reais = Label(frame_bottom, text='', bg=fundo, fg=co1, relief='flat', anchor='center', font=('Arial 12'))
l_p_reais.place(x=10, y=160)

l_p_kwz = Label(frame_bottom, text='', bg=fundo, fg=co1, relief='flat', anchor='center', font=('Arial 12'))
l_p_kwz.place(x=10, y=190)

info()

janela.mainloop()