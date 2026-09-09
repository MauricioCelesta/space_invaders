import pygame as pg
import sys
import os
from config import WIDTH, HEIGHT, WHITE, BLACK, GRAY, RED, MENU_BACKGROUND_IMAGE, SCORES_FILE


class MenuPuntajes:
    def __init__(self, ventana, volver_mtd):
        self.ventana = ventana
        self.volver_mtd = volver_mtd

    def cargar_puntajes(self, archivo):
        puntajes = []
        try:
            with open(archivo, 'r') as file:
                for linea in file:
                    nombre, puntaje = linea.strip().split(',')
                    puntajes.append((nombre, int(puntaje)))
        except FileNotFoundError:
            print(f"No se encontro el archivo {archivo}")
        return sorted(puntajes, key=lambda x: x[1], reverse=True)[:5]

    def cargar_imagen(self, nombre_archivo):
        ruta = os.path.join("img", nombre_archivo)
        return pg.image.load(ruta).convert_alpha()

    def mostrar_texto(self, texto, fuente, color, superficie, x, y):
        texto_objeto = fuente.render(texto, True, color)
        rectangulo_texto = texto_objeto.get_rect()
        rectangulo_texto.center = (x, y)
        superficie.blit(texto_objeto, rectangulo_texto)

    def dibujar_boton(self, texto, fuente, color, superficie, x, y, ancho, alto):
        pg.draw.rect(superficie, color, (x, y, ancho, alto))
        self.mostrar_texto(texto, fuente, BLACK, superficie, x + ancho / 2, y + alto / 2)

    def mostrar_puntajes(self, puntajes):
        self.ventana.fill(BLACK)

        fondo = self.cargar_imagen(MENU_BACKGROUND_IMAGE)
        fondo = pg.transform.scale(fondo, (WIDTH, HEIGHT))
        self.ventana.blit(fondo, (0, 0))

        self.mostrar_texto("Mejores Puntajes", pg.font.Font(None, 48), WHITE, self.ventana, WIDTH // 2, 50)
        self.mostrar_texto("Space Invaders Hybridge", pg.font.Font(None, 36), WHITE, self.ventana, WIDTH // 2, 120)

        if not puntajes:
            self.mostrar_texto("Aun no hay registros", pg.font.Font(None, 36), RED, self.ventana, WIDTH // 2, HEIGHT // 2)
        else:
            y_desplazamiento = 250
            for i, (nombre, puntaje) in enumerate(puntajes, 1):
                color_texto = WHITE if i == 1 else RED
                tamano_fuente = 42 if i == 1 else 36
                self.mostrar_texto(
                    f"{i}. {nombre}: {puntaje}", pg.font.Font(None, tamano_fuente),
                    color_texto, self.ventana, WIDTH // 2, y_desplazamiento
                )
                y_desplazamiento += 60

        self.dibujar_boton("<", pg.font.Font(None, 36), GRAY, self.ventana, 20, 20, 50, 50)
        pg.display.update()

    def ejecutar(self):
        puntajes = self.cargar_puntajes(SCORES_FILE)
        self.mostrar_puntajes(puntajes)

        while True:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif evento.type == pg.MOUSEBUTTONDOWN:
                    if evento.button == 1:
                        x, y = evento.pos
                        if 20 <= x <= 70 and 20 <= y <= 70:
                            self.volver_mtd()
                            return