class Mapa(object):
	def __init__ (self,ancho,alto):
		self.ancho=ancho
		self.alto=alto
		self.monedas=[]
		self.robot=None
	def cargar_robot(self,robot):
		self.robot=robot
	def agregar_monedas(self,moneda):
		self.monedas.append(moneda)
	def contar_moneda(self,x,y):
		contador=0
	def dibujar (self,x,y):
		res=" "
		for x in range(self.ancho):
			for y in range(self.alto):
			for x=self.robot.x and y=self.robot.y:
				res+=self.robot.dibujar()
	def quitar_monedas(self,moneda):
	def contar_monedas(self,x,y):
		contador=0
		




		