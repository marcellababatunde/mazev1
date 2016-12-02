# Imports
import pygame
import intersects
import random
import time
import math

# Initialize game engine
pygame.init()


# Window
WIDTH = 1250
HEIGHT = 975
SIZE = (WIDTH, HEIGHT)
TITLE = "Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# stages
START = 0
PLAYING = 1
END = 2

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PlayerColor = (255, 255, 255)        


# Make a player
player =  [200, 150, 25, 25]
player_vx = 0
player_vy = 0
player_speed = 5

# make walls
'''       starting x, starting y, width, height    '''
wall1 =  [300, 275, 200, 25]
wall2 =  [400, 450, 200, 25]
wall3 =  [100, 100, 25, 200]
wall4 =  [200, 200, 25, 400]
wall5 =  [500, 200, 450, 25]
wall6 =  [700, 100, 275, 25]
wall7 =  [700, 100, 25, 200]
wall8 =  [700, 50, 25, 975]
wall9 =  [0, 700, 675, 25]
wall10 = [750, 700, 500, 25]
wall11 = [650, 725, 25, 150]
wall12 = [650, 900, 25, 100]
wall13 = [725, 500, 75, 25]
wall14 = [950, 200, 25, 150]
wall15 = [825, 500, 100, 25]
wall16 = [950, 375, 25, 100]
wall17 = [950, 500, 25, 25]
wall18 = [950, 350, 25, 25]
wall19 = [950, 475, 25, 25]
wall20 = [800, 500, 25, 25]

walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall13, wall14, wall15, wall16, wall17]
walls2 = [wall10, wall11, wall12, wall18, wall19, wall20]

# Make coins

def setup():
    global coins, stage
    
    coin1 = [300, 500, 25, 25]
    coin2 = [400, 200, 25, 25]
    coin3 = [150, 150, 25, 25]
    coin4 = [800, 300, 25, 25]
    coin5 = [800, 150, 25, 25]
    coin6 = [200, 800, 25, 25]
    coin7 = [875, 675, 25, 25]
    coin8 = [875, 725, 25, 25]
    coin9 = [950, 925, 25, 25]
    coin10 = [400, 925, 25, 25]

    coins = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10]

    stage = START
    
# Game loop
setup()
win = False
score = 0
done = False


    

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:

            if stage == START:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING
                    
            elif stage == PLAYING:
                if event.key == pygame.K_c:
                    PlayerColor = (random.randint(1,255),random.randint(1,255),random.randint(1,255))

            elif stage == END:
                if event.key == pygame.K_SPACE:
                    setup()

    if stage == PLAYING:
        pressed = pygame.key.get_pressed()

        up = pressed[pygame.K_UP]
        down = pressed[pygame.K_DOWN]
        left = pressed[pygame.K_LEFT]
        right = pressed[pygame.K_RIGHT]

        if up:
            player_vy = -player_speed
        elif down:
            player_vy = player_speed
        else:
            player_vy = 0
            
        if left:
            player_vx = -player_speed
        elif right:
            player_vx = player_speed
        else:
            player_vx = 0
        
    # Game logic (Check for collisions, update points, etc.)
    if stage == PLAYING:
        ''' move the player in horizontal direction '''
        player[0] += player_vx

        ''' resolve collisions horizontally '''
        for w in walls:
            if intersects.rect_rect(player, w):        
                if player_vx > 0:
                    player[0] = w[0] - player[2]
                elif player_vx < 0:
                    player[0] = w[0] + w[2]

        for w in walls2:
            if intersects.rect_rect(player, w):        
                if player_vx > 0:
                    player[0] = w[0] - player[2]
                elif player_vx < 0:
                    player[0] = w[0] + w[2]


        ''' move the player in vertical direction '''
        player[1] += player_vy
        
        ''' resolve collisions vertically '''
        for w in walls:
            if intersects.rect_rect(player, w):                    
                if player_vy > 0:
                    player[1] = w[1] - player[3]
                if player_vy < 0:
                    player[1] = w[1] + w[3]

        for w in walls2:
            if intersects.rect_rect(player, w):                    
                if player_vy > 0:
                    player[1] = w[1] - player[3]
                if player_vy < 0:
                    player[1] = w[1] + w[3]



        ''' here is where you should resolve player collisions with screen edges '''
        if player[1] < 0:
            player[1] = 0
        if player[1] + player[3] > HEIGHT:
            player[1] = HEIGHT - player[3]
        if player[0] < 0:
            player[0] = 0
        if player[0] + player[2] > WIDTH:
            player[0] = WIDTH - player[2]


        ''' get the coins '''
        #coins = [c for c in coins if not intersects.rect_rect(player, c)]

        hit_list = [c for c in coins if intersects.rect_rect(player, c)]
    
        for hit in hit_list:
            coins.remove(hit)
            score += 1
            print("sound!")

        if len(coins) == 0:
            win = True


    

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    PlayerColor = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
    pygame.draw.rect(screen, PlayerColor, player)

    
    for w in walls:
        RED = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
        pygame.draw.rect(screen, RED, w)

    for w in walls2:
        pygame.draw.rect(screen, BLACK, w)
        
    for c in coins:
        pygame.draw.rect(screen, YELLOW, c)

    ''' begin/end game text '''
    if stage == START:
        font = pygame.font.Font(None, 64)
        text1 = font.render("Press SPACE to play.", True, WHITE)
        screen.blit(text1, [400, 500])

    if stage == PLAYING:
        font = pygame.font.Font(None, 64)
        text1 = font.render("Score: " + str(score), True, WHITE)
        screen.blit(text1, [0, 0])
    
    if win:
        font = pygame.font.Font(None, 64)
        text = font.render("You Win!", 1, GREEN)
        screen.blit(text, [((WIDTH/2)-96), ((HEIGHT/2)-32)])

    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()

    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
