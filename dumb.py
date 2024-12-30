import pygame
#Initial template from https://www.pygame.org/docs/tut/newbieguide.html
#Author: Simon Goater Dec 2024
#Copying without attribution not permitted.
#My first pygame project. To run...
#sudo apt install python3-pygame
#python3 dumb.py
print("Press 'r' to restart!!")
pygame.init()
my_font = pygame.font.SysFont('Comic Sans MS', 60)
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

rects = pygame.Rect(screen_width-330,80,290,80)
rectm_colours = [(255,0,0), (0,255,0), (0,0,255), (0,255,255), (127,80,80), (55,80,127)]
rectm_xdir = [1,0,-1,0]
rectm_ydir = [0,1,0,-1]
l,t,w,h = 25,25,150,150
rectm = pygame.Rect(l,t,w,h)
colourno = 0
maxcolourno = 0
rectm_colour = 0
rectm_dir = 0
rectm_speed = 1

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(rectm.collidepoint(pygame.mouse.get_pos())):
              rectm_colour = (1 + rectm_colour) % len(rectm_colours)
              rectm_dir = (1 + rectm_dir) % 4
              rectm_speed += 1
              colourno += 1
              if (colourno > maxcolourno):
                maxcolourno = colourno
                
    keys = pygame.key.get_pressed()
    if keys[114] == 1: #Restart if key r pressed
      l,t,w,h = 25,25,150,150
      del rectm  
      rectm = pygame.Rect(l,t,w,h)
      colourno = 0
      maxcolourno = 0
      rectm_colour = 0
      rectm_dir = 0
      rectm_speed = 1
    
    # Do logical updates here.
    # ...

    screen.fill((100,0,100))  # Fill the display with a solid color

    # Render the graphics here.
    pygame.draw.rect(screen, (150,0,150), rects)
    text_surface = my_font.render(f"SCORE = {maxcolourno}", False, (0, 0, 0))
    screen.blit(text_surface, (screen_width - 300,100))
    pygame.draw.rect(screen, rectm_colours[rectm_colour], rectm)
    # ...

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
    rectm.move_ip(rectm_speed*rectm_xdir[rectm_dir], rectm_speed*rectm_ydir[rectm_dir])
    if (rectm.x + w < 0) or (rectm.x > screen_width) or (rectm.y > screen_height) or (rectm.y + h < 0):
      if (w > 50):
        w -= 5
      if (h > 50):
        h -= 5
      del rectm  
      rectm = pygame.Rect(l,t,w,h)
      rectm_colour = 0
      rectm_dir = 0
      rectm_speed = 1
      colourno = 0
      
