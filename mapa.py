class Mapa(object):
	def __init__ (self,ancho,alto):
		self.ancho=ancho
		self.alto=alto
		self.monedas=[]
		self.robot=None
	def asignar_robot(self,robot):
		self.robot=robot
	def agregar_monedas(self,monedas):
		self.monedas.append()
		return monedas
		mapa_ancho=80
		mapa_largo=25
	def cargar_instruciones(nombre_archivo):
		lista = []
		ins_file = open(nombre_archivo)
		for linea in ins_file: 
			lista.append(list(linea.strip()))
		return (lista)

	