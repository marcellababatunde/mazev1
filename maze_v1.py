# Imports
import pygame
import intersects
import random
import time
import math

# Initialize game engine
pygame.init()


# Window
WIDTH = 1000
HEIGHT = 750
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
BLUE = (35, 229, 255)
PlayerColor = (255, 255, 255)
enemycolor = (255, 0, 0)
red = (255, 0, 0)


# Make a player/enemy
player =  [0, 0, 25, 25]
player_vx = 0
player_vy = 0
player_speed = 5
enemy = [975, 0, 25, 25]
enemy_vx = 0
enemy_vy = 0
enemy_speed = 8

# make walls
wall1 = [25, 25, 25, 100]
wall2 = [0, 150, 50, 25]
wall3 = [0, 200, 25, 25]
wall4 = [0, 300, 25, 75]
wall5 = [0, 425, 175, 25]
wall6 = [0, 475, 25, 25]
wall7 = [0, 575, 25, 25]
wall8 = [0, 675, 25, 25]
wall9 = [0, 725, 25, 25]
wall10 = [25, 250, 25, 25]
wall11 = [25, 525, 25, 25]
wall12 = [25, 625, 25, 25]
wall13 = [50, 200, 25, 200]
wall14 = [50, 475, 25, 250]
wall15 = [75, 50, 125, 25]
wall16 = [75, 475, 25, 25]
wall17 = [75, 575, 25, 25]
wall18 = [75, 675, 25, 25]
wall19 = [100, 100, 25, 100]
wall20 = [100, 225, 150, 25]
wall21 = [100, 275, 150, 25]
wall22 = [100, 325, 150, 25]
wall23 = [100, 375, 100, 25]
wall24 = [100, 525, 25, 25]
wall25 = [100, 625, 25, 25]
wall26 = [100, 750, 25, 25]
wall27 = [125, 475, 25, 275]
wall28 = [150, 125, 100, 25]
wall29 = [150, 175, 175, 25]
wall30 = [150, 475, 75, 25]
wall31 = [175, 0, 25, 75]
wall32 = [175, 550, 175, 25]
wall33 = [175, 600, 25, 150]
wall34 = [225, 125, 25, 250]
wall35 = [225, 425, 25, 100]
wall36 = [250, 0, 25, 100]
wall37 = [250, 400, 425, 25]
wall38 = [250, 625, 125, 25]
wall39 = [250, 675, 25, 75]
wall40 = [275, 75, 225, 25]
wall41 = [275, 250, 25, 125]
wall42 = [275, 450, 25, 75]
wall43 = [275, 700, 200, 25]
wall44 = [325, 325, 25, 50]
wall45 = [325, 475, 75, 25]
wall46 = [325, 550, 25, 100]
wall47 = [350, 0, 25, 50]
wall48 = [350, 100, 25, 100]
wall49 = [350, 325, 100, 25]
wall50 = [375, 375, 25, 25]
wall51 = [375, 475, 25, 125]
wall52 = [375, 600, 150, 25]
wall53 = [400, 25, 150, 25]
wall54 = [375, 250, 25, 75]
wall55 = [300, 250, 75, 25]
wall56 = [425, 150, 25, 150]
wall57 = [425, 325, 25, 50]
wall58 = [425, 450, 25, 200]
wall59 = [425, 650, 100, 25]
wall60 = [475, 225, 175, 25]
wall61 = [475, 650, 25, 75]
wall62 = [500, 475, 25, 100]
wall63 = [425, 350, 300, 25]
wall64 = [550, 0, 25, 100]
wall65 = [550, 175, 200, 25]
wall66 = [550, 700, 125, 25]
wall67 = [625, 250, 25, 75]
wall68 = [625, 500, 125, 25]
wall69 = [650, 0, 25, 175]
wall70 = [650, 450, 75, 25]
wall71 = [650, 525, 25, 150]
wall72 = [675, 225, 100, 25]
wall73 = [450, 450, 125, 25]
wall74 = [575, 450, 25, 250]
wall75 = [700, 0, 25, 25]
wall76 = [700, 50, 25, 100]
wall77 = [700, 350, 25, 125]
wall78 = [700, 600, 100, 25]
wall79 = [700, 650, 25, 100]
wall80 = [750, 25, 25, 25]
wall81 = [750, 350, 25, 125]
wall82 = [775, 75, 25, 175]
wall83 = [775, 475, 25, 150]
wall84 = [775, 650, 25, 75]
wall85 = [800, 0, 25, 25]
wall86 = [825, 100, 175, 25]
wall87 = [825, 125, 25, 50]
wall88 = [825, 175, 125, 25]
wall89 = [825, 300, 25, 150]
wall90 = [825, 550, 175, 25]
wall91 = [775, 675, 150, 25]
wall92 = [650, 300, 175, 25]
wall93 = [850, 25, 25, 25]
wall94 = [850, 225, 25, 50]
wall95 = [900, 0, 25, 25]
wall96 = [900, 275, 100, 25]
wall97 = [900, 350, 100, 25]
wall98 = [900, 375, 25, 50]
wall99 = [900, 425, 75, 25]
wall100 = [900, 550, 25, 175]
wall101 = [950, 25, 25, 25]
wall102 = [925, 600, 50, 25]
wall103 = [925, 700, 50, 25]
wall104 = [950, 650, 50, 25]
wall105 = [800, 475, 175, 25]
wall106 = [725, 50, 250, 25]
wall107 = [500, 150, 25, 175]
wall108 = [375, 125, 225, 25]
wall109 = [875, 225, 125, 25]


walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14, wall15, wall16, wall17, wall18, wall19, wall20,
         wall21, wall22, wall23, wall24, wall25, wall26, wall27, wall28, wall29, wall30, wall31, wall32, wall33, wall34, wall35, wall36, wall37, wall38, wall39,
         wall40, wall41, wall42, wall43, wall44, wall45, wall46, wall47, wall48, wall49, wall50, wall51, wall52, wall53, wall54, wall55, wall56, wall57, wall58,
         wall59, wall60, wall61, wall62, wall63, wall64, wall65, wall66, wall67, wall68, wall69, wall70, wall71, wall72, wall73, wall74, wall75, wall76, wall77,
         wall78, wall79, wall80, wall81, wall82, wall83, wall84, wall85, wall86, wall87, wall88, wall89, wall90, wall91, wall92, wall93, wall94, wall95, wall96,
         wall97, wall98, wall99, wall100, wall101, wall102, wall103, wall104, wall105, wall106, wall107, wall108, wall109]




#Make switch
#switch = [800, 150, 25, 25]

#Make doors
#door1 = [950, 100, 25, 100]

#doors = [door1]

#Make collidables
#collidables = walls + doors
 
# Make coins
def format_time(seconds):
    m = seconds // 60
    s = seconds % 60

    if s < 10:
        s = "0" + str(s)

    return str(m) + ":" + str(s)

def setup():
    global coins, stage, time_remaining, ticks
    
    coin1 = [0, 250, 25, 25]
    coin2 = [0, 600, 25, 25]
    coin3 = [50, 100, 25, 25]
    coin4 = [50, 725, 25, 25]
    coin5 = [100, 675, 25, 25]
    coin6 = [125, 0, 25, 25]
    coin7 = [150, 575, 25, 25]
    coin8 = [175, 300, 25, 25] 
    coin9 = [250, 375, 25, 25]
    coin10 = [300, 25, 25, 25]
    coin11 = [300, 575, 25, 25]
    coin12 = [325, 300, 25, 25]
    coin13 = [325, 675, 25, 25]
    coin14 = [350, 425, 25, 25]
    coin15 = [375, 175, 25, 25]
    coin16 = [375, 650, 25, 25]
    coin17 = [450, 525, 25, 25]
    coin18 = [475, 175, 25, 25]
    coin19 = [525, 0, 25, 25]
    coin20 = [550, 200, 25, 25]
    coin21 = [550, 300, 25, 25]
    coin22 = [600, 25, 25, 25]
    coin23 = [600, 600, 25, 25]
    coin24 = [675, 0, 25, 25]
    coin25 = [450, 625, 25, 25]
    coin26 = [725, 100, 25, 25]
    coin27 = [725, 250, 25, 25]
    coin28 = [725, 550, 25, 25]
    coin29 = [750, 0, 25, 25]
    coin30 = [750, 175, 25, 25]
    coin31 = [800, 325, 25, 25]
    coin32 = [875, 125, 25, 25]
    coin33 = [875, 600, 25, 25]
    coin34 = [925, 25, 25, 25]
    coin35 = [925, 400, 25, 25]
    coin36 = [950, 575, 25, 25]
    coin37 = [975, 250, 25, 25]
    
    


    coins = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10, coin11, coin12, coin13, coin14, coin15, coin16, coin17, coin18, coin19, coin20,
             coin21, coin22, coin23, coin24, coin25, coin26, coin27, coin28, coin29, coin30, coin31, coin32, coin33, coin34, coin35, coin36, coin37]

    stage = START
    time_remaining = 120
    ticks = 0
    
