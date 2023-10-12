if True: #How things work
    #How corners work
    #We have to check the x and y positions for the previous and next block in BOTH directions (x and y)
    #For example:
    #
    #top left       
    #
    #               y = -1
    #             ----------                                                                                              | -y
    #            |          |                                                                                             |
    #         ---           |                                                                                             |
    #        |              |     so if x is -1 and y is -1 we know that it is a top left corner              +x---------- ---------- -x
    #  x = -1|              |                                                                                             |
    #        |              |                                                                                             |
    #         --------------                                                                                              | +y
    #
    #top right
    #
    #            y = -1
    #          ----------
    #         |          |
    #         |           ---
    #         |              |            so if x is 1 and y is -1 it us a top right corner
    #         |              | x = 1
    #         |              |
    #          --------------
    #
    #bottom left
    #
    #            
    #          --------------                                        
    #         |              |             
    #  x = -1 |              |              
    #         |              |     so if x is -1 and y is 1 then it is a bottom left corner  
    #          ---           |   
    #             |          |   
    #              ----------  
    #                y = 1
    #
    #bottom right
    #
    #            
    #          --------------                                        
    #         |              |            so if x is 1 and y is 1 then it is a bottom right corner             
    #         |              | x = 1          
    #         |              |        
    #         |           ---
    #         |          |   
    #          ----------  
    #            y = 1

    #Enumerate and the if statement
    #Enumerate allows us to get the index(so the position in the list) of the object we are currently on in the list
    #For example lets say I have a list(names = ["Steve","Charles","Mathew"]) and I want to know to index of the items
    #I would use this: for index,name in enumerate(names):
    #                       print(index,name)
    #The output would be:
    #0 Steve
    #1 Charles
    #2 Mathew
    #Now in the if statement that we are using enumerate() for is going to check the position within the list body aswell as the position(Vector2) stored within that index of the list
    #This list contains all the positions(Vector2) of each block of our snake

    #How direction works (Moves snake to right)
    #[Vector2(5,10),Vector2(4,10),Vector2(3,10)]
    #[Vector2(5,10),Vector2(4,10)]          (+ Vector2(1,0)    What Happens: Vector2(5,10) + Vector2(1,0) = Vector2(6,10))
    #[Vector2(6,10),Vector2(5,10),Vector2(4,10)]

    #How to add a new block to the snake body (Snake still moving right)
    #[Vector2(5,10),Vector2(4,10),Vector2(3,10)]
    #[Vector2(6,10),Vector2(5,10),Vector2(4,10),Vector2(3,10)] (+ Vector2(1,0)    What Happens: It adds a new Vector2
                                                                #by adding direction(which contains a Vector2 like Vector2(1,0))
                                                                #to the first Vector2 in the list which in this case is Vector(5,10)

    #Why it is important to make sure that if the snake is moving in a direction (Up) that you cannot press the opposite key (Down)
    #If the snake is moving up and you press down, it will move into itself and so end the game
    pass

#Imports
import pygame
import random
from pygame.locals import *
from pygame import Vector2
from random import randint, choice, randrange
from glitch_this import ImageGlitcher


#Initialize Pygame
pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096) #Pre Initialezes the sound in pygame
pygame.event.set_allowed([QUIT,KEYDOWN])

#Declarations
#Screen Size
cell_size = 40 #The size of the cells
cell_num = 20 #The amount of cells
grid = cell_size*cell_num #The grid (aka. The Screen)
#Screen
flags = DOUBLEBUF
screen = pygame.display.set_mode((grid,grid),flags,16) #Display a window and store it in screen
pygame.display.set_caption("Snake Glitched") #Set the window caption
#Unspesified
FPS = pygame.time.Clock() #Frames per second
game_active = False
transition_count = 1
tech_index = 0
tut_index = 0
display_mode = "menu"
tutorials = [pygame.image.load("Assets/graphics/tutorials/security.png").convert_alpha(),
             pygame.image.load("Assets/graphics/tutorials/randint.png").convert_alpha(),
             pygame.image.load("Assets/graphics/tutorials/multithread.png").convert_alpha(),
             pygame.image.load("Assets/graphics/tutorials/malware.png").convert_alpha(),
             pygame.image.load("Assets/graphics/tutorials/trojan.png").convert_alpha(),
             pygame.image.load("Assets/graphics/tutorials/ransom.png").convert_alpha()]
#Fonts
boba_font = pygame.font.Font("Assets/font/Boba Cups.ttf",30)
origin_font = pygame.font.Font("Assets/font/OriginTech.ttf",30)
blacklisted_font = pygame.font.Font("Assets/font/Blacklisted.ttf",20)
doctor_font = pygame.font.Font("Assets/font/Doctor Glitch.otf",30)
doctor_small = pygame.font.Font("Assets/font/Doctor Glitch.otf",30)
badsignal_font = pygame.font.Font("Assets/font/Bad Signal.otf",50)
pixel_font = pygame.font.Font("Assets/font/Pixeltype.ttf",30)
#Music
music = pygame.mixer.Sound("Assets/sound/Music/MainLevel.wav")
tech_music = pygame.mixer.Sound("Assets/sound/Music/TechLevel.wav")
main_music = pygame.mixer.Sound("Assets/sound/Music/MainMenu.wav")
boss_music = pygame.mixer.Sound("Assets/sound/Music/Boss.wav")
#Audio
audio = [pygame.mixer.Sound("Assets/sound/Dialogue/N1.mp3"),
        pygame.mixer.Sound("Assets/sound/Dialogue/V1.mp3"),
        pygame.mixer.Sound("Assets/sound/Dialogue/M1.mp3"),
        pygame.mixer.Sound("Assets/sound/Dialogue/V2.mp3"),
        pygame.mixer.Sound("Assets/sound/Dialogue/M2.mp3"),
        pygame.mixer.Sound("Assets/sound/Dialogue/V3.mp3"),
        pygame.mixer.Sound("Assets/sound/Dialogue/M3.mp3"),
        pygame.mixer.Sound("Assets/sound/Dialogue/V4.mp3"),
        pygame.mixer.Sound("Assets/sound/Dialogue/M4.mp3"),
        pygame.mixer.Sound("Assets/sound/Dialogue/V5.mp3"),
        pygame.mixer.Sound("Assets/sound/Dialogue/M5.mp3"),
        pygame.mixer.Sound("Assets/sound/Dialogue/V6.mp3"),
        pygame.mixer.Sound("Assets/sound/Dialogue/M6.mp3"),
        pygame.mixer.Sound("Assets/sound/Dialogue/V7.mp3"),
        pygame.mixer.Sound("Assets/sound/Dialogue/M7.mp3"),
        pygame.mixer.Sound("Assets/sound/Dialogue/V8.mp3"),
        pygame.mixer.Sound("Assets/sound/Dialogue/M8.mp3"),
        pygame.mixer.Sound("Assets/sound/Dialogue/N2.mp3"),
        pygame.mixer.Sound("Assets/sound/Dialogue/N1.mp3")]
