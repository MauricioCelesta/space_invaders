import pygame as pg
from config import BULLET_IMAGE, SCORES_FILE


class Juego:
    def __init__(self, fuente, fps, vidas, ventana, ancho_pantalla, alto_pantalla, balas=0, reloj=None):
        self.fuente = fuente
        self.ancho = ancho_pantalla
        self.alto = alto_pantalla
        self.fps = fps
        self.vidas = vidas
        self.nivel = 1
        self.contador = 0
        self.ventana = ventana
        self.reloj = reloj if reloj is not None else pg.time.Clock()
        self.balas = balas
        self.imagen_bala = pg.image.load(BULLET_IMAGE).convert_alpha()

        registros = self.leer_registros(SCORES_FILE)
        if len(registros) > 0:
            self.jugador_recordista, self.max_puntaje = registros[0]
        else:
            self.jugador_recordista, self.max_puntaje = None, 0

    def salir(self):
        se_solicito_salir = False
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                se_solicito_salir = True
        return se_solicito_salir

    def fin_del_juego(self):
        if self.vidas <= 0:
            self.contador = 0
            while True:
                self.reloj.tick(self.fps)
                etiqueta_perdiste = self.fuente.render('GAME OVER', 1, (255, 255, 255))
                self.ventana.blit(
                    etiqueta_perdiste,
                    ((self.ancho - etiqueta_perdiste.get_width()) / 2,
                     (self.alto - etiqueta_perdiste.get_height()) / 2)
                )
                pg.display.update()
                self.contador += 1
                if self.contador == self.fps * 3:
                    break
            return True
        else:
            return False

    def recargar_balas(self, cantidad_balas):
        self.balas = cantidad_balas

    def dibujar_hud(self):
        desplazamiento = 0
        etiqueta_vidas = self.fuente.render(f'Vidas: {self.vidas}', 1, (255, 255, 255))
        etiqueta_nivel = self.fuente.render(f'Nivel: {self.nivel}', 1, (255, 255, 255))
        self.ventana.blit(etiqueta_vidas, (10, 10))
        self.ventana.blit(etiqueta_nivel, (self.ancho - etiqueta_nivel.get_width() - 10, 10))
        for _ in range(self.balas):
            desplazamiento += self.imagen_bala.get_width()
            self.ventana.blit(self.imagen_bala, (self.ancho - desplazamiento, self.alto - 50))

    def leer_registros(self, nombre_archivo):
        registros = []
        try:
            with open(nombre_archivo, 'r') as archivo:
                for linea in archivo:
                    nombre, puntuacion = linea.strip().split(",")
                    registros.append((nombre, int(puntuacion)))
        except FileNotFoundError:
            print("El archivo no existe")

        return sorted(registros, key=lambda x: x[1], reverse=True)[:5]