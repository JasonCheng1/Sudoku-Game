import pygame #import the pygame module
pygame.init() #initilize pygame always have to do this at begining of program
ScreenWidth = 500
ScreenHeight = 500
win = pygame.display.set_mode((ScreenWidth, ScreenHeight))#width and height of the window which is what you draw on (the dimension of the winodw must be in a tuple)
pygame.display.set_caption("First Game")#Name of the pop up window


#If you want to move the character the parameters are below
x = 250 #x-cooridnate
y = 250 #y-coordinate 
width = 40 #width of character
height = 60 #height of character
vel = 5 #velocity of character

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < ScreenWidth - width - vel:
        x += vel
    if keys[pygame.K_UP] and y > vel:
        y -= vel
    if keys[pygame.K_DOWN] and y < ScreenHeight - height - vel:
        y += vel
    
    win.fill((0,0,0)) #resets the window to all black
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))#draw red rectangle specified by x,y,z 
    pygame.display.update()#updates the window
pygame.quit()