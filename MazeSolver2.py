
import time, random, math

from PIL import Image, ImageDraw

Solved = False

with Image.open("Maze.png") as img:
    Width = img.width
    Height = img.height

Fast = int(input("Fast Mode? (1/0) "))

Maze = []

if Width/2 == round(Width/2):
    Width = Width + 1

if Height/2 == round(Height/2):
    Height = Height + 1


Y = math.ceil(Height/2)
X = math.floor(Width/2)

I = 1


def MakeMaze():
    Maze = []

    A = 0
    B = 0

    while A < Width:
        Maze = Maze + [[]]
        B = 0
        while B < Height:
            Maze[A] = Maze[A] + ['# ']
            B = B + 1
        A = A + 1

    return(Maze)


def Render(Maze):
    A = 0
    B = 0  
    Buffer = ""

    while A < Height:
        B = 0
        Temp = ""
        while B < Width:
            Temp = Temp + Maze[B][A]
            B = B + 1
        Buffer = Buffer + Temp + '\n'
        A = A + 1
    print(Buffer)

def Render2(Maze):
    A = 0
    B = 0
    Buffer = ''
    while A < Height:
        B = 0
        Temp = ""
        while B < Width:
            if X == B and Y == A:
                Temp = Temp + '@ '
            else:
                match Maze[B][A]:
                    case '# ':
                        Temp = Temp + '# '
                    case '. ':
                        Temp = Temp + '. '
                    case 'F ':
                        Temp = Temp + 'F '
                    case _:
                        Temp = Temp + '  '
                    
            B = B + 1
        Buffer = Buffer + Temp + '\n'
        A = A + 1
    print(Buffer)

def Load(Maze):
    A = 0
    B = 0

    with Image.open("Maze.png") as img:
        while A < Height:
            B = 0
            while B < Width:
                match img.getpixel((B,A)):
                    case 255:
                        Maze[B][A] = '  '
                    case 0:
                        Maze[B][A] = '# '
                    case 200:
                        Maze[B][A] = '  '
                    case 100:
                        Maze[B][A] = 'F '
                B = B + 1
            A = A + 1
    return(Maze)

def IS(X,Y):

    if X > -1 and X < Width and Y > -1 and Y < Height:
        return(Maze[X][Y])
    else:
        return('')

def Solve(Maze,X,Y):
    Solvede = False
    if Maze[X][Y+1] == 'F ':
        Solvede = True
    if Maze[X][Y-1] == 'F ':
        Solvede = True
    if Maze[X+1][Y] == 'F ':
        Solvede = True
    if Maze[X-1][Y] == 'F ':
        Solvede = True
    Maze[X][Y] = '. '
    if IS(X+1,Y) == '  ':
        X = X + 1
    elif IS(X,Y+1) == '  ':
        Y = Y + 1
    elif IS(X-1,Y) == '  ':
        X = X - 1
    elif IS(X,Y-1) == '  ':
        Y = Y - 1
    elif IS(X+1,Y) == '. ':
        Maze[X][Y] = '4 '
        X = X + 1
    elif IS(X,Y+1) == '. ':
        Maze[X][Y] = '4 '
        Y = Y + 1
    elif IS(X-1,Y) == '. ':
        Maze[X][Y] = '4 '
        X = X - 1
    elif IS(X,Y-1) == '. ':
        Maze[X][Y] = '4 '
        Y = Y - 1
        
    return(Maze,Solvede,X,Y)


Maze = MakeMaze()

Maze = Load(Maze)
Render(Maze)
X,Y = 1,1

Maze[1][1] = 'E '

while Solved == False:
    I = I + 1
    if Fast == 0:
        Render2(Maze)
    Maze,Solved,X,Y = Solve(Maze,X,Y)

Render2(Maze)

IMG = Image.new("L",(Width,Height),0)

A = 0
B = 0
while A < Height:
    B = 0
    while B < Width:
        match IS(B,A):
            case 'F ':
                IMG.putpixel((B,A),100)
            case '# ':
                IMG.putpixel((B,A),0)
            case '. ':
                IMG.putpixel((B,A),200)
            case _:
                IMG.putpixel((B,A),255)

        B = B + 1
    A = A + 1
IMG.show()
IMG.save('Maze.png', "PNG")