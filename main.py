import pygame

pygame.font.init()

WIN_WIDTH = 600
WIN_HEIGHT = 500

STAT_FONT = pygame.font.SysFont("comicsans", 25)
TEXT_SCORE = "Score: "


class Snake:
    def __init__(self, x, y, vel_hor, vel_ver):
        self.x = x
        self.y = y
        self.vel_hor = vel_hor
        self.vel_ver = vel_ver

    def draw_snake(self, x, y, win):
        self.x = x
        self.y = y
        lead_rect = pygame.Rect((x, y, 15, 15))
        pygame.draw.rect(win, (36, 252, 3), lead_rect)


def draw_window(snake, win):
    text = STAT_FONT.render("SCORE: ", 1, (255, 255, 255))
    win.blit(text, (10, 20))
    snake.draw_snake(snake.x, snake.y, win)

    pygame.display.update()


def main():
    loop = True
    snake = Snake(300, 300, 0, 0)
    clock = pygame.time.Clock()

    while loop:
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        draw_window(snake, window)
        clock.tick(5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.vel_ver = 0
                    snake.vel_hor = -15
                if event.key == pygame.K_RIGHT:
                    snake.vel_ver = 0
                    snake.vel_hor = 15
                if event.key == pygame.K_DOWN:
                    snake.vel_hor = 0
                    snake.vel_ver = 15
                if event.key == pygame.K_UP:
                    snake.vel_hor = 0
                    snake.vel_ver = -15

        snake.x += snake.vel_hor
        snake.y += snake.vel_ver


if __name__ == '__main__':
    main()
