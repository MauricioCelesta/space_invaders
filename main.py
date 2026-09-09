import pygame as pg
from pygame import mixer
import sys
from config import WIDTH, HEIGHT, TITLE, BACKGROUND_IMAGE, TITLE_IMAGE, BACKGROUND_MUSIC, EXPLOSION_SOUND, WIN_SOUND, FPS


def main():
    pg.init()
    win = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption(TITLE)
    pg.display.set_icon(pg.image.load(TITLE_IMAGE))

    try:
        mixer.music.load(BACKGROUND_MUSIC)
        mixer.music.play(-1)
    except pg.error:
        print("No se pudo cargar el sonido de fondo")

    from game import Juego
    from player import Jugador
    from enemy import Enemigo
    from draw import Dibujo
    from menu import MenuPrincipal
    from menu_puntajes import MenuPuntajes
    from menu_acerca_de import MenuAcercaDe
    from ventana_nombre import PantallaNombre

    reloj = pg.time.Clock()
    fuente = pg.font.SysFont('comicsans', 50)

    def jugar():
        puntaje = 0
        corriendo = True

        juego = Juego(fuente, FPS, 3, win, WIDTH, HEIGHT, 0, reloj)

        jugador = Jugador(x=0, y=HEIGHT - 120, velocidad_x=5, velocidad_y=4)
        jugador.x = (WIDTH - jugador.obtener_ancho()) // 2

        enemigo_base = Enemigo(velocidad=4)
        cantidad_enemigos = 4
        enemigos = enemigo_base.crear(cantidad_enemigos)

        dibujo = Dibujo(win)
        dibujo.dibujar(juego, jugador, enemigos, FPS, puntaje)

        while corriendo:
            reloj.tick(FPS)

            if juego.fin_del_juego():
                if puntaje >= juego.max_puntaje:
                    try:
                        sonido = pg.mixer.Sound(WIN_SOUND)
                        sonido.play()
                    except pg.error:
                        pass
                    PantallaNombre(win, puntaje, mostrar_menu_principal).ejecutar()
                else:
                    mostrar_menu_principal()
                corriendo = False
                continue

            if juego.salir():
                corriendo = False
                continue

            if len(enemigos) == 0:
                juego.nivel += 1
                cantidad_enemigos += 1
                enemigo_base.aumentar_velocidad()
                jugador.aumentar_velocidad()
                enemigos = enemigo_base.crear(cantidad_enemigos)
                if juego.nivel % 3 == 0:
                    if jugador.max_cantidad_balas < 10:
                        jugador.max_cantidad_balas += 1
                    if juego.vidas < 6:
                        juego.vidas += 1

            jugador.mover()
            jugador.crear_balas()
            juego.recargar_balas(len(jugador.balas))
            jugador.actualizar_temporizadores()

            for enemigo in enemigos[:]:
                enemigo.mover()
                if jugador.detectar_impacto(enemigo):
                    enemigos.remove(enemigo)
                    try:
                        sonido_choque = pg.mixer.Sound(EXPLOSION_SOUND)
                        sonido_choque.play()
                    except pg.error:
                        pass
                    puntaje += 1
                elif enemigo.y + enemigo.obtener_alto() >= HEIGHT:
                    juego.vidas -= 1
                    enemigos.remove(enemigo)

            dibujo.dibujar(juego, jugador, enemigos, FPS, puntaje)

    def mostrar_puntajes():
        MenuPuntajes(win, mostrar_menu_principal).ejecutar()

    def mostrar_acerca_de():
        MenuAcercaDe(win, mostrar_menu_principal).ejecutar()

    def mostrar_menu_principal():
        MenuPrincipal(win, jugar, mostrar_puntajes, mostrar_acerca_de).menu_principal()

    mostrar_menu_principal()
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()