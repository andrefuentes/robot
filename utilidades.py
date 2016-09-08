
def cargar_mapa(mapa):
	lista=[]
	m=open("robot/mapa_1.txt")
	for linea in m:
		linea=list(linea.strip())
		linea=lista.append(linea)
	return(lista)
def cargar_instruciones(nombre_archivo):
	lista = []
	ins_file = open(nombre_archivo)
	for linea in ins_file: 
		lista.append(list(linea.strip()))
	return (lista)
	

	
