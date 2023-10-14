from pygame import *
from random import randint


speed = 10
#create game window
window = display.set_mode((700, 500))
display.set_caption("catch")
#set scene background
background = transform.scale(image.load("background.png"),(700,500))

#creat 2 sprites and place them on the scene
sprite1 = transform.scale(image.load('sprite1.png'),(100, 100))
sprite2 = transform.scale(image.load('sprite2.png'),(100, 100))
x1 = randint(0, 300)
y1 = randint(250,350)
x2 = randint(0, 300)
y2 = randint(250,350)

#handle "click on the "Close the window"" event 

click = time.Clock()



game = True
while game:
    window.blit(background, (0, 0))


    for e in event.get():
        if e.type == QUIT:
            game = False


    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))
    

    keys_pressed = key.get_pressed()


    if keys_pressed[K_LEFT] and x1 > 5:
         x1 -= speed
    if keys_pressed[K_RIGHT] and x1 < 595:
        x1 += speed
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= speed
    if keys_pressed[K_DOWN] and y1 < 395:
        y1 += speed

    if keys_pressed[K_a] and x2 > 5:
         x2 -= speed
    if keys_pressed[K_d] and x2 < 595:
        x2 += speed
    if keys_pressed[K_w] and y2 > 5:
        y2 -= speed
    if keys_pressed[K_s] and y2 < 395:
        y2 += speed


    display.update()
    click.tick(60)
