import pygame as pg
import random
from ship import Barco
from config import WIDTH, ENEMY_BLUE_IMAGE, ENEMY_GREEN_IMAGE, ENEMY_PURPLE_IMAGE, SHOT_BLUE_IMAGE, SHOT_GREEN_IMAGE, SHOT_PURPLE_IMAGE

IMAGEN_ENEMIGO_AZUL = pg.image.load(ENEMY_BLUE_IMAGE).convert_alpha()
IMAGEN_ENEMIGO_VERDE = pg.image.load(ENEMY_GREEN_IMAGE).convert_alpha()
IMAGEN_ENEMIGO_MORADO = pg.image.load(ENEMY_PURPLE_IMAGE).convert_alpha()
IMAGEN_DISPARO_AZUL = pg.image.load(SHOT_BLUE_IMAGE).convert_alpha()
IMAGEN_DISPARO_VERDE = pg.image.load(SHOT_GREEN_IMAGE).convert_alpha()
IMAGEN_DISPARO_MORADO = pg.image.load(SHOT_PURPLE_IMAGE).convert_alpha()


class Enemigo(Barco):
    COLOR = {
        'azul': (IMAGEN_ENEMIGO_AZUL, IMAGEN_DISPARO_AZUL),
        'verde': (IMAGEN_ENEMIGO_VERDE, IMAGEN_DISPARO_VERDE),
        'morado': (IMAGEN_ENEMIGO_MORADO, IMAGEN_DISPARO_MORADO),
    }

    def __init__(self, velocidad, x=50, y=50, color='azul', salud=100):
        super().__init__(x, y, salud)
        self.imagen_nave, self.imagen_bala = self.COLOR[color]
        self.mascara = pg.mask.from_surface(self.imagen_nave)
        self.velocidad = velocidad

    def mover(self):
        self.y += self.velocidad

    def crear(self, cantidad):
        enemigos = []
        for _ in range(cantidad):
            enemigo = Enemigo(
                x=random.randrange(20, WIDTH - self.imagen_nave.get_width() - 20),
                y=random.randrange(-1000, -100),
                color=random.choice(['azul', 'verde', 'morado']),
                velocidad=self.velocidad
            )
            enemigos.append(enemigo)
        return enemigos

    def aumentar_velocidad(self):
        self.velocidad *= 1.02