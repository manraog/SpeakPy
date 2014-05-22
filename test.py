#!/usr/bin/python3

import subprocess, string, time, configparser

def escuchar():
	#Grabar audio del microfono, convertirlo a FLAC
	#y enviarlo a Google quien devolvera un JSON
	envio = subprocess.Popen(["./STT.sh"], shell=True, universal_newlines=True, stdout=subprocess.PIPE)
	texto = envio.communicate()[0]
	texto = texto.strip('\n')
	print(texto)

escuchar()