#Juego basado en Zelda
import pygame
import ConfigParser

ANCHO=600
ALTO=400

NEGRO=[0,0,0]
BLANCO=[255,255,255]
GRIS=[155,155,155]
HABANO=[240,230,180]
ROJO=[255,0,0]
VERDE=[0,255,0]
AZUL=[0,0,255]

def recorte(img,fil,col,ini_f):
    m=[]
    for i in range(fil):
        fila=[]
        for j in range(col):
            cuadro=img.subsurface(j*32,(i+ini_f)*32,32,32)
            fila.append(cuadro)
        m.append(fila)
    return m

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

class Jugador(pygame.sprite.Sprite):
    def __init__(self,matriz_img,pos=[190,150]):
        pygame.sprite.Sprite.__init__(self)
        self.matriz_img=matriz_img
        self.accion=0
        self.cont_accion=0
        self.lim_accion=[0,0,0,0,5,5,6,7,2,2,2,2,2,2,2,2]
        self.image=self.matriz_img[self.accion][self.cont_accion]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velxp=0
        self.velxn=0
        self.velyp=0
        self.velyn=0
        self.vely_mojado=0
        self.velx_mojado=0
        self.vida=100
        self.espada=0
        self.arco=0
        #self.bloques=None

    def update(self):

        self.rect.y+=self.velyp+self.velyn+self.vely_mojado

        #Colisiones en el eje Y
        ls_col=pygame.sprite.spritecollide(self,bloques,False)
        for b in ls_col:
            if (self.rect.bottom > b.rect.top) and (self.rect.bottom <= b.rect.top+8):
                #print "Colision 1"
                self.velyp=0
                self.rect.bottom = b.rect.top
                f.vely=0
                for be in bloques:
                    be.vely=0
                for be in bloques_agua:
                    be.vely=0
                for be in bloques_lava:
                    be.vely=0
                for b in enemigos1:
                    b.vely=0
                for b in enemigos2:
                    b.vely=0
                for b in ataque_flecha:
                    b.vely=0
                for b in generadores:
                    b.vely=0
            elif (self.rect.top < b.rect.bottom) and (self.rect.top >= b.rect.bottom-8):
                #print "Colision 2"
                self.velyn=0
                self.rect.top = b.rect.bottom
                f.vely=0
                for be in bloques:
                    be.vely=0
                for be in bloques_agua:
                    be.vely=0
                for be in bloques_lava:
                    be.vely=0
                for b in enemigos1:
                    b.vely=0
                for b in enemigos2:
                    b.vely=0
                for b in ataque_flecha:
                    b.vely=0
                for b in generadores:
                    b.vely=0

        self.rect.x+=self.velxp+self.velxn+self.velx_mojado

        #Colisiones en el eje X
        ls_col=pygame.sprite.spritecollide(self,bloques,False)
        for b in ls_col:
            if (self.rect.right > b.rect.left) and (self.rect.right <= b.rect.left+8):
                #print "Colision 3"
                self.velxp=0
                self.rect.right = b.rect.left
                f.velx=0
                for be in bloques:
                    be.velx=0
                for be in bloques_agua:
                    be.velx=0
                for be in bloques_lava:
                    be.velx=0
                for b in enemigos1:
                    b.velx=0
                for b in enemigos2:
                    b.velx=0
                for b in ataque_flecha:
                    b.velx=0
                for b in generadores:
                    b.velx=0
            elif (self.rect.left < b.rect.right) and (self.rect.left >= b.rect.right-8):
                #print "Colision 4"
                self.velxn=0
                self.rect.left = b.rect.right
                f.velx=0
                for be in bloques:
                    be.velx=0
                for be in bloques_agua:
                    be.velx=0
                for be in bloques_lava:
                    be.velx=0
                for b in enemigos1:
                    b.velx=0
                for b in enemigos2:
                    b.velx=0
                for b in ataque_flecha:
                    b.velx=0
                for b in generadores:
                    b.velx=0


        #Colision enemigos
        ls_enemigo=pygame.sprite.spritecollide(self,enemigos1,False)
        if  ls_enemigo != []:
            self.vida+=5
        ls_enemigo=pygame.sprite.spritecollide(self,enemigos2,False)
        if  ls_enemigo != []:
            self.vida-=5
        #Comportamiento con la lava
        ls_lava=pygame.sprite.spritecollide(self,bloques_lava,False)
        if ls_lava != []:
            self.vida-=1
        #Comportamiento con el agua
        ls_agua=pygame.sprite.spritecollide(self,bloques_agua,False)
        if ls_agua != []:
            self.vely_mojado=3
            if self.velxp+self.velxn==0:
                self.velx_mojado=0
            elif self.velxp+self.velxn>0:
                self.velx_mojado=-3
            elif self.velxp+self.velxn<0:
                self.velx_mojado=3
        else:
            self.vely_mojado=0
            self.velx_mojado=0

        #Empuje de la caja del moviemiento del mapa
        if self.rect.y > (ALTO-110):
            #print "Caja 1"
            self.rect.y = ALTO-110
            self.velxp=0
            self.velxn=0
            f.vely=-5
            f.velx=0
            for b in bloques:
                b.vely=-5
                b.velx=0
            for bf in bloques_agua:
                bf.vely=-5
                bf.velx=0
            for bf in bloques_lava:
                bf.vely=-5
                bf.velx=0
            for b in enemigos1:
                b.vely=-5
                b.velx=0
            for b in enemigos2:
                b.vely=-5
                b.velx=0
            for b in ataque_flecha:
                b.vely=-5
                b.velx=0
            for b in generadores:
                b.vely=-5
                b.velx=0
        elif self.rect.y < 70:
            #print "Caja 2"
            self.rect.y = 70
            self.velxp=0
            self.velxn=0
            if ls_agua!=[]:
                f.vely=2
                f.velx=0
                for b in bloques:
                    b.vely=2
                    b.velx=0
                for bf in bloques_agua:
                    bf.vely=2
                    bf.velx=0
                for bf in bloques_lava:
                    bf.vely=2
                    bf.velx=0
                for b in enemigos1:
                    b.vely=2
                    b.velx=0
                for b in enemigos2:
                    b.vely=2
                    b.velx=0
                for b in ataque_flecha:
                    b.vely=2
                    b.velx=0
                for b in generadores:
                    b.vely=2
                    b.velx=0
            else:
                f.vely=5
                f.velx=0
                for b in bloques:
                    b.vely=5
                    b.velx=0
                for bf in bloques_agua:
                    bf.vely=5
                    bf.velx=0
                for bf in bloques_lava:
                    bf.vely=5
                    bf.velx=0
                for b in enemigos1:
                    b.vely=5
                    b.velx=0
                for b in enemigos2:
                    b.vely=5
                    b.velx=0
                for b in ataque_flecha:
                    b.vely=5
                    b.velx=0
                for b in generadores:
                    b.vely=5
                    b.velx=0


        if self.rect.x > (ANCHO-200):
            #print "Caja 3"
            self.rect.x = ANCHO-200
            self.velyp=0
            self.velyn=0
            if ls_agua!=[]:
                f.velx=-2
                f.vely=0
                for b in bloques:
                    b.velx=-2
                    b.vely=0
                for bf in bloques_agua:
                    bf.velx=-2
                    bf.vely=0
                for bf in bloques_lava:
                    bf.velx=-2
                    bf.vely=0
                for b in enemigos1:
                    b.velx=-2
                    b.vely=0
                for b in enemigos2:
                    b.velx=-2
                    b.vely=0
                for b in ataque_flecha:
                    b.velx=-2
                    b.vely=0
                for b in generadores:
                    b.velx=-2
                    b.vely=0
            else:
                f.velx=-5
                f.vely=0
                for b in bloques:
                    b.velx=-5
                    b.vely=0
                for bf in bloques_agua:
                    bf.velx=-5
                    bf.vely=0
                for bf in bloques_lava:
                    bf.velx=-5
                    bf.vely=0
                for b in enemigos1:
                    b.velx=-5
                    b.vely=0
                for b in enemigos2:
                    b.velx=-5
                    b.vely=0
                for b in ataque_flecha:
                    b.velx=-5
                    b.vely=0
                for b in generadores:
                    b.velx=-5
                    b.vely=0
        elif self.rect.x < 150:
            #print "Caja 4"
            self.rect.x = 150
            self.velyp=0
            self.velyn=0
            f.velx=5
            f.vely=0
            for b in bloques:
                b.velx=5
                b.vely=0
            for bf in bloques_agua:
                bf.velx=5
                bf.vely=0
            for bf in bloques_lava:
                bf.velx=5
                bf.vely=0
            for b in enemigos1:
                b.velx=5
                b.vely=0
            for b in enemigos2:
                b.velx=5
                b.vely=0
            for b in ataque_flecha:
                b.velx=5
                b.vely=0
            for b in generadores:
                b.velx=5
                b.vely=0

        #Manejo de sprites jugador
        if self.arco>=1 and self.arco<4:
            if self.accion==0 or self.accion==4:
                self.accion=12
                if self.arco==1:
                    fle=Flecha(flecha_derecha,[self.rect.right-10,self.rect.top+16])
                    fle.velx_pro=7
                    ataque_flecha.add(fle)
            elif self.accion==1 or self.accion==5:
                self.accion=13
                if self.arco==1:
                    fle=Flecha(flecha_izquierda,[self.rect.left-5,self.rect.top+16])
                    fle.velx_pro=-7
                    ataque_flecha.add(fle)
            elif self.accion==2 or self.accion==6:
                self.accion=14
                if self.arco==1:
                    fle=Flecha(flecha_abajo,[self.rect.left+14,self.rect.bottom-7])
                    fle.vely_pro=7
                    ataque_flecha.add(fle)
            elif self.accion==3 or self.accion==7:
                self.accion=15
                if self.arco==1:
                    fle=Flecha(flecha_arriba,[self.rect.left+14,self.rect.top-6])
                    fle.vely_pro-=7
                    ataque_flecha.add(fle)
            self.arco+=1
        elif self.arco==4:
            self.arco=0
            if self.accion==12:
                self.accion=0
                ataque_espada.remove(ataque_espada)
            elif self.accion==13:
                self.accion=1
                ataque_espada.remove(ataque_espada)
            elif self.accion==14:
                self.accion=2
                ataque_espada.remove(ataque_espada)
            elif self.accion==15:
                self.accion=3
                ataque_espada.remove(ataque_espada)
        elif self.espada>=1 and self.espada<4:
            if self.accion==0 or self.accion==4 or self.accion==8:
                self.accion=8
                if self.espada==1:
                    esp=Ataque([self.rect.right,self.rect.top],16,32)
                    ataque_espada.add(esp)
            elif self.accion==1 or self.accion==5 or self.accion==9:
                self.accion=9
                if self.espada==1:
                    esp=Ataque([self.rect.left-16,self.rect.top],16,32)
                    ataque_espada.add(esp)
            elif self.accion==2 or self.accion==6 or self.accion==10:
                self.accion=10
                if self.espada==1:
                    esp=Ataque([self.rect.left,self.rect.bottom],32,16)
                    ataque_espada.add(esp)
            elif self.accion==3 or self.accion==7 or self.accion==11:
                self.accion=11
                if self.espada==1:
                    esp=Ataque([self.rect.left,self.rect.top-16],32,16)
                    ataque_espada.add(esp)
            self.espada+=1
            for e in ataque_espada:
                if self.accion==8:
                    e.rect.left=self.rect.right
                    e.rect.top=self.rect.top
                elif self.accion==9:
                    e.rect.left=self.rect.left-16
                    e.rect.top=self.rect.top
                elif self.accion==10:
                    e.rect.left=self.rect.left
                    e.rect.top=self.rect.bottom
                elif self.accion==11:
                    e.rect.left=self.rect.left
                    e.rect.top=self.rect.top-16
        elif self.espada==4:
            self.espada=0
            if self.accion==8:
                self.accion=0
                ataque_espada.remove(ataque_espada)
            elif self.accion==9:
                self.accion=1
                ataque_espada.remove(ataque_espada)
            elif self.accion==10:
                self.accion=2
                ataque_espada.remove(ataque_espada)
            elif self.accion==11:
                self.accion=3
                ataque_espada.remove(ataque_espada)
        else:
            if self.velyn+self.velyp > 0:
                self.accion=6
            elif self.velyn+self.velyp < 0:
                self.accion=7
            elif self.velxn+self.velxp > 0:
                self.accion=4
            elif self.velxn+self.velxp < 0:
                self.accion=5
            elif self.velyn+self.velyp == 0:
                if self.accion==6:
                    self.accion=2
                elif self.accion==7:
                    self.accion=3
            if self.velxn+self.velxp == 0:
                if self.accion==4:
                    self.accion=0
                elif self.accion==5:
                    self.accion=1

        if self.cont_accion<self.lim_accion[self.accion]:
            self.cont_accion+=1
        else:
            self.cont_accion=0

        self.image=self.matriz_img[self.accion][self.cont_accion]

