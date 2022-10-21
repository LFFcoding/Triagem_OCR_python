import os
from tkinter import filedialog, Tk
from PIL import Image
import pytesseract

#identifica o caminho do executável
root = Tk(screenName="Triagem (minimize e use o Prompt)")
root.attributes("-topmost", True)
pathexec = os.getcwd()

#define o caminho do OCR
pytesseract.pytesseract.tesseract_cmd = f'{pathexec}' + r"\Tesseract-OCR\tesseract.exe"

#define os códigos dos documentos
cod1 = f"TREC"
cod2 = f"DCDP"
cod3 = f"CDRL"
cod4 = f"DCRL"
cod5 = f"DCDD"
cod6 = f"DCGM"
cod7 = f"CPGM"
cod8 = f"DCTH"

#solicita do usuário, a pasta fonte
input("Selecione a pasta onde estão as imagens que serão Triadas: (enter)")

pathfonte = filedialog.askdirectory()
os.chdir(pathfonte)

#solicita do usuário a pasta destino
input("Selecione a pasta destino: (enter)")

pathdestino = filedialog.askdirectory()

#cria pastas de triagem (caso ainda não existam)
os.makedirs(f'{pathdestino}' + r"/Termo_de_representacao_da_entidade_conveniada", exist_ok=True)
os.makedirs(f'{pathdestino}' + r"/Documento_de_identificacao_do_procurador", exist_ok=True)
os.makedirs(f'{pathdestino}' + r"/Comprovante_da_representacao_legal", exist_ok=True)
os.makedirs(f'{pathdestino}' + r"/Documentos_de_identificacao_do_representante_legal", exist_ok=True)
os.makedirs(f'{pathdestino}' + r"/Documentos_de_identificaca_do_interessado", exist_ok=True)
os.makedirs(f'{pathdestino}' + r"/Documento_de_identificacao_de_todos_os_membros_do_grupo_familiar", exist_ok=True)
os.makedirs(f'{pathdestino}' + r"/Comprovantes_das_relacoes_previdenciarias_do_interessado_e_do_grupo_familiar", exist_ok=True)
os.makedirs(f'{pathdestino}' + r"/Outros_documentos", exist_ok=True)
os.makedirs(f'{pathdestino}' + r"/Nao_identificado", exist_ok=True)

#cria lista dos arquivos da pasta fonte
imglist = os.listdir(pathfonte)

#identifica as imagens na pasta fonte e inicia triagem
for img in imglist:
    if img.endswith(".png"):
        imgname = (f"{pathfonte}" + r"/" + f"{img}")
        print("Processando imagem " + f"{imgname}")
        imgobj = Image.open(imgname)
        imgtext = pytesseract.image_to_string(imgobj, lang='por')
        if imgtext.count(cod1) >= 1:
            os.rename(imgname, f"{pathdestino}" + r"/Termo_de_representacao_da_entidade_conveniada/" + f"{img}")
        elif imgtext.count(cod2) >= 1:
            os.rename(imgname, f"{pathdestino}" + r"/Documento_de_identificacao_do_procurador/" + f"{img}")
        elif imgtext.count(cod3) >= 1:
            os.rename(imgname, f"{pathdestino}" + r"/Comprovante_da_representacao_legal/" + f"{img}")
        elif imgtext.count(cod4) >= 1:
            os.rename(imgname, f"{pathdestino}" + r"/Documentos_de_identificacao_do_representante_legal/" + f"{img}")
        elif imgtext.count(cod5) >= 1:
            os.rename(imgname, f"{pathdestino}" + r"/Documentos_de_identificaca_do_interessado/" + f"{img}")
        elif imgtext.count(cod6) >= 1:
            os.rename(imgname, f"{pathdestino}" + r"/Documento_de_identificacao_de_todos_os_membros_do_grupo_familiar/" + f"{img}")
        elif imgtext.count(cod7) >= 1:
            os.rename(imgname, f"{pathdestino}" + r"/Comprovantes_das_relacoes_previdenciarias_do_interessado_e_do_grupo_familiar/" + f"{img}")
        elif imgtext.count(cod8) >= 1:
            os.rename(imgname, f"{pathdestino}" + r"/Outros_documentos/" + f"{img}")
        else:
            os.rename(imgname, f"{pathdestino}" + r"/Nao_identificado/" + f"{img}")

input("Triagem concluída!")