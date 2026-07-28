import pygame as pg
from ship import Barco
from bala import Bala
from config import WIDTH, HEIGHT, PLAYER_IMAGE, BULLET_IMAGE

IMAGEN_JUGADOR = pg.image.load(PLAYER_IMAGE).convert_alpha()
IMAGEN_BALA_JUGADOR = pg.image.load(BULLET_IMAGE).convert_alpha()


class Jugador(Barco):
    def __init__(self, x, y, velocidad_x, velocidad_y, salud=100):
        super().__init__(x, y, salud)
        self.imagen_nave = IMAGEN_JUGADOR
        self.imagen_bala = IMAGEN_BALA_JUGADOR
        self.salud_maxima = salud
        self.velocidad_bala = -10
        self.contador_espera_creacion = 0
        self.max_cantidad_balas = 3
        self.velocidad_x = velocidad_x
        self.velocidad_y = velocidad_y
        self.mascara = pg.mask.from_surface(self.imagen_nave)

    def mover(self):
        teclas = pg.key.get_pressed()
        if (teclas[pg.K_UP] or teclas[pg.K_w]) and (self.y > 0):
            self.y -= self.velocidad_y
        elif (teclas[pg.K_DOWN] or teclas[pg.K_s]) and (self.y < HEIGHT - self.imagen_nave.get_height() - 60):
            self.y += self.velocidad_y
        if (teclas[pg.K_RIGHT] or teclas[pg.K_d]) and (self.x < WIDTH - self.imagen_nave.get_width()):
            self.x += self.velocidad_x
        elif (teclas[pg.K_LEFT] or teclas[pg.K_a]) and (self.x > 0):
            self.x -= self.velocidad_x

    def aumentar_velocidad(self):
        if self.velocidad_x < 10:
            self.velocidad_x += 1.25
            self.velocidad_y += 1.25
        elif self.velocidad_x >= 10:
            self.velocidad_x = 10
            self.velocidad_y = 8
        if self.tiempo_espera > 25:
            self.tiempo_espera *= 0.9

    def crear_balas(self):
        if (len(self.balas) < self.max_cantidad_balas) and (self.contador_espera_creacion == 0):
            bala = Bala(self.x, self.y, self.imagen_bala)
            self.balas.append(bala)
            self.contador_espera_creacion = 1
        for bala in self.balas_disparadas:
            if bala.y <= -40:
                self.balas_disparadas.pop(0)

    def actualizar_temporizadores(self):
        if self.contador_espera_bala >= 20:
            self.contador_espera_bala = 0
        elif self.contador_espera_bala > 0:
            self.contador_espera_bala += 1

        if self.contador_espera_creacion >= self.tiempo_espera:
            self.contador_espera_creacion = 0
        elif self.contador_espera_creacion > 0:
            self.contador_espera_creacion += 1

    def disparar(self, ventana):
        teclas = pg.key.get_pressed()

        if teclas[pg.K_SPACE] and (len(self.balas) > 0) and (self.contador_espera_bala == 0):
            self.balas[-1].x = self.x + (self.imagen_nave.get_width() - self.imagen_bala.get_width()) / 2
            self.balas[-1].y = self.y + 10
            self.balas_disparadas.append(self.balas.pop())
            self.contador_espera_bala = 1
            self.contador_espera_creacion = 1

        for bala in self.balas_disparadas:
            bala.mover(self.velocidad_bala)
            bala.dibujar(ventana)

    def detectar_impacto(self, enemigo):
        for bala in self.balas_disparadas:
            if bala.colision(enemigo):
                self.contador_espera_creacion = self.tiempo_espera * 0.8
                return True
        return False