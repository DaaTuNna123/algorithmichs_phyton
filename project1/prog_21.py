import play
from random import randint

forest = play.new_image(image="1.png", x=0, y=0, size = 200 )

a = play.new_image(image="3.png", x=-300, y=-150, size = 20)


scor_text = play.new_text(words="score: ", x=-300, y=250)
score_point = play.new_text(words="0", x=-240, y=250)


apples=[]

@play.when_program_starts
def do():
    for i in range(20):
        xm = randint(-290,290)
        ym = randint(-200,200)
        apples.append(play.new_image(image="2.png", x=xm, y=ym, size=15))



@play.repeat_forever
def do():
    if play.key_is_pressed("w"):
        a.y = a.y + 5
    if play.key_is_pressed("s"):
        a.y = a.y - 5
    if play.key_is_pressed("d"):
        a.x = a.x + 5
    if play.key_is_pressed("a"):
        a.x = a.x - 5
        
    

    

    for apple in apples:
        if a.is_touching(apple):
            apple.hide()
            apples.remove(apple)


    score_point.words = str(20 - len(apples))
    
    if score_point.words == str(20):
        play.new_image(image="12345.png", x=0, y=0, size=350)
        a.hide()

play.start_program()