bits = pygame.mixer.Sound("Assets/sound/Dialogue/bits.mp3")
#Border
area_size = ((cell_num*cell_size)-160,(cell_num*cell_size)-160)
area_pos = (400,400)
area_surf = pygame.Surface(area_size)
area_rect = area_surf.get_rect(center=area_pos)
#Backrounds
main_bg = pygame.image.load("Assets/graphics/backrounds/MainBg.png").convert_alpha() #Main Backround (Level 1)
main_bg = pygame.transform.scale(main_bg, screen.get_size())
tech_bg_list = [pygame.image.load("Assets/graphics/backrounds/TechBg.png"),
           pygame.image.load("Assets/graphics/backrounds/TechBg2.png"),
           pygame.image.load("Assets/graphics/backrounds/TechBoss.png")] #Tech Backround (Level 2)
credits_bg = pygame.image.load("Assets/graphics/backrounds/Credits.png").convert_alpha()
#Timers
SCREEN_UPDATE = pygame.USEREVENT+1
pygame.time.set_timer(SCREEN_UPDATE,150) #Set SCREEN_UPDATE event
FAST_UPDATE = pygame.USEREVENT+2
pygame.time.set_timer(FAST_UPDATE,60) #Set FAST_UPDATE event
SLOW_UPDATE = pygame.USEREVENT+3
pygame.time.set_timer(SLOW_UPDATE,1000) #Set SLOW_UPDATE event

#Play Main Menu Music
main_music.play(loops=-1)
main_music.set_volume(0.3)

#pause
display = ""
status = False

