import pygame as pg


class Bala:
    def __init__(self, x, y, imagen):
        self.x = x
        self.y = y
        self.imagen = imagen
        self.mascara = pg.mask.from_surface(self.imagen)

    def dibujar(self, ventana):
        ventana.blit(self.imagen, (self.x, self.y))

    def mover(self, velocidad):
        self.y += velocidad

    def colision(self, objeto):
        desplazamiento = (int(self.x - objeto.x - 30), int(self.y - objeto.y - 20))
        return self.mascara.overlap(objeto.mascara, desplazamiento)