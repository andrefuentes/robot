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
		if self.direccion="UPSS":
			return "^"
		elif self.direccion=">":
			return ">"
		elif self.direccion="<":
			return "<"                                
		elif self.direccion="v":
			return "v"
	def pick(self):
		for x in len(mapa.lista):
		
		return monedas

^
