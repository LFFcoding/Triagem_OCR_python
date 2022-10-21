import os
from tkinter import filedialog, Tk

root = Tk(screenName="Renomeie (minimize e use o prompt)")
root.attributes("-topmost", True)

pathexec = os.getcwd()

print("Renomeie os seus arquivos :)  por Leonardo Ferreira")

input("Pressione enter para selecionar a pasta fonte:")

pathfonte = filedialog.askdirectory()

os.chdir(pathfonte)

filelist = os.listdir(pathfonte)

print("Renomeie os seus arquivos :)  por Leonardo Ferreira")

arcnm = input("Defina o nome dos arquivos:")
arctp = input("Defina o tipo dos arquivos na pasta, que serão renomeados: (.jpg , .png , .doc , etc.")

input("Pressione enter para iniciar:")

for file, files in enumerate(filelist, start=1):
    if files.endswith(f"{arctp}"):
        filenm = f"{pathfonte}" + r"/" + f"{files}"
        print("Processando arquivo: " + f"{filenm}")
        os.rename(filenm, f"{pathfonte}" + r"/" + f"{arcnm}" + f"{file}" + f"{arctp}")
input("Pressione enter para finalizar:")