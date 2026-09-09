import pygame as pg
import sys
import os
from config import WIDTH, HEIGHT, WHITE, RED, MENU_BACKGROUND_IMAGE, HYBRIDGE_LOGO


class MenuPrincipal:
    DIRECTORIO_IMAGENES = "img"

    def __init__(self, ventana, iniciar_juego_mtd, iniciar_puntajes_mtd, iniciar_acerca_de_mtd):
        self.ventana = ventana
        self.iniciar_juego_mtd = iniciar_juego_mtd
        self.iniciar_puntajes_mtd = iniciar_puntajes_mtd
        self.iniciar_acerca_de_mtd = iniciar_acerca_de_mtd

    def cargar_imagen(self, nombre_archivo):
        ruta = os.path.join(self.DIRECTORIO_IMAGENES, nombre_archivo)
        return pg.image.load(ruta).convert_alpha()

    def mostrar_texto(self, texto, fuente, color, superficie, x, y):
        texto_objeto = fuente.render(texto, True, color)
        rectangulo_texto = texto_objeto.get_rect()
        rectangulo_texto.center = (x, y)
        superficie.blit(texto_objeto, rectangulo_texto)
        return rectangulo_texto

    def menu_principal(self):
        opciones = ["Iniciar juego", "Puntajes", "Acerca de"]
        opcion_seleccionada = 0
        selector_rect = pg.Rect(0, 0, 300, 50)

        fondo = self.cargar_imagen(MENU_BACKGROUND_IMAGE)
        fondo = pg.transform.scale(fondo, (WIDTH, HEIGHT))

        imagen = self.cargar_imagen(HYBRIDGE_LOGO)
        imagen = pg.transform.scale(imagen, (80, 80))

        while True:
            self.ventana.blit(fondo, (0, 0))
            self.mostrar_texto("Space Invaders", pg.font.Font(None, 64), WHITE, self.ventana, WIDTH // 2, HEIGHT // 4)
            self.mostrar_texto("Hybridge", pg.font.Font(None, 36), WHITE, self.ventana, WIDTH // 2, HEIGHT // 4 + 40)
            self.ventana.blit(imagen, (WIDTH // 2 - 40, HEIGHT // 4 + 60))

            rectangulos_texto = []
            for i, opcion in enumerate(opciones):
                rect_texto = self.mostrar_texto(
                    opcion, pg.font.Font(None, 32), WHITE, self.ventana,
                    WIDTH // 2, HEIGHT // 4 + 90 * (i + 1) + 100
                )
                rectangulos_texto.append(rect_texto)

            selector_rect.centerx = WIDTH // 2
            selector_rect.centery = rectangulos_texto[opcion_seleccionada].centery - 10
            pg.draw.rect(self.ventana, RED, selector_rect, 2)

            pg.display.update()

            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_UP:
                        opcion_seleccionada = (opcion_seleccionada - 1) % len(opciones)
                    elif evento.key == pg.K_DOWN:
                        opcion_seleccionada = (opcion_seleccionada + 1) % len(opciones)
                    elif evento.key == pg.K_RETURN:
                        opcion_elegida = opciones[opcion_seleccionada]
                        if opcion_elegida.lower() == "iniciar juego":
                            self.iniciar_juego_mtd()
                            return
                        elif opcion_elegida.lower() == "puntajes":
                            self.iniciar_puntajes_mtd()
                            return
                        elif opcion_elegida.lower() == "acerca de":
                            self.iniciar_acerca_de_mtd()
                            return