#Classes
class SNAKE: #The Class for the snake
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)] #The position of blocks for the snake body
        self.direction = Vector2(0,0) #if the direction is changed the snake will continue into that direction
        self.new_block = False #Sets new_block to false otherwise the snake would grow without stopping
        self.snake_state = 0
        self.snake_head_up = []
        self.head_rect = pygame.Rect(self.body[0].x,self.body[0].y,cell_size,cell_size)
        if True:
            #Load all images into surfaces and use .convert_alpa() to format them into a picture format pygame better understands

            #Head
            self.head_down = pygame.image.load("Assets/graphics/snake/head/head down/def_head_down.png").convert_alpha()
            self.head_up = pygame.image.load("Assets/graphics/snake/head/head up/def_head_up.png").convert_alpha()
            self.head_left = pygame.image.load("Assets/graphics/snake/head/head left/def_head_left.png").convert_alpha()
            self.head_right = pygame.image.load("Assets/graphics/snake/head/head right/def_head_right.png").convert_alpha()

            #Body
            self.bod_vert = pygame.image.load("Assets/graphics/snake/body/body vert/def_body_vert.png").convert_alpha()
            self.bod_horiz = pygame.image.load("Assets/graphics/snake/body/body horiz/def_body_horiz.png").convert_alpha()

            #Turns
            self.turn_tl = pygame.image.load("Assets/graphics/snake/turn/top left/def_topleft.png").convert_alpha()
            self.turn_bl = pygame.image.load("Assets/graphics/snake/turn/bottom left/def_bottomleft.png").convert_alpha()
            self.turn_tr = pygame.image.load("Assets/graphics/snake/turn/top right/def_topright.png").convert_alpha()
            self.turn_br = pygame.image.load("Assets/graphics/snake/turn/bottom right/def_bottomright.png").convert_alpha()

            #Tail
            self.tail_down = pygame.image.load("Assets/graphics/snake/tail/tail down/def_tail_down.png").convert_alpha()
            self.tail_up = pygame.image.load("Assets/graphics/snake/tail/tail up/def_tail_up.png").convert_alpha()
            self.tail_left = pygame.image.load("Assets/graphics/snake/tail/tail left/def_tail_left.png").convert_alpha()
            self.tail_right = pygame.image.load("Assets/graphics/snake/tail/tail right/def_tail_right.png").convert_alpha()


            #Transformation States w/ Animation
            #Head
            self.head_down_1 = pygame.image.load("Assets/graphics/snake/head/head down/head_down_1.png").convert_alpha()
            self.head_up_1 = pygame.image.load("Assets/graphics/snake/head/head up/head_up_1.png").convert_alpha()
            self.head_left_1 = pygame.image.load("Assets/graphics/snake/head/head left/head_left_1.png").convert_alpha()
            self.head_right_1 = pygame.image.load("Assets/graphics/snake/head/head right/head_right_1.png").convert_alpha()
            self.head_down_2 = pygame.image.load("Assets/graphics/snake/head/head down/head_down_2.png").convert_alpha()
            self.head_up_2 = pygame.image.load("Assets/graphics/snake/head/head up/head_up_2.png").convert_alpha()
            self.head_left_2 = pygame.image.load("Assets/graphics/snake/head/head left/head_left_2.png").convert_alpha()
            self.head_right_2 = pygame.image.load("Assets/graphics/snake/head/head right/head_right_2.png").convert_alpha()
            self.head_down_3 = pygame.image.load("Assets/graphics/snake/head/head down/head_down_3.png").convert_alpha()
            self.head_up_3 = pygame.image.load("Assets/graphics/snake/head/head up/head_up_3.png").convert_alpha()
            self.head_left_3 = pygame.image.load("Assets/graphics/snake/head/head left/head_left_3.png").convert_alpha()
            self.head_right_3 = pygame.image.load("Assets/graphics/snake/head/head right/head_right_3.png").convert_alpha()
           #Body           
            self.bod_vert_1 = pygame.image.load("Assets/graphics/snake/body/body vert/body_vert_1.png").convert_alpha()
            self.bod_horiz_1 = pygame.image.load("Assets/graphics/snake/body/body horiz/body_horiz_1.png").convert_alpha()
            self.bod_vert_2 = pygame.image.load("Assets/graphics/snake/body/body vert/body_vert_2.png").convert_alpha()
            self.bod_horiz_2 = pygame.image.load("Assets/graphics/snake/body/body horiz/body_horiz_2.png").convert_alpha()
            self.bod_vert_3 = pygame.image.load("Assets/graphics/snake/body/body vert/body_vert_3.png").convert_alpha()
            self.bod_horiz_3 = pygame.image.load("Assets/graphics/snake/body/body horiz/body_horiz_3.png").convert_alpha()
           #Turn            
            self.turn_tl_1 = pygame.image.load("Assets/graphics/snake/turn/top left/topleft_1.png").convert_alpha()
            self.turn_bl_1 = pygame.image.load("Assets/graphics/snake/turn/bottom left/bottomleft_1.png").convert_alpha()
            self.turn_tr_1 = pygame.image.load("Assets/graphics/snake/turn/top right/topright_1.png").convert_alpha()
            self.turn_br_1 = pygame.image.load("Assets/graphics/snake/turn/bottom right/bottomright_1.png").convert_alpha()
            self.turn_tl_2 = pygame.image.load("Assets/graphics/snake/turn/top left/topleft_2.png").convert_alpha()
            self.turn_bl_2 = pygame.image.load("Assets/graphics/snake/turn/bottom left/bottomleft_2.png").convert_alpha()
            self.turn_tr_2 = pygame.image.load("Assets/graphics/snake/turn/top right/topright_2.png").convert_alpha()
            self.turn_br_2 = pygame.image.load("Assets/graphics/snake/turn/bottom right/bottomright_2.png").convert_alpha()
            self.turn_tl_3 = pygame.image.load("Assets/graphics/snake/turn/top left/topleft_3.png").convert_alpha()
            self.turn_bl_3 = pygame.image.load("Assets/graphics/snake/turn/bottom left/bottomleft_3.png").convert_alpha()
            self.turn_tr_3 = pygame.image.load("Assets/graphics/snake/turn/top right/topright_3.png").convert_alpha()
            self.turn_br_3 = pygame.image.load("Assets/graphics/snake/turn/bottom right/bottomright_3.png").convert_alpha()
           #Tail           
            self.tail_down_1 = pygame.image.load("Assets/graphics/snake/tail/tail down/tail_down_1.png").convert_alpha()
            self.tail_up_1 = pygame.image.load("Assets/graphics/snake/tail/tail up/tail_up_1.png").convert_alpha()
            self.tail_left_1 = pygame.image.load("Assets/graphics/snake/tail/tail left/tail_left_1.png").convert_alpha()
            self.tail_right_1 = pygame.image.load("Assets/graphics/snake/tail/tail right/tail_right_1.png").convert_alpha()
            self.tail_down_2 = pygame.image.load("Assets/graphics/snake/tail/tail down/tail_down_2.png").convert_alpha()
            self.tail_up_2 = pygame.image.load("Assets/graphics/snake/tail/tail up/tail_up_2.png").convert_alpha()
            self.tail_left_2 = pygame.image.load("Assets/graphics/snake/tail/tail left/tail_left_2.png").convert_alpha()
            self.tail_right_2 = pygame.image.load("Assets/graphics/snake/tail/tail right/tail_right_2.png").convert_alpha()
            self.tail_down_3 = pygame.image.load("Assets/graphics/snake/tail/tail down/tail_down_3.png").convert_alpha()
            self.tail_up_3 = pygame.image.load("Assets/graphics/snake/tail/tail up/tail_up_3.png").convert_alpha()
            self.tail_left_3 = pygame.image.load("Assets/graphics/snake/tail/tail left/tail_left_3.png").convert_alpha()
            self.tail_right_3 = pygame.image.load("Assets/graphics/snake/tail/tail right/tail_right_3.png").convert_alpha()

            #Snake Surfaces (For animation)
            #Head
            self.snake_head_up = [self.head_up,self.head_up_1,self.head_up_2,self.head_up_3]
            self.head_up_current = self.snake_head_up[self.snake_state]
            self.snake_head_down = [self.head_down,self.head_down_1,self.head_down_2,self.head_down_3]
            self.head_down_current = self.snake_head_down[self.snake_state]
            self.snake_head_left = [self.head_left,self.head_left_1,self.head_left_2,self.head_left_3]
            self.head_left_current = self.snake_head_left[self.snake_state]
            self.snake_head_right = [self.head_right,self.head_right_1,self.head_right_2,self.head_right_3]
            self.head_right_current = self.snake_head_right[self.snake_state]
            #Body
            self.snake_vert = [self.bod_vert,self.bod_vert_1,self.bod_vert_2,self.bod_vert_3]   #snake_vert
            self.snake_vert_current = self.snake_vert[self.snake_state]
            self.snake_horiz = [self.bod_horiz,self.bod_horiz_1,self.bod_horiz_2,self.bod_horiz_3]
            self.snake_horiz_current = self.snake_horiz[self.snake_state]
            #Turn
            self.snake_tl = [self.turn_tl,self.turn_tl_1,self.turn_tl_2,self.turn_tl_3]
            self.snake_tl_current = self.snake_tl[self.snake_state]
            self.snake_bl = [self.turn_bl,self.turn_bl_1,self.turn_bl_2,self.turn_bl_3]
            self.snake_bl_current = self.snake_bl[self.snake_state]
            self.snake_tr = [self.turn_tr,self.turn_tr_1,self.turn_tr_2,self.turn_tr_3]
            self.snake_tr_current = self.snake_tr[self.snake_state]
            self.snake_br = [self.turn_br,self.turn_br_1,self.turn_br_2,self.turn_br_3]
            self.snake_br_current = self.snake_br[self.snake_state]
            #Tail
            self.snake_tail_up = [self.tail_up,self.tail_up_1,self.tail_up_2,self.tail_up_3]
            self.snake_tail_up_current = self.snake_tail_up[self.snake_state]
            self.snake_tail_down = [self.tail_down,self.tail_down_1,self.tail_down_2,self.tail_down_3]
            self.snake_tail_down_current = self.snake_tail_down[self.snake_state]
            self.snake_tail_left = [self.tail_left,self.tail_left_1,self.tail_left_2,self.tail_left_3]
            self.snake_tail_left_current = self.snake_tail_left[self.snake_state]
            self.snake_tail_right = [self.tail_right,self.tail_right_1,self.tail_right_2,self.tail_right_3]
            self.snake_tail_right_current = self.snake_tail_right[self.snake_state]
            
            #Audio
            self.crunch_sound = pygame.mixer.Sound("Assets/sound/Effects/crunch.wav")      
    def draw_snake(self): #Draws the snake
        global display_mode, tut_index
        #Body Rotation
        self.snake_vert_current = self.snake_vert[self.snake_state]
        self.snake_horiz_current = self.snake_horiz[self.snake_state]
        #Turn Rotation
        self.snake_tl_current = self.snake_tl[self.snake_state]
        self.snake_bl_current = self.snake_bl[self.snake_state]   
        self.snake_tr_current = self.snake_tr[self.snake_state]
        self.snake_br_current = self.snake_br[self.snake_state]
        
        self.update_head_graphics() #Call the update_head_graphics function
        self.update_tail_graphics() #Call the update_tail_graphics function
        for index,block in enumerate(self.body): #gives us the index of the object within the list (More info at line 1)
            x_pos = block.x*cell_size #x position of the block
            y_pos = block.y*cell_size #y position of the block
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size) #Makes a rect around each of the blocks (x,y,width,height)
            if not area_rect.colliderect(block_rect): #Checks if the snake is outside the boundries
                main.check_fail("fail")
                main.hit.play()
                main.shield = False
                if display_mode == "tech":
                    main.memory += 1
                break
            for virus in enemy.enemies: #Check if snake hit an enemy
                if virus[1].colliderect(block_rect):
                    if virus[2] == "ransom": #If snake hit a randsomware enemy
                        if not main.shield:
                            display_mode = "ransom"
                        enemy.enemies.remove(virus)
                        enemy.change("random",False)
                    elif virus[2] == "malware": #If snake hit a malware enemy
                        if not main.shield:
                            if main.score >= 40:
                                main.score -= 40
                            elif main.score >= 20:
                                main.score -= 20
                            elif main.score >= 10:
                                main.score -= 10
                            elif main.score >= 5:
                                main.score -= 5
                            main.memory += 1
                        enemy.enemies.remove(virus)
                        enemy.change("malware",True)
            if index == 0: #If the index of self.body is 0 (which is the head)
                screen.blit(self.head,block_rect) #Display the head with the appropriate direction the head should face
                self.head_rect = block_rect
            elif index == len(self.body)-1: #Take the length of the body(default lenght is 3) and minus it with 1(which would give us 2 if the body has no extra parts) and that would always be the last item in the list
                screen.blit(self.tail,block_rect) #Display the appropriate orientation of the tail
            else: #Body relation (Horizontal or Verical)
                previous_block = self.body[index+1] - block #Gets the next block in the index
                next_block = self.body[index-1] - block #Gets the previous block in the index
                if previous_block.x == next_block.x:                                                         #Changes Snake Body
                    screen.blit(self.snake_vert_current,block_rect) #Snake body is vertical
                if previous_block.y == next_block.y:
                    screen.blit(self.snake_horiz_current,block_rect) #Snake body is horizontal                                                        
                else: #Turn relations (More info at line 1)
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1: #Top Left
                        screen.blit(self.snake_tl_current,block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1: #Bottom Left
                        screen.blit(self.snake_bl_current,block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1: #Bottom Left
                        screen.blit(self.snake_tr_current,block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1: #Bottom Left
                        screen.blit(self.snake_br_current,block_rect)
    def move_snake(self,active):  #Moves and adds new block to the snake
        if self.new_block  == True: #Adds a new block to the snake body (More info at line 1)
            body_copy = self.body[:] #Copies the entire list
            body_copy.insert(0,body_copy[0] + self.direction) #inserts at the beginning of the list, the first item in the list + the direction (More info at line 1)
            self.body = body_copy #Replaces the original list with the new one
            self.new_block = False #Sets new block to false otherwise the snake would continously grow
        else: #Moves the snake
            if active:
                body_copy = self.body[:-1] #Copies everyblock except the last one (We need to delete the last one otherwise the snake will continue to grow)
                body_copy.insert(0,body_copy[0] + self.direction) #inserts at the beginning of the list, the first item in the list + the direction (More info at line 1)
                self.body = body_copy #Replace the old list with the new }one
    def add_block(self):  #Allows the block to be added
        self.new_block = True #This allows the function move_snake to add a new block onto the snake body
    def update_head_graphics(self):  #Updates position and rotation of the head
        head_relation = self.body[1] - self.body[0] #head relation = the result of body[1] (the Vector2 of block behind the head) - body[0] (the Vector2 of the head)
        
        #Head
        self.head_up_current = self.snake_head_up[self.snake_state]
        self.head_down_current = self.snake_head_down[self.snake_state]
        self.head_left_current = self.snake_head_left[self.snake_state]
        self.head_right_current = self.snake_head_right[self.snake_state]

        if head_relation == Vector2(1,0): #If the result of the math done in the variable above is Vector2(1,0) then the head is facing left
            self.head = self.head_left_current #Update self.head to display the image of the snake head turned left
        elif head_relation == Vector2(-1,0): #If the result of the math done in the variable above is Vector2(-1,0) then the head is facing right
            self.head = self.head_right_current #Update self.head to display the image of the snake head turned right
        elif head_relation == Vector2(0,1): #If the result of the math done in the variable above is Vector2(1,0) then the head is facing up
            self.head = self.head_up_current #Update self.head to display the image of the snake head turned up
        elif head_relation == Vector2(0,-1): #If the result of the math done in the variable above is Vector2(1,0) then the head is facing down
            self.head = self.head_down_current #Update self.head to display the image of the snake head turned down
    def update_tail_graphics(self):  #Updates position and rotation of the tail
    
        self.snake_tail_up_current = self.snake_tail_up[self.snake_state]
        self.snake_tail_down_current = self.snake_tail_down[self.snake_state]
        self.snake_tail_left_current = self.snake_tail_left[self.snake_state]
        self.snake_tail_right_current = self.snake_tail_right[self.snake_state]

        tail_relation = self.body[-2] - self.body[-1] #tail relation = the result of body[-2](the Vector2 of block infront of the tail) - body[-1](the Vector2 of the tail)
        if tail_relation == Vector2(1,0): #If the result of the math done in the variable above is Vector2(1,0) then the tail is facing left
            self.tail = self.snake_tail_left_current #Update self.tail to display the image of the snake tail turned left
        elif tail_relation == Vector2(-1,0): #If the result of the math done in the variable above is Vector2(-1,0) then the tail is facing right
            self.tail = self.snake_tail_right_current #Update self.tail to display the image of the snake tail turned right
        elif tail_relation == Vector2(0,1): #If the result of the math done in the variable above is Vector2(1,0) then the tail is facing up
            self.tail = self.snake_tail_up_current #Update self.tail to display the image of the snake tail turned up
        elif tail_relation == Vector2(0,-1): #If the result of the math done in the variable above is Vector2(1,0) then the tail is facing down
            self.tail = self.snake_tail_down_current #Update self.tail to display the image of the snake tail turned down
    def play_crunch_sound(self): #Sound that plays when the edible is eaten
        self.crunch_sound.play()
    def reset(self): #Moves snake to starting position
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)] #Sets back to default snake body and position
        self.direction = Vector2(0,0)
    def head_test(self):
                #Body Rotation
        self.snake_vert_current = self.snake_vert[self.snake_state]
        self.snake_horiz_current = self.snake_horiz[self.snake_state]
        #Turn Rotation
        self.snake_tl_current = self.snake_tl[self.snake_state]
        self.snake_bl_current = self.snake_bl[self.snake_state]   
        self.snake_tr_current = self.snake_tr[self.snake_state]
        self.snake_br_current = self.snake_br[self.snake_state]
        
        self.update_head_graphics() #Call the update_head_graphics function
        self.update_tail_graphics() #Call the update_tail_graphics function
        for index,block in enumerate(self.body): #gives us the index of the object within the list (More info at line 1)
            x_pos = block.x*cell_size #x position of the block
            y_pos = block.y*cell_size #y position of the block
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size) #Makes a rect around each of the blocks (x,y,width,height)
            if not area_rect.colliderect(block_rect): #Checks if the snake is outside the boundries
                main.check_fail("fail")
                main.hit.play()
                main.shield = False
                break
            for enemy in self.enemies:
                if enemy[1].colliderect(block_rect):
                    if enemy[2] == "ransom":
                        self.enemies.remove(enemy)
                        self.change("random",False)
                    elif enemy[2] == "malware":
                        self.enemies.remove(enemy)
                        self.change("malware",True)
            surf = pygame.Surface((cell_size,cell_size))
            surf_enemy = pygame.Surface((cell_size,cell_size))
            surf.fill((12,76,23))
            screen.blit(surf,snake.body[0])
            screen.blit(surf_enemy,enemy[1])
            
            if index == 0: #If the index of self.body is 0 (which is the head)
                screen.blit(self.head,block_rect) #Display the head with the appropriate direction the head should face
                self.head_rect = block_rect
                print("found")
            else:
                print("nope")
