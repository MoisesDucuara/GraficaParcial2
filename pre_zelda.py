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

ls_col=None

class Jugador(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([50,50]) # Revisar esta instruccion con: ([50,50],32,32)
        self.image.fill(ROJO)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velxp=0
        self.velxn=0
        self.velyp=0
        self.velyn=0
        self.bloques=None


    def update(self):
        self.rect.x+=self.velxp
        self.rect.x+=self.velxn
        '''
        ls_col=pygame.sprite.spritecollide(self,bloques,False)
        for b in ls_col:
            if self.velx > 0:
                if self.rect.right > b.rect.left:
                    self.rect.right = b.rect.left
                    self.velx=0
            else:
                if self.rect.left < b.rect.right:
                    self.rect.left = b.rect.right
                    self.velx=0
                    '''

        self.rect.y+=self.velyp
        self.rect.y+=self.velyn
        '''
        ls_col=pygame.sprite.spritecollide(self,bloques,False)
        for b in ls_col:
            if self.vely > 0:
                if self.rect.bottom > b.rect.top:
                    self.rect.bottom = b.rect.top
                    self.vely=0
            else:
                if self.rect.top < b.rect.bottom:
                    self.rect.top = b.rect.bottom
                    self.vely=0
                    '''

pygame.init()
#Definicion de variables
reloj=pygame.time.Clock()
ventana=pygame.display.set_mode([ANCHO,ALTO])

jugadores=pygame.sprite.Group()

j=Jugador([200,250])
jugadores.add(j)

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
            elif event.key == pygame.K_LEFT:
                j.velxn=0
                #j.vely=0
            elif event.key == pygame.K_UP:
                j.velyn=0
                #j.velx=0
            elif event.key == pygame.K_DOWN:
                j.velyp=0
                #j.velx=0


    #Actualizacion de objetos
    jugadores.update()

    #Actualizacon de imagenes
    ventana.fill(NEGRO)
    jugadores.draw(ventana)
    pygame.display.flip()
    reloj.tick(60)
