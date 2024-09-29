import play
import pygame
from random import randint, choice

a = play.new_image(image="345526.png", x=0, y=0, size=200)

point_box = play.new_box(color='white', border_color="black", border_width=3 ,x=-282, y=275, width=235, height=40)
point_text = play.new_text(words="your points:", color="blue" ,x=-300, y=275, font=None, font_size=40 )
point = play.new_text(words="10" , color="purple", x=-200, y=272, font=None, font_size=40)
n = 10

buttom = play.new_image(image="yess.png", x=0, y=-180, size= 50)

# პროექტისთვის საჭირო ხმების ჩატვირთვა
but_sou = pygame.mixer.Sound('but_sou.ogg')
win_sou = pygame.mixer.Sound("dzlivss.ogg")
lose_sou = pygame.mixer.Sound("lose.ogg")
during_sou = pygame.mixer.Sound("during the game.ogg")

place1 = play.new_box(color="light green", x=-240,y=0,
width=110, height=200,border_width=5, border_color="green")


place2 = play.new_box(color="light green", x=-80,y=0,
width=110, height=200, border_width=5, border_color="green")


place3 = play.new_box(color="light green", x=80,y=0,
width=110, height=200,border_width=5, border_color="green")


place4 = play.new_box(color="light green", x=240,y=0,
width=110, height=200,border_width=5, border_color="green")

result = play.new_text(words="you win 10 point!!!", x=0,y=180, font=None, font_size=40,color="green")


#შემთხვევითი სურათები 
img1 = play.new_image(image='p1.png', x=-240, size=26)
img2 =play.new_image(image='p2.png', x=-80, size=40)
img3 =play.new_image(image='p3.png', x=80, size=45)
img4 =play.new_image(image='p4.png', x=240, size=20)

img5 = play.new_image(image='p1.png', x=-240, size=26)
img6 =play.new_image(image='p2.png', x=-80, size=40)
img7 =play.new_image(image='p3.png', x=80, size=45)
img8 =play.new_image(image='p4.png', x=240, size=20)

img9 = play.new_image(image='p1.png', x=-240, size=26)
img10 =play.new_image(image='p2.png', x=-80, size=40)
img11 =play.new_image(image='p3.png', x=80, size=45)
img12 =play.new_image(image='p4.png', x=240, size=20)

img13 = play.new_image(image='p1.png', x=-240, size=26)
img14 =play.new_image(image='p2.png', x=-80, size=40)
img15 =play.new_image(image='p3.png', x=80, size=45)
img16 =play.new_image(image='p4.png', x=240, size=20)


@play.when_program_starts
def start():
    
    img1.hide()
    img2.hide()
    img3.hide()
    img4.hide()
    img5.hide()
    img6.hide()
    img7.hide()
    img8.hide()
    img9.hide()
    img10.hide()
    img11.hide()
    img12.hide()
    img13.hide()
    img14.hide()
    img15.hide()
    img16.hide()

    result.hide()


@play.repeat_forever
def do():
    global n
    during_sou.play()
    if n <= 0:
        during_sou.stop()
        place1.hide()
        place2.hide()
        place3.hide()
        place4.hide()
        lose_sou.play()
        you_lose = play.new_image(image="jehgjj.png", size = 300 )


   
    if n >= 50:
        during_sou.stop()
        place1.hide()
        place2.hide()
        place3.hide()
        place4.hide()
        win_sou.play()
        you_win = play.new_image(image="you win.png", size = 350)



@buttom.when_clicked
async def click():
    global point ,n
    but_sou.play()

    i1 = choice([img1, img2, img3, img4])
    i2 = choice([img5, img6, img7, img8])
    i3 = choice([img9, img10, img11, img12])
    i4 = choice([img13, img14, img15, img16])

    i1.x = -240
    i2.x = -80
    i3.x = 80
    i4.x = 240

    i1.show()
    i2.show()
    i3.show()
    i4.show()

    n_1_3 = [i1.image, i2.image, i3.image, i4.image].count('p1.png')
    n_2_3 = [i1.image, i2.image, i3.image, i4.image].count('p2.png')
    n_3_3 = [i1.image, i2.image, i3.image, i4.image].count('p3.png')
    n_4_3 = [i1.image, i2.image, i3.image, i4.image].count('p4.png')

    n_1_2 = [i1.image, i2.image, i3.image, i4.image].count('p1.png')
    n_2_2 = [i1.image, i2.image, i3.image, i4.image].count('p2.png')
    n_3_2 = [i1.image, i2.image, i3.image, i4.image].count('p3.png')
    n_4_2 = [i1.image, i2.image, i3.image, i4.image].count('p4.png')

    if i1.image == i2.image == i3.image == i4.image:
        n = n + 5
        point.words = str(n)
    elif n_1_3 == 3 or n_2_3 == 3 or n_3_3 == 3 or n_4_3 == 3:
        n = n + 3
        point.words = str(n)
    elif n_1_3 == 2 or n_2_3 == 2 or n_3_3 == 2 or n_4_3 == 2:
        n = n + 1
        point.words = str(n)
    else:
        n = n - 50
        point.words = str(n)

    await play.timer(seconds = 2.0)

    i1.hide()
    i2.hide()
    i3.hide()
    i4.hide()

play.start_program()