import pygame as pg
import os
from config import WIDTH, HEIGHT, WHITE, BLACK, GRAY, MENU_BACKGROUND_IMAGE, SCORES_FILE


class PantallaNombre:
    def __init__(self, ventana, puntaje, terminar_mtd):
        self.ventana = ventana
        self.fuente_titulo = pg.font.Font(None, 30)
        self.fuente_subtitulo = pg.font.Font(None, 36)
        self.fuente_input = pg.font.Font(None, 36)
        self.texto_input = ""
        self.input_activo = False
        self.fondo = self.cargar_imagen(MENU_BACKGROUND_IMAGE)
        self.puntaje = puntaje
        self.terminar_mtd = terminar_mtd

    def cargar_imagen(self, nombre_archivo):
        ruta = os.path.join("img", nombre_archivo)
        return pg.transform.scale(pg.image.load(ruta).convert(), (WIDTH, HEIGHT))

    def escribir_en_archivo(self, nombre_archivo, contenido):
        ruta = os.path.join(os.getcwd(), nombre_archivo)
        try:
            with open(ruta, 'a') as archivo:
                archivo.write(contenido + '\n')
        except PermissionError:
            print(f"No tiene permisos para escribir en '{os.path.dirname(ruta)}'")
        except Exception as e:
            print(f"Error al escribir en el archivo: {e}")

    def _guardar_y_salir(self):
        nombre = self.texto_input.strip() if self.texto_input.strip() else "Jugador"
        self.escribir_en_archivo(SCORES_FILE, f"{nombre},{self.puntaje}")
        self.terminar_mtd()

    def ejecutar(self):
        titulo_texto = "Felicidades! Superaste el maximo puntaje. Ingresa tu nombre:"
        titulo_render = self.fuente_titulo.render(titulo_texto, True, WHITE)
        titulo_rect = titulo_render.get_rect(center=(WIDTH / 2, 50))

        subtitulo_texto = "Space Invaders Hybridge"
        subtitulo_render = self.fuente_subtitulo.render(subtitulo_texto, True, WHITE)
        subtitulo_rect = subtitulo_render.get_rect(center=(WIDTH / 2, 100))

        caja_input = pg.Rect(200, 200, 400, 50)
        boton_aceptar = pg.Rect(300, 300, 200, 50)

        while True:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    pg.quit()
                    return
                if evento.type == pg.MOUSEBUTTONDOWN:
                    if caja_input.collidepoint(evento.pos):
                        self.input_activo = not self.input_activo
                    else:
                        self.input_activo = False
                    if boton_aceptar.collidepoint(evento.pos):
                        self._guardar_y_salir()
                        return
                if evento.type == pg.KEYDOWN and self.input_activo:
                    if evento.key == pg.K_RETURN:
                        self._guardar_y_salir()
                        return
                    elif evento.key == pg.K_BACKSPACE:
                        self.texto_input = self.texto_input[:-1]
                    else:
                        self.texto_input += evento.unicode

            self.ventana.blit(self.fondo, (0, 0))

            pg.draw.rect(self.ventana, BLACK, titulo_rect)
            self.ventana.blit(titulo_render, titulo_rect)

            pg.draw.rect(self.ventana, BLACK, subtitulo_rect)
            self.ventana.blit(subtitulo_render, subtitulo_rect)

            color_input = GRAY if not self.input_activo else WHITE
            pg.draw.rect(self.ventana, color_input, caja_input, 2)
            texto_superficie = self.fuente_input.render(self.texto_input, True, WHITE)
            self.ventana.blit(texto_superficie, (caja_input.x + 5, caja_input.y + 5))

            pg.draw.rect(self.ventana, GRAY, boton_aceptar)
            texto_boton = self.fuente_input.render("Aceptar", True, BLACK)
            texto_boton_rect = texto_boton.get_rect(center=boton_aceptar.center)
            self.ventana.blit(texto_boton, texto_boton_rect)

            pg.display.flip()