import pygame, sys, random
import data.engine as e
import time

clock = pygame.time.Clock()

from pygame.locals import *

pygame.mixer.pre_init(44100, -16, 2, 512)  # stop delay on sounds (frequency, size, mono/stereo, buffer)
pygame.init()  # initiates pygame
pygame.mixer.set_num_channels(64)
pygame.display.set_caption('Pygame Platformer')
WINDOW_SIZE = (600, 400)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)  # initiate the window

font = pygame.font.SysFont(None, 20)
click = False


def draw_text(text, font, colour, surface, x, y): # simple function to place text
    textobj = font.render(text, 1, colour)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu():
    global click
    while True:

        screen.fill((0, 0, 0))
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)

        if button_1.collidepoint(mx, my):  # button 1 collision with mouse effects
            pygame.draw.rect(screen, (255, 255, 0), button_1)
            if click:
                game()
        else:
            pygame.draw.rect(screen, (255, 0, 0), button_1)

        if button_2.collidepoint((mx, my)):  # button 2 collision with mouse effects
            pygame.draw.rect(screen, (255, 255, 0), button_2)
            if click:
                pass
        else:
            pygame.draw.rect(screen, (255, 0, 0), button_2)

        screen.blit(font.render('New Game', True, (255, 255, 255), (255, 0, 0)), (110, 120))
        screen.blit(font.render('Button in development', True, (255, 255, 255), (255, 0, 0)), (80, 220))

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)


