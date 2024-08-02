import pygame

window_width = 600
window_height = 500

game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("SwitchIt!")
bg = pygame.image.load('Backgrounds/castle_background.png')
wizard_run_left = [pygame.image.load('sprites/male/Wizard/run_left/00.png'), pygame.image.load('sprites/male/Wizard/run_left/10.png'),
                   pygame.image.load('sprites/male/Wizard/run_left/20.png'), pygame.image.load('sprites/male/Wizard/run_left/30.png'),
                   pygame.image.load('sprites/male/Wizard/run_left/40.png'), pygame.image.load('sprites/male/Wizard/run_left/50.png'),
                   pygame.image.load('sprites/male/Wizard/run_left/60.png'), pygame.image.load('sprites/male/Wizard/run_left/70.png')]

wizard_run_right = [pygame.image.load('sprites/male/Wizard/run/00.png'), pygame.image.load('sprites/male/Wizard/run/10.png'),
                    pygame.image.load('sprites/male/Wizard/run/20.png'), pygame.image.load('sprites/male/Wizard/run/30.png'),
                    pygame.image.load('sprites/male/Wizard/run/40.png'), pygame.image.load('sprites/male/Wizard/run/50.png'),
                    pygame.image.load('sprites/male/Wizard/run/60.png'), pygame.image.load('sprites/male/Wizard/run/70.png')]

wizard_idle = [pygame.image.load('sprites/male/Wizard/idle/00.png'), pygame.image.load('sprites/male/Wizard/idle/10.png'),
               pygame.image.load('sprites/male/Wizard/idle/20.png'), pygame.image.load('sprites/male/Wizard/idle/30.png'),
               pygame.image.load('sprites/male/Wizard/idle/40.png'), pygame.image.load('sprites/male/Wizard/idle/50.png')]

               
width = 128
height = 128
vel = 5
x = 0 + vel
y = window_height - height - vel
walk_count = 0
left = False
right = False

clock = pygame.time.Clock()

def redraw_images():
    global walk_count
    game_window.blit(bg, (0,0))

    if walk_count + 1 >= 18:
        walk_count = 0

    if left == True:
        game_window.blit(wizard_run_left[walk_count//3], (x,y))
        walk_count += 1

    elif right == True:
        game_window.blit(wizard_run_right[walk_count//3],(x,y))
        walk_count += 1

    else:
        game_window.blit(wizard_idle[walk_count//3], (x,y))
        walk_count += 1


    #else:
        #game_window.blit(wizard_idle[walk_count//3],(x,y))
        #walk_count += 1
        
    pygame.display.update()
    
    
    

isJump = False
JumpCount = 10


run = True
while run == True:
    clock.tick(45) #needed ai assistance

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()

    if keys[pygame.K_LEFT] and x > 5:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < window_width - vel - width:
        x += vel
        left = False
        right = True
    else:
        left = False
        right = False
        
    if not(isJump):
        if keys[pygame.K_SPACE] or mouse[0]: #needed ai assistance with the mouse
            isJump = True
    else:
        if JumpCount >= -10:
            neg = 1
            #"neg" is used to conctrol which way the avatar goes during the jump whether it be up or down on the screen.
            if JumpCount < 0:
                #This if statement is needed to manipulate the "neg" variable so that it controls which way it goes on the screen.
                neg = -1
                #We would want "neg" to be a negative number when "JumpCount" is less than zero as we would want the avatar to move back down after it has been initially launched upwards.
                #Also as we go down, the y coordinate increases so as we have two negatives, the avatar will move down.
            y -= JumpCount ** 2 * 0.75 * neg
            #This controls the avatar's jump.
            #We square the "JumpCount" variable as it changes the acceleration of the avatar as it travels upwards and downwards.
            JumpCount -= 1
            #This is used to control the characteristic of the avatar's jump.
        else:
            isJump = False
            JumpCount = 10
            #This else statement ensures that a jump cannot be completed while a current jump is taking place.
            #"JumpCount" is reset to its initial value.
        
    #game_window.blit(bg, (0,0))
    #pygame.draw.rect(game_window, (255,0,0), (x,y,width,height))
    #pygame.display.update()

    redraw_images()
  
pygame.quit()
