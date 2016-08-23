def cargar_mapa(mapa):
	lista=[]
	m=open(mapa/"mapa_1.txt")
	for linea in m:
		lista.append(list(linea.strip()))
	return(lista)


