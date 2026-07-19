import pygame
from ship import Barco
from bala import Bala
from config import WIDTH, HEIGHT, PLAYER_IMAGE, BULLET_IMAGE

IMAGEN_JUGADOR = pygame.image.load(PLAYER_IMAGE).convert_alpha()
IMAGEN_BALA_JUGADOR = pygame.image.load(BULLET_IMAGE).convert_alpha()


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
        self.mascara = pygame.mask.from_surface(self.imagen_nave)

    def mover(self):
        teclas = pygame.key.get_pressed()
        if (teclas[pygame.K_UP] or teclas[pygame.K_w]) and (self.y > 0):
            self.y -= self.velocidad_y
        elif (teclas[pygame.K_DOWN] or teclas[pygame.K_s]) and (self.y < HEIGHT - self.imagen_nave.get_height() - 60):
            self.y += self.velocidad_y
        if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (self.x < WIDTH - self.imagen_nave.get_width()):
            self.x += self.velocidad_x
        elif (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) and (self.x > 0):
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