import time
mapa_ancho=80
mapa_largo=25
def imprimir_robot(x,y):
	r=(" " * cargar_mapa)*y
	r+=" " * x +" * "
	r+=" "+cargar_mapa*(mapa_largo+(y+1))
	return(r)
steps=19
for i in range(steps)
	time.sleep(0.3)
	print (imprimir_robot(5+i,i))
def cargar_instruciones(nombre_archivo):
	lista = []
	ins_file = open(nombre_archivo)
	for linea in ins_file: 
		lista.append(list(linea.strip()))
	return (lista)
	



