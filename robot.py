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
		if self.direccion=="UP":
			self.y-=1
		if self.direccion=="right":
			self.x+=1
		if self.direccion=="down":
			self.y-=1
		else:
			self.x+=1
	def dibujar(self):
		if self.direccion="UP":
			return "^"
		elif self.direccion="left":
			return ">"
		elif self.direccion="right":
			return "<"                                
		elif self.direccion="down":
			return "v"
	def rotar (self):
		if self.direccion=="UP":
			self.direccion=="right":
		if self.direccion="right":
			self.direccion=="left"
		if self.direccion=="left":
			self.direccion="down"
		if self.direccion=="down"
			self.direccion="UP"
	def pick(self):