class FOOD:  #The Class for the edibles
    def __init__(self):
        self.glitcher = ImageGlitcher()
        self.pos = Vector2(randint(0,cell_num -1),randint(0,cell_num -1))
        self.edible_rect = pygame.Rect((self.pos.x * cell_size),(self.pos.y * cell_size),cell_size,cell_size)
        self.chicken = pygame.image.load("Assets/graphics/edible/food/chicken.png")
        self.glitch = pygame.image.load("Assets/graphics/edible/food/chicken.png")
        self.file = pygame.image.load("Assets/graphics/edible/food/file.png")
        self.edible = [self.chicken,self.glitch,self.file]
    def draw_edible(self): #Draws the edible
        self.edible_rect = pygame.Rect((self.pos.x * cell_size),(self.pos.y * cell_size),cell_size,cell_size) #Set the position of the edible
        if not area_rect.colliderect(self.edible_rect): #Check if edible is in bounds
            self.randomize()
            self.draw_edible()
        else:
            if display_mode == "none":
                if not main.score == 9: #Check if the amount of edible eaten are 9
                    screen.blit(self.edible[0], self.edible_rect)
                else: #If the amount is 9, then display the glitch edible
                    glitched = self.glitcher.glitch_image("Assets/graphics/edible/food/chicken.png", 2.5, color_offset=True) #Glitch the chicken edible
                    glitched.save("Assets/graphics/edible/food/chicken_glitch.png") #Save the image
                    self.edible[1] = pygame.image.load("Assets/graphics/edible/food/chicken_glitch.png") #Replace the image of the glitch edible
                    screen.blit(self.edible[1], self.edible_rect)
            elif display_mode != "glitch":
                screen.blit(self.edible[2], self.edible_rect)
    def randomize(self): #Randomizes position of the edible
        self.pos.x = randint(0,cell_num -1) #Store new positions within the vector
        self.pos.y = randint(0,cell_num -1)
