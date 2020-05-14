#Juego basado en Zelda
import pygame

ANCHO=600
ALTO=400

NEGRO=[0,0,0]
BLANCO=[255,255,255]
GRIS=[155,155,155]
HABANO=[240,230,180]
ROJO=[255,0,0]
VERDE=[0,255,0]
AZUL=[0,0,255]

class Fondo(pygame.sprite.Sprite):
    def __init__(self,img,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0

    def update(self):
        self.rect.x+=self.velx
        self.rect.y+=self.vely
        print "f.velx: "+str(self.velx)

class Jugador(pygame.sprite.Sprite):
    def __init__(self,pos=[190,150]):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([35,35])
        self.image.fill(ROJO)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velxp=0
        self.velxn=0
        self.velyp=0
        self.velyn=0
        #self.bloques=None


    def update(self):

        self.rect.x+=self.velxp+self.velxn
        #print "j.velxn: "+str(self.velxn)
        #print "j.velxp: "+str(self.velxp)
        #self.rect.x+=self.velxp
        #self.rect.x+=self.velxn

        ls_col=pygame.sprite.spritecollide(self,bloques,False)
        for b in ls_col:
            if (self.velxp+self.velxn) > 0:
                if self.rect.right > b.rect.left:
                    self.rect.right = b.rect.left
                    j.velxp=0
                    f.velx=0
                    for be in bloques:
                        be.velx=0
            elif self.velxn < 0:
                if self.rect.left < b.rect.right:
                    self.rect.left = b.rect.right
                    j.velxn=0
                    f.velx=0
                    for be in bloques:
                        be.velx=0

        if self.rect.x > (ANCHO-200):
            self.rect.x = ANCHO-200
            f.velx=-5
            for b in bloques:
                b.velx=-5
        elif self.rect.x < 150:
            self.rect.x = 150
            f.velx=5
            for b in bloques:
                b.velx=5

        self.rect.y+=self.velyp+self.velyn
        #self.rect.y+=self.velyp
        #self.rect.y+=self.velyn

        if self.rect.y > (ALTO-110):
            self.rect.y = ALTO-110
            f.vely=-5
            for b in bloques:
                b.vely=-5
        elif self.rect.y < 70:
            self.rect.y = 70
            f.vely=5
            for b in bloques:
                b.vely=5

        ls_col=pygame.sprite.spritecollide(self,bloques,False)
        for b in ls_col:
            if (self.velyp+self.velyn) > 0:
                if self.rect.bottom > b.rect.top:
                    self.rect.bottom = b.rect.top
                    j.velyp=0
                    f.vely=0
                    for be in bloques:
                        be.vely=0
            elif self.velyn < 0:
                if self.rect.top < b.rect.bottom:
                    self.rect.top = b.rect.bottom
                    j.velyn=0
                    f.vely=0
                    for be in bloques:
                        be.vely=0

class Bloque(pygame.sprite.Sprite):
    def __init__(self,pos,d_an,d_al,cl=VERDE):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([d_an,d_al])
        self.image.fill(cl)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0

    def update(self):
        self.rect.x+=self.velx
        self.rect.y+=self.vely


if __name__ == '__main__':
    pygame.init()
    #Definicion de variables
    reloj=pygame.time.Clock()
    ventana=pygame.display.set_mode([ANCHO,ALTO],32) # Revisar esta instruccion con: ([ANCHO,ALTO],32,32)

    fondo_img=pygame.image.load('fondo2.png')

    fondos=pygame.sprite.Group()
    jugadores=pygame.sprite.Group()
    bloques=pygame.sprite.Group()

    f=Fondo(fondo_img,[0,0])
    fondos.add(f)

    j=Jugador()
    jugadores.add(j)

    b=Bloque([300,300],200,120)
    bloques.add(b)

    b=Bloque([400,250],100,300,HABANO)
    bloques.add(b)

    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j.velxp=5
                    #j.vely=0
                elif event.key == pygame.K_LEFT:
                    j.velxn=-5
                    #j.vely=0
                elif event.key == pygame.K_UP:
                    j.velyn=-5
                    #j.velx=0
                elif event.key == pygame.K_DOWN:
                    j.velyp=5
                    #j.velx=0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    j.velxp=0
                    f.velx=0
                    for b in bloques:
                        b.velx=0
                elif event.key == pygame.K_LEFT:
                    j.velxn=0
                    f.velx=0
                    for b in bloques:
                        b.velx=0
                elif event.key == pygame.K_UP:
                    j.velyn=0
                    f.vely=0
                    for b in bloques:
                        b.vely=0
                elif event.key == pygame.K_DOWN:
                    j.velyp=0
                    f.vely=0
                    for b in bloques:
                        b.vely=0


        #Actualizacion de objetos
        jugadores.update()
        fondos.update()
        bloques.update()

        #Actualizacon de imagenes
        ventana.fill(NEGRO)
        #ventana.blit(fondo_img,[0,0])
        fondos.draw(ventana)
        jugadores.draw(ventana)
        bloques.draw(ventana)
        pygame.draw.line(ventana, BLANCO, [150,0], [150,ALTO])
        pygame.draw.line(ventana, BLANCO, [ANCHO-150,0], [ANCHO-150,ALTO])
        pygame.display.flip()
        reloj.tick(60)
