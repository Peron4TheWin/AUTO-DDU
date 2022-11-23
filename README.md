
# AUTO DDU 
 Esto es un auto [DDU](https://www.guru3d.com/files-details/display-driver-uninstaller-download.html) compatible con windows 10, solamente abres el exe y tus drivers de video se desintalaran completamente para dejarte espacio a una nueva instalacion de drivers de video limpios.

&nbsp;

# tips - sugerencias y problemas
desconozco si tiene algun problema actualmente, pero no lo creo, si tienes algun problema o sugerencia puedes abrir un issue en el repositorio de github o hablarme directamente por discord `peron#0268`.



algunos tips
- Auto DDU no desactiva windows defender, asi que si tienes windows defender activado, debes desactivarlo para que tus drivers no se reinstalen de forma automatica.

- Si reinicias tu pc en modo seguro con el comando `bcdedit /set {current} safeboot minimal` y luego abres el auto DDU, haras el proceso mas seguro y rapido. 
(usa el comando `bcdedit /deletevalue {current} safeboot` para desactivar el modo seguro)
# <p align="center">KernelOS-Guide
una guia de como instalar kernelOS (win 10 1809 ) y tambien instalacion de drivers de internet



## <p align="center">Antes de instalar KernelOS :
----  

ASEGURATE DE TENER SECURE BOOT DESHABILITADO  
Esta puede ser una opción individual (enable/disable) o una lista de keys que pueden borrarse 
¿que es KernelOS?
KernelOS es un sistema operativo customizado basado en windows 10 version 1809

## <p align="center">¿Qué problemas presenta KernelOS?  
----
                                                                
                                                                
                                                                
Este es un windows customizado y con muchísimas funciones que normalmente están en windows normal, aquí la lista de las cosas que kernelOS win10 no soporta

Unsupported  -  KernelOS
KernelOS 1809 v1.3 


* Restore Point
* Printing
* Bluetooth
* Xbox Apps
* Remote Desktop
* Windows Defender
* Windows Search
* Snip Sketch
* Microsoft Store
* Voice Recognition
* Mobile Hotspot
* Cheating or cracked software

También muchos instaladores presentaran errores de “missing fonts” o similares como LibreOffice o Photoshop
Para estos se recomienda buscar versiones alternativas o el programa mismo pero portable (esto sera fixeado en la version 1.4 de la iso, actualmente solo la 1.3 esta disponible) 
Antes de instalar asegurate que lo que quieras usar sea compatible con windows 10 versión 1809
Si bien el soporte oficial por parte del desarrollador se encuentra pausado, puedes unirte al [discord](https://discord.io/KernelOS)

## <p align="center">¿Cómo instalar KernelOS?
----
                                                                
                                                                
Instalar KernelOS puede ser un procedimiento difícil para la gente que no está acostumbrada, si lees bien la guia te aseguro que inclusive el mas desentendido podria realizar la instalación

Ahora sí, prosigamos con la instalación

Antes que nada necesitarás el archivo .ISO (Optical disc image)
El link de descarga es el siguiente 
(si tienes el error “no puedes ver ni descargar el archivo actualmente” `recuerda loguearte en google drive` ya que el archivo pesa mas de 1gb y por eso no te dejara bajarlo sin loguearte)
Si el link no te funciona (puede ser porque la versión se actualizó, el owner quito la descarga o otros factores) dentro del discord posiblemente encontraras la version mas actual Rufus
                                                                                                                                                
Antes que nada la versión de rufus que tienes que utilizar es esta ya que otras podrían dar errores


![image](https://user-images.githubusercontent.com/94873456/183282561-08ec44a5-71e0-4fc2-b159-e05df6a023c7.png)


Una vez que abran rufus tendrán una interfaz similar a la siguiente, pero en la casilla DEVICE
Puede tener un nombre y almacenamiento (GB) 

Una vez que estén en la pantalla ARRASTRAN EL ARCHIVO .ISO A RUFUS
Un video referencial x si no entienden

## <p align="center">OPCIONES DE RUFUS
----                                              
                                                                       
                                                                      

“Partition scheme and target system type”
Asegurate de que esté en “GPT partition scheme for UEFI”
“File system”
Asegurate de que este en “NTFS” (si tienes un error al bootear, puedes reemplazarlo por FAT32)

Todas las demás opciones dejarlas como vienen después de configurar las dos opciones anteriores en orden

## <p align="center">PRIMER PASO TERMINADO!!!
----
                                                                      
                                                                      
Actualmente terminaste el paso 1 de la instalación no solo de KernelOS, si no de cualquier Sistema operativo en general, conseguir un pendrive booteable.
El siguiente paso una vez que ya dispones del pendrive booteable es
### BOOTEAR EL PENDRIVE
----
                                                                        
                                                                        
Cuando ya tienes el pendrive booteable, solo queda bootearlo pero, ¿cómo bootear un pendrive?
Para esto tendrás que acceder a las BOOT OPTIONS de tu bios, si tu bios es antigua puede ser que no tengas esa opción, pero la que siempre tendrás es “boot priority”, aquí unos ejemplos
### BOOT PRIORITY
----
                                                                           
![image](https://user-images.githubusercontent.com/94873456/183282572-93ef81ca-2071-42b6-8566-d858064934a3.png)



### BOOT OPTIONS
----


![image](https://user-images.githubusercontent.com/94873456/183282583-4520aebf-268c-49f8-b5e0-4194f8ea43c1.png)


## <p align="center">PASO DOS COMPLETADO, PENDRIVE BOOTEADO
                                                                
                                                                



![image](https://user-images.githubusercontent.com/94873456/183282596-3fa6db16-e249-43d1-a88b-b711751bad4b.png)


En esta parte la cantidad de particiones y discos no serán las mismas para todos pero esto no es relevante

En esta pantalla tendrás que ingresar la siguiente combinación de teclas: SHIFT + F10
Si tienes una notebook esta combinación puede ser SHIFT+FN+F10
Una vez apretada esta combinación de teclas, entrar en una pantalla negra en la que puedes escribir, primero tendrás que escribir DISKPART obviamente después de cada comando que pondre aqui tendras que apretar enter, luego del comando diskpart tendras que introducir el comando LIST DISK y obtendrás una lista con tu cantidad de discos + tu pendrive


![image](https://user-images.githubusercontent.com/94873456/183282606-2d553351-a6f2-42b4-97f1-3fed8893b1e4.png)


En este caso yo dispongo de 2 discos y un pendrive que generalmente será la última opción, en este caso DISK 2.

Una vez que consigas la cantidad total de discos que dispone tu PC, tendrás que introducir los siguientes comandos

Donde X es igual a tu disco

select disk X
clean
convert gpt

Si dispones de más de un disco tendrás que hacer el procedimiento según la cantidad de discos
Reemplazando por ejemplo si tienes 2 discos: 
la x = 0, hacer el procedimiento(los 3 comandos mencionados arriba) y luego x = 1 y volver a hacer el procedimiento de 3 comandos

Una vez terminado con todo esto (formatear los discos y convertirlos a formato GPT)
Cerraremos la ventana negra desde arriba a la derecha 

Con esto volveremos a donde estabamos originalmente sin diferencia, pero al darle a REFRESH abajo a la izquierda del cuadro solo nos saldrá la cantidad  de discos de nuestro PC,
Por ejemplo 1

Seleccionaremos el disco donde queramos instalar el sistema operativo y daremos click en “NEW” y luego en “NEXT”

Con esto se nos quedará el disco dividido en aproximadamente 4 particiones, clickeamos la que diga a su derecha “PRIMARY” y luego abajo a la derecha “next”

Una vez terminado esto el sistema operativo empezará a instalarse


![image](https://user-images.githubusercontent.com/94873456/183282612-29ddb6ec-de76-45a4-987b-4824ba0bf14b.png)


Si booteaste el pendrive por el medio “Boot Priority” recuerda desconectar el pendrive una vez que el proceso haya terminado

Una vez terminado se booteara por primera vez nuestro nuevo sistema operativo, KernelOS

## <p align="center">PASO TRES, WINDOWS INSTALADO
----
                                                                    
                                                                    
Una vez que el windows haya booteado por primera vez, tendremos que completar el script inicial, este es segun la eleccion del usuario completamente, lee bien las opciones y si no sabes que son no las actives

## <p align="center">PASO CUATRO, SCRIPT FINALIZADO
----
                                                              
                                                              
Una vez que hayas finalizado el script inicial y se haya reiniciado tu PC serás capaz de usar kernelOS pero todavía faltan cosas

No tengo wifi, que hago?
(si te aparecen las redes wifi pero no te deja escribir la contraseña, simplemente apreta la tecla WINDOWS + la tecla R (win+r) ,escribe ctfmon.exe y dale enter y te dejara)	
Es normal que no tengas wifi en kernelOS al inicio, ya que estos necesitan drivers de wifi, pero ¿como consigo mis drivers?
Estos pueden ser conseguidos al ser buscados por HARDWARE ID, para conseguir nuestro hardware id haremos lo siguiente


Apretamos la combinación “WINDOWS+X” y bajaremos con las flechas hasta “device manager” 
Una vez dentro iremos a “Other Devices” y buscaremos “Network Controller” , le damos segundo click, properties, iremos a “Details” y en la casilla de seleccion pondremos “hardware ids” y tendremos algo asi:


![image](https://user-images.githubusercontent.com/94873456/183282622-71a0a08b-92bc-4720-800c-a2525786d1ec.png)


Segundo click en la primera opción y copiar, la mia es “PCI\VEN_10EC&DEV_8168&SUBSYS_86771043&REV_15” pero la suya será distinta
Ahora entraremos en esta página (https://driverpack.io/es/catalog) desde otra pc o desde un celular y ingresamos nuestro hardware id, aquí un ejemplo


![image](https://user-images.githubusercontent.com/94873456/183282632-62574eda-cc7b-4309-80cd-8be7d9867f4c.png)


Y le damos “Buscar”
Ahora tendremos una pantalla similar a esta


![image](https://user-images.githubusercontent.com/94873456/183282640-5777faf2-8afa-4d30-b709-8945a2eedec4.png)


Da click en “Download ZIP”
Y obtendrás un archivo zip, mueve este desde tu otra pc con un pendrive o desde tu telefono con un cable USB a tu pc sin internet, al extraer el zip obtendras algo con muchas carpetas y al final un aproximado de 3 archivos, un .INF, un .SYS y un .CAT
Para actualizar nuestros drivers tendremos que hacer el procedimiento que ya hicimos antes para obtener nuestro “HARDWARE ID” pero en vez de ir a esa pestaña iremos a “driver” y luego “update driver”


![image](https://user-images.githubusercontent.com/94873456/183282651-2ae5a945-255c-4c56-becc-5f8c3e10704b.png)

![image](https://user-images.githubusercontent.com/94873456/183282663-ab00f423-cee3-4b91-9ced-bf31b790397a.png)

![image](https://user-images.githubusercontent.com/94873456/183282676-406626c1-3280-4678-9b0d-20cff029c397.png)

![image](https://user-images.githubusercontent.com/94873456/183282691-3cc90b7c-c708-411a-a321-1ac6dded8100.png)

![image](https://user-images.githubusercontent.com/94873456/183282702-e7699152-99e1-4d3b-9e22-b6ec80d038ef.png)


NOS MOVEMOS HASTA LA CARPETA DONDE EXTRAIMOS EL ZIP HASTA LLEGAR AL .INF


![image](https://user-images.githubusercontent.com/94873456/183282709-60d5d588-bb0e-4f22-a41c-81fadfb49874.png)

![image](https://user-images.githubusercontent.com/94873456/183282722-6c022e20-2c66-4d99-b348-475757c5c70b.png)

![image](https://user-images.githubusercontent.com/94873456/183282732-98901e7b-c6eb-4cf9-8cd2-58e0c1047b5e.png)


WIFI SOLUCIONADO
Con esto nuestro problema de WIFI / Ethernet será solucionado

COMO INSTALO LOS DRIVERS DE MI PLACA?
Para instalar los drivers de tu placa sigue lo siguiente:  
<br/><br/><br/>

#### AMD
----
Para amd podrás instalar los drivers de forma manual o automática, ambas son útiles.
De forma manual puedes sacar el panel de AMD, [aqui te dejo mi video](https://www.youtube.com/watch?v=pYWBeQIqFZU) te dejo un video de como deblotear los drivers de AMD, esto no es un debloteo serio ya que en si solo borro un par de archivos y no modificó el .INF que es lo realmente importante, pero esto es para usuarios avanzados y no es necesario para nada<br/><br/><br/>
#### NVidia
----
En nvidia es siempre 100% recomendado usar NVCLEANINSTALL
Este permite deblotear los drivers de nvidia de forma “automática”
[Aqui](https://youtu.be/THX6yO0hjx8) un link de como instalar los drivers



## <p align="center"> Final
----
Aquí termina la guia para usuarios básicos, si no eres un entendido no hace falta que pases de aquí ya que si bien lo que mostraré es una guia del post install de KernelOS, puede dar fallas si no se hace bien y dejar tu windows inutilizable haciéndote que tengas que repetir todo este proceso

## <p align="center"> Post Install
----
una guia completa del [post install](https://docs.google.com/document/d/1KvuhSwrzqJYDqTUY7EZyTFgZ2sjc0eCCmEeoblq3ZCo/edit), hecha por varios usuarios de KernelOS, para usuarios avanzados
