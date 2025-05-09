# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode([1920, 1080])
clock = pygame.time.Clock()
running = True

font = pygame.font.Font('freesansbold.ttf', 32)

text = font.render('Jag heter Beatrice', True, 'blue')

while running:
    #Quit game if you close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("red")
    screen.blit(text, (0,0))

    pygame.display.update()

print('quit')
pygame.quit()


    