# Game loop
setup()
win = False
doors_open = False
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

        playerup = pressed[pygame.K_UP]
        playerdown = pressed[pygame.K_DOWN]
        playerleft = pressed[pygame.K_LEFT]
        playerright = pressed[pygame.K_RIGHT]

        if playerup:
            player_vy = -player_speed
        elif playerdown:
            player_vy = player_speed
        else:
            player_vy = 0
            
        if playerleft:
            player_vx = -player_speed
        elif playerright:
            player_vx = player_speed
        else:
            player_vx = 0

        enemyup = pressed[pygame.K_w]
        enemydown = pressed[pygame.K_s]
        enemyleft = pressed[pygame.K_a]
        enemyright = pressed[pygame.K_d]

        if enemyup:
            enemy_vy = -enemy_speed
        elif enemydown:
            enemy_vy = enemy_speed
        else:
            enemy_vy = 0
            
        if enemyleft:
            enemy_vx = -enemy_speed
        elif enemyright:
            enemy_vx = enemy_speed
        else:
            enemy_vx = 0


        
        
    # Game logic (Check for collisions, update points, etc.)
    if stage == PLAYING:
        ''' move the player in horizontal direction '''
        player[0] += player_vx

        enemy[0] += enemy_vx

        ''' resolve collisions horizontally '''
        for w in walls:
            if intersects.rect_rect(player, w):        
                if player_vx > 0:
                    player[0] = w[0] - player[2]
                elif player_vx < 0:
                    player[0] = w[0] + w[2]


            if intersects.rect_rect(enemy, w):        
                if enemy_vx > 0:
                    enemy[0] = w[0] - enemy[2]
                elif enemy_vx < 0:
                    enemy[0] = w[0] + w[2]


        '''for w in walls2:
            if intersects.rect_rect(player, w):        
                if player_vx > 0:
                    player[0] = w[0] - player[2]
                elif player_vx < 0:
                    player[0] = w[0] + w[2]'''


        ''' move the player in vertical direction '''
        player[1] += player_vy

        enemy[1] += enemy_vy
        
        ''' resolve collisions vertically '''
        if doors_open:
            walls = walls + doors
        
        for w in walls:
            if intersects.rect_rect(player, w):                    
                if player_vy > 0:
                    player[1] = w[1] - player[3]
                if player_vy < 0:
                    player[1] = w[1] + w[3]

            if intersects.rect_rect(enemy, w):                    
                if enemy_vy > 0:
                    enemy[1] = w[1] - enemy[3]
                if enemy_vy < 0:
                    enemy[1] = w[1] + w[3]

         #for w in walls2:

         #if intersects.rect_rect(player, w):
            #if player_vy > 0:
                #player[1] = w[1] - player[3]
            #if player_vy < 0:
                #player[1] = w[1] + w[3]


    ''' timer stuff '''
    if stage == PLAYING:
        ticks += 1

        if ticks % refresh_rate == 0:
            time_remaining -= 1

        if time_remaining == 0:
            stage = END

        

        ''' here is where you should resolve player collisions with screen edges '''
        if player[1] < 0:
            player[1] = 0
        if player[1] + player[3] > HEIGHT:
            player[1] = HEIGHT - player[3]
        if player[0] < 0:
            player[0] = 0
        if player[0] + player[2] > WIDTH:
            player[0] = WIDTH - player[2]


        if enemy[1] < 0:
            enemy[1] = 0
        if enemy[1] + enemy[3] > HEIGHT:
            enemy[1] = HEIGHT - enemy[3]
        if enemy[0] < 0:
            enemy[0] = 0
        if enemy[0] + enemy[2] > WIDTH:
            enemy[0] = WIDTH - enemy[2]    


        ''' get the coins '''
        #coins = [c for c in coins if not intersects.rect_rect(player, c)]

        hit_list = [c for c in coins if intersects.rect_rect(player, c)]
    
        for hit in hit_list:
            coins.remove(hit)
            score += 100
            print("sound!")

        if len(coins) == 0:
            win = True


    ''' open door on switch contact 
    if intersects.rect_rect(player, switch):
        doors_open = True
        
        collidables = [c for c in collidables if c not in doors]'''
        
    
    if len(coins) == 0:
        win = True
        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)

    screen.fill(BLACK)

    enemycolor = red
    PlayerColor = GREEN
    pygame.draw.rect(screen, PlayerColor, player)
    pygame.draw.rect(screen, enemycolor, enemy)
    
    for w in walls:
        RED = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
        pygame.draw.rect(screen, RED, w)

    '''for w in walls2:
        pygame.draw.rect(screen, BLACK, w)'''
        
    for c in coins:
        pygame.draw.rect(screen, YELLOW, c)

    #pygame.draw.rect(screen, YELLOW, switch)

    if doors_open:
        for d in doors:
            pygame.draw.rect(screen, BLUE, d)
    
    ''' timer text '''
    if stage == PLAYING:
        font = pygame.font.Font(None, 64)
        timer_text = font.render(format_time(time_remaining), True, WHITE)
        screen.blit(timer_text, [900, 0])

    ''' begin/end game text '''
    if stage == START:
        font = pygame.font.Font(None, 64)
        text1 = font.render("Press SPACE to play.", True, WHITE)
        screen.blit(text1, [300, 350])
        player =  [200, 150, 25, 25]

    if stage == PLAYING:
        font = pygame.font.Font(None, 64)
        text1 = font.render("Score: " + str(score), True, WHITE)
        screen.blit(text1, [0, 0])
    
    if win:
        font = pygame.font.Font(None, 64)
        text = font.render("You Win!", 1, GREEN)
        screen.blit(text, [((WIDTH/2)-96), ((HEIGHT/2)-32)])

    if time_remaining == 0:
        font = pygame.font.Font(None, 64)
        text1 = font.render("Game Over!", 1, GREEN)
        text2 = font.render("Press SPACE to play again", 1, GREEN)
        screen.blit(text1, [((WIDTH/2)-96), ((HEIGHT/2)-32)])
        screen.blit(text2, [250, 400])
        score = 0
    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()

    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
