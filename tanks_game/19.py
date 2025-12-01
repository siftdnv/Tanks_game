import pygame
import random
import sys
import time
w=800
h=600
x=20
y=h//2
x1=920
x2=22
FPS=60
score=0
score1=0
max_score=0
gover=0
clock=pygame.time.Clock()
white=(255,255,255)
BLACK=(0,0,0)
grey=(125,158,192)
x_enemy=(300,380,460,540,220,140,60)
pygame.mixer.pre_init(44100,-16,5,512)
pygame.init()
screen=pygame.display.set_mode((w,h))
game_over=pygame.mixer.Sound("game_over.mp3")
bullet_sound=pygame.mixer.Sound("bullet.mp3")
even_sound=pygame.mixer.Sound("even_del.mp3")
tank=pygame.image.load("tank_right.png")
pul=pygame.image.load("pull.png")
enemy=pygame.image.load("enemyy.png")
#pygame.image.load("C:/Users/1/Desktop/krt/бег/бег1.png"),
#pygame.image.load("C:/Users/1/Desktop/krt/бег/бег2.png"),
#pygame.image.load("C:/Users/1/Desktop/krt/бег/бег3.png"),
#pygame.image.load("C:/Users/1/Desktop/krt/бег/бег4.png"),
#pygame.image.load("C:/Users/1/Desktop/krt/бег/бег5.png"),
#pygame.image.load("C:/Users/1/Desktop/krt/бег/бег2.png"),
enemy_anim=[
    pygame.image.load("enemyy.png"),
    pygame.image.load("enemyy.png"),
    pygame.image.load("enemyy.png"),
    pygame.image.load("enemyy.png"),
    pygame.image.load("enemyy.png"),
    pygame.image.load("enemyy.png"),
]
enemy_frame=0
font=pygame.font.Font("Cyrillic.ttf",35)
text1=font.render("Вы проиграли!",True,(238,59,59))
text2=font.render("Начать заново",True,(139,76,57))
text2_rect=text2.get_rect(topleft=(140,290))
text3=font.render("Score:",True,(white))
text4=font.render("Патроны:",True,(BLACK))
bullets=[]
bullets_list=5
enemy_list=[]
enemy_timer=pygame.USEREVENT+1
pygame.time.set_timer(enemy_timer,900)
def draw_text(surf,text,x,y):
    text_score=font.render(text,True,(BLACK))
    surf.blit(text_score,(x,y))
running = True
gameplay=True
while running ==True:
    screen.fill(white)
    screen.blit(tank,(x,y))
    screen.blit(text4,(90,20))
    draw_text(screen,str(score),x2,20)
    draw_text(screen,str(bullets_list),350,20)
    if gameplay:
        pygame.draw.line(screen,BLACK,[80,610],[80,0],2)
        pul_rect=pul.get_rect(topleft=(x+50,y+5))
        y1=random.choice(x_enemy)
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                running
                sys.exit()
                running=False
            elif i.type==enemy_timer:
                enemy_list.append(enemy.get_rect(topleft=(x1,y1)))
            elif i.type==pygame.KEYDOWN:
                if i.key==pygame.K_SPACE and bullets_list>0:
                    bullet_sound.play()
                    bullets.append(pul_rect)
                    bullets_list-=1
        if enemy_list:
            for (ind,elem) in enumerate (enemy_list):
                screen.blit(enemy_anim[enemy_frame//10],(elem.x,elem.y))
                if enemy_frame==59:
                    enemy_frame=0
                else:
                    enemy_frame+=1
                elem.x-=4
                if elem.x<-10:
                    enemy_list.pop(ind)
        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            tank=pygame.image.load("tank_up.png")
            y=y-5
        elif keys[pygame.K_DOWN]:
            tank=pygame.image.load("tank_down.png")
            y=y+5
        else:
            tank=pygame.image.load("tank_right.png")
        for (i,el) in enumerate (bullets):
            screen.blit(pul,(el.x,el.y))
            el.x+=12
            if el.x>802:
                bullets.pop(i)
            if enemy_list:
                for (ind, enem) in enumerate(enemy_list):
                    if el.colliderect(enem):
                        even_sound.play()
                        enemy_list.pop(ind)
                        bullets.pop(i)
                        score+=1
                        bullets_list+=1
        if enemy_list:
            for elemen in enemy_list:
                if elemen.x==80:
                    gameplay=False
                    print("LOSE")
                    print(max_score)
                    game_over.play()
        if score>max_score:
            max_score=score
        if score>=10:
            x2=8
    else:
        screen.fill(grey)
        screen.blit(text1,(165,250))
        screen.blit(text2,text2_rect)
        screen.blit(text3, (280,320))
        draw_text(screen,str(score),470,320)
        bullets.clear()
        enemy_list.clear()
        bullets_list=5
        x=20
        y=300
        mouse=pygame.mouse.get_pos()
        if text2_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            score=0
            gameplay=True
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT:
            running=False
            sys.exit()
    pygame.display.update()
    clock.tick(FPS)
