def cargar_mapa(mapa):
	lista=[]
	m=open("mapa_1.txt")
	for linea in m:
		linea=list(linea.strip())
		linea=lista.append(linea)
	return(lista)

