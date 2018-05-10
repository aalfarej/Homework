import pygame
import sys
import os # new code below



'''
Setup
'''
worldx = 1024
worldy = 688
fps   = 40  # frame rate
ani   = 4   # animation cycles
BLUE  = (25,25,200)
BLACK = (23,23,23 )
WHITE = (254,254,254)

clock = pygame.time.Clock()
pygame.init()


world       = pygame.display.set_mode([worldx,worldy])
backdrop    = pygame.image.load(os.path.join('images','stage.png')).convert()
backdropbox = world.get_rect()

class Player(pygame.sprite.Sprite):
    '''
    Spawn a player
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0  # move along X
        self.movey = 0  # move along Y
        self.frame = 0  # count frames
        self.images = []
        img = pygame.image.load(os.path.join('images','pac1.png')).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect  = self.image.get_rect()

    def control(self, x, y):
        '''
        control player movement
        '''
        self.movex += x
        self.movey += y

    def update(self):
        '''
        Update sprite position
        '''
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        # moving left
        # if self.movex < 0:
        #     self.frame += 1
        #     if self.frame > 3 * ani:
        #         self.frame = 0
        #     self.image = self.images[self.frame // ani]
        #
        # # moving right
        # if self.movex > 0:
        #     self.frame += 1
        #     if self.frame > 3 * ani:
        #         self.frame = 0
        #     self.image = self.images[(self.frame // ani) + 4]

player = Player()   # spawn player
player.rect.x = 0   # go to x
player.rect.y = 0   # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10  # how many pixels to move

main = True
'''
Main loop
'''
while main == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left')
                player.control(-steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right')
                player.control(steps, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('up')
                player.control(0,-steps)

            if event.key == pygame.K_DOWN or event.key == ord('x'):
                print('down')
                player.control(0,steps)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left stop')
                player.control(steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right stop')
                player.control(-steps, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('up stop')
                player.control(0, steps)
            if event.key == pygame.K_DOWN or event.key == ord('x'):
                print('down stop')
                player.control(0, -steps)
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

    world.blit(backdrop, backdropbox)
    player.update()  # update player position
    player_list.draw(world)  # draw player
    pygame.display.flip()
    clock.tick(fps)


# new code below

# player = Player()   # spawn player
# player.rect.x = 0   # go to x
# player.rect.y = 0   # go to y
# player_list = pygame.sprite.Group()
# player_list.add(player)