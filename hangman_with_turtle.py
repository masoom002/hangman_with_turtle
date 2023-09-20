from pics import words
from random import choice
from string import ascii_lowercase
from time import sleep
import pygame
import turtle
pygame.mixer.init()
turtle.speed(5)
turtle.hideturtle()
turtle.pensize(2)
writer = turtle.Pen()
writer.ht()
#______________________________________________________________________________________________________________________
def draw_gallows():
    turtle.up()
    turtle.home()
    turtle.pendown()
    turtle.left(90)
    turtle.forward(175)
    turtle.left(90)
    turtle.forward(74)
    turtle.left(90)
    turtle.forward(35)
def draw_head():
    turtle.right(90)
    turtle.circle(15)
    turtle.circle(15, 180)
def draw_toroso():
    turtle.right(90)
    turtle.fd(60)
def draw_firstarm():
    turtle.goto(-74, 100)
    turtle.pendown()
    turtle.left(55)
    turtle.forward(45)
    turtle.right(180)
    turtle.forward(45)
    turtle.penup()
def draw_secondarm():
    turtle.goto(-74, 100)
    turtle.pendown()
    turtle.left(70)
    turtle.forward(45)
    turtle.right(180)
    turtle.forward(45)
    turtle.penup()
def draw_firstleg():
    turtle.pendown()
    turtle.right(125)
    turtle.forward(50)
    turtle.left(30)
    turtle.forward(60)
    turtle.right(180)
    turtle.forward(60)
def draw_secondleg():
    turtle.lt(120)
    turtle.fd(60)

#____________________________________________________________________________________________________________________
functions=[draw_gallows,draw_head,draw_toroso,draw_firstarm,draw_secondarm,draw_firstleg,draw_secondleg]

def game():
    writer.clear()
    turtle.clear()
    writer.up()
    writer.goto(0, -200)
    writer.down()
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('sounds/background.mp3'))
    alphabet=list(ascii_lowercase)
    alphabet.append(" ")
    answer=choice(words)
    print(answer)
    guess=list(len(answer)*'_')
    writer.write(' '.join(guess), font=('', 20), align='center')
    i=0
        
    while i<7:
        letter=turtle.textinput("Hangman","enter a letter:").lower()
        while letter not in list(ascii_lowercase):
            letter=(turtle.textinput("Hangman","enter a letter:")).lower()
        if letter not in answer:
            functions[i]()
            i = i+1
        else:
            index=-1
            while True:
                try:
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("sounds/correct answer.mp3"))
                    index=answer.index(letter,index+1) 
                    guess[index]=letter
                except:
                    break
            writer.undo()
            print(guess)
            writer.write(' '.join(guess), font=('', 20), align='center')
            if "".join(guess)==answer:
                writer.up()
                writer.goto(0, -280)
                writer.down()
                writer.write("good job kid let's play again ;-;",font=("",20), align='center')
                pygame.mixer.Channel(0).play(pygame.mixer.Sound("sounds/win.mp3"))
                sleep(4)
                game()
    if i==7:
        writer.up()
        writer.goto(0, -280)
        writer.down()
        writer.write(f"ha ha ha game over ;) answer was ({answer})",font=("",20), align='center')
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('sounds/lose.mp3'))
        sleep(5)
        game()

game()
turtle.done()