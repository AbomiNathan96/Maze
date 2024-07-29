import math

import sys

from PIL import Image, ImageDraw

import random

Hight = int(input("What is the Width of the maze? "))

Width = int(input("What is the Hight of the maze? "))

random.seed = int(input("Whats the seed of the maze? "))

Fast = int(input("Fast Mode? (1/0) "))

Maze = []

if Hight/2 == round(Hight/2):
    Hight = Hight + 1

if Width/2 == round(Width/2):
    Width = Width + 1


Y = math.ceil(Width/2)
X = math.floor(Hight/2)


def MakeMaze():
    Maze = []

    A = 0
    B = 0

    while A < Hight:
        Maze = Maze + [[]]
        B = 0
        while B < Width:
            Maze[A] = Maze[A] + ['# ']
            B = B + 1
        A = A + 1

    return(Maze)

def Render(Maze):
    A = 0
    B = 0
    Buffer = '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'

    while A < Width:
        B = 0
        Temp = ""
        while B < Hight:
            Temp = Temp + Maze[B][A]
            B = B + 1
        Buffer = Buffer + Temp + "\n"
        A = A + 1
    print(Buffer)

Maze = MakeMaze()




def IS(X,Y):

    if X > -1 and X < Width and Y > -1 and Y <  Hight:
        return(Maze[Y][X])
    else:
        return('  ')

def Mazeify(Width,Hight):
    Y = 1
    X = 1

    EXITN = 1

    Generating = True

    EX = []
    EY = []
    ET = []

    C = 0

    GoalExists = False
    I = 0

    while Generating == True:
        I = I + 1
        if Fast == 0:
            Render(Maze)
        C = 1
        if IS(X+2,Y) == '# ':
            C = C + 1
        if IS(X-2,Y) == '# ':
            C = C + 1
        if IS(X,Y+2) == '# ':
            C = C + 1
        if IS(X,Y-2) == '# ':
            C = C + 1

        Maze[Y][X] = '. '
        if IS(X+2,Y) == '# ' and random.randrange(C) == 0:
            Maze[Y][X+1] = '. '
            X = X + 2
            GoalExists = False
        elif IS(X,Y-2) == '# ' and random.randrange(C) == 0:
            Maze[Y-1][X] = '. '
            Y = Y - 2
            GoalExists = False
        elif IS(X-2,Y) == '# ' and random.randrange(C) == 0:
            Maze[Y][X-1] = '. '
            X = X - 2
            GoalExists = False
        elif IS(X,Y+2) == '# ' and random.randrange(C) == 0:
            Maze[Y+1][X] = '. '
            Y = Y + 2
            GoalExists = False
        elif IS(X+2,Y) != '# ' and IS(X,Y+2) != '# ' and IS(X,Y-2) != '# ' and IS(X-2,Y) != '# ':
            I = I - 1
            if GoalExists == False:
                EX = EX + [X]
                EY = EY + [Y]
                ET = ET + [I]
                GoalExists = True
            if IS(X+1,Y) == '. ':
                Maze[Y][X+1] = '  '
                Maze[Y][X] = '  '
                X = X + 2
            elif IS(X,Y-1) == '. ':
                Maze[Y-1][X] = '  '
                Maze[Y][X] = '  '
                Y = Y - 2
            elif IS(X-1,Y) == '. ':
                Maze[Y][X-1] = '  '
                Maze[Y][X] = '  '
                X = X - 2
            elif IS(X,Y+1) == '. ':
                Maze[Y+1][X] = '  '
                Maze[Y][X] = '  '
                Y = Y + 2
            else:
                EXITN = random.randrange(len(EY))
                Maze[EY[EXITN]][EX[EXITN]] = 'F '
                Generating = False
                Maze[1][1] = '  '
                print("ticks "+str(ET[EXITN]))
                print("the goal is at "+str(EX[EXITN])+', '+str(EY[EXITN]))
    

Mazeify(Hight,Width)
print(' ')
print(' ')
print(' ')



Option = input('This image will be saved if you press enter')

IMG = Image.new("L",(Hight,Width),0)

A = 0
B = 0
while A < Width:
    B = 0
    while B < Hight:
        if IS(A,B) == '  ':
            IMG.putpixel((B,A),255)
        elif IS(A,B) == 'F ':
            IMG.putpixel((B,A),100)
        B = B + 1
    A = A + 1
IMG.show()
IMG.save('Maze.png', "PNG")