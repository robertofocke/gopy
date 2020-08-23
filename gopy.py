import requests

headers={"User-Agent": "Mozilla"}
emails=input("lista de posibles usuarios: ")
f=open(emails,"r")
for linea in f:
	respuesta=requests.get("https://mail.google.com/mail/gxlu?email="+linea[:-1],headers=headers)
	
	if 'Set-Cookie' in respuesta.headers:
		print (linea[:-1])
f.closed
	
