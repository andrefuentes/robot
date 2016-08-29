import time
class Robot(object):
	def __init__(self,x,y):
		self.monedas=monedas
		self.y=y
		self.x=x
		self.fichas=0
		self.direccion="UP"
		self.mapa=None
	def colocar_en_mapa(self,mapa):
		self.mapa=mapa
	def mover(self):
		if self.direccion==0 and self.x<80:
			self.x+=1
		if self.direccion==80 and self.y<25:
			self.y+=1
		if self.direccion==80 and self.y<25:
			self.x-=1
		if self.direccion==0 and self.x<80:
			self.y-=1
	def rotar(self):
		if self.direccion="^"	
			return "^"
		elif self.direccion=">"
			return ">"
		elif self.direccion="<"
			return "<"
		elif self.direccion="v"
			return "v"
	def pick(self):
		for x in len(mapa.lista):
		return monedas
class Mapa(object):
	def __init__ (self,ancho,alto):
		self.ancho=ancho
		self.alto=alto
		self.monedas=[]
		self.robot=None
	def asignar_robot(self,robot):
		self.robot=robot
	def agregar_monedas(self,monedas):
		return monedas
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
class Monedas (object):
	def __init__ (self,x,y):
		self.x=x
		self.y=y
<
>
v
^
