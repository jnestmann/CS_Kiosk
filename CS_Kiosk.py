# Import statements
import datetime
import glob
import logging
import pygame
from sys import exit

# Define constants
BLACK = (0, 0, 0)
WHITE = (0xFF, 0xFF, 0xFF)
EKUMARRON = (0x4a, 0x18, 0x2d)
SCREEN_SIZE = (1920, 1080)
SCREEN_TITLE = "Computer Science Department at EKU"

# component setup & initializations
pygame.init()
logging.basicConfig(filename="logs/screen_click.log", level=logging.DEBUG)

program_start = datetime.datetime.now()
logging.info("\nProgram started: " + str(program_start))

slides_list = glob.glob('images\slideshow_slides\*.jpg')
logging.info(slides_list)

next_slide = 0

screen = pygame.display.set_mode(SCREEN_SIZE, pygame.FULLSCREEN)
pygame.display.set_caption(SCREEN_TITLE)

start_slide = pygame.image.load('images/slideshow_slides/start_slide.jpg')
screen.blit(start_slide, [0, 0])

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

def get_slide(next_slide, slides_list, since_refresh, tds):
    refresh_time = since_refresh + datetime.timedelta(seconds=tds)
    logging.info("Refresh time: " + str(refresh_time))
    now = datetime.datetime.now()
    logging.info("Current time:" + str(now))
    if now > refresh_time:
        logging.info("Refresh slide")
        since_refresh = now
        if next_slide >= len(slides_list):
            next_slide = 0
        slide_filename = slides_list[next_slide]
        slide = pygame.image.load(slide_filename).convert()
        screen.blit(slide, (0, 0))
        return_packet = (next_slide + 1, since_refresh)
        logging.info("Return packet includes " + str(return_packet))
        return (next_slide + 1, since_refresh)
    else:
        return (next_slide, since_refresh)
    # slide_filename = slides_list[next_slide]
    # slide= pygame.image.load(slide_filename).convert()


def update_kiosk(section_request):
    kiosk_slides = ['images/kiosk_slides/directory.jpg',
                    'images/kiosk_slides/events.jpg',
                    'images/kiosk_slides/programs.jpg',
                    'images/kiosk_slides/clubs.jpg'
                   ]
    if section_request == 1:
        slide_filename = kiosk_slides[0]
    elif section_request == 2:
        slide_filename = kiosk_slides[1]
    else:
        slide_filename = kiosk_slides[2]
    slide = pygame.image.load(slide_filename).convert()
    screen.blit(slide, (110, 115))

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
key_value = 0
inner_slide = 1
since_refresh = datetime.datetime.now()

# ----- Main Program Loop ------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            logging.info("Key: {} pressed".format(event.key))
            if event.key == 27:
                pquit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if presentation_mode == 'slideshow':
                presentation_mode = 'kiosk'
            elif presentation_mode == 'kiosk':
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

    # update display
    #screen.fill(WHITE)
    
    if presentation_mode == 'slideshow':
        next_slide, since_refresh = get_slide(next_slide, slides_list, since_refresh, 10)
    else:
        set_background()
        update_kiosk(inner_slide)


    pygame.display.flip()
    clock.tick(60)

pquit()
