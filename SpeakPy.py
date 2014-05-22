#!/usr/bin/python3

import subprocess, string, time, configparser

def escuchar():
	#Grabar audio del microfono, convertirlo a FLAC
	#y enviarlo a Google quien devolvera un JSON
	envio = subprocess.Popen(["./STT.sh"], shell=True, universal_newlines=True, stdout=subprocess.PIPE)
	texto = envio.communicate()[0]
	texto = texto.strip('\n')
	return texto

def decir(frase):
	#Enviar texto a Google y reproducir el audio devuelto
	url="http://translate.google.com.mx/translate_tts?tl=es&q=" + frase
	reproduccion = subprocess.call(['mplayer', '-ao', 'alsa', '-noconsolecontrols', url], shell=False)

def buscar(texto):
   existe = False
   archivo = open("commands.txt")
   linea = archivo.readline()
   while linea != "":
      if linea.find('!') >= 0:
      	linea = linea.strip('!')
      	linea = linea.rstrip('\n')
      	linea = linea.split('=')
      	if texto.find(linea[0]) >= 0:
      		existe = True
      		comando = linea[1]
      		comando.find('+')
      		comando = comando.split('+')
      		return comando
      		#proceso = subprocess.call(comando, shell=False)
      linea = archivo.readline()
   if not existe:
   		return 'no existe'
   archivo.close()

while True:
	clave = escuchar()
	print('Escuche:' + clave)
	if clave == 'Janis':
		decir("Dime Ricardo")
		orden = escuchar()
		comando = buscar(orden)
		if comando != 'no existe':
			proceso = subprocess.Popen(comando, shell=False)
			#time.sleep(3)
			while proceso.poll() == None:
				#print('-> ¿Cerrar?')
				terminar = escuchar()
				#print('Terminar:' + terminar)
				if terminar == 'cerrar':
					proceso.kill()
		else:
			decir('comando incorrecto')