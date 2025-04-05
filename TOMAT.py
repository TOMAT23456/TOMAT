import pygame
print("xcvb")
WIDTH = 1000
HEIGHT = 500
FPS = 30

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("yu")
clock = pygame.time.Clock()

img_fon = pygame.image.load("i3.png").convert_alpha()
img_fon = pygame.transform.scale(img_fon, (WIDTH, HEIGHT))
img_chocopay = pygame.image.load("chocopay.png").convert_alpha()
img_work = pygame.image.load("work.png").convert_alpha()


class Player(pygame.sprite.Sprite):
    def _init_(self, image, x, y):
        super()._init_()
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.x_change = 0
        self.y_change = 0

    def update(self):
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        if self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = WIDTH
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0
        if self.rect.bottom < 0:
            self.rect.top = HEIGHT


chocopay = Player(img_chocopay, 100, 100)
work = Player(img_work, 100, 100)

all_sprites = pygame.sprite.Group()
all_sprites.add(chocopay, work)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                work.x_change = -5
            if event.key == pygame.K_RIGHT:
                work.x_change = 5
            if event.key == pygame.K_UP:
                work.y_change = -5
            if event.key == pygame.K_DOWN:
                work.y_change = 5



        elif event.type == pygame.KEYUP:
             if event.key in (pygame.K_RIGHT , pygame.K_LEFT):
                 work.x_change = 0
             if event.key in (pygame.K_UP , pygame.K_DOWN):
                 work.y_change = 0

    screen.blit(img_fon, (0, 0))

    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()

pygame.quit()