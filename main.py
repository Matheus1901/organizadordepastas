#organize suas pastas com esse código (é seguro)
import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione a pasta")

lista_arquivos = os.listdir(caminho)

locais = {
    "imagens": [".png", ".jpg", ".jpeg", ".PNG", ".JPEG" ],
    "planilhas": [".xlsx"],
    "powerpoints": [".pptx"],
    "words": [".docx"],
    "corel": [".cdr", ".CDR"],
    "compactados": [".zip"],
    "pdfs": [".pdf"],
    "csv": [".csv"],
    "aplicativos": [".exe"]

}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}" , f"{caminho}/{pasta}/{arquivo}")

            