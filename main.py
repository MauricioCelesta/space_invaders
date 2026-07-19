import pygame as pg
from config import WIDTH, HEIGHT, TITLE, BACKGROUND_IMAGE, TITLE_IMAGE, PLAYER_IMAGE, BULLET_IMAGE, FPS, BLACK, WHITE
import sys
def main():
    pg.init()
    win = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption(TITLE)
    background_img = pg.image.load(BACKGROUND_IMAGE).convert()
    title_img = pg.image.load(TITLE_IMAGE).convert()
    player_img = pg.image.load(PLAYER_IMAGE).convert_alpha()
    bullet_img = pg.image.load(BULLET_IMAGE).convert_alpha()
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()
        win.blit(background_img, (0, 0))
        win.blit(player_img, ((WIDTH - player_img.get_width()) // 2, HEIGHT - 60))
        pg.display.update()

if __name__ == "__main__":
    main()