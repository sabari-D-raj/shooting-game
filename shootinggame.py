import pygame
import random
import sys
import os

pygame.init()
WIDTH, HEIGHT = 800, 800
display=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Shooter")
clock=pygame.time.Clock()
fps = 60

base_path = os.path.dirname(__file__)
image_path = os.path.join(base_path, "images", "base.png")
target_path = os.path.join(base_path, "images", "target.png")
player_path=os.path.join(base_path, "images", "playeer.png")
if not os.path.exists(image_path):
    print("Image not found:", image_path)
    sys.exit(1)

background = pygame.image.load(image_path).convert()
target=pygame.image.load(target_path).convert_alpha()
player=pygame.image.load(player_path).convert_alpha()
target_width,target_height=100,100
target=pygame.transform.scale(target,(target_width,target_height))
player_size=250
player_x, player_y = 390, 500
player=pygame.transform.scale(player,(player_size,player_size))
WOOD_RECT = pygame.Rect(0, 0, WIDTH, HEIGHT // 2)
def random_target_positioon():
    marginX,marginY=target_width//2,target_height//2
    spaxeX=random.randint(WOOD_RECT.left+marginX,WOOD_RECT.right-marginX)
    spaxeY=random.randint(WOOD_RECT.top+marginY,WOOD_RECT.bottom-marginY)
    return (spaxeX - target_width//2, spaxeY - target_height//2)
target_pos = random_target_positioon()
target_rect = pygame.Rect(target_pos[0], target_pos[1], target_width, target_height)
target_alive = True       

running=True
while running:
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT:
            running=False
    key=pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        running=False
    elif key[pygame.K_a]:
        player_x-=5
    elif key[pygame.K_d]:
        player_x+=5
    display.blit(background,(0,0))
    display.blit(target,(300,300))
    display.blit(player,(player_x,player_y))
    clock.tick(fps)

    pygame.display.update()
pygame.quit()
sys.exit()