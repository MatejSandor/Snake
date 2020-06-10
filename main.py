import pygame

pygame.font.init()

WIN_WIDTH = 600
WIN_HEIGHT = 500

STAT_FONT = pygame.font.SysFont("comicsans", 25)
TEXT_SCORE = "Score: "


class Snake:
    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.vel = 0

    def draw_snake(self, x, y, win):
        self.x = x
        self.y = y
        pygame.draw.rect(win, (36, 252, 3), (x, y, 15, 15))


def draw_window(snake, win):
    text = STAT_FONT.render("SCORE: ", 1, (255, 255, 255))
    win.blit(text, (10, 20))
    snake.draw_snake(snake.x, snake.y, win)

    pygame.display.update()


def main():
    loop = True
    while loop:
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        draw_window(Snake(100, 100, 0), window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                quit()


if __name__ == '__main__':
    main()
