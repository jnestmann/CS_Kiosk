# Import statements
import datetime
import glob
import logging
import pygame
from sys import exit
import time

# Define constants
BLACK = (0, 0, 0)
WHITE = (0xFF, 0xFF, 0xFF)
EKUMARRON = (0x4a, 0x18, 0x2d)
SCREEN_SIZE = (1920, 1080)
SCREEN_TITLE = "Computer Science Department at EKU"

# component setup & initializations
pygame.init()
logging.basicConfig(filename="logs/screen_click.log", level=logging.DEBUG)

slides_list = glob.glob('images\slides\*.jpg')
logging.info(slides_list)

next_slide = 0

program_start = datetime.datetime.now()
logging.info("\nProgram started: " + str(program_start))

screen = pygame.display.set_mode(SCREEN_SIZE, pygame.FULLSCREEN)
pygame.display.set_caption(SCREEN_TITLE)

presentation_mode = 'slideshow'

def pquit():
    program_end = datetime.datetime.now()
    logging.info("Program ended normally at " + str(program_end))
    pygame.quit()
    exit()

def draw_inner_monitor(set_inner_monitor):
    if set_inner_monitor == 0:
        pass
    elif set_inner_monitor == 1:
        new_display_image = 'images/gray.jpg'
        new_display = pygame.image.load(new_display_image).convert()
        screen.blit(new_display, (110,63))
    else:
        pass

def set_background():
    background_image_filename = 'images/metalic_background.jpg'
    background = pygame.image.load(background_image_filename).convert()
    screen.blit(background, (0,0))

def get_slide(next_slide, slides_list):
    if next_slide == len(slides_list):
        next_slide = 0
    slide_filename = slides_list[next_slide]
    slide = pygame.image.load(slide_filename).convert()
    screen.blit(slide, (0, 0))
    return next_slide + 1

def update_inner_monitor(section_request):
    kiosk_slides = ['images/slides/jumbo.jpg',
                    'images/slides/gray.jpg',
                    'images/slides/color_change.jpg',
                    'images/slides/green.jpg'
                   ]
    if section_request == 1:
        slide_filename = slides_list[0]
    elif section_request == 2:
        slide_filename = slides_list[1]
    else:
        slide_filename = slides_list[2]
    slide = pygame.image.load(slide_filename).convert()
    screen.blit(slide, (110, 115))

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
key_value = 0
inner_slide = 1

# ----- Main Program Loop ------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            logging.info("Key: {} pressed".format(event.key))
            if event.key == 27:
                pquit()
        elif presentation_mode == 'slideshow':
            if event.type == pygame.MOUSEBUTTONDOWN:
                presentation_mode = 'kiosk'
        elif presentation_mode == 'kiosk':
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                logging.info("The mouse coordinates were "
                             "({}, {}).".format(mousex, mousey))
                if 1521 <= mousex <= 1630 and 465 <= mousey <= 592:
                    logging.info("Directory accessed")
                    inner_slide = 1
                elif 1378 <= mousex <= 1500 and 602 <= mousey <= 721:
                    logging.info("Events accessed")
                    inner_slide = 2
                elif 1655 <= mousex <= 1778 and 610 <= mousey <= 723:
                    inner_slide = 3
                elif 1519 <= mousex <= 1637 and 744 <= mousey <= 867:
                    inner_slide = 4
                elif 1317 <= mousex <=1473 and 401 <= mousey <= 448:
                    presentation_mode = 'slideshow'
                elif 1317 <= mousex <= 1349 and 949 <= mousey <= 981:
                    pquit()

    screen.fill(WHITE)
    
    if presentation_mode == 'slideshow':
        next_slide = get_slide(next_slide, slides_list)
        time.sleep(4)
    else:
        set_background()
        update_inner_monitor(inner_slide)


    pygame.display.flip()
    clock.tick(60)
pquit()