class MAIN:  #The main gameplay
    def __init__(self):
        #Globals
        global display_mode
        #Classes
        self.snake = SNAKE()
        self.edible = FOOD()
        self.glitcher = ImageGlitcher()
        self.power = POWERUP()
        #Active True/False
        self.first = True
        self.second = True
        self.third = True
        self.fourth = True
        self.dialogue_active = True
        self.move_active = True
        self.tut_complete = False
        self.enemy = False
        self.shield = False
        self.check = False
        self.powerup = False
        self.eat = False
        self.transition_state = False
        self.tech_mode = False
        self.glitch_active = False
        #Numerical
        self.score = 0
        self.score_count = 0
        self.trancount = 0
        self.glitch_count = 0.1
        self.dialogue_index = 0
        self.memory = 10
        #Other
        self.rgb = ("#caac84") 
        self.font = boba_font
        self.tech_index = tech_index
        
        

        #Main Menu
        self.title = pygame.image.load("Assets/graphics/buttons/Title.png").convert_alpha()
        self.start = pygame.image.load("Assets/graphics/buttons/StartT/Start.png")
        self.exit = pygame.image.load("Assets/graphics/buttons/StartT/Exit.png").convert_alpha()
        self.credits = pygame.image.load("Assets/graphics/buttons/StartT/Credits.png").convert_alpha()
        self.title_rect = self.title.get_rect(center=(400,160))
        self.start_rect = self.start.get_rect(center=(400,400))
        self.exit_rect = self.exit.get_rect(center=(400,450))
        self.credits_rect = self.credits.get_rect(center=(400,550))
        self.back = pygame.Surface((40,40))
        self.back_rect = self.back.get_rect(center=(40,760))

        #Popups
        self.pause = pygame.image.load("Assets/graphics/pause/pause.png").convert_alpha()
        self.pause_rect = self.pause.get_rect(center=(400,400))
        self.ransom = pygame.image.load("Assets\graphics\popups\Ransom.png")
        self.ransom_rect = self.ransom.get_rect(topleft=(0,0))

        #Glitch
        self.warn = pygame.image.load("Assets/graphics/popups/Warning.png").convert_alpha()

        #Audio
        self.hit = pygame.mixer.Sound("Assets/sound/Effects/hit.wav")

        #Dialogue
        self.frames = [pygame.image.load("Assets/graphics/dialogue/1.png").convert_alpha(),
                  pygame.image.load("Assets/graphics/dialogue/2.png").convert_alpha(),
                  pygame.image.load("Assets/graphics/dialogue/3.png").convert_alpha(),
                  pygame.image.load("Assets/graphics/dialogue/4.png").convert_alpha(),
                  pygame.image.load("Assets/graphics/dialogue/5.png").convert_alpha(),
                  pygame.image.load("Assets/graphics/dialogue/6.png").convert_alpha(),
                  pygame.image.load("Assets/graphics/dialogue/7.png").convert_alpha(),
                  pygame.image.load("Assets/graphics/dialogue/8.png").convert_alpha(),
                  pygame.image.load("Assets/graphics/dialogue/9.png").convert_alpha(),
                  pygame.image.load("Assets/graphics/dialogue/10.png").convert_alpha(),
                  pygame.image.load("Assets/graphics/dialogue/11.png").convert_alpha(),
                  pygame.image.load("Assets/graphics/dialogue/12.png").convert_alpha(),
                  pygame.image.load("Assets/graphics/dialogue/13.png").convert_alpha(),
                  pygame.image.load("Assets/graphics/dialogue/14.png").convert_alpha(),
                  pygame.image.load("Assets/graphics/dialogue/15.png").convert_alpha(),
                  pygame.image.load("Assets/graphics/dialogue/16.png").convert_alpha(),
                  pygame.image.load("Assets/graphics/dialogue/17.png").convert_alpha(),
                  pygame.image.load("Assets/graphics/dialogue/18.png").convert_alpha(),
                  pygame.image.load("Assets/graphics/dialogue/1.png").convert_alpha()]     
    def update(self): #Updates methods by using a timer that is contained within the main game loop
        global display_mode
        self.battle() #Run the tech battle
        self.snake.move_snake(self.move_active) #Snake movement (SNAKE class)
        self.check_collision() #Checks collision 
        self.check_fail("null") #Checks wether snake is outside boudries or hit itself
        self.display(display_mode) #Update the screen
    def fast_update(self): #Updates at a faster speed
        self.transform() #Play the snake eat animation
    def slow_update(self): #Updates at slow speeds
        pass
    def draw_elements(self): #Draws the elements
        self.edible.draw_edible() #Fruit (FOOD class)
        self.snake.draw_snake() #Snake (SNAKE class)
        if display_mode == "tech": #Spawn enemy only if it is tech mode
            enemy.spawn_enemy()
        if self.score_count >= self.memory: #Spawn a powerup if the score_count and memory are the same
            self.power.spawn_power()
        if display_mode == "tech": #Spawn the boss if it is tech map
            boss.spawn_boss()
        self.draw_score(self.font, self.rgb) #Score
        self.dialogue(self.dialogue_active) #Convos
    def check_collision(self): #Checks wether the snake head is ontop of the edible pos
        global display_mode
        if self.edible.pos == self.snake.body[0]: #Check if snake ate an edible
            if self.score == 9: #If snake ate 10 edibles
                if display_mode == "none":
                    self.snake.play_crunch_sound() #Play the crunch sound
                    display_mode = "glitch"
                else:
                    self.score += 1
                    self.snake.play_crunch_sound() #Play the crunch sound
                    self.edible.randomize() #Randomize the edible location (FOOD class)
                    self.snake.add_block() #Add a new block to the snake body (SNAKE class)
                    self.eat = True
                    self.score_count += 1
            else:
                self.score += 1
                self.snake.play_crunch_sound() #Play the crunch sound
                self.edible.randomize() #Randomize the edible location (FOOD class)
                self.snake.add_block() #Add a new block to the snake body (SNAKE class)
                self.eat = True
                self.score_count += 1
        if self.power.pos == self.snake.body[0]: #Check if snake ate a powerup
            if display_mode != "none" and self.score_count >= self.memory:
                self.power.consume()
                self.eat = True
    def check_fail(self,force): #Checks wether snake moves into border or hits itself
        if force == "fail": #Forces a game over
            self.game_over()
            self.shield = False
            if display_mode == "tech" and not snake.move_snake:
                self.memory += 1
        elif force == "null": #Checks if the snake hits itself
            for block in self.snake.body[1:]: #Copy every other part of the body except the first (the head)
                if block == self.snake.body[0]: #If block (aka. any part of the body) is at the same snake.body[0] (which is the head of the snake)
                    self.game_over()
                    self.shield = False
                    if display_mode == "tech" and not snake.move_snake:
                        self.memory += 1
    def game_over(self): #Resets the snake
        self.snake.reset() #Resets the snake game
    def draw_score(self,style,rgb):  #Updates the score
        score_x = (grid - 710) #The x value of the score
        score_y = (grid - 760) #The y value of the score
        if style == boba_font:
            score_surface = style.render(f"<Score:{self.score}>", True, rgb) #Create a score surface
            score_rect = score_surface.get_rect(center=(score_x,score_y)) #Place a rect around the surface
        elif style == badsignal_font:
            score_surface = style.render(f"BiScotrse: {self.score}", True, rgb) #Create a score surface
            score_rect = score_surface.get_rect(center=(score_x,score_y)) #Place a rect around the surface
        else:
            score_surface = style.render(f"Bits - {self.score} -", True, rgb)
            score_rect = score_surface.get_rect(center=(score_x,score_y)) #Create a score surface
        if display_mode == "tech":
            score_x = (grid - 650)
            score_y = (grid - 730)
            mem_surface = style.render(f"Memory Leak: {main.memory}", True, rgb)
            mem_rect = mem_surface.get_rect(center=(score_x,score_y)) #Create a score surface 
            screen.blit(score_surface,score_rect)
            screen.blit(mem_surface,mem_rect)
        else: 
            screen.blit(score_surface,score_rect) #Place the score on the screen
    def transform(self): #Change the snake skin/Animate
        if self.tech_mode == True: #Checks wether snake is tech
            if self.eat == True:
                if self.snake.snake_state >= 3: #Animates the Tech skin
                    self.snake.snake_state = 1
                    self.eat = False
                else: 
                    self.snake.snake_state += 1     
    def glitch(self,active):  #Glitch Effect
        global display_mode, transition_count
        if active:
            if self.glitch_count <= 9: #Changes the intensity of the glitch effect
                self.glitch_count += 0.1
            else:
                self.glitch_count = 10
            surf_screen = pygame.Surface(screen.get_size())
            surf_screen.blit(main_bg,(0,0))
            pygame.image.save(surf_screen,"Assets/screenshots/Screen.jpg") #Saves the current state of the backround
            glitched = self.glitcher.glitch_image("Assets/screenshots/Screen.jpg", glitch_amount=self.glitch_count, color_offset= True) #Glitches the backround image
            glitched.save('Assets/screenshots/Glitch.jpg') #Saves it as a new image
            self.converted = pygame.image.load('Assets/screenshots/Glitch.jpg') #Stores the image into a new variable
            if self.glitch_count < 10:
                display_mode = "glitch"
            else:
                self.transcount()
    def display(self,mode): #Changes Display
        global area_size, area_pos
        if mode == "glitch":
            self.powerup = False
            self.glitch_active = True
            self.font = badsignal_font
            self.rgb = (255,255,255)
            self.glitch(self.glitch_active)
            screen.blit(self.converted,(0,0))
            self.draw_elements()
            screen.blit(self.warn,(0,0))
        elif mode == "tech":
            tech_bg = pygame.transform.scale(tech_bg_list[self.tech_index], screen.get_size())
            tech_music.set_volume(0.3)
            area_size = ((cell_num*cell_size)-160,(cell_num*cell_size)-407)
            area_pos = (400,523)
            if self.dialogue_active:
                screen.blit(tech_bg,(0,0))
                self.dialogue(True)
            else:
                self.move_active = True
                screen.blit(tech_bg,(0,0))
                main.draw_elements()
        elif mode == "none":
            main_music.set_volume(0)
            music.set_volume(0.3)
            self.glitch_count = 0.1
            screen.blit(main_bg,(0,0))
            self.move_active = "start"
            area_size = ((cell_num*cell_size)-160,(cell_num*cell_size)-160)
            area_pos = (400,400)
            screen.blit(main_bg,(0,0))
            self.draw_elements()
        elif mode == "clear":
            self.move_active = False
            self.glitch(self.glitch_active)
            screen.fill((0,0,0))
            music.set_volume(0)
            tech_music.set_volume(0)
            main_music.set_volume(0)
        elif mode == "menu":
            screen.fill((0,0,0))
            screen.blit(self.title,self.title_rect)
            screen.blit(self.start,self.start_rect)
            screen.blit(self.exit,self.exit_rect)
            screen.blit(self.credits,self.credits_rect)
        elif mode == "credits":
            screen.blit(credits_bg,(0,0))
        elif mode == "pause":
            self.move_active = False
            music.set_volume(0.1)
            tech_music.set_volume(0.1)
            boss_music.set_volume(0.1)
            screen.blit(main.pause,main.pause_rect)
        elif mode == "ransom":
            self.move_active = False
            if self.first == False:
                boss_music.set_volume(0.1)
            else:
                tech_music.set_volume(0.1)
            screen.blit(main.ransom,main.ransom_rect)
    def transcount(self): #Duration of the glitch effect
        global transition_count, display_mode
        self.trancount += 1
        if self.trancount == 5: #Setup tech map when glitch transition is over
            self.powerup = False
            self.glitch_active = False
            self.tech_mode = True
            self.score_count = 5
            self.score = 5
            self.font = origin_font
            self.rgb = (9, 219, 212)
            self.snake.reset()
            self.edible.randomize()
            music.fadeout(10)
            tech_music.play(loops=-1)
            display_mode = "tech"
            self.dialogue_active = True
            audio[main.dialogue_index].play()
            self.edible.draw_edible()
            self.trancount = 0
    def battle(self):
        if self.score >= 5 and self.score <= 10 or self.first == False: #show powerups
            pass 
        if self.score > 10 or self.first == False: #enemies
            enemy.change("random",False)
            enemy.spawn_enemy()
        if self.second == False: #Rage Boss
            boss_music.set_volume(0.5)
            boss.boss_index = 1
            if self.tech_index >= 2:
                self.tech_index = 0
            else:
                self.tech_index += 1
        elif self.first == False: #Boss
            boss_music.set_volume(0.5)
            self.tech_index = 1
            tech_music.stop()
        if self.dialogue_active:
            boss_music.set_volume(0.3) 
    def dialogue(self,active):
        if active:
            if self.dialogue_index >= len(self.frames):
                print("Reached Max Frames")
            else:
                self.surf = self.frames[self.dialogue_index]
                self.rect = self.surf.get_rect(topleft=(0,0))
                screen.blit(self.surf,self.rect)
                self.move_active = False
        else:
            if display_mode == "tech":
                if self.score >= 20: #Boss Fight
                    if self.first:
                        self.first = False
                        self.dialogue_active = True
                        audio[main.dialogue_index].play()
                        boss_music.play(loops=-1)
                        enemy.limit = 6
                if self.score >= 40: #Rage
                    if self.second:
                        self.second = False
                        self.dialogue_active = True
                        audio[main.dialogue_index].play()
                        enemy.limit = 12
                if self.score >= 50: #Death
                    if self.third:
                        self.third = False
                        self.dialogue_active = True
                        audio[main.dialogue_index].play()
