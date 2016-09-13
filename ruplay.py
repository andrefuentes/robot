import time
from monedas import Monedas
from mapa import Mapa 
from robot import Robot
from utilidades import cargar_mapa,cargar_instruciones
mapa="mapas/mapa_1.txt"
ins="instrucciones/intruciones.txt"
mapa= cargar_mapa(mapa)
for y in range(mapa.altura):
	for x in range(mapa.ancho):
		if mapa ==" ":
			robocop= Robot(x,y)
		else:
			cantidad_de_monedas= int(mapa[y][x])
			for i in range(cantidad_monedas):
				moneda = monedas(y,x)
				mapa.agregar_moneda(monedas)
print (mapa.dibujar())
for i in instrucciones:
	if i == "MOVER":
		robocops.mover()
	elif i == "ROTAR":
		robocop.rotar()
	else:
		robocop.recoger_moneda(robocop.x, robocop.y)
	print (mapa.dibujar())
	print (robocop.x)
	print (robocop.y)			