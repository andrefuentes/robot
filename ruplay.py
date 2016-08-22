def mapas():
	lista=[]
	m=open("mapa_1.txt")
	for linea in m:
		lista.append(list(linea.strip()))
	print(lista)