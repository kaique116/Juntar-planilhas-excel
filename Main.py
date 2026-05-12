import tkinter as tk
from tkinter import messagebox
import pandas as pd

def juntar_planilhas():
    planilha1 = pd.read_excel(informar_planilha1.get())
    planilha2 = pd.read_excel(informar_planilha2.get())

    planilha_completa = pd.concat([planilha1, planilha2], ignore_index=True)

    planilha_completa.to_excel("Planilha_completa.xlsx")

    messagebox.showinfo("Sucesso", "Planilhas juntas com sucesso!")

    

janela = tk.Tk()
janela.title("Juntar Planilhas")
janela.geometry("300x200")

informar_planilha1 = tk.Entry(janela)
informar_planilha1.pack()
informar_planilha2 = tk.Entry(janela)
informar_planilha2.pack()

botao_juntar = tk.Button(janela, text='Clica aqui para juntar as planilhas', command=juntar_planilhas)
botao_juntar.pack()

janela.mainloop()
