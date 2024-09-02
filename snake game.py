import turtle
import time
import random


delay=0.1
scoer=0
high_score=0


window=turtle.Screen()
window.title("GAME")
window.bgcolor("red")
window.setup(width=600,height=600)
window.tracer(0)



snake=turtle.Turtle()
snake.shape("circle")
snake.speed(0)
snake.color("orange")
snake.goto(0,0)
snake.penup()
snake.direction="stop"

frog=turtle.Turtle()
frog.shape("circle")
frog.speed(0)
frog.color("black")
frog.goto(0,100)
frog.penup()



center=turtle.Turtle()
center.shape("circle")
center.color("pink")
center.speed(0)
center.penup()
center.goto(0,200)
center.hideturtle()
center.write("Score =0 :: High score=o",align="center",font=("candara", 24, "bold"))

def group():
    if snake.direction != "down":
       snake.direction ="up" 
def godown(): 
    if snake.direction != "up":
        snake.direction = "down"
def goleft():
    if snake.direction != "right":
        snake.direction = "left"
def goright():
    if snake.direction != "left":
        snake.direction = "right"

def move():
    if snake.direction == "up":
        y=snake.ycor()
        snake.sety(y+20)
    if snake.direction == "down":
        y=snake.ycor()
        snake.sety(y-20)
    if snake.direction == "left":
        x=snake.xcor()
        snake.setx(x-20)
    if snake.direction == "right":
        x=snake.xcor()
        snake.setx(x+20)
        
window.listen()
window.onkeypress(group,"8")
window.onkeypress(godown,"2")
window.onkeypress(goleft,"4")
window.onkeypress(goright,"6")

segment=[]

while True:
    window.update()
    if snake.xcor()>290 or snake.xcor()< -290 or snake.ycor()>290 or snake.ycor()<-290:
        time.sleep(1)
        snake.goto(0,0)
        snake.direction="stop"
        snake.color("yellow")
        snake.shape("circle")
        for segments in segment:
            segments.goto(1000,1000)
        
        segment.clear()
        scoer=0
        delay=0.1
        
    if snake.distance(frog) < 20:
        x=random.randint(-290, 290)
        y=random.randint(-290,290)
        frog.goto(x,y)
        
        
        new_segment=turtle.Turtle()
        new_segment.shape("circle")
        new_segment.speed(0)
        new_segment.color("grey")
        new_segment.penup()
        segment.append(new_segment)
        scoer += 10
        delay=0.1
        if scoer > high_score:
            high_score=scoer
        center.clear()
        center.write("Score :{}  High score={}".format(scoer,high_score),
                     align="center",font=("candara", 24, "bold"))

        
    
    for index in range(len(segment)-1, 0, -1):
            x = segment[index-1].xcor()
            y = segment[index-1].ycor()
            segment[index].goto(x, y)
            
    if len(segment) >0:
            x=snake.xcor()
            y=snake.ycor()
            segment[0].goto(x, y)
        
        
        
    move()
    for segments in segment:
        if segments.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0,0)
            snake.direction="stop"
            snake.color("yellow")
            snake.shape("circle")
            for segments in segment:
                segments.goto(1000,1000)
            
            segment.clear()
            scoer=0
            delay=0.1
            center.clear()
            center.write("Score :{}  High score={}".format(scoer,high_score),
                        align="center",font=("candara", 24, "bold"))
    
    time.sleep(delay)
window.mainloop()