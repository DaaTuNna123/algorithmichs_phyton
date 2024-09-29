from pygame import *
from random import randint, choice

font.init()
font1 = font.Font(None, 80)
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))

font2 = font.Font(None, 36)


mixer.init()
mixer.music.load('msc.mp3')
mixer.music.play()
mixer.music.set_volume(0.5)
fire_sound = mixer.Sound('gun_laser.ogg')

img_back = "air.bck.png"
img_bullet = "b.png" 
img_player = "player.png" 
img_enemy1 = "enemy.png" 
img_enemy2 = "second_enemy.png"
img_enemy3 = "third_enemy.png"

score = 0 
goal = 30 
lost = 0
max_lost = 3 

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

       
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
            window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 500:
            self.rect.x += self.speed


    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx + 15, self.rect.top + 45, 50, 20, 10)
        bullets.add(bullet)


class Enemy(GameSprite):
    
    def update(self):
        self.rect.x -= self.speed
        

class Bullet(GameSprite):
    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.kill()


win_width = 750
win_height = 550
display.set_caption("AIR COMBAT")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

ship = Player(img_player, 5, win_height - 100, 100, 100, 15)
 


monsters = sprite.Group()
for i in range(1, 6):
    r = choice([img_enemy1, img_enemy2, img_enemy3])
    monster = Enemy(r, win_width - 20, randint(100, win_height - 50), 120, 70, randint(6, 10))
    monsters.add(monster)
 

bullets = sprite.Group()

finish = False
run = True 
while run:
   
    for e in event.get():
        if e.type == QUIT:
            run = False

        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                ship.fire()
 
 
    if not finish:
        
        window.blit(background,(0,0))

       
        text = font2.render("Score: " + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))

        text_lose = font2.render("Missed: " + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))

        
        ship.update()
        monsters.update()
        bullets.update()
       
        ship.reset()
        monsters.draw(window)
        bullets.draw(window)
        
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
           
            score = score + 1
            r = choice([img_enemy1, img_enemy2, img_enemy3])
            monster = Enemy(r, win_width - 20, randint(100, win_height - 50), 120, 70, randint(6, 10))
            monsters.add(monster)
        
        for i in monsters:
            if i.rect.x < 0:
                i.rect.y = randint(180, win_width - 80)
                i.rect.x = 600
                lost = lost + 1
                print(lost)


       
        if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
            finish = True 
            window.blit(lose, (200, 200))

        
        if score >= goal:
            finish = True
            window.blit(win, (200, 200))

        display.update()
    
    time.delay(50)