class POWERUP:   #The Class for the Powerups
    def __init__(self):
        global area_rect
        self.pos = Vector2(randint(0,cell_num -1),randint(0,cell_num -1))
        self.randomize()
        self.powerups = {"multithread": {"image": pygame.image.load("Assets/graphics/powerups/multithread.png")},
                         "randint": {"image": pygame.image.load("Assets/graphics/powerups/randint.png")},
                         "shield": {"image": pygame.image.load("Assets/graphics/powerups/shield.png")}}
        self.powerup = random.choice(list(self.powerups.keys()))
    def spawn_power(self): #Spawn the powerups
        surf = self.powerups[self.powerup]["image"] #get the correct image
        rect = surf.get_rect(topleft=(cell_size,cell_size)) #rect the surf
        rect.topleft = (self.pos.x * cell_size, self.pos.y * cell_size) #get pos

        if not area_rect.colliderect(rect) or edible.pos == self.pos: #Make sure powerup is in area
            self.randomize()
        else:
            rect.topleft = (self.pos.x * cell_size, self.pos.y * cell_size)
            screen.blit(surf, rect)
    def randomize(self):
        self.pos = Vector2(randint(0,cell_num -1),randint(0,cell_num -1))
    def new_power(self):
        self.powerup = random.choice(list(self.powerups.keys())) #Choose new powerup
    def playsound(self):
        if self.powerup == "multithread":
            self.multisound = pygame.mixer.Sound("Assets/sound/Effects/multithread.wav")
            self.multisound.play()
        if self.powerup == "randint":
            self.randintsound = pygame.mixer.Sound("Assets/sound/Effects/randint.wav")
            self.randintsound.play()
        if self.powerup == "shield":
            self.shieldsound = pygame.mixer.Sound("Assets/sound/Effects/shield.wav")
            self.shieldsound.play()
    def consume(self):
        if self.powerup == "multithread":
            self.multithread()
        if self.powerup == "randint":
            self.randval()
        if self.powerup == "shield":
            self.shield()
        self.new_power()
        self.randomize()
        main.score_count = 0
        if main.memory >= 10:
            main.memory -= 5
    def multithread(self):
        main.score += 2
        self.playsound()
    def randval(self):
        main.score += randint(1,5)
        self.playsound()
    def shield(self):
        main.shield = True
        self.playsound()
