1. **Navegação Básica no Terminal**
   - `pwd` (para verificar o diretório atual)
   - `ls` (para listar conteúdos do diretório)
   - `mkdir diretorio` (para criar um novo diretório/pasta)
   - `cd diretorio` (para mudar para outro diretório, use `cd ..` para voltar)
   - `cat arquivo.extensao` (para visualizar o conteúdo de um arquivo)
   - **Sugestão de Prática:** 
     - Listar conteúdo do diretório atual: `ls`
     - Criar um diretório: `mkdir dio`
     - Navegar para ele: `cd dio`
     - Verificar o diretório atual: `pwd`
     - Listar conteúdo (deve estar vazio): `ls`
     - Voltar para o diretório anterior: `cd ..`

2. **Manipulação de Arquivos e Diretórios**
   - `touch arquivo.extensao` (para criar um novo arquivo)
   - `comando > arquivo.extensao` (adiciona o resultado do comando no arquivo, sobrescrevendo o conteúdo existente)
   - `comando >> arquivo.extensao` (adiciona o resultado do comando no fim do arquivo, mantendo o conteúdo existente)
   - `cp arquivo.txt destino/` (para copiar o arquivo)
   - `mv arquivo.txt destino/` (para mover o arquivo)
   - `rm arquivo.txt` (para remover o arquivo)
   - **Sugestão de Prática:**
     - Criar arquivo: `touch mentoria.txt`
     - Listar conteúdo (deve ter o novo arquivo): `ls`
     - Incluir texto no arquivo: `echo "Seus Primeiros Passos no Linux" > mentoria.txt`
     - Visualizar o conteúdo de mentoria.txt (deve ter uma linha): `cat mentoria.txt`
     - Adicionar mais texto no arquivo: `echo "Bem-vindo(a) à Mentoria!" >> mentoria.txt`
     - Visualizar o conteúdo de mentoria.txt (deve ter duas linhas): `cat mentoria.txt`
     - Copiar para 'dio': `cp mentoria.txt dio/`
     - Listar conteúdo (mentoria.txt ainda deve existir, afinal só foi copiado): `ls`
     - Mover um arquivo: `mv mentoria.txt dio/mentoria_renomeado.txt`
     - Listar conteúdo (mentoria.txt não existirá mais, pois foi movido): `ls`
     - Navegar para a pasta 'dio': `cd dio`
     - Listar conteúdo (deve ter os arquivos mentoria.txt e mentoria_renomeado.txt): `ls`
     - Excluir arquivo: `rm dio/mentoria_renomeado.txt`
     - Listar conteúdo (deve ter apenas o arquivo mentoria.txt): `ls`

3. **Gerenciamento de Permissões em Arquivos**
   - `chmod 755 arquivo.txt` (para mudar permissões do arquivo)
   - **Sugestão de Prática:**
     - Criar arquivo: `touch script.sh`
     - Incluir o texto "echo Oi, Linux!" ao arquivo de script: `echo "echo Oi, Linux!" > script.sh`
     - Tenta executar o arquivo (deve dar erro): `./script.sh`
     - Listar conteúdo mostrando as permissões (justificando o erro): `ls -l`
     - Mudar permissão: `chmod 755 script.sh`
     - Tenta executar o arquivo: `./script.sh`

   - **Tabela de Permissões Octal para `chmod`**

     | Número | Permissão    | Descrição                               |
     | ------ | ------------ | --------------------------------------- |
     | 7      | rwx (4+2+1)  | Leitura, escrita e execução             |
     | 6      | rw- (4+2)    | Leitura e escrita                       |
     | 5      | r-x (4+1)    | Leitura e execução                      |
     | **4**      | **r-- (4)**      | **Apenas leitura**                          |
     | 3      | -wx (2+1)    | Escrita e execução                      |
     | **2**      | **-w- (2)**      | **Apenas escrita**                          |
     | **1**      | **--x (1)**      | **Apenas execução**                         |
     | 0      | --- (0)      | Sem permissões                          |

      [Referência 'chmod'](https://guialinux.uniriotec.br/chmod/)

4. **Pesquisa de Arquivos**
   - `find . -name "*.txt"` (para encontrar arquivos .txt)
   - `grep "texto" arquivo.txt` (para buscar um texto específico dentro de um arquivo)
   - **Sugestão de Prática:**
     - Buscar por arquivos .txt no diretório atual: `find . -name "*.txt"`
     - Buscar a palavra 'Linux' em todos os arquivos: `grep "Linux" *` (extremamente util para busca em logs)

## Referências Interessantes
- [Guia Linux](https://guialinux.uniriotec.br) (UNIRIO)
- [GuiaFoca](https://guiafoca.org)
- [Linux is a MUST. Seriously...](https://blog.amigoscode.com/p/linux-is-a-must-seriously)

- Projeto obtido no github da DIO no Link a seguir: https://github.com/digitalinnovationone/linux-primeiros-passos/blob/main/README.md, sendo feitas algumas alterações.