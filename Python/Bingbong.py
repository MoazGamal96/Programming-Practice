#Turtle module 
from pydoc import writedoc
from tkinter import font
import turtle




wind =turtle.Screen() #screen intialize
wind.title("PingPong") #window title
wind.bgcolor("black") #widow background color
wind.setup(width=800,height=600) #windo barametrs 
wind.tracer(0) #controle window update


#Madrab1 
madrab1 = turtle.Turtle()#intialize turtle object (shap)
madrab1.speed(0)#animation speed
madrab1.shape("square")#object shape
madrab1.color("blue")# shapecolor
madrab1.shapesize(stretch_wid=5, stretch_len=1) # size config
madrab1.penup()#anti line drawing
madrab1.goto(-350,0)#oject position


#madrab2 
madrab2= turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=5, stretch_len=1)
madrab2.penup()
madrab2.goto(350,0)


#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2


#score 
score1= 0
score2= 0
score = turtle.Turtle()
score.speed(0)
score.penup()
score.color("white")
score.hideturtle()
score.goto(0, 260)
score.write("Player1: 0  Player2: 0", align= "center" , font= ("courir",24,"normal"))


#Function
def madrab1_up():
    y = madrab1.ycor() # y pos get 
    y += 20 #set y pos  + 20
    madrab1.sety(y) #set y to new pos  

def madrab1_down():
    y = madrab1.ycor()
    y -= 20 #set y pos -20
    madrab1.sety(y)

def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)

def madrab2_down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)


#Keyboard bining
wind.listen()# windo key input
wind.onkeypress(madrab1_up, "w")# w pres pos up +20
wind.onkeypress(madrab1_down, "s")# s press  pos down -20
wind.onkeypress(madrab2_up, "Up") 
wind.onkeypress(madrab2_down, "Down")


#main Game loop
while True:
    wind.update() #screen updat while 


   # ball moving 
    ball.setx( ball.xcor() + ball.dx) #ball start move at 0 then loop run  + 2.5 at xaxis 
    ball.sety( ball.ycor() + ball.dy) #ball start move at 0 then loop run  + 2.5 at yaxis 
   #border check , top border+300px, bot border-300px, ball is 20px
    if ball.ycor () >290: # if ball top
      ball.sety(290)      #set y +290
      ball.dy *= -1       #revers direction
      score.write("Player1: 0  Player2: 0", align= "center" , font= ("courir",24,"normal"))


    if ball.ycor() <-290:
      ball.sety(-290)
      ball.dy *= -1


    if ball.xcor() >390:
       ball.goto(0, 0)
       ball.dx *=-1
       score1 += 1
       score.clear()
       score.write("Player1: {}  Player2: {}".format(score1, score2), align= "center" , font= ("courir",24,"normal"))


    if ball.xcor() <-390:
       ball.goto(0, 0)
       ball.dx *=-1
       score2 += 1
       score.clear()
       score.write("Player1: {}  Player2: {}".format(score1, score2), align= "center" , font= ("courir",24,"normal"))

    #BALL HITING MADRAB
    if (ball.xcor() > 340
     and ball.xcor() < 350 
     and (ball.ycor()<madrab2.ycor() + 40 
     and ball.ycor() >madrab2.ycor() -40 ) ):

        ball.setx(340)
        ball.dx *=-1

    if (ball.xcor() < -340
     and ball.xcor() > -350 
     and (ball.ycor()<madrab1.ycor() + 40 
     and ball.ycor() >madrab1.ycor() -40 ) ):

        ball.setx(-340)
        ball.dx *=-1

