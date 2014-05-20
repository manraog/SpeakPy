#!/usr/bin/python3

import subprocess, string, time, configparser

def escuchar():
	#Grabar audio del microfono, convertirlo a FLAC
	#y enviarlo a Google quien devolvera un JSON
	print('Grabando voz...')
	voz_raw = subprocess.Popen(['arecord', '-D', 'plughw:1,0', '-q', '-f', 'cd', '-t', 'wav', '-d', '3', '-r', '16000'], shell=False, stdout=subprocess.PIPE)
	voz_flac = subprocess.call(['flac', '-', '-f', '--best', '--sample-rate', '16000', '-s', '-o', 'voz.flac'], shell=False, stdin=voz_raw.stdout)
	print('Convirtiendo voz a texto...')
	envio = subprocess.Popen('wget -q -U "Mozilla/5.0" --post-file voz.flac --header "Content-Type: audio/x-flac; rate=16000" -O - "https://www.google.com.mx/speech-api/v2/recognize?output=json&lang=es&key=AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw"', shell=True, universal_newlines=True, stdout=subprocess.PIPE)
	texto = envio.communicate()[0]
	texto = texto.split('"')
	if len(texto) < 9:
		return " "
	else:
		return texto[9] 

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
	if clave == 'Janis':
		decir("Dime Ricardo")
		orden = escuchar()
		comando = buscar(orden)
		if comando != 'no existe':
			proceso = subprocess.Popen(comando, shell=False)
			time.sleep(2)
			while proceso.poll() == None:
				print('estoy en while')
				terminar = escuchar()
				if terminar == 'cerrar':
					proceso.kill()
		else:
			decir('comando incorrecto')