#📂 Organizador de Arquivos com Python

Este script organiza automaticamente os arquivos da sua Área de Trabalho, movendo-os para pastas específicas com base em suas extensões.

🛠️ Funcionalidades

✅ Identifica arquivos por extensão
✅ Move arquivos para pastas organizadas (Imagens, Documentos, Vídeos, etc.)
✅ Cria as pastas automaticamente, caso não existam
✅ Funciona com Windows + OneDrive
✅ Tratamento de erros para evitar falhas inesperadas

🚀 Como Usar

1️⃣ Instale o Python

Se ainda não tem o Python instalado, baixe-o aqui.

2️⃣ Baixe o Script

Salve o arquivo organizador.py no seu computador.

3️⃣ Execute o Script

Abra o terminal (cmd ou PowerShell) e vá até a pasta onde salvou o script:

cd "C:\Users\SEU_USUARIO\Caminho\Para\O\Script"

Agora execute o script:

python organizador.py

📁 Estrutura das Pastas

O script organiza os arquivos em pastas na Área de Trabalho, como:

Área de Trabalho
│-- Imagens
│-- Documentos
│-- Vídeos
│-- Áudio
│-- Compactados
│-- Executáveis
│-- Códigos

📌 Extensões Suportadas

Imagens: .jpg, .jpeg, .png, .gif, .bmp, .svg

Documentos: .pdf, .docx, .txt, .xlsx, .pptx, .csv

Vídeos: .mp4, .avi, .mkv, .mov

Áudio: .mp3, .wav, .aac, .ogg

Compactados: .zip, .rar, .7z

Executáveis: .exe, .msi, .bat

Códigos: .py, .java, .cpp, .js, .html, .css

🔧 Personalização

Se quiser adicionar novas extensões, edite o dicionário file_categories no código e adicione as extensões desejadas.

❌ Possíveis Problemas

O script não moveu os arquivos → Verifique se os nomes das pastas estão corretos

Erro de permissão → Tente rodar o script como Administrador

Caminho errado da área de trabalho → Atualize a variável desktop no código

📌 Autor

Victor Hugo Ribeiro dos Santos Azambuja Prim

Se tiver dúvidas ou sugestões, me avise! 🚀

