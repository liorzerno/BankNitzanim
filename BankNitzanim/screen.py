import pygame
import consts

pygame.init()

screen = pygame.display.set_mode((800, 600))

def background():
    screen.fill(consts.DARK_BLUE)
    pygame.display.flip()

def start_button():
    font = pygame.font.SysFont("Ariel", 30)
    text = font.render("CREATE BANK \n    ACCOUNT", False, consts.WHITE)
    button = pygame.Rect(consts.BUTTON_X, consts.BUTTON_Y, consts.BUTTON_WIDTH, consts.BUTTON_HEIGHT)
    pygame.draw.rect(text, consts.DARK_PURPLE, button)

def draw_game():
    background()
    start_button()