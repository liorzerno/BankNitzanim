import pygame
import consts

pygame.init()

screen = pygame.display.set_mode((800, 600))

def background():
    screen.fill(consts.DARK_BLUE)
    pygame.display.flip()

def start_button():
    font = pygame.font.SysFont("Comic Sans MS", 30)
    text = font.render("CREATE BANK \nACCOUNT", False, consts.WHITE)
    button = pygame.Rect(consts.BUTTON_X, consts.BUTTON_Y, consts.BUTTON_WIDTH, consts.BUTTON_HEIGHT)
    screen.blit(text, button)

def draw_game():
    background()
    start_button()