import os
import requests
import zipfile
os.system('cls')
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



# CONSEGUIR PLACA
os.system(r'wmic path win32_VideoController get name | findstr /i /V "name" > placa.txt')
with open('placa.txt') as f:
    lines = f.readlines()
lines=str(lines)
ttt=lines.lower()

#DETECTAR PLACA
print(ttt)
if "nvidia" in ttt:
    DDUF("nvidia")
elif "amd" in ttt:
    DDUF("amd")
elif "intel" in ttt:
    DDUF("intel")
else:
    raise Exception("no se pudo detectar tu placa, contacta a peron#0268 en DS")