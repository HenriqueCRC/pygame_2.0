#Importando Bibliotecas
import pygame, sys, time

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

            #Lógica
            pygame.display.update()
            self.clock.tick(FRAMERATE)
if __name__=='__main__':
    game=Game()
    game.run()
            
            