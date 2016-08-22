def cargar_instruciones(nombre_archivo):
	lista = []
	ins_file = open(nombre_archivo)
	for linea in ins_file: 
		lista.append(list(linea.strip()))
	return (lista)
	



