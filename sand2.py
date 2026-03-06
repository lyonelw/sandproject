import pygame
import random
import math

pygame.init()

grain_size = 10
square = 90
width = grain_size * square
height = grain_size * square
circlerad = 3*grain_size
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
placing = False
grains = []
colors = []
moving_grains = []
#for i in range(0, 400):
#    grains.append((i, 399))
while running:
    num = random.randint(0, 7)
    if num == 0:
        randcolor = "gold"
    elif num == 1:
        randcolor = "gold1"
    elif num == 2:
        randcolor = "gold2"
    elif num == 3:
        randcolor = "gold3"
    elif num == 4:
        randcolor = "lightgoldenrod1"
    elif num == 5:
        randcolor = "khaki1"
    elif num == 6:
        randcolor = "khaki2"
    elif num == 7:
        randcolor = "lightgoldenrodyellow"
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                placing = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                placing = False
    new_grains = []
    circle = []
    if placing:
        pos = pygame.mouse.get_pos()
        pos = (pos[0]//grain_size*grain_size, pos[1]//grain_size*grain_size)
        for i in range(pos[0]-circlerad, pos[0]+circlerad):
            for j in range(pos[1]-circlerad, pos[1]+circlerad):
                if math.sqrt((pos[0]-i)**2+(pos[1]-j)**2) < circlerad:
                    circle.append((i//grain_size*grain_size, j//grain_size*grain_size))
        for point in circle:
            if point not in grains:
                grains.append(point)
                colors.append(randcolor)
    for i, (x, y) in enumerate(grains):
        screen.fill(colors[i], ((x, y), (grain_size, grain_size)))
        new_y = y+grain_size
        target_pos = ((x, new_y))
        if y < height-grain_size and target_pos not in grains:
            new_grains.append((x, new_y))
            colors.append(randcolor)
        else:
            new_grains.append((x, y))
            colors.append(randcolor)
        #if y < height-grain_size and y > (height-grain_size*10) and (x-grain_size, new_y) not in grains:
        #    new_grains.append((x-grain_size, new_y))
        #    colors.append(randcolor)
        #if y < height-grain_size and y > (height-grain_size*10) and (x+grain_size, new_y) not in grains:
        #    new_grains.append((x+grain_size, new_y)) 
        #    colors.append(randcolor)
    grains = new_grains

    pygame.display.flip()
    clock.tick(144)

pygame.quit()
