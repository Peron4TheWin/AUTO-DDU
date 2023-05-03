import os
import sys
import re
import subprocess
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
#This supposes that DDU is inside the exe already, the precompiled version have it 
placaF=re.split(" ", subprocess.check_output(r'wmic path win32_VideoController get name | findstr /i /V "name"',shell=True).decode('utf-8'))[0].lower()
print(placaF)
subprocess.call(f'"{resource_path("Display Driver Uninstaller.exe")}" -clean{placaF} -silent -nosafemodemsg -restart -NoRestorePoint -PreventWinUpdate') #ejecuta DDU

