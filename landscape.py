pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

sun_x = 100
moon_x = 100
skyR = 135
skyG = 206 
skyB = 235
cspdR = 1
cspdG = 1
cspdB = 1
treepos = 110
# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
#Sun and moon rotate every approx 6.5 seconds
#The game runs at 30 FPS
#To get skyR at 135 from 30, I need to get 105 units in 195 frames
#To get skyG at 206 from 30, I need to gain 176 units in 195 frames. 
#To get skyB at 235 from 59, I need to gain 176 units in 195 frames.
    # GAME STATE UPDATES
    # All game math and comparisons happen here
    sun_x += 4.85
    moon_x += 4.85
    skyR += cspdR
    skyG += cspdG
    skyB += cspdB
    if sun_x > 700:
        sun_x -= 1700
    if moon_x > 700: 
        moon_x -= 1700
    # Making the sky darker
    if skyR > 135:
        cspdR = -0.53
    if skyG > 206:
        cspdG = -0.9
    if skyB > 235:
        cspdB = -0.9
    #Making the sky brighter
    if skyR < 30:
        cspdR = 0.53
    if skyG < 30: 
        cspdG = 0.9
    if skyB < 59: 
        cspdB = 0.9
    # DRAWING
    screen.fill((skyR, skyG, skyB))  # always the first drawing command

    pygame.draw.circle(screen, (255, 255, 30), (sun_x, 100), 70)
    pygame.draw.circle(screen, (211, 211, 211), (moon_x + 900, 100), 50)
    pygame.draw.rect(screen, (7, 163, 33), (000, 400, 800, 100))
    pygame.draw.rect(screen, (128, 96, 22), (treepos, 150, 40, 250))
    pygame.draw.circle(screen, (7, 163, 33), (treepos + 40, 150), 40)
    pygame.draw.circle(screen, (7, 163, 33), (treepos + 55, 150), 40)
    pygame.draw.circle(screen, (7, 163, 33), (treepos + 10, 170), 40)
    pygame.draw.circle(screen, (7, 163, 33), (treepos + 20, 176), 40)
    pygame.draw.circle(screen, (7, 163, 33), (treepos - 30, 150), 40)
    pygame.draw.circle(screen, (7, 163, 33), (treepos + 20, 120), 40)
    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------



pygame.quit()
