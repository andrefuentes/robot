def cargar_mapa(mapa):
	lista=[]
	m=open(mapa,"r")
	for linea in m:
		linea=list(linea.strip())
		linea=lista.append(linea)
	return(lista)

