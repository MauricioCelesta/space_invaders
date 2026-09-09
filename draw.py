import pygame as pg
from config import BACKGROUND_IMAGE, WHITE

FONDO = pg.image.load(BACKGROUND_IMAGE).convert()


class Dibujo:
    def __init__(self, ventana):
        self.ventana = ventana
        self.fuente = pg.font.SysFont('comicsans', 50)

    def dibujar(self, juego, jugador, enemigos, fps, puntos):
        self.ventana.blit(FONDO, (0, 0))
        jugador.disparar(self.ventana)

        for enemigo in enemigos[:]:
            enemigo.dibujar(self.ventana)

        jugador.dibujar(self.ventana)

        juego.dibujar_hud()
        etiqueta_puntos = self.fuente.render(f'Puntos: {puntos}', 1, WHITE)
        self.ventana.blit(etiqueta_puntos, ((self.ventana.get_width() - etiqueta_puntos.get_width()) / 2, 10))
        pg.display.update()