def game():
    display = pygame.Surface((300, 200))  # used as the surface for rendering, which is scaled

    player_health = 6
    stab = False  # used for player attacking
    cant_attack = False  # if player attacking or not used in later calculations
    hit = False  # bool for if been hit recently or not
    when_hit = 0.0  # float for timing how long player cant be hurt for
    moving_right = False
    moving_left = False
    vertical_momentum = 0
    air_timer = 0 # used to make sure player isnt jumping whilst already in the air

    true_scroll = [0, 0] # camera scrolling

    CHUNK_SIZE = 8 # each chunk is 8 by 8

    def generate_chunk(x, y):
        chunk_data = []
        for y_pos in range(CHUNK_SIZE): # 0 - 7 (not including 8)
            for x_pos in range(CHUNK_SIZE): # 0 -7 (not including 8)
                target_x = x * CHUNK_SIZE + x_pos # x * 8 (size of each chunk) + exact x_position inside of chunk
                target_y = y * CHUNK_SIZE + y_pos # y * 8 (size of each chunk) + exact y_position inside of chunk
                tile_type = 0 # defaulting 0 which is empty
                if target_y == 6 and target_x in range(1, 4): # setting conditions for tiles to spawn
                    tile_type = 1 # grass (platform)
                if target_y == 7 and target_x in range(11, 16):
                    tile_type = 1 # grass (platform)
                if target_y in range(4, 10) and target_x == 7:
                    tile_type = 2 # dirt (wall)
                if target_y > 10:
                    tile_type = 2  # dirt
                elif target_y == 10:
                    tile_type = 1  # grass
                elif target_y == 9:
                    if random.randint(1, 5) == 1:
                        if tile_type == 0:
                            tile_type = 3  # plant 1/5 chance
                if tile_type != 0:
                    chunk_data.append([[target_x, target_y], tile_type]) # returning list of x,y and block type
        return chunk_data

    class jumper_obj():
        def __init__(self, loc):
            self.loc = loc

        def render(self, surf, scroll): # rendering in the jumper based off its location and screens scroll
            surf.blit(jumper_img, (self.loc[0] - scroll[0], self.loc[1] - scroll[1]))

        def get_rect(self): # getting rectangles x, y and width and height
            return pygame.Rect(self.loc[0], self.loc[1], 8, 9)

        def collision_test(self, rect): # adding collisions
            jumper_rect = self.get_rect()
            return jumper_rect.colliderect(rect)

    # loading animations from engine.py
    e.load_animations('data/images/entities/')

    game_map = {}  # starts empty gets used with generate chunks to generate the world
    # loading all the images
    grass_img = pygame.image.load('data/images/grass.png')
    dirt_img = pygame.image.load('data/images/dirt.png')
    plant_img = pygame.image.load('data/images/plant.png').convert()
    plant_img.set_colorkey((255, 255, 255))
    heart_img_full = pygame.image.load('data/images/heart.png').convert()
    heart_img_full.set_colorkey((255, 255, 255))
    heart_img_half = pygame.image.load('data/images/half_heart.png').convert()
    heart_img_half.set_colorkey((255, 255, 255))
    heart_img_empty = pygame.image.load('data/images/empty_heart.png').convert()
    heart_img_empty.set_colorkey((255, 255, 255))

    jumper_img = pygame.image.load('data/images/jumper.png').convert()
    jumper_img.set_colorkey((255, 255, 255))
    # for generating the chunks line 87 generate chunk function
    tile_index = {1: grass_img,
                  2: dirt_img,
                  3: plant_img
                  }
    # audio setup
    jump_sound = pygame.mixer.Sound('data/audio/jump.wav')
    jump_sound.set_volume(0.2)
    grass_sounds = [pygame.mixer.Sound('data/audio/grass_0.wav'), pygame.mixer.Sound('data/audio/grass_1.wav')]
    grass_sounds[0].set_volume(0.2)
    grass_sounds[1].set_volume(0.2)
    pop_sound = pygame.mixer.Sound('data/audio/pop.wav')
    pop_sound.set_volume(0.3)
    # music setup
    pygame.mixer.music.load('data/audio/music.wav')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)
    music_play = True
    grass_sound_timer = 0  # timer defaulted at 0 for when grass sounds get played

    player = e.entity(60, 70, 7, 14, 'player')  # create and spawn player in
    # create and spawn player sword in as object locked to player for determining
    # hitbox when attacking
    sword = pygame.Rect((player.x - 5), player.y, 17, 6)

    enemies = []

    # creating 5 random enemies in random locations
    def create_enemies():
        a = 5
        for i in range(a):
            enemies.append([0, 2, e.entity(random.randint(-200, 900) - 300, 150, 13, 13, 'enemy')])
            if enemies[0][2] in range((player.x - 30), (player.x + 30)):
                enemies.pop(-1)
                a += 1

        # setting background objects for parrallax effect

    background_objects = [[4, [120, 10, 70, 400]], [4, [280, 30, 40, 400]], [2, [30, 40, 40, 400]],
                          [2, [130, 90, 100, 400]], [2, [300, 80, 120, 400]]]

    jumper_objects = []
    # randomly creates a jumper obj which bounces the character high
    for i in range(5):
        jumper_objects.append(jumper_obj((random.randint(0, 600) - 300, 150)))

    while True:  # game loop
        display.fill((146, 244, 255))  # clear screen by filling it with blue
        sword.x = int(player.x - 5)  # setting sword to always be where the player is
        sword.y = int(player.y)  # setting sword to always be where the player is

        # spawns enemies as they die
        if enemies.__len__() <= 4:
            create_enemies()

        if grass_sound_timer > 0:
            grass_sound_timer -= 1
            # scroll is following the player and /20 is giving it a slow follow rather than locked on
        true_scroll[0] += (player.x - true_scroll[0] - 152) / 20
        true_scroll[1] += (player.y - true_scroll[1] - 106) / 20
        scroll = true_scroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])

        # parrallax effect where differrent objects in background moves at different speeds
        pygame.draw.rect(display, (7, 80, 75), pygame.Rect(0, 120, 300, 80))
        for background_object in background_objects:
            obj_rect = pygame.Rect(background_object[1][0] - int(scroll[0] / background_object[0]),
                                   background_object[1][1] - int(scroll[1] / background_object[0]),
                                   background_object[1][2],
                                   background_object[1][3])

            if background_object[0] == 2:
                pygame.draw.rect(display, (14, 222, 150), obj_rect)
            else:
                pygame.draw.rect(display, (9, 91, 85), obj_rect)

        tile_rects = []
        # tile rendering around player based off generate chunk function
        for y in range(4):
            for x in range(4):
                target_x = x - 1 + int(round(scroll[0] / (CHUNK_SIZE * 16))) # returning x coordinate
                target_y = y - 1 + int(round(scroll[1] / (CHUNK_SIZE * 16))) # returning y coordinate
                target_chunk = str(target_x) + ';' + str(target_y) # putting the two together
                if target_chunk not in game_map: # if not created yet create it
                    game_map[target_chunk] = generate_chunk(target_x, target_y)
                for tile in game_map[target_chunk]: # display objects as long as they exist on the screen
                    display.blit(tile_index[tile[1]], (tile[0][0] * 16 - scroll[0], tile[0][1] * 16 - scroll[1]))
                    if tile[1] in [1, 2]:
                        tile_rects.append(pygame.Rect(tile[0][0] * 16, tile[0][1] * 16, 16, 16))

            # set momentum for player based on key presses
        player_movement = [0, 0]
        if moving_right == True:
            player_movement[0] += 2
        if moving_left == True:
            player_movement[0] -= 2
        player_movement[1] += vertical_momentum
        vertical_momentum += 0.2
        if vertical_momentum > 3:
            vertical_momentum = 3

            # setting animations based on players movements
        if player_movement[0] == 0 and stab is False:
            player.set_action('idle')
        if player_movement[0] > 0 and stab is False:
            player.set_flip(False)
            player.set_action('run')
        if player_movement[0] < 0 and stab is False:
            player.set_flip(True)
            player.set_action('run')
        if player_movement[0] == 0 and stab is True:
            player.set_action('stab')
        if player_movement[0] > 0 and stab is True:
            player.set_flip(False)
            player.set_action('stab_run')
        if player_movement[0] < 0 and stab is True:
            player.set_flip(True)
            player.set_action('stab_run')

        collision_types = player.move(player_movement, tile_rects)

        if collision_types['bottom'] == True:  # if collided with ground
            air_timer = 0  # reset jump
            vertical_momentum = 0  # remove vertical momentum
            if player_movement[0] != 0:  # if moving on ground play grass sounds
                if grass_sound_timer == 0:
                    grass_sound_timer = 30
                    random.choice(grass_sounds).play()
        else:
            air_timer += 1  # otherwise air timer +1 so you cant jump in the air somehow

        player.change_frame(1)  # how much to change animation frames by per frame
        player.display(display, scroll)  # calls display function to show character on screen and scroll camera

        for jumper in jumper_objects:
            jumper.render(display, scroll)  # spawns in jumper objects that bounce players
            if jumper.collision_test(player.obj.rect):
                vertical_momentum = -6

        display_r = pygame.Rect(scroll[0], scroll[1], 300, 200)  # setting current camera co-ordinates

        for number, enemy in enumerate(enemies):  # for each enemy we spawn into a list
            if display_r.colliderect(enemy[2].obj.rect):  # if they are in camera
                enemy[0] += 0.2
                if enemy[0] > 3:  # setting vertical movement capped at 3
                    enemy[0] = 3
                enemy_movement = [0, enemy[0]]
                if player.x > enemy[2].x + 3:  # setting horizontal movement relative to player
                    enemy_movement[0] = 1
                if player.x < enemy[2].x - 3:  # setting horizontal movement relative to player
                    enemy_movement[0] = -1
                enemy[2].move(enemy_movement, tile_rects)  # movement function
                if collision_types['bottom'] == True:  # if touching ground stop falling
                    enemy[0] = 0

            enemy[2].display(display, scroll)
            if player.obj.rect.colliderect(enemy[2].obj.rect):
                if enemy_movement[0] > 0:  # moving right
                    player_movement[0] += 15  # knock player left
                elif enemy_movement[0] < 0:  # moving left
                    player_movement[0] -= 15  # knock player right
                vertical_momentum = -3  # always knock player up
                player.move(player_movement, tile_rects)

                if hit == False:  # if player gets hit
                    player_health -= 1
                    hit = True  # setting hit to true so player cant be hit again for a short while
                    when_hit = time.time()
            if (time.time() - when_hit) >= 1:
                hit = False  # invulnerable for 1 second
            if hit == False and (time.time() - when_hit) >= 10 and player_health < 6:
                player_health = 6  # temporary regen if not hurt for 10 secs

            if stab == True:  # if player is attacking
                if cant_attack == False:  # if player is able to attack
                    cant_attack = True  # make it so they can't attack while attacking / for a short duration
                    time_attack = time.time()  # grab time they attacked
                if sword.colliderect(enemy[2].obj.rect):  # if they hit something with attack
                    enemy[1] -= 1
                    # knockback enemies if hit depending on location
                    if enemy[2].x < player.x:
                        enemy_movement[0] = -10
                    elif enemy[2].x > player.x:
                        enemy_movement[0] = 10
                    enemy[2].move(enemy_movement, tile_rects)  # movement function for kncokback effect
                    stab = False  # so enemy wont keep taking ticks of damage if still in range of "sword"
                    print("bam")
                    if enemy[1] == 0:  # if enemy dead
                        enemies.pop(number)  # remove from enemies list
                        pop_sound.play()  # play sound
                        if player_health < 6:  # if player wounded, 33% chance to heal
                            a = random.randrange(1, 4)
                            if a == 1:
                                player_health += 1

            if cant_attack == True:  # resets cant_attack every .4 secs - prevents spam attacking
                if (time.time() - time_attack) >= 0.4:
                    stab = False
                    cant_attack = False

        for event in pygame.event.get():  # event loop
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_m:
                    if music_play == True:
                        pygame.mixer.music.fadeout(1000)
                        music_play = False
                    elif music_play == False:
                        pygame.mixer.music.play(-1)
                        music_play = True
                if event.key == K_RIGHT:
                    moving_right = True
                if event.key == K_LEFT:
                    moving_left = True
                if event.key == K_UP:
                    if air_timer < 6:
                        jump_sound.play()
                        vertical_momentum = -5
                if event.key == K_k:  # test button fornow
                    if cant_attack == False:
                        stab = True
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    moving_right = False
                if event.key == K_LEFT:
                    moving_left = False

        heart_full_scaled = pygame.transform.scale(heart_img_full, (20, 20))
        heart_half_scaled = pygame.transform.scale(heart_img_half, (20, 20))
        heart_empty_scaled = pygame.transform.scale(heart_img_empty, (20, 20))
        display.blit(heart_empty_scaled, (5, 5))
        display.blit(heart_empty_scaled, (30, 5))
        display.blit(heart_empty_scaled, (55, 5))

        hearts = player_health / 2  # all of the hearts related items below are setting up images based off health
        if hearts == 0:
            pygame.mixer.music.fadeout(1000)
            game_over()
        elif hearts == 0.5:
            display.blit(heart_half_scaled, (5, 5))
        elif hearts == 1:
            display.blit(heart_full_scaled, (5, 5))
        elif hearts == 1.5:
            display.blit(heart_full_scaled, (5, 5))
            display.blit(heart_half_scaled, (30, 5))
        elif hearts == 2:
            display.blit(heart_full_scaled, (5, 5))
            display.blit(heart_full_scaled, (30, 5))
        elif hearts == 2.5:
            display.blit(heart_full_scaled, (5, 5))
            display.blit(heart_full_scaled, (30, 5))
            display.blit(heart_half_scaled, (55, 5))
        elif hearts == 3:
            display.blit(heart_full_scaled, (5, 5))
            display.blit(heart_full_scaled, (30, 5))
            display.blit(heart_full_scaled, (55, 5))

        screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))
        pygame.display.update()
        clock.tick(60)


def game_over():
    global click
    while True:

        screen.fill((0, 0, 0))
        draw_text('Game Over', font, (255, 255, 255), screen, 200, 200)

        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(150, 250, 200, 50)

        if button_1.collidepoint(mx, my):  # button 1 collision with mouse effects
            pygame.draw.rect(screen, (255, 255, 0), button_1)
            if click:
                main_menu()
        else:
            pygame.draw.rect(screen, (255, 0, 0), button_1)

        screen.blit(font.render('Continue', True, (255, 255, 255), (255, 0, 0)), (230, 260))

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)


main_menu()
