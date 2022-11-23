import subprocess,re,requests,zipfile                                                                               #importes
DDU = "https://cdn.discordapp.com/attachments/901637950520033291/1033126099456106546/ddu.zip"                       #descarga DDU
local_file = 'ddu.zip'
r = requests.get(DDU, allow_redirects=True)
open('ddu.zip', 'wb').write(r.content)
with zipfile.ZipFile("ddu.zip", 'r') as zip_ref:zip_ref.extractall()                                                #extrae DDU
placaF=re.split(" ", subprocess.check_output(r'wmic path win32_VideoController get name | findstr /i /V "name"',shell=True).decode('utf-8'))[0].lower() #obtiene el nombre de la placa
subprocess.call(f'"Display Driver Uninstaller.exe" -clean{placaF} -silent -nosafemodemsg -restart -NoRestorePoint -PreventWinUpdate') #ejecuta DDU
