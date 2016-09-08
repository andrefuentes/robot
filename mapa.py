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
		def dibujar(self):
        resultado = ""
        for y in range(self.altura):
            for x in range(self.ancho):
                if x == self.robot.x and y == self.robot.y:
                    resultado += self.robot.dibujar()

                elif self.contar_monedas_en(x, y) > 0:
                    resultado += self.contar_monedas_en(x, y)
                else:
                    resultado += " "

            resultado += "\n"

        return resultado
	def quitar_monedas(self,x,y):
		quitar_monedas-=1
			for remover in range(len(self.monedas)):
				if moneda.x=x and moneda.y=y
					moneda=self.monedas[remover]
					self.moneda.pop(moneda)
					break		
	def contar_monedas(self,x,y):
		contador=0
		for monedas in self.monedas:
			if moneda.x==x and moneda.y==y:
				contador+=1
		return contador
	def 




		