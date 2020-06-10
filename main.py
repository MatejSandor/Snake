import pygame

WIN_WIDTH = 400
WIN_HEIGHT = 300


class Snake:
    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.vel = 0


def draw_window(snake, win):
    pass


def main():
    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))


if __name__ == '__main__':
    main()
