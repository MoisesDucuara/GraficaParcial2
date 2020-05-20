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
        self.lim_accion=[0,0,0,0,5,5,6,7,2,2,2,2]
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

        #Manejo de sprites jugador
        if self.espada>=1 and self.espada<4:
            if self.accion==0 or self.accion==4:
                self.accion=8
                if self.espada==1:
                    esp=Bloque(personaje_img,[self.rect.right,self.rect.top])
                    esp.image=pygame.Surface([16,32])
                    esp.image.fill(AZUL)
                    ataque_espada.add(esp)
            elif self.accion==1 or self.accion==5:
                self.accion=9
            self.espada+=1
        elif self.espada==4:
            self.espada=0
            if self.accion==8:
                self.accion=0
                ataque_espada.remove(ataque_espada)
            if self.accion==9:
                self.accion=1
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
    def __init__(self,matriz_img,pos,tipo):
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
        self.cont_mov=0

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
                    if j.rect.x < self.rect.x:
                        self.velx_pro=-2
                        self.vely_pro=0
                    elif j.rect.x > self.rect.x:
                        self.velx_pro=2
                        self.vely_pro=0
                    if j.rect.y < self.rect.y:
                        self.vely_pro=-2
                        self.velx_pro=0
                    elif j.rect.y > self.rect.y:
                        self.vely_pro=2
                        self.velx_pro=0
            else:
                self.velx_pro=0
                self.vely_pro=0


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
    personaje_img=pygame.image.load('jugador.png')
    enemigos_img=pygame.image.load('enemigos.png')

    #recorte de imagenes
    matriz_imagenes=recorte(tileset_img,63,32,0)
    matriz_jugador=recorte(personaje_img,12,8,0)
    matriz_enemigos_1=recorte(enemigos_img,4,3,0)
    matriz_enemigos_2=recorte(enemigos_img,4,3,4)

    #creacion de grupos
    fondos=pygame.sprite.Group()
    jugadores=pygame.sprite.Group()
    bloques=pygame.sprite.Group()
    bloques_agua=pygame.sprite.Group()
    bloques_lava=pygame.sprite.Group()
    ataque_espada=pygame.sprite.Group()
    enemigos1=pygame.sprite.Group()
    enemigos2=pygame.sprite.Group()

    #constructor del fondo
    f=Fondo(fondo_img,[-250,-200])
    fondos.add(f)

    #constructor del jugador
    j=Jugador(matriz_jugador)
    jugadores.add(j)
    #fin de contructor del jugador

    #constructor de enemigos
    ene=Enemigo(matriz_enemigos_1,[200,200],1)
    enemigos1.add(ene)

    ene2=Enemigo(matriz_enemigos_2,[200,130],2)
    enemigos2.add(ene2)
    #fin de constructor enemigo


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


        #Actualizacion de objetos
        jugadores.update()
        fondos.update()
        bloques.update()
        bloques_agua.update()
        bloques_lava.update()
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
        enemigos1.draw(ventana)
        enemigos2.draw(ventana)
        jugadores.draw(ventana)
        pygame.draw.line(ventana, BLANCO, [150,0], [150,ALTO])
        pygame.draw.line(ventana, BLANCO, [ANCHO-168,0], [ANCHO-168,ALTO])
        pygame.draw.line(ventana, BLANCO, [0,70], [ANCHO,70])
        pygame.draw.line(ventana, BLANCO, [0,ALTO-78], [ANCHO,ALTO-78])
        pygame.display.flip()
        reloj.tick(15)
