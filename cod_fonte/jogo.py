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
        self.active = True

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

        #texto
        self.font = pygame.font.Font('./img/fonte/BD_Cartoon_Shout.ttf', 30)
        self.ecore = 0

        #menu
        self.menu_surf = pygame.image.load('./img/menu/menu.png').convert_alpha()
        self.menu_rect = self.menu_surf.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
    def collisions(self): 
        if pygame.sprite.spritecollide(self.plane,self.collision_sprites,False, pygame.sprite.collide_mask)\
            or self.plane.rect.top <= 0 :
            for sprite in self.collision_sprites.sprites():
                if sprite.sprite_type == 'obstacle' :  
                    sprite.kill()
            self.active = False
            self.plane.kill()

    def diplay_score(self): 
         if self. active:
             self.score = pygame.time.get_ticks() // 1000
             y = WINDOW_HEIGHT / 10
         else:
            y = WINDOW_HEIGHT / 2 + (self.menu_rect.height / 1.5)

         score_surf = self.font.render(str(self.score),True,'blue')
         score_rect = score_surf.get_rect(midtop = (WINDOW_WIDTH / 2, y))
         self.display_surface.blit(score_surf, score_rect)

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

                    if self.active:
                        self.plane.jump()
                    else:
                        self.plane = Plane(self.all_sprites, self.scale_factor / 1.7)
                        self.active = True          
                if event.type == self.obstacle_timer and self.active:
                     Obstacle([self.all_sprites, self.collision_sprites], self.scale_factor * 1.1)

            #Lógica
            self.display_surface.fill('black')
            self.all_sprites.update(dt)
            self.all_sprites.draw(self.display_surface)
            self.diplay_score()

            if self.active: 
                self.collisions()
            else:
                self.display_surface.blit(self.menu_surf, self.menu_rect)

            pygame.display.update()
            self.clock.tick(FRAMERATE)
if __name__=='__main__':
    game=Game()
    game.run()         