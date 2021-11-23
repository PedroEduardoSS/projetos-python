import pygame, sys

class Block(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(path), (75, 75)).convert_alpha()
        self.rect = self.image.get_rect(center = (x_pos, y_pos))

class Player1(Block):
    def __init__(self, path, x_pos, y_pos, speed, bullet_group, enemy_bullet):
        super().__init__(path, x_pos, y_pos)
        self.health = 30
        self.speed = speed
        self.bullet_group = bullet_group
        self.enemy_bullet = enemy_bullet

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        elif keys[pygame.K_s]:
            self.rect.y += self.speed
        elif keys[pygame.K_a]:
            self.rect.x -= self.speed
        elif keys[pygame.K_d]:
            self.rect.x += self.speed
        elif keys[pygame.K_LCTRL] and len(self.bullet_group) <= 5:
            pygame.mixer.Sound.play(shot_sound)
            self.bullet_group.add(self.create_bullet())

    def constrain(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= WIDTH / 2:
            self.rect.right = WIDTH / 2

    def create_bullet(self):
        return BulletBlue('images/bullet-blue.png', self.rect.centerx, self.rect.centery)

    def collision(self):
        for heat in range(self.health):
            if pygame.sprite.spritecollide(player1, bullet_red, True):
                self.health -= 1

    def show_score(self):
        self.score = font.render(f"Health: {self.health}", True, (0, 204, 0))
        self.score_rect = self.score.get_rect(topleft = (3, 3))
        screen.blit(self.score, self.score_rect)

    def show_winner(self):
        self.winner = font.render("Red Wins", True, (200, 0, 0))
        self.winner_rect = self.winner.get_rect(center = (WIDTH / 2, HEIGHT / 2))

        if self.health == 0:
            screen.fill("white")
            screen.blit(self.winner, self.winner_rect)

    def update(self):
        self.input()
        self.create_bullet()
        self.collision()
        self.show_score()
        self.show_winner()
        self.constrain()

class Player2(Block):
    def __init__(self, path, x_pos, y_pos, speed, bullet_group, enemy_bullet):
        super().__init__(path, x_pos, y_pos)
        self.health = 30
        self.speed = speed
        self.bullet_group = bullet_group
        self.enemy_bullet = enemy_bullet

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        elif keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif keys[pygame.K_RCTRL] and len(self.bullet_group) <= 5:
            pygame.mixer.Sound.play(shot_sound)
            self.bullet_group.add(self.create_bullet())

    def constrain(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.left <= WIDTH / 2:
            self.rect.left = WIDTH / 2
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH

    def create_bullet(self):
        return BulletRed('images/bullet-red.png', self.rect.centerx, self.rect.centery)

    def collision(self):
        for heat in range(self.health):
            if pygame.sprite.spritecollide(player2, bullet_blue, True):
                self.health -= 1

    def show_score(self):
        self.score = font.render(f"Health: {self.health}", True, (0, 204, 0))
        self.score_rect = self.score.get_rect(topright = (WIDTH - 3, 3))
        screen.blit(self.score, self.score_rect)

    def show_winner(self):
        self.winner = font.render("Blue Wins", True, (0, 0, 200))
        self.winner_rect = self.winner.get_rect(center = (WIDTH / 2, HEIGHT / 2))

        if self.health == 0:
            screen.fill("white")
            screen.blit(self.winner, self.winner_rect)

    def update(self):
        self.input()
        self.create_bullet()
        self.collision()
        self.show_score()
        self.show_winner()
        self.constrain()

class BulletBlue(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(path), (15, 10))
        self.rect = self.image.get_rect(center = (x_pos, y_pos))

    def update(self):
        self.rect.x += 8

        if self.rect.x >= WIDTH:
            self.kill()

class BulletRed(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(path), (15, 10))
        self.rect = self.image.get_rect(center = (x_pos, y_pos))

    def update(self):
        self.rect.x -= 8

        if self.rect.x <= 0:
            self.kill()

pygame.mixer.pre_init(44100, -16, 2,64)
pygame.init()
clock = pygame.time.Clock()

WIDTH = 1280
HEIGHT = 720

font = pygame.font.Font('font/Pixeltype.ttf', 50)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Spaceship-War')
game_active = True
bg_surf = pygame.image.load('images/BG-SWAR.jpg').convert()

bullet_blue = pygame.sprite.Group()
bullet_red = pygame.sprite.Group()

player1 = Player1('images/left.png', WIDTH/2 - 320, HEIGHT/2, 7, bullet_blue, bullet_red)
player2 = Player2('images/right.png', WIDTH/2 + 320, HEIGHT/2, 7, bullet_red, bullet_blue)
ships_group = pygame.sprite.Group()
ships_group.add(player1, player2)

shot_sound = pygame.mixer.Sound('sounds/shot.mp3')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    if game_active:
        screen.blit(bg_surf, (0, 0))
        ships_group.draw(screen)
        ships_group.update()
        bullet_blue.draw(screen)
        bullet_blue.update()
        bullet_red.draw(screen)
        bullet_red.update()
        
        pygame.draw.line(screen, 'white', (WIDTH / 2, 0), (WIDTH / 2, HEIGHT), 7)

    pygame.display.update()
    pygame.display.flip()
    clock.tick(30)