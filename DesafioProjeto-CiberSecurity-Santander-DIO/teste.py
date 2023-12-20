import tkinter as tk
from tkinter import filedialog

def selecionar_arquivo():
    # Abre uma janela de diálogo para selecionar o arquivo
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt")])

    # Verifica se o usuário selecionou um arquivo
    if arquivo:
        # Primeiramente lê, mostra abaixo, e após criptografa o arquivo
        with open(arquivo, 'r') as f:
            conteudo = f.read()
            print("Conteúdo do arquivo:")
            print(conteudo)


# Cria uma janela
janela = tk.Tk()
janela.title("Selecione um arquivo para Criptografar")

# Cria um botão para chamar a função de seleção de arquivo
botao_selecionar = tk.Button(janela, text="Selecione um arquivo para Criptografar", command=selecionar_arquivo)
botao_selecionar.pack(pady=30)

# Inicia o loop da interface gráfica
janela.mainloop()