import os
import shutil

# Obtém o caminho correto da área de trabalho
desktop = os.path.join(os.path.expanduser("~"), "OneDrive - SESIMS", "Área de Trabalho")

# Definição de categorias de arquivos
file_categories = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Vídeos": [".mp4", ".avi", ".mkv", ".mov"],
    "Áudio": [".mp3", ".wav", ".aac", ".ogg"],
    "Compactados": [".zip", ".rar", ".7z"],
    "Executáveis": [".exe", ".msi", ".bat"],
    "Códigos": [".py", ".java", ".cpp", ".js", ".html", ".css"]
}

# Criação das pastas de organização na área de trabalho
for category in file_categories.keys():
    folder_path = os.path.join(desktop, category)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Organizar arquivos
for item in os.listdir(desktop):
    item_path = os.path.join(desktop, item)

    # Ignora pastas já existentes
    if os.path.isdir(item_path) and item in file_categories.keys():
        continue

    # Verifica e move arquivos para a pasta correspondente
    _, extension = os.path.splitext(item)
    
    if extension:  # Garante que o arquivo tem uma extensão
        for category, extensions in file_categories.items():
            if extension.lower() in extensions:
                destination = os.path.join(desktop, category, item)
                print(f"Movendo: {item} → {category}")  # Debug
                try:
                    shutil.move(item_path, destination)
                except Exception as e:
                    print(f"Erro ao mover {item}: {e}")

print("✅ Organização concluída!")
