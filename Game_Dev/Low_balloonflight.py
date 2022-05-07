
import pgzrun
from pgzero.builtins import Actor
from random import randint

WIDTH = 800
HEIGHT = 600
GRAVITY_STRENGTH = 2

balloon = Actor('balloon')
balloon.pos = 400, 300

bird = Actor('bird-up')
bird.pos = randint(800, 1600), randint(10, 200)

# add another bird actor 
birdtwo = Actor('bird-up')
birdtwo.pos = randint(800, 1600), randint(10, 200)

house = Actor('house')
house.pos = randint(800, 1600), 460

housetwo = Actor('house')
housetwo.pos = randint(800, 1600), 460

tree = Actor('tree')
tree.pos = randint(800, 1600), 450

treetwo = Actor('tree')
treetwo.pos = randint(800, 1600), 450

bird_up = True
bird_uptwo = True #set bird up to be true for bird two 
up = False
game_over = False
score = 0
number_of_updates = 0



scores = []


def update_high_scores():
    global score, scores
    filename = r"C:/Users/Crystal/Desktop/EE104/EE104_Lab8/Game_dev/highscore.txt"
    scores = []
    with open(filename, 'r') as file:
        line = file.readline()
        high_scores = line.split()
        for high_score in high_scores:
            if(score > int(high_score)):
                scores.append(str(score) + ' ')
                score = int(high_score)
            else:
                scores.append(str(high_score) + ' ')
    with open(filename, 'w') as file:
        for high_score in scores:
            file.write(high_score)


def display_high_scores():
    screen.draw.text('HIGH SCORES', (350, 150), color='white')
    y = 175
    position = 1
    for high_score in scores:
        screen.draw.text(str(position) + '.  ' + high_score, (350, y),
                         color='white')
        y += 25
        position += 1


def draw():
    screen.blit('background', (0,0))
    if not game_over:
        balloon.draw()
        bird.draw()
        birdtwo.draw() #draw another bird 
        house.draw()
        housetwo.draw()#draw another house
        tree.draw()
        treetwo.draw()
        screen.draw.text('Score: ' + str(score), (700, 5), color='black')
    else:
        display_high_scores()


def on_mouse_down():
    global up
    up = True
    balloon.y -= 50


def on_mouse_up():
    global up
    up = False


def flap():
    global bird_up, bird_uptwo
    if bird_up:
        bird.image = 'bird-down'
        bird_up = False
    else:
        bird.image = 'bird-up'
        bird_up = True
   
    #add another bird to flap 
    if bird_uptwo:
        birdtwo.image = 'bird-down'
        bird_uptwo = False
    else:
        birdtwo.image = 'bird-up'
        bird_uptwo = True


def update():
    global game_over, score, number_of_updates, subtract_life
    if not game_over:
        if not up:
            balloon.y += GRAVITY_STRENGTH  # gravity
        if bird.x > 0:
            bird.x -= 10 #made the bird fly faster 
            if number_of_updates == 20: #changed correlated to the speed of the bird 
                flap()
                number_of_updates = 0
            else:
                number_of_updates += 1
        else:
            bird.x = randint(800, 1600)
            bird.y = randint(10, 200)
            score += 1
            number_of_updates = 0
       
        #add another bird and the constraints 
        if birdtwo.x > 0:
            birdtwo.x -= 6 #made the bird fly faster 
            if number_of_updates == 12: 
                flap()
                number_of_updates = 0
            else:
                number_of_updates += 1
        else:
            birdtwo.x = randint(400, 1200)
            birdtwo.y = randint(5, 100)
            score += 1
            number_of_updates = 0

        if house.right > 0:
            house.x -= 2
            score_up()
        else:
            house.x = randint(800, 1600) #800
            

        if tree.right > 0:
            tree.x -= 2
            score_up()
        else:
            tree.x = randint(800, 1600) #800
         #add new house and tree contraints   
        if housetwo.right > 0:
            housetwo.x -= 3
            score_up()
        else:
            housetwo.x = randint(800, 1600) #800

        if treetwo.right > 0:
            treetwo.x -= 3
            score_up()
        else:
            treetwo.x = randint(800, 1600) #800
            
       
            
        if balloon.top < 0 or balloon.bottom > 560:
            game_over = True
            update_high_scores()

        if (balloon.collidepoint(bird.x, bird.y) or
                balloon.collidepoint(house.x, house.y) or
                balloon.collidepoint(tree.x, tree.y) or 
                balloon.collidepoint(birdtwo.x, birdtwo.y) or 
                balloon.collidepoint(housetwo.x, housetwo.y) or
                balloon.collidepoint(treetwo.x, treetwo.y)):
            # subtract_life()
            game_over = True
            update_high_scores()
            
def score_up():
    global score
    if tree.right == 400 or tree.right == 399:
        score = score + 1
    if house.right == 400 or house.right == 399:
        score = score + 1
    if treetwo.right == 400 or treetwo.right == 399:
        score = score + 1
    if housetwo.right == 400 or housetwo.right == 399:
        score = score + 1
            


pgzrun.go()