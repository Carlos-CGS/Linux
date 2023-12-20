import tkinter as tk
from tkinter import filedialog
import os
import pyaes

def selecionar_arquivo():
    # Abre uma janela de diálogo para selecionar o arquivo
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt")])

    # Verifica se o usuário selecionou um arquivo
    if arquivo:
        # Faz algo com o arquivo, por exemplo, lê o conteúdo
        with open(arquivo, 'rb') as f:
            conteudo = f.read()
            
            # Chave para criptografar o arquivo
            key = b"crypto789456123"
            aes = pyaes.AESModeOfOperationCTR(key)

            # Criptografar o arquivo
            crypto_data = aes.encrypt(conteudo)

            # Salvar o arquivo criptografado
            nome_arquivo_cripto = arquivo + ".virusCrypto"
            with open(nome_arquivo_cripto, 'wb') as novo_arquivo:
                novo_arquivo.write(crypto_data)
            
            print(f"Arquivo criptografado salvo como {nome_arquivo_cripto}")

# Cria uma janela
janela = tk.Tk()
janela.title("Selecionar Arquivo")

# Cria um botão para chamar a função de seleção de arquivo
botao_selecionar = tk.Button(janela, text="Selecionar Arquivo", command=selecionar_arquivo)
botao_selecionar.pack(pady=20)

# Inicia o loop da interface gráfica
janela.mainloop()
