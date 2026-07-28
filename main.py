import pygame as pg
import sys
from config import WIDTH, HEIGHT, TITLE, BACKGROUND_IMAGE, TITLE_IMAGE, FPS, BLACK, WHITE


def main():
    pg.init()
    win = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption(TITLE)

    from game import Juego
    from player import Jugador

    background_img = pg.image.load(BACKGROUND_IMAGE).convert()
    title_img = pg.image.load(TITLE_IMAGE).convert()

    reloj = pg.time.Clock()
    fuente = pg.font.SysFont('Arial', 50)

    jugador = Jugador(x=0, y=HEIGHT - 100, velocidad_x=5, velocidad_y=5)
    jugador.x = (WIDTH - jugador.obtener_ancho()) // 2

    juego = Juego(fuente=fuente, fps=FPS, contador=0, ventana=win, vidas=3,
                  ancho_pantalla=WIDTH, alto_pantalla=HEIGHT, reloj=reloj)

    running = True
    while running:
        reloj.tick(FPS)

        if juego.salir():
            running = False
            break

        jugador.mover()
        jugador.crear_balas()
        jugador.actualizar_temporizadores()

        win.blit(background_img, (0, 0))
        jugador.dibujar(win)
        jugador.disparar(win)

        pg.display.update()

    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()