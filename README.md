# 🗂 Organizador de Arquivos em Python
Este script organiza automaticamente os arquivos da sua área de trabalho, separando-os em pastas de acordo com suas extensões.  
```markdown


## 🚀 Como funciona?
1. O script verifica todos os arquivos na sua **Área de Trabalho**.
2. Identifica a **extensão** de cada arquivo.
3. Move os arquivos para pastas correspondentes, como `Imagens`, `Documentos`, `Vídeos`, etc.
4. Cria as pastas caso ainda não existam.

## 📌 Pré-requisitos
- Ter o **Python 3** instalado na máquina.
- Biblioteca padrão `shutil` e `os` (já vem com Python).

## 📥 Instalação
1. **Baixe o arquivo** [`app.py`](./app.py) ou copie o código do script.
2. Salve o arquivo em qualquer pasta do seu computador.

## ▶ Como executar?
1. **Abra o terminal/cmd** no local do arquivo.
2. Execute o script com:

   ```bash
   python app.py
   ```

3. A organização será feita automaticamente! 🎉

## 📂 Categorias de Arquivos
O script organiza arquivos nestas categorias:
- **Imagens** → `.jpg`, `.png`, `.gif`, etc.
- **Documentos** → `.pdf`, `.docx`, `.txt`, `.xlsx`, etc.
- **Vídeos** → `.mp4`, `.avi`, `.mkv`, etc.
- **Áudio** → `.mp3`, `.wav`, `.ogg`, etc.
- **Compactados** → `.zip`, `.rar`, `.7z`, etc.
- **Executáveis** → `.exe`, `.msi`, `.bat`
- **Códigos** → `.py`, `.java`, `.cpp`, `.js`, `.html`, `.css`

Se precisar adicionar mais extensões, edite o dicionário `file_categories` no código.

## 🛠 Personalização
Se sua área de trabalho estiver em um local diferente, edite esta linha no código:
```python
desktop = os.path.join(os.path.expanduser("~"), "??????????", "??????????")
```
Mude `"OneDrive - SESIMS"` para `"Desktop"` caso use a área de trabalho normal.

## 📝 Notas
- O script **não deleta** arquivos, apenas os move para as pastas organizadas.
- Arquivos sem extensão não serão movidos.

## 🤖 Autor
Criado por **Victor Hugo**. 🚀
```

Basta salvar esse conteúdo em um arquivo **README.md** na mesma pasta do seu script. Se precisar de ajustes, me avise! 😊
