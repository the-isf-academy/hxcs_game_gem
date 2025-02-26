# /////////// INSTRUCTIONS /////////////////
# 👾 Let's make a game!
# 
# 1️⃣ Run the file & install
#    - in the Terminal run the command: pip3 install pgzero
#    - play the game
#
# 2️⃣ Add in your own charachter sprite!
# 
# 3️⃣ Add these features in the game
#     - left and up arrow keys move the charachter
#     - score increases when you collect a gem
#     - the gem moves to a random location, every time it is collected
# 
# 4️⃣ extension feature ideas
#     - timer : user must collect gems in 30s or less 
#     - power ups: increaser user's speed 
#     - obstacles: if uesr hits the game is over
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# imports required libraries
import pgzrun
from helpers import *
from random import randint

# sets size of screen width
WIDTH = 500
# sets size of screen height
HEIGHT = 500

# sets screen background color (rgb color value)
BACKGROUND_COLOR = (149, 161, 171)

# creates a player sprite
player = Actor(image='alien.png', anchor=('center', 'bottom'))
player.scale = .5        # scales the sprite image
player.x = 250          # sets the start X position
player.y = 250          # sets the start Y position
player.speed = 10

# creates a gem sprite
gem = Actor(image='gem.png')
gem.scale = 1
gem.x = randint(0, WIDTH)
gem.y = randint(0, HEIGHT)

score = 0

# controls what gets draw on the screen
def draw():
    global score

    # draws the background
    screen.fill(BACKGROUND_COLOR) 

    # draws the player
    player.draw()

    # draws the gem
    gem.draw()

    # draws the score
    screen.draw.text(f"Score: {score}", centerx=50, centery=20)


# controls what happens every frame
def update():
    global score

    # if the right arrow key is pressed
    if keyboard[keys.RIGHT] and player.x < WIDTH:

        # moves the player to the right
        player.x += player.speed

        # flips the character to face to the right
        player.flip_x = False

    # if the down arrow is pressed
    if keyboard[keys.DOWN] and player.y < HEIGHT:

        # moves the player down
        player.y += player.speed


    # if the player collides with the gem
    if player.colliderect(gem):
        # move the gem x,y location to a random location
        gem.x = 100
        gem.y = 100


# runs the game
pgzrun.go()