class Enemigo(pygame.sprite.Sprite):
    def __init__(self,matriz_img,pos,tipo,ene):
        pygame.sprite.Sprite.__init__(self)
        self.matriz_img=matriz_img
        self.tipo=tipo
        self.accion=0
        self.cont_accion=0
        self.lim_accion=[2,2,2,2]
        self.image=self.matriz_img[self.accion][self.cont_accion]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0
        self.velx_pro=0
        self.vely_pro=0
        self.cont_mov=0 #Es para tener la secuencia del enemigo1
        self.vida=100
        self.ene=ene

    def update(self):
        self.rect.x+=self.velx+self.velx_pro

        #Colisiones en el eje X
        ls_col=pygame.sprite.spritecollide(self,bloques,False)
        for b in ls_col:
            if (self.rect.right > b.rect.left) and (self.rect.right <= b.rect.left+8):
                #print "Colision 3"
                self.velxp=0
                self.rect.right = b.rect.left
                f.velx=0
                for be in bloques:
                    be.velx=0
                for be in bloques_agua:
                    be.velx=0
                for be in bloques_lava:
                    be.velx=0
                for b in enemigos1:
                    b.velx=0
                for b in enemigos2:
                    b.velx=0
            elif (self.rect.left < b.rect.right) and (self.rect.left >= b.rect.right-8):
                #print "Colision 4"
                self.velxn=0
                self.rect.left = b.rect.right
                f.velx=0
                for be in bloques:
                    be.velx=0
                for be in bloques_agua:
                    be.velx=0
                for be in bloques_lava:
                    be.velx=0
                for b in enemigos1:
                    b.velx=0
                for b in enemigos2:
                    b.velx=0

        self.rect.y+=self.vely+self.vely_pro

        #Colisiones en el eje Y
        ls_col=pygame.sprite.spritecollide(self,bloques,False)
        for b in ls_col:
            if (self.rect.bottom > b.rect.top) and (self.rect.bottom <= b.rect.top+8):
                #print "Colision 1"
                self.velyp=0
                self.rect.bottom = b.rect.top
                f.vely=0
                for be in bloques:
                    be.vely=0
                for be in bloques_agua:
                    be.vely=0
                for be in bloques_lava:
                    be.vely=0
                for b in enemigos1:
                    b.vely=0
                for b in enemigos2:
                    b.vely=0
            elif (self.rect.top < b.rect.bottom) and (self.rect.top >= b.rect.bottom-8):
                #print "Colision 2"
                self.velyn=0
                self.rect.top = b.rect.bottom
                f.vely=0
                for be in bloques:
                    be.vely=0
                for be in bloques_agua:
                    be.vely=0
                for be in bloques_lava:
                    be.vely=0
                for b in enemigos1:
                    b.vely=0
                for b in enemigos2:
                    b.vely=0


        if self.tipo==1:
            if self.cont_mov==0:
                self.velx_pro=-5
                self.vely_pro=0
            elif self.cont_mov==3:
                self.velx_pro=0
                self.vely_pro=5
            elif self.cont_mov==6:
                self.velx_pro=5
                self.vely_pro=0
            elif self.cont_mov==9:
                self.velx_pro=0
                self.vely_pro=-5
            elif self.cont_mov==11:
                self.cont_mov=-1
            self.cont_mov+=1
        if self.tipo==2:
            if j.rect.right > self.rect.left-20 and j.rect.left < self.rect.right+20:
                if j.rect.top < self.rect.bottom+20 and j.rect.bottom > self.rect.top-20:
                    if j.rect.left+16 < self.rect.left:
                        self.velx_pro=-2
                        self.vely_pro=0
                    if j.rect.left+16 > self.rect.right:
                        self.velx_pro=2
                        self.vely_pro=0
                    if j.rect.top+16 < self.rect.top:
                        self.vely_pro=-2
                        self.velx_pro=0
                    if j.rect.top+16 > self.rect.bottom:
                        self.vely_pro=2
                        self.velx_pro=0
            else:
                self.velx_pro=0
                self.vely_pro=0


        #Manejo de danho
        ls_ataque=pygame.sprite.spritecollide(self,ataque_espada,True)
        if  ls_ataque != []:
            self.vida-=20
            print "ene1: "+str(self.vida)
        ls_fle=pygame.sprite.spritecollide(self,ataque_flecha,True)
        if  ls_fle != []:
            self.vida-=10

        #Muerte
        if self.vida<=0:
            if self.tipo==1:
                if self.ene==0:
                    ls_ene1[0]=100
                elif self.ene==1:
                    ls_ene1[1]=100
                elif self.ene==2:
                    ls_ene1[2]=100
                elif self.ene==3:
                    ls_ene1[3]=100
            elif self.tipo==2:
                if self.ene==0:
                    ls_ene2[0]=100
                elif self.ene==1:
                    ls_ene2[1]=100
                elif self.ene==2:
                    ls_ene2[2]=100
                elif self.ene==3:
                    ls_ene2[3]=100
            self.kill()

        #Manejo de sprites enemigo
        if self.vely_pro > 0:
            self.accion=0
        elif self.vely_pro < 0:
            self.accion=3
        elif self.velx_pro > 0:
            self.accion=2
        elif self.velx_pro < 0:
            self.accion=1
        elif self.vely_pro == 0 and self.velx_pro == 0:
            self.cont_accion=0

        if self.cont_accion<self.lim_accion[self.accion]:
            self.cont_accion+=1
        else:
            self.cont_accion=0

        self.image=self.matriz_img[self.accion][self.cont_accion]

