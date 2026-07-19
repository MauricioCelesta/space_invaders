import pygame
import os

IMAGEN_BALA = pygame.image.load(os.path.join('img', 'bullet_image.png'))


class Juego:
    def __init__(self, fuente, fps, contador, ventana, vidas, ancho_pantalla, alto_pantalla, balas=0, reloj=None):
        self.fuente = fuente
        self.ventana = ventana
        self.alto = alto_pantalla
        self.ancho = ancho_pantalla
        self.balas = balas
        self.imagen_bala = IMAGEN_BALA
        self.vidas = vidas
        self.fps = fps
        self.reloj = reloj if reloj is not None else pygame.time.Clock()
        self.contador = contador

    def salir(self):
        se_solicito_salir = False
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                se_solicito_salir = True
        return se_solicito_salir

    def fin_del_juego(self):
        if self.vidas <= 0:
            self.contador = 0
            while True:
                self.reloj.tick(self.fps)
                etiqueta_perdiste = self.fuente.render('Game Over', 1, (255, 255, 255))
                self.ventana.blit(
                    etiqueta_perdiste,
                    ((self.ancho - etiqueta_perdiste.get_width()) / 2,
                     (self.alto - etiqueta_perdiste.get_height()) / 2)
                )
                pygame.display.update()
                self.contador += 1
                if self.contador == self.fps * 3:
                    break
            return True
        else:
            return False