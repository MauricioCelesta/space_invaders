class Barco:
    def __init__(self, x, y, salud=100):
        self.x = x
        self.y = y
        self.salud = salud
        self.imagen_nave = None
        self.imagen_bala = None
        self.contador_espera_bala = 0
        self.balas = []
        self.balas_disparadas = []
        self.tiempo_espera = 120

    def dibujar(self, ventana):
        ventana.blit(self.imagen_nave, (self.x, self.y))

    def obtener_ancho(self):
        return self.imagen_nave.get_width()

    def obtener_alto(self):
        return self.imagen_nave.get_height()