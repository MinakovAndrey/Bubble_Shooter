import pygame as pg
import sys
from random import randint

WHITE = (255, 255, 255)
RED = (225, 0, 0)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
PURPLE = (255, 0, 255)
LIGHTBLUE = (0, 255, 255)
COLOR = [RED, GREEN, BLUE, YELLOW, BLACK, PURPLE, LIGHTBLUE]

score = 0
FPS = 60
hardmode=1
d=[0 for j in range(0,hardmode)]
x=[randint(50,1150) for j in range(0,hardmode)]
y=[randint(50,550) for j in range(0,hardmode)]
r=[randint(10,50) for j in range(0,hardmode)]
vx=[randint(-3,4) for j in range(0,hardmode)]
vy=[randint(-3,4) for j in range(0,hardmode)]
col=[randint(0,6) for j in range(0,hardmode)]
j=0

def click(event):
    global j
    for j in range(0, hardmode):
        d[j] = ((event.pos[0] - x[j]) ** 2 + (event.pos[1] - y[j]) ** 2) ** 0.5
        if d[j]<=r[j]:
            return True
    return False


def new_ball(j):
    global x, y, r, col, vx, vy,f
    f=randint(1,50)
    if f==20:
        x[j] = randint(50, 1150)
        y[j] = randint(50, 550)
        r[j] = 20
        vx[j] = randint(-5, 6)
        vy[j] = randint(-5, 6)
    x[j] = randint(100, 1150)
    y[j] = randint(100, 550)
    r[j] = randint(10, 50)
    vx[j] = randint(-3, 4)
    vy[j] = randint(-3, 4)
    col[j] = COLOR[randint(0, 6)]
    pg.draw.circle(sc, col[j], (x[j], y[j]), r[j])


def update_score(j):
    global score,scoretext
    if f==20:
        score += int((25000 * (vx[j] ** 2 + vy[j] ** 2) ** 0.5 / r[j] ** 2) // 1)
    else:
        score += int((2500 * (vx[j] ** 2 + vy[j] ** 2) ** 0.5 / r[j] ** 2) // 1)
    scoretext = 'Score: ', str(score)


def update_position():
    global x, y, vx, vy
    for k in range(0,hardmode):
        if (x[k] >= 1200 - r[k]) or (x[k] <= r[k]):
            vx[k] = -vx[k]
            x[k] += vx[k]
        else:
            x[k] += vx[k]
        if (y[k] >= 600 - r[k]) or (y[k] <= r[k]):
            vy[k] = -vy[k]
            y[k] += vy[k]
        else:
            y[k] += vy[k]
        if f==20:
            col[k]=COLOR[randint(0, 6)]
        pg.draw.circle(sc, col[k], (x[k], y[k]), r[k])


def up_count():
    global hardmode,x,y,r,vx,vy,col,d
    hardmode += 1
    x = x + [randint(50, 1150)]
    y = y + [randint(50, 550)]
    r = r + [randint(10, 50)]
    vx = vx + [randint(-3, 4)]
    vy = vy + [randint(-3, 4)]
    col = col + [randint(0, 6)]
    d = d + [0]


def draw_text():
    global text_surface, text_rect
    font = pg.font.Font('freesansbold.ttf', 24)
    text_surface=font.render('SCORE: '+str(score), True, BLACK)
    text_rect=text_surface.get_rect()
    text_rect.center(500,400)
    surf.blit(text_surface,text_rect)

pg.init()
sc = pg.display.set_mode((1200, 600))
pg.display.set_caption('Bubble shooter')
font = pg.font.SysFont('freesansbold.ttf', 24)
sc.fill(WHITE)
pg.display.update()
clock = pg.time.Clock()
for j in range(0,count):
    new_ball(j)

while 1:
    clock.tick(FPS)
    for i in pg.event.get():
        if i.type == pg.QUIT:
            print(score)
            pg.quit()
            sys.exit()
        if i.type == pg.MOUSEBUTTONDOWN:
            if click(i):
                update_score(j)
                for k in range(0,count):
                    new_ball(j)
                if score>=count*100:
                    up_count()
    draw_text()
    sc.fill(WHITE)
    text_surface,rect = font.render('SCORE:'+str(score),True, BLACK)
    sc.blit(text_surface,(40,250))
    pg.display.flip()

