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

paused = False
def random_target_positioon():
    marginX,marginY=target_width//2,target_height//2
    spaxeX=random.randint(WOOD_RECT.left+marginX,WOOD_RECT.right-marginX)
    spaxeY=random.randint(WOOD_RECT.top+marginY,WOOD_RECT.bottom-marginY)
    return (spaxeX - target_width//2, spaxeY - target_height//2)
target_pos = random_target_positioon()
target_rect = pygame.Rect(target_pos[0], target_pos[1], target_width, target_height)
target_alive = True 
target_move_timer = 0
target_move_interval = 2000 
bulllets = []
BULLET_WIDTH, BULLET_HEIGHT = 6, 12
BULLET_SPEED = 12
score = 0
level= 1
def spaw_target():
    global target_pos, target_rect, target_alive
    target_pos = random_target_positioon()
    target_rect.topleft = target_pos
    target_alive = True
def fire_bullet():
    bx = player_x + player_size // 2 - BULLET_WIDTH // 2
    by = player_y  
    rect = pygame.Rect(bx, by, BULLET_WIDTH, BULLET_HEIGHT)
    bulllets.append(rect)
def score_and_level():
    font=pygame.font.SysFont("Arial",30)
    score_surf = font.render(f"Score: {score}", True, (255, 255, 255))
    level_surf = font.render(f"Level: {level}", True, (255, 255, 255))
    display.blit(score_surf, (10, 10))
    display.blit(level_surf, (10, 50))
def paused_menu():
    font=pygame.font.SysFont("Arial",30)
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))
    display.blit(overlay, (0, 0))
    text = font.render("PAUSED", True, (255, 255, 255))
    info = font.render("Press P to Resume    Q to Quit", True, (255, 255, 255))
    display.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20)))
    display.blit(info, info.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30)))
running=True
last_move_change = pygame.time.get_ticks()
spaw_target()
while running:
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_p:
                paused=not paused
            if paused  and event.key==pygame.K_q:
                running=False
            if event.key==pygame.K_SPACE and not paused:
                fire_bullet()
            elif event.type==pygame.MOUSEBUTTONDOWN and not paused:
                if event.button==1:
                    fire_bullet()
            if score >= level * 5:
                level += 1
                target_move_interval = max(500, target_move_interval - 200)

    key=pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        running=False
    elif key[pygame.K_a]:
        player_x-=5
    elif key[pygame.K_d]:
        player_x+=5
    for b in bulllets[:]:
        b.y -= BULLET_SPEED
        if b.bottom < 0:
            bulllets.remove(b)
        elif target_alive and b.colliderect(target_rect):
            bulllets.remove(b)
            target_alive = False
            score += 1
    current_time = pygame.time.get_ticks()
    if current_time - target_move_timer > target_move_interval:
        spaw_target()
        target_move_timer = current_time
    display.blit(background,(0,0))
    display.blit(target, target_pos)

    display.blit(player,(player_x,player_y))
    clock.tick(fps)

    for b in bulllets:
        pygame.draw.rect(display, (255, 220, 0), b)
    pygame.draw.rect(display, (0,255,0), target_rect, 2)
    score_and_level()
    if paused:
        paused_menu()
        
    pygame.display.update()
pygame.quit()
sys.exit()