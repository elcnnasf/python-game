import pgzrun
from random import randint


WIDTH = 900
HEIGHT = 500
score = 0


fox = Actor("fox.png")
fox.pos = 100,100 

coin = Actor("coin1.png")
coin.pos = 200, 200

back = Actor("background.png")
back.pos = 450, 250



game_over = False
def draw():
    back.draw()
    fox.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))
    if game_over:
        screen.fill("Green")
        screen.draw.text("Final Score: " + str(score), topleft=(300, 200), fontsize=60)

def place_coin():
     coin.x = randint(20, (WIDTH - 20))
     coin.y = randint(20, (HEIGHT - 20))
def time_up():
    global game_over
    game_over = True
def update():
     global score
     if keyboard.left:
        fox.x = fox.x - 8
     elif keyboard.right:
        fox.x = fox.x + 8
     elif keyboard.up:
        fox.y = fox.y - 8
     elif keyboard.down:
        fox.y = fox.y + 8
      
     coin_collected = fox.colliderect(coin)    
     if coin_collected:
        score = score + 100
        place_coin()







clock.schedule(time_up, 15.0)
place_coin()
pgzrun.go()