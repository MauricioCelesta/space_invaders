import pygame as pg
from config import WIDTH, HEIGHT


class MenuPrincipal:
    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)
    ROJO = (255, 0, 0)

    DIRECTORIO_IMAGENES = "img"

    def __init__(self, iniciar_juego, iniciar_puntuaciones, iniciar_creditos):
        self.iniciar_juego = iniciar_juego
        self.iniciar_puntuaciones = iniciar_puntuaciones
        self.iniciar_creditos = iniciar_creditos