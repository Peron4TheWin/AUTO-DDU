
# AUTO DDU 
 Esto es un auto [DDU](https://www.guru3d.com/files-details/display-driver-uninstaller-download.html) compatible con windows 10, solamente abres el exe y tus drivers de video se desintalaran completamente para dejarte espacio a una nueva instalacion de drivers de video limpios.

&nbsp;

# tips - sugerencias y problemas
desconozco si tiene algun problema actualmente, pero no lo creo, si tienes algun problema o sugerencia puedes abrir un issue en el repositorio de github o hablarme directamente por discord `peron#0268`.



algunos tips
- Auto DDU no desactiva windows defender, asi que si tienes windows defender activado, debes desactivarlo para que tus drivers no se reinstalen de forma automatica.

- Si reinicias tu pc en modo seguro con el comando `bcdedit /set {current} safeboot minimal` y luego abres el auto DDU, haras el proceso mas seguro y rapido. 
(usa el comando `bcdedit /deletevalue {current} safeboot` para desactivar el modo seguro)
