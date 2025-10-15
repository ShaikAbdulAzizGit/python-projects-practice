import turtle
import time
import random 

WIDTH=500
HEIGHT=500

MIN_RACERS=2
MAX_RACERS=10

def init_turtle():
    screen=turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Turtle Racing")

def get_number_of_racers():
    while True:
        racers=input("Enter the number of racers: ").strip()
        if racers.isdigit():
            racers=int(racers)
        else:
            print("Invalid input please enter numerical value !.")
            continue

        if MIN_RACERS <= racers <= MAX_RACERS:
            return racers
        else:
            print(f"Racers not in Range {MIN_RACERS}-{MAX_RACERS} . Please try again !.")

def get_turtles(colors):
    turtles=[]
    spacing_x=WIDTH//(len(colors)+1)
    for i , color in enumerate(colors):
        racer=turtle.Turtle()
        racer.shape('turtle')
        racer.color(color)
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1) * spacing_x,-HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def race_turtles(colors):
    turtles=get_turtles(colors)
    while True:
        for racer in turtles:
            distance=random.randrange(1,20)
            racer.forward(distance)

            x,y=racer.pos()
            if y>=HEIGHT//2 -10:
                return colors[turtles.index(racer)]


colors=['brown','black','red','pink','orange','yellow','cyan','blue','purple','green']
random.shuffle(colors)


racers=get_number_of_racers()
init_turtle()
turtle_colors=colors[:racers]
winner=race_turtles(turtle_colors)

print(f"{winner} Turtle won the race !.")

time.sleep(5)
