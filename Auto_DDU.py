import re
import subprocess
import os
import requests
import zipfile
def split_sentence(sentence, character):
    return re.split(character, sentence)
def cmd(command):
    return subprocess.check_output(command, shell=True).decode('utf-8')
command = r'wmic path win32_VideoController get name | findstr /i /V "name"'

subprocess.call("cls", shell=True)

placa=cmd(command)
final=split_sentence(placa, ' ')[0].lower()

# USAR DDU
def DDUF(placaF:str):
    os.system(f'"Display Driver Uninstaller.exe" -clean{placaF} -silent -nosafemodemsg -restart')

# INSTALAR DDU
DDU = "https://cdn.discordapp.com/attachments/1005754191563722793/1005763660167262238/DDU.zip"
local_file = 'ddu.zip'
r = requests.get(DDU, allow_redirects=True)
open('ddu.zip', 'wb').write(r.content)
with zipfile.ZipFile("ddu.zip", 'r') as zip_ref:
    zip_ref.extractall()

if placa in ['nvidia', 'geforce']:
    DDUF('nvidia')
elif placa in ['amd', 'radeon']:
    DDUF('amd')
elif placa in ['intel', 'hd graphics']:
    DDUF('intel')
else:
    print('Placa no soportada')
    print('Presione cualquier tecla para salir')
    input()