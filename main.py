import pygame # import library
pygame.init() 
# Create the window
win = pygame.display.set_mode((800, 600))
img = pygame.image.load('assets/Top_Down_Survivor/knife/idle/survivor-idle_knife_0.png').convert_alpha()
font = pygame.font.SysFont ("arial", 72)
text = font.render ("Welcome", True,  (255, 255, 255))


  
  # Create
run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False


  
 
        
    
  


win.fill((100, 50, 20))
win.blit(img, (400, 300))
win.blit(text, (400, 300))

  # Draw a rectangle  
  #Update the display
pygame.display.update()

print("Ending game")
pygame.quit()
