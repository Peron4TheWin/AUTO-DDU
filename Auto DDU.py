import os
import wmi
import requests
import zipfile

computer = wmi.WMI()
gpu_info = computer.Win32_VideoController()[0]
placa = '{0}'.format(gpu_info.AdapterCompatibility)
placaF = placa.lower()
DDU = "https://cdn.discordapp.com/attachments/1005754191563722793/1005763660167262238/DDU.zip"
local_file = 'ddu.zip'
r = requests.get(DDU, allow_redirects=True)
open('ddu.zip', 'wb').write(r.content)

with zipfile.ZipFile("ddu.zip", 'r') as zip_ref:
    zip_ref.extractall()

os.system(f'"Display Driver Uninstaller.exe" -clean{placaF} -silent -nosafemodemsg -restart')