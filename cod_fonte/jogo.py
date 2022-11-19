#Importando Bibliotecas
import pygame, sys, time
from sprites import BG, Ground, Plane, Obstacle

#Definindo Tamanho da Janela
WINDOW_WIDTH=480
WINDOW_HEIGHT=800
FRAMERATE=120

class Game:
    def __init__(self):

        #Início
        pygame.init()
        self.display_surface=pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Flappy Bird')
        self.clock=pygame.time.Clock()

        #Sprites
        self.all_sprites=pygame.sprite.Group()
        self.collision_sprites=pygame.sprite.Group()

        #Escala
        bg_height=pygame.image.load('./img/ambiente/background.png').get_height()
        self.scale_factor=WINDOW_HEIGHT/bg_height

        #Ajustes Sprite
        BG(self.all_sprites, self.scale_factor)
        Ground([self.all_sprites, self.collision_sprites], self.scale_factor)
        self.plane=Plane(self.all_sprites, self.scale_factor/1.7)

        #tempo
        self.obstacle_timer = pygame.USEREVENT + 1 
        pygame.time.set_timer(self.obstacle_timer, 1400)

    def collisions(self): 
        if pygame.sprite.spritecollide(self.plane,self.collision_sprites,False, pygame.sprite.collide_mask)\
            or self.plane.rect.top <= 0 :
            pygame.quit()
            sys.exit()

    def run(self):
        last_time=time.time()
        while True:
            #Tempo
            dt=time.time() - last_time
            last_time=time.time()

            #Loop
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key==pygame.K_SPACE:
                        self.plane.jump()          
                if event.type == self.obstacle_timer:
                     Obstacle([self.all_sprites, self.collision_sprites], self.scale_factor * 1.1)

            #Lógica
            self.display_surface.fill('black')
            self.all_sprites.update(dt)
            self.collisions()
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()
            self.clock.tick(FRAMERATE)
if __name__=='__main__':
    game=Game()
    game.run()         