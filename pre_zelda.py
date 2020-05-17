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

def recorte(img,fil,col):
    m=[]
    for i in range(fil):
        fila=[]
        for j in range(col):
            cuadro=img.subsurface(j*32,i*32,32,32)
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
    def __init__(self,pos=[190,150]):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([32,48])
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

        self.rect.y+=self.velyp+self.velyn

        ls_col=pygame.sprite.spritecollide(self,bloques,False)
        for b in ls_col:
            if (self.rect.bottom > b.rect.top) and (self.rect.bottom <= b.rect.top+5):
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
            elif (self.rect.top < b.rect.bottom) and (self.rect.top >= b.rect.bottom-5):
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

        ls_agua=pygame.sprite.spritecollide(self,bloques_agua,False)
        for b in ls_agua:
            if (self.rect.bottom > b.rect.top) and (self.rect.bottom <= b.rect.top+5):
                print "Agua 1"
            elif (self.rect.top < b.rect.bottom) and (self.rect.top >= b.rect.bottom-5):
                print "Agua 2"

        ls_lava=pygame.sprite.spritecollide(self,bloques_lava,False)
        for b in ls_lava:
            if (self.rect.bottom > b.rect.top) and (self.rect.bottom <= b.rect.top+5):
                print "Lava 1"
            elif (self.rect.top < b.rect.bottom) and (self.rect.top >= b.rect.bottom-5):
                print "Lava 2"

        self.rect.x+=self.velxp+self.velxn

        ls_col=pygame.sprite.spritecollide(self,bloques,False)
        for b in ls_col:
            if (self.rect.right > b.rect.left) and (self.rect.right <= b.rect.left+5):
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
            elif (self.rect.left < b.rect.right) and (self.rect.left >= b.rect.right-5):
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

        ls_agua=pygame.sprite.spritecollide(self,bloques_agua,False)
        for b in ls_agua:
            if (self.rect.right > b.rect.left) and (self.rect.right <= b.rect.left+5):
                print "Agua 3"
            elif (self.rect.left < b.rect.right) and (self.rect.left >= b.rect.right-5):
                print "Agua 4"

        ls_lava=pygame.sprite.spritecollide(self,bloques_lava,False)
        for b in ls_lava:
            if (self.rect.right > b.rect.left) and (self.rect.right <= b.rect.left+5):
                print "Lava 3"
            elif (self.rect.left < b.rect.right) and (self.rect.left >= b.rect.right-5):
                print "Lava 4"

        if self.rect.y > (ALTO-110):
            #print "Caja 1"
            self.rect.y = ALTO-110
            f.vely=-5
            for b in bloques:
                b.vely=-5
            for bf in bloques_agua:
                bf.vely=-5
            for bf in bloques_lava:
                bf.vely=-5
        elif self.rect.y < 70:
            #print "Caja 2"
            self.rect.y = 70
            f.vely=5
            for b in bloques:
                b.vely=5
            for bf in bloques_agua:
                bf.vely=5
            for bf in bloques_lava:
                bf.vely=5

        if self.rect.x > (ANCHO-200):
            #print "Caja 3"
            self.rect.x = ANCHO-200
            self.velxp=0
            f.velx=-5
            for b in bloques:
                b.velx=-5
            for bf in bloques_agua:
                bf.velx=-5
            for bf in bloques_lava:
                bf.velx=-5
        elif self.rect.x < 150:
            #print "Caja 4"
            self.rect.x = 150
            f.velx=5
            for b in bloques:
                b.velx=5
            for bf in bloques_agua:
                bf.velx=5
            for bf in bloques_lava:
                bf.velx=5

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


if __name__ == '__main__':
    pygame.init()
    #Definicion de variables
    reloj=pygame.time.Clock()
    ventana=pygame.display.set_mode([ANCHO,ALTO],32) # Revisar esta instruccion con: ([ANCHO,ALTO],32,32)

    #carga de imagenes
    fondo_img=pygame.image.load('fondo3.png')
    tileset_img=pygame.image.load('set_rpg.png')

    #creacion de grupos
    fondos=pygame.sprite.Group()
    jugadores=pygame.sprite.Group()
    bloques=pygame.sprite.Group()
    bloques_agua=pygame.sprite.Group()
    bloques_lava=pygame.sprite.Group()

    #constructor del fondo
    f=Fondo(fondo_img,[-250,-200])
    fondos.add(f)

    #constructor del jugador
    j=Jugador()
    jugadores.add(j)

    '''
    b=Bloque([300,300],200,120)
    bloques.add(b)
    '''
    #fin de contructor del jugador

    matriz_imagenes=recorte(tileset_img,63,32)
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
                elif event.key == pygame.K_LEFT:
                    j.velxn=0
                    f.velx=0
                    for b in bloques:
                        b.velx=0
                    for b in bloques_agua:
                        b.velx=0
                    for b in bloques_lava:
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
                elif event.key == pygame.K_DOWN:
                    j.velyp=0
                    f.vely=0
                    for b in bloques:
                        b.vely=0
                    for b in bloques_agua:
                        b.vely=0
                    for b in bloques_lava:
                        b.vely=0


        #Actualizacion de objetos
        jugadores.update()
        fondos.update()
        bloques.update()
        bloques_agua.update()
        bloques_lava.update()

        #Actualizacon de imagenes
        ventana.fill(NEGRO)
        #ventana.blit(fondo_img,[0,0])
        fondos.draw(ventana)
        jugadores.draw(ventana)
        #bloques.draw(ventana)
        #bloques_agua.draw(ventana)
        #bloques_lava.draw(ventana)
        pygame.draw.line(ventana, BLANCO, [150,0], [150,ALTO])
        pygame.draw.line(ventana, BLANCO, [ANCHO-168,0], [ANCHO-168,ALTO])
        pygame.draw.line(ventana, BLANCO, [0,70], [ANCHO,70])
        pygame.draw.line(ventana, BLANCO, [0,ALTO-78], [ANCHO,ALTO-78])
        pygame.display.flip()
        reloj.tick(60)
