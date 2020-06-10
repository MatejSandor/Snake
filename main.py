import pygame

WIN_WIDTH = 600
WIN_HEIGHT = 500

STAT_FONT = pygame.font.SysFont("comicsans", 25)
TEXT_SCORE = "Score: "


class Snake:
    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.vel = 0


def draw_window(snake, win):
    win.blit(TEXT_SCORE, (20, 20))


def main():
    loop = True
    while loop:
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                quit()


if __name__ == '__main__':
    main()