class ENEMY:
    def __init__(self):
        self.limit = 3
        self.body = pygame.Surface((0,0))
        self.body_rect = self.body.get_rect(center=(0,0))
        self.pos = Vector2(randint(0,cell_num -1),randint(0,cell_num -1))
        self.body_rect = pygame.Rect((self.pos.x * cell_size),(self.pos.y * cell_size),cell_size,cell_size)
        self.ransom_surf = [pygame.image.load("Assets/graphics/enemies/1.png").convert_alpha(),
                            pygame.image.load("Assets/graphics/enemies/2.png").convert_alpha(),
                            pygame.image.load("Assets/graphics/enemies/3.png").convert_alpha()]
        self.malware_surf = [pygame.image.load("Assets/graphics/enemies/Malware.png").convert_alpha(),
                             pygame.image.load("Assets/graphics/enemies/Malware_down.png").convert_alpha(),
                             pygame.image.load("Assets/graphics/enemies/Malware_left.png").convert_alpha(),
                             pygame.image.load("Assets/graphics/enemies/Malware_right.png").convert_alpha()]
        self.enemies = []
        self.enemy_types = ["malware","ransom"]
    def randomize(self):
        while True:
            cell_x, cell_y = randrange(0,cell_num-1), randrange(0,cell_num-1)
            x = (cell_x * cell_size)
            y = (cell_y * cell_size)
            self.test_rect = pygame.Rect(x, y, cell_size, cell_size)
            if area_rect.colliderect(self.test_rect):
                break
        self.pos = Vector2(x, y) 
    def change(self,mode,clicked):
        if len(self.enemies) < self.limit:
            enemy_type = choice(self.enemy_types)
            self.randomize()

            if mode == "random":
                if enemy_type == "ransom":
                    self.randomize()
                    self.body = choice(self.ransom_surf)
                    self.body_rect = self.body.get_rect(topleft=self.pos)
                    self.enemies.append([self.body, self.body_rect, "ransom"])
                elif enemy_type == "malware":
                    self.randomize()
                    self.body = choice(self.malware_surf)
                    self.body_rect = self.body.get_rect(topleft=self.pos)
                    self.enemies.append([self.body,self.body_rect,"malware"])
            elif mode == "ransom":
                self.randomize()
                self.body = choice(self.ransom_surf)
                self.body_rect = self.body.get_rect(topleft=self.pos)
                self.enemies.append([self.body, self.body_rect, "ransom"])
            elif mode == "malware":
                if not clicked:
                    self.randomize()
                    self.body = choice(self.malware_surf)
                    self.body_rect = self.body.get_rect(topleft=self.pos)
                    self.enemies.append([self.body,self.body_rect,"malware"])
                else:
                    self.randomize()
                    self.body = choice(self.malware_surf)
                    self.body_rect = self.body.get_rect(topleft=self.pos)
                    self.enemies.append([self.body,self.body_rect,"malware"])
                    self.randomize()
                    self.body = choice(self.malware_surf)
                    self.body_rect = self.body.get_rect(topleft=self.pos)
                    self.enemies.append([self.body,self.body_rect,"malware"])
    def spawn_enemy(self):
        if len(self.enemies) != 0:
            for enemy in self.enemies:
                if enemy[2] == "ransom":
                    screen.blit(enemy[0], enemy[1])
                elif enemy[2] == "malware":
                    screen.blit(enemy[0], enemy[1])
