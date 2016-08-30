class Monedas (object):
	def __init__ (self,x,y):
		self.x=x
		self.y=y
	def imprimir_robot(x,y):
		r=(" " * cargar_mapa)*y
		r+=" " * x +" * "
		r+=" "+cargar_mapa*(mapa_largo+(y+1))
		return(r)
		steps=19
		for i in range(steps)
		time.sleep(0.3)
		print (imprimir_robot(5+i,i))