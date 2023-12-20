import tkinter as tk
from tkinter import filedialog
import os
import pyaes

def selecionar_arquivo():
    # Abre uma janela de diálogo para selecionar o arquivo
    arquivo_criptografado = filedialog.askopenfilename(filetypes=[("Arquivos Criptografados", "*.virusCrypto")])

    # Verifica se o usuário selecionou um arquivo
    if arquivo_criptografado:
        # Chave/código para descriptografar o arquivo
        key = b"crypto789456123"
        aes = pyaes.AESModeOfOperationCTR(key)

        # Abre o arquivo criptografado
        with open(arquivo_criptografado, 'rb') as f:
            conteudo_criptografado = f.read()

            # Descriptografa o arquivo
            decrypt_data = aes.decrypt(conteudo_criptografado)

            # Remove o arquivo criptografado
            os.remove(arquivo_criptografado)

            # Cria um novo arquivo descriptografado
            nome_arquivo_descriptografado = os.path.splitext(arquivo_criptografado)[0]  
            # Remove a extensão .virusCrypto
            with open(nome_arquivo_descriptografado, 'wb') as novo_arquivo:
                novo_arquivo.write(decrypt_data)

            print(f"Arquivo descriptografado salvo como {nome_arquivo_descriptografado}")

# Cria uma janela
janela = tk.Tk()
janela.title("Selecionar Arquivo Criptografado")

# Cria um botão para chamar a função de seleção de arquivo
botao_selecionar = tk.Button(janela, text="Selecionar Arquivo Criptografado", command=selecionar_arquivo)
botao_selecionar.pack(pady=20)

# Inicia o loop da interface gráfica
janela.mainloop()