class BOSS:
    def __init__(self):
        self.boss_index = 0
        self.boss_surf = [pygame.image.load("Assets/graphics/enemies/boss.png"),
                          pygame.image.load("Assets/graphics/enemies/boss_rage.png")]
        self.surf = pygame.Surface((800,800))
        self.rect = self.surf.get_rect(topleft=(0,0))
        self.boss_rect = self.boss_surf[self.boss_index].get_rect(center=(400,100))

        self.velos = 1
        self.state = "right"
    def movement(self):
        self.boss_rect = self.boss_surf[self.boss_index].get_rect(center=(400,100))
        if self.rect.left-100 >= self.boss_rect.left:
            self.state = "right"
            self.boss_rect.x += self.velos
        elif self.rect.right+100 <= self.boss_rect.right:
            self.state = "left"
            self.boss_rect.x -= self.velos
        else:
            if self.state == "right":
                self.boss_rect.x += self.velos
            else:
                self.boss_rect.x -= self.velos
    def spawn_boss(self):
        self.boss_rect = self.boss_surf[self.boss_index].get_rect(center=(400,100))
        if main.first == False:
            screen.blit(self.boss_surf[self.boss_index],self.boss_rect)
            self.movement()

#Objects
main = MAIN()
snake = SNAKE()
edible = FOOD()
power = POWERUP()
enemy = ENEMY()
boss = BOSS()

#Main Menu
while not game_active:
    left, middle, right = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    mouse = pygame.Surface((1,1))
    mouse_rect = mouse.get_rect(center=(mouse_pos))
    for event in pygame.event.get(): #Store events in event
        if event.type == pygame.QUIT: #If the event is to close pygame then quit the program
            pygame.quit()
            exit()
       
    #If user left clicks 
    if left:
        if display_mode == "menu":
            if main.start_rect.colliderect(mouse_rect): #Start
                game_active = True
                display_mode = "none"
                music.play(loops=-1)
            if main.exit_rect.colliderect(mouse_rect): #Exit
                pygame.quit()
                exit()
            if main.credits_rect.colliderect(mouse_rect): #Credits
                display_mode = "credits"
        if display_mode == "credits":
            if main.back_rect.colliderect(mouse_rect):
                display_mode = "menu"
   

    main.display(display_mode)
    pygame.display.update()
    FPS.tick(60)

audio[main.dialogue_index].play()
#Main Game Loop
while game_active:
    left, middle, right = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    mouse_surf = pygame.Surface((10,10))
    mouse_rect = mouse_surf.get_rect(center=mouse_pos)
    for event in pygame.event.get(): #Store events in event
        if event.type == pygame.QUIT: #If the event is to close pygame then quit the program
            pygame.quit()
            exit()
        if event.type == SCREEN_UPDATE: #If the time is 150
            main.update() #Call the update function from the MAIN() class
        if event.type == FAST_UPDATE:
            main.fast_update()
        if event.type == SLOW_UPDATE:
            main.slow_update()
        if event.type == pygame.KEYDOWN: #Checks wether a key on your keyboard is pressed
            if event.key == pygame.K_UP: #If the pressed key is the up arrow
                if main.snake.direction.y != 1: #Checks to make sure snake isnt going down (More info at line 1)
                    main.snake.direction = Vector2(0,-1) #Changes the direction of the snake by making the y -1
            elif event.key == pygame.K_DOWN: #If the pressed key is the down arrow
                if main.snake.direction.y != -1: #Checks to make sure snake isnt going up (More info at line 1)
                    main.snake.direction = Vector2(0,1) #Changes the direction of the snake by making the y 1
            elif event.key == pygame.K_LEFT: #If the pressed key is the left arrow
                if main.snake.direction.x != 1: #Checks to make sure snake isnt going right (More info at line 1)
                    main.snake.direction = Vector2(-1,0) #Changes the direction of the snake by making the x -1
            elif event.key == pygame.K_RIGHT: #If the pressed key is the right arrow
                if main.snake.direction.x != -1: #Checks to make sure snake isnt going left (More info at line 1)
                    main.snake.direction = Vector2(1,0) #Changes the direction of the snake by making the x 1
            elif event.key == pygame.K_SPACE: #Testing
                key_list = [1,9,11,13]
                audio[main.dialogue_index].stop()
                audio[main.dialogue_index].set_volume(1)
                if main.dialogue_active:
                    if main.dialogue_index >= 17:
                        pygame.quit()
                        exit()
                    else:
                        main.dialogue_index += 1
                        if main.dialogue_index in key_list:
                            main.dialogue_active = False
                        else:
                            audio[main.dialogue_index].play()
            elif event.key == pygame.K_ESCAPE:
                    if status == False:
                        display = display_mode
                        display_mode = "pause"
                        status = True
                    else:
                        display_mode = display
                        status = False

    if left:
        if display_mode == "pause":
            resume = pygame.Surface((280,60))
            resume_rect = resume.get_rect(center=(400,310))
            leave = pygame.Surface((150,60))
            leave_rect = leave.get_rect(center=(400,480))
            if resume_rect.colliderect(mouse_rect):
                display_mode = display
                status = False
            elif leave_rect.colliderect(mouse_rect):
                pygame.quit()
                exit()
        elif display_mode == "ransom":
            bitcoin = pygame.Surface((80,80))
            bitcoin_rect = bitcoin.get_rect(center=(400,650))
            skull = pygame.Surface((40,40))
            skull_rect = skull.get_rect(center=(760,40))
            if bitcoin_rect.colliderect(mouse_rect):
                if main.score >= 50:
                    main.score -= 50
                    display_mode = "tech"
                elif main.score >= 40:
                    main.score -= 40
                    display_mode = "tech"
                elif main.score >= 30:
                    main.score -= 30
                    display_mode = "tech"
                elif main.score >= 20:
                    main.score -= 20
                    display_mode = "tech"
                elif main.score >= 10:
                    main.score -= 10
                    display_mode = "tech"
                else:
                    bits.stop()
                    bits.play()
            if skull_rect.colliderect(mouse_rect):
                main.memory += 1
                display_mode = "tech"
                bits.stop()

    #Borders
    area_surf = pygame.Surface(area_size)
    area_rect = area_surf.get_rect(center=area_pos)      
    pygame.display.update() #Update the display
    FPS.tick(60) #Set the FPS to 60