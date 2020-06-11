import pygame
import random

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
        self.lead_rect = pygame.Rect((x, y, 15, 15))

    def draw_snake(self, x, y, win):
        self.x = x
        self.y = y
        pygame.draw.rect(win, (36, 252, 3), self.lead_rect)

    def moved_out(self):
        if self.x < 0:
            self.x = WIN_WIDTH
        if self.x > WIN_WIDTH:
            self.x = 0
        if self.y < 0:
            self.y = WIN_HEIGHT
        if self.y > WIN_HEIGHT:
            self.y = 0

    def get_mask(self):
        return pygame.mask.from_surface(self.lead_rect)


class Apple:
    def __init__(self):
        self.x = random.randrange(0, WIN_WIDTH-15)
        self.y = random.randrange(60, WIN_HEIGHT-15)

    def draw_apple(self, win):
        apple_rect = pygame.Rect((self.x, self.y, 15, 15))
        pygame.draw.rect(win, (235, 64, 52), apple_rect)

    def collide(self):
        pass


def draw_window(snake, win, apples):
    text = STAT_FONT.render("SCORE: ", 1, (255, 255, 255))
    win.blit(text, (10, 20))
    snake.draw_snake(snake.x, snake.y, win)

    for apple in apples:
        apple.draw_apple(win)

    pygame.display.update()


def main():
    loop = True
    snake = Snake(300, 300, 0, 0)
    clock = pygame.time.Clock()
    apples = []

    for i in range(4):
        apple = Apple()
        apples.append(apple)

    while loop:
        window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        draw_window(snake, window, apples)
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
        snake.moved_out()


if __name__ == '__main__':
    main()