class Generador(pygame.sprite.Sprite):
    def __init__(self,img,pos,tipo):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.tipo=tipo
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0
        self.integridad=100
        self.cantidad_enemigos=1
        self.lista_pos=[416,704]

    def update(self):
        self.rect.x+=self.velx
        self.rect.y+=self.vely

        #Manejo de danho
        ls_ataque=pygame.sprite.spritecollide(self,ataque_espada,True)
        if  ls_ataque != []:
            self.integridad-=20
        ls_fle=pygame.sprite.spritecollide(self,ataque_flecha,True)
        if  ls_fle != []:
            self.integridad-=1

        #Muerte
        if self.integridad<=0:
            self.kill()

class Bloque(pygame.sprite.Sprite):
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

        pygame.sprite.spritecollide(self,ataque_flecha,True)

class Ataque(pygame.sprite.Sprite):
    def __init__(self,pos,d_an,d_al):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([d_an,d_al])
        self.image.fill(AZUL)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0

class Flecha(pygame.sprite.Sprite):
    def __init__(self,img,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0
        self.velx_pro=0
        self.vely_pro=0

    def update(self):
        self.rect.x+=self.velx+self.velx_pro
        self.rect.y+=self.vely+self.vely_pro


if __name__ == '__main__':
    pygame.init()
    #Definicion de variables
    ls_ene1=[1,1,1,1]
    ls_ene2=[1,1,1,1]
    reloj=pygame.time.Clock()
    ventana=pygame.display.set_mode([ANCHO,ALTO],32) # Revisar esta instruccion con: ([ANCHO,ALTO],32,32)

    #carga de imagenes
    fondo_img=pygame.image.load('fondo3.png')
    tileset_img=pygame.image.load('set_rpg.png')
    personaje_img=pygame.image.load('jugador.png')
    enemigos_img=pygame.image.load('enemigos.png')
    flecha_derecha=pygame.image.load('flecha_derecha.png')
    flecha_izquierda=pygame.image.load('flecha_izquierda.png')
    flecha_arriba=pygame.image.load('flecha_arriba.png')
    flecha_abajo=pygame.image.load('flecha_abajo.png')

    #recorte de imagenes
    matriz_imagenes=recorte(tileset_img,63,32,0)
    matriz_jugador=recorte(personaje_img,16,8,0)
    matriz_enemigos_1=recorte(enemigos_img,4,3,0)
    matriz_enemigos_2=recorte(enemigos_img,4,3,4)

    #creacion de grupos
    fondos=pygame.sprite.Group()
    jugadores=pygame.sprite.Group()
    bloques=pygame.sprite.Group()
    bloques_agua=pygame.sprite.Group()
    bloques_lava=pygame.sprite.Group()
    ataque_espada=pygame.sprite.Group()
    ataque_flecha=pygame.sprite.Group()
    enemigos1=pygame.sprite.Group()
    enemigos2=pygame.sprite.Group()
    generadores=pygame.sprite.Group()

    #constructor del fondo
    f=Fondo(fondo_img,[-250,-200])
    fondos.add(f)

    #constructor del jugador
    j=Jugador(matriz_jugador)
    jugadores.add(j)
    #fin de contructor del jugador

    #constructor de enemigos
    '''
    ene=Enemigo(matriz_enemigos_1,[200,200],1)
    enemigos1.add(ene)

    ene2=Enemigo(matriz_enemigos_2,[200,130],2)
    enemigos2.add(ene2)
    '''

    #fin de constructor enemigo

    #constructor de generadores mapa parser

    parser_gene=ConfigParser.ConfigParser()
    parser_gene.read('parcer_generador.par')

    parser_gene_info_img=parser_gene.get('info','img')

    parser_gene_info_mapa=parser_gene.get('info','mapa')
    parser_gene_info_mapa=parser_gene_info_mapa.split('\n')

    pos_bloq_col=0
    pos_bloq_fil=0

    for i in parser_gene_info_mapa:
        for e in i:
            if parser_gene.get(e,'tipo') == 'vacio':
                pos_bloq_col+=1
            elif parser_gene.get(e,'tipo') == 'generador1':
                fl=int(parser_gene.get(e,'fil'))
                cl=int(parser_gene.get(e,"col"))
                gene=Generador(matriz_imagenes[fl][cl],[pos_bloq_col*32-250,pos_bloq_fil*32-200],1)
                generadores.add(gene)
                pos_bloq_col+=1
            elif parser_gene.get(e,'tipo') == 'generador2':
                fl=int(parser_gene.get(e,'fil'))
                cl=int(parser_gene.get(e,"col"))
                gene=Generador(matriz_imagenes[fl][cl],[pos_bloq_col*32-250,pos_bloq_fil*32-200],2)
                generadores.add(gene)
                pos_bloq_col+=1
        pos_bloq_col=0
        pos_bloq_fil+=1


    #construccion del mapa parser
    parser_bloque=ConfigParser.ConfigParser()
    parser_bloque.read('parcer_mapa.par')

    parser_bloque_info_img=parser_bloque.get('info','img')

    parser_bloque_info_mapa=parser_bloque.get('info','mapa')
    parser_bloque_info_mapa=parser_bloque_info_mapa.split('\n')

    pos_bloq_col=0
    pos_bloq_fil=0

    for i in parser_bloque_info_mapa:
        for e in i:
            if parser_bloque.get(e,'tipo') == 'vacio':
                pos_bloq_col+=1
            elif parser_bloque.get(e,'tipo') == 'transparente':
                fl=int(parser_bloque.get(e,'fil'))
                cl=int(parser_bloque.get(e,"col"))
                b=Bloque(matriz_imagenes[fl][cl],[pos_bloq_col*32-250,pos_bloq_fil*32-200])
                bloques.add(b)
                pos_bloq_col+=1
            elif parser_bloque.get(e,'tipo') == 'agua':
                fl=int(parser_bloque.get(e,'fil'))
                cl=int(parser_bloque.get(e,"col"))
                bf=Bloque(matriz_imagenes[fl][cl],[pos_bloq_col*32-250,pos_bloq_fil*32-200])
                bloques_agua.add(bf)
                pos_bloq_col+=1
            elif parser_bloque.get(e,'tipo') == 'lava':
                fl=int(parser_bloque.get(e,'fil'))
                cl=int(parser_bloque.get(e,"col"))
                bf=Bloque(matriz_imagenes[fl][cl],[pos_bloq_col*32-250,pos_bloq_fil*32-200])
                bloques_lava.add(bf)
                pos_bloq_col+=1
        pos_bloq_col=0
        pos_bloq_fil+=1
    #fin de la constriccion del mapa parser


    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j.velxp=5
                    j.velyp=0
                    j.velyn=0
                elif event.key == pygame.K_LEFT:
                    j.velxn=-5
                    j.velyp=0
                    j.velyn=0
                elif event.key == pygame.K_UP:
                    j.velyn=-5
                    j.velxp=0
                    j.velxn=0
                elif event.key == pygame.K_DOWN:
                    j.velyp=5
                    j.velxp=0
                    j.velxn=0
                elif event.key == pygame.K_c:
                    j.espada=1
                elif event.key == pygame.K_x:
                    j.arco=1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    j.velxp=0
                    f.velx=0
                    for b in bloques:
                        b.velx=0
                    for b in bloques_agua:
                        b.velx=0
                    for b in bloques_lava:
                        b.velx=0
                    for b in enemigos1:
                        b.velx=0
                    for b in enemigos2:
                        b.velx=0
                    for b in ataque_flecha:
                        b.velx=0
                    for b in generadores:
                        b.velx=0
                elif event.key == pygame.K_LEFT:
                    j.velxn=0
                    f.velx=0
                    for b in bloques:
                        b.velx=0
                    for b in bloques_agua:
                        b.velx=0
                    for b in bloques_lava:
                        b.velx=0
                    for b in enemigos1:
                        b.velx=0
                    for b in enemigos2:
                        b.velx=0
                    for b in ataque_flecha:
                        b.velx=0
                    for b in generadores:
                        b.velx=0
                elif event.key == pygame.K_UP:
                    j.velyn=0
                    f.vely=0
                    for b in bloques:
                        b.vely=0
                    for b in bloques_agua:
                        b.vely=0
                    for b in bloques_lava:
                        b.vely=0
                    for b in enemigos1:
                        b.vely=0
                    for b in enemigos2:
                        b.vely=0
                    for b in ataque_flecha:
                        b.vely=0
                    for b in generadores:
                        b.vely=0
                elif event.key == pygame.K_DOWN:
                    j.velyp=0
                    f.vely=0
                    for b in bloques:
                        b.vely=0
                    for b in bloques_agua:
                        b.vely=0
                    for b in bloques_lava:
                        b.vely=0
                    for b in enemigos1:
                        b.vely=0
                    for b in enemigos2:
                        b.vely=0
                    for b in ataque_flecha:
                        b.vely=0
                    for b in generadores:
                        b.vely=0


        #if cont_enem<1:
        #    cont_enem+=1
        for a in generadores:
            #if 0<a.cantidad_enemigos:
            #    a.cantidad_enemigos-=1
            if a.integridad>1:
                if a.tipo==1:
                    if ls_ene1[0]==1:
                        ene10=Enemigo(matriz_enemigos_1,[416+f.rect.x,704+f.rect.y],1,0)
                        enemigos1.add(ene10)
                    if ls_ene1[1]==1:
                        ene11=Enemigo(matriz_enemigos_1,[544+f.rect.x,704+f.rect.y],1,1)
                        enemigos1.add(ene11)
                    if ls_ene1[2]==1:
                        ene12=Enemigo(matriz_enemigos_1,[416+f.rect.x,800+f.rect.y],1,2)
                        enemigos1.add(ene12)
                    if ls_ene1[3]==1:
                        ene13=Enemigo(matriz_enemigos_1,[544+f.rect.x,800+f.rect.y],1,3)
                        enemigos1.add(ene13)

                    if ls_ene1[0]>0:
                        ls_ene1[0]-=1
                    if ls_ene1[1]>0:
                        ls_ene1[1]-=1
                    if ls_ene1[2]>0:
                        ls_ene1[2]-=1
                    if ls_ene1[3]>0:
                        ls_ene1[3]-=1
                elif a.tipo==2:
                    if ls_ene2[0]==1:
                        ene10=Enemigo(matriz_enemigos_2,[928+f.rect.x,768+f.rect.y],2,0)
                        enemigos1.add(ene10)
                    if ls_ene2[1]==1:
                        ene11=Enemigo(matriz_enemigos_2,[1056+f.rect.x,832+f.rect.y],2,1)
                        enemigos1.add(ene11)
                    if ls_ene2[2]==1:
                        ene12=Enemigo(matriz_enemigos_2,[928+f.rect.x,832+f.rect.y],2,2)
                        enemigos1.add(ene12)
                    if ls_ene2[3]==1:
                        ene13=Enemigo(matriz_enemigos_2,[1088+f.rect.x,928+f.rect.y],2,3)
                        enemigos1.add(ene13)

                    if ls_ene2[0]>0:
                        ls_ene2[0]-=1
                    if ls_ene2[1]>0:
                        ls_ene2[1]-=1
                    if ls_ene2[2]>0:
                        ls_ene2[2]-=1
                    if ls_ene2[3]>0:
                        ls_ene2[3]-=1

        #Actualizacion de objetos
        jugadores.update()
        fondos.update()
        bloques.update()
        bloques_agua.update()
        bloques_lava.update()
        ataque_flecha.update()
        generadores.update()
        enemigos1.update()
        enemigos2.update()

        #Actualizacon de imagenes
        ventana.fill(NEGRO)
        #ventana.blit(fondo_img,[0,0])
        fondos.draw(ventana)
        bloques.draw(ventana)
        bloques_agua.draw(ventana)
        bloques_lava.draw(ventana)
        ataque_espada.draw(ventana)
        ataque_flecha.draw(ventana)
        generadores.draw(ventana)
        enemigos1.draw(ventana)
        enemigos2.draw(ventana)
        jugadores.draw(ventana)
        pygame.draw.line(ventana, BLANCO, [150,0], [150,ALTO])
        pygame.draw.line(ventana, BLANCO, [ANCHO-168,0], [ANCHO-168,ALTO])
        pygame.draw.line(ventana, BLANCO, [0,70], [ANCHO,70])
        pygame.draw.line(ventana, BLANCO, [0,ALTO-78], [ANCHO,ALTO-78])
        pygame.display.flip()
        reloj.tick(15)
