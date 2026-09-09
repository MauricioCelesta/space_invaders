import pygame as pg
import sys
import os
import webbrowser
from config import WIDTH, HEIGHT, WHITE, BLACK, GRAY, RED, MENU_BACKGROUND_IMAGE


class MenuAcercaDe:
    def __init__(self, ventana, volver_mtd):
        self.ventana = ventana
        self.volver_mtd = volver_mtd

    def cargar_imagen(self, nombre_archivo):
        ruta = os.path.join("img", nombre_archivo)
        return pg.image.load(ruta).convert_alpha()

    def mostrar_texto(self, texto, fuente, color, superficie, x, y):
        texto_objeto = fuente.render(texto, True, color)
        rectangulo_texto = texto_objeto.get_rect()
        rectangulo_texto.topleft = (x, y)
        superficie.blit(texto_objeto, rectangulo_texto)

    def dibujar_boton(self, texto, fuente, color, superficie, x, y, ancho, alto):
        pg.draw.rect(superficie, color, (x, y, ancho, alto))
        texto_ancho, texto_alto = fuente.size(texto)
        texto_x = x + (ancho - texto_ancho) // 2
        texto_y = y + (alto - texto_alto) // 2
        self.mostrar_texto(texto, fuente, BLACK, superficie, texto_x, texto_y)

    def mostrar_contenido(self, contenido, fuente_contenido, y_desplazamiento):
        espacio_horizontal_disponible = WIDTH - 100
        for linea in contenido.split('\n'):
            palabras = linea.split()
            texto_linea = ""
            for palabra in palabras:
                texto_linea_temp = texto_linea + palabra + " "
                texto_ancho_temp = fuente_contenido.size(texto_linea_temp)[0]
                if texto_ancho_temp < espacio_horizontal_disponible:
                    texto_linea = texto_linea_temp
                else:
                    self.mostrar_texto(
                        texto_linea.strip(), fuente_contenido, WHITE, self.ventana,
                        (WIDTH - fuente_contenido.size(texto_linea.strip())[0]) // 2, y_desplazamiento
                    )
                    y_desplazamiento += fuente_contenido.size(texto_linea.strip())[1]
                    texto_linea = palabra + " "
            self.mostrar_texto(
                texto_linea.strip(), fuente_contenido, WHITE, self.ventana,
                (WIDTH - fuente_contenido.size(texto_linea.strip())[0]) // 2, y_desplazamiento
            )
            y_desplazamiento += fuente_contenido.size(texto_linea.strip())[1]

    def mostrar_menu(self):
        self.ventana.fill(BLACK)

        fondo = self.cargar_imagen(MENU_BACKGROUND_IMAGE)
        fondo = pg.transform.scale(fondo, (WIDTH, HEIGHT))
        self.ventana.blit(fondo, (0, 0))

        titulo_texto = "Acerca De"
        titulo_fuente = pg.font.Font(None, 48)
        titulo_ancho = titulo_fuente.size(titulo_texto)[0]
        titulo_x = (WIDTH - titulo_ancho) // 2
        self.mostrar_texto(titulo_texto, titulo_fuente, WHITE, self.ventana, titulo_x, 50)

        subtitulo_texto = "Space Invaders Hybridge"
        subtitulo_fuente = pg.font.Font(None, 36)
        subtitulo_ancho = subtitulo_fuente.size(subtitulo_texto)[0]
        subtitulo_x = (WIDTH - subtitulo_ancho) // 2
        self.mostrar_texto(subtitulo_texto, subtitulo_fuente, WHITE, self.ventana, subtitulo_x, 120)

        contenido = (
            "Explora la galaxia y aprende Programacion Orientada a Objetos (POO) "
            "con nuestro emocionante Space Invaders!\n"
            "Cada nave, cada disparo, todo es un objeto interactivo!\n"
            "Unete a nosotros para una experiencia divertida y educativa en este "
            "emocionante cruce de juego y aprendizaje.\n"
            "Preparate para salvar el universo!"
        )
        fuente_contenido = pg.font.Font(None, 30)
        y_desplazamiento = max(200, subtitulo_fuente.size(subtitulo_texto)[1] + 120)
        self.mostrar_contenido(contenido, fuente_contenido, y_desplazamiento)

        texto_enlace = "Haz clic aqui para visitar Hybridge!"
        fuente_enlace = pg.font.Font(None, 30)
        enlace_ancho = fuente_enlace.size(texto_enlace)[0]
        enlace_x = (WIDTH - enlace_ancho) // 2
        self.mostrar_texto(texto_enlace, fuente_enlace, RED, self.ventana, enlace_x, 500)

        self.dibujar_boton("<", pg.font.Font(None, 36), GRAY, self.ventana, 20, 20, 50, 50)
        pg.display.update()

    def ejecutar(self):
        self.mostrar_menu()

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
                        elif 300 <= y <= 520:
                            webbrowser.open("https://hybridge.education")