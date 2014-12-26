SpeakPy
===========
SpeakPy es un script hecho en Python que te permitira dar ordenes a tu Raspberry Pi utilizando los servicios de reconocimiento de voz de Google, aunque puede ser usado en cualquier sistema Linux.

Por el momento solo se puede llamar Janis al sistema, se puede cambiar editando el código en Python, en un futuro se agregara la funció desde un archivo de configuración.

Comandos
==========
Las ordenes se encuentran en el archivo commands.txt completamente editable, siempre y cuando se cumpla la siguiente sintaxis:

`![COMANDO DE VOZ]=[COMANDO]`

En el caso de comando con argumentos se sigue la siguiente sintaxis:

`![COMANDO DE VOZ]=[COMANDO]+[ARGUMENTO]`
