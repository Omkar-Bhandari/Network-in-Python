import pygame
from network import Network

pygame.init()

width = 500
height = 500
win = pygame.display.set_mode((width,height))

clientNum = 0

class Player:
    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 1

    def draw(self,win):
        pygame.draw.rect(win , self.color , self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x , self.y , self.width , self.height)



def readpos(str):
    str = str.split(",")
    return int(str[0]),int(str[1])

def makepos(tup):
    return str(tup[0]) + "," +str(tup[1])


def RedrawWindow(win,Player,Player2):
    win.fill((255,255,255))
    Player.draw(win)
    Player2.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    startpos = readpos(n.getPos())
    p = Player(startpos[0],startpos[1],25,25,(0,0,255))
    p2 = Player(0,0,25,25,(255,0,255))

    while run:

        p2pos = readpos(n.send(makepos((p.x,p.y))))
        p2.x = p2pos[0]
        p2.y = p2pos[1]
        p2.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                run = False

        p.move()
        RedrawWindow(win,p,p2)

main()