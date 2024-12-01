import tkinter as tk

#criando a janela
window = tk.Tk()
window.geometry("600x600")
window.title("janela legal")

#adicionando o frame
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill='x', expand=True )

#adicionando o label
label = tk.Label(frame, text="Olá, Mundo")
label.pack(fill='x', expand=True)


# 4 - Adicionando input
frase_lab = tk.Label(frame, text="Frase")
frase_lab.pack(fill='x', expand=True)

frase_inp = tk.Entry(frame)
frase_inp.pack(fill='x', expand=True)

# 5 - Função para alterar texto do label
def click():
    label.config(text=frase_inp.get())
    
    
# 6 - Adicionando botão
button = tk.Button(frame, text="Enviar", command=click)
button.pack()

window.mainloop()