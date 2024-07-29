import math, msvcrt

from PIL import Image, ImageDraw

Solved = False

with Image.open("Maze.png") as img:
    Width = img.width
    Height = img.height

Maze = []

if Width/2 == round(Width/2):
    Width = Width + 1

if Height/2 == round(Height/2):
    Height = Height + 1


Y = math.ceil(Height/2)
X = math.floor(Width/2)
#I dont remembor what these are for
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
    Buffer = '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
    while A < Height:
        B = 0
        Temp = ""
        while B < Width:
            if X == B and Y == A:
                Temp = Temp + '@ '
            else:
                match IS(B,A):
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



Maze = MakeMaze()
Maze = Load(Maze)
X,Y = -1,-1
Render(Maze)
X,Y = 1,1

Solving = True
while Solving == True:
    
    I = I + 1
    match msvcrt.getch():
        case b'M':
            if IS(X+1,Y) != '# ':
                X = X + 1
        case b'K':
            if IS(X-1,Y) != '# ':
                X = X - 1
        case b'P':
            if IS(X,Y+1) != '# ':
                Y = Y + 1
        case b'H':
            if IS(X,Y-1) != '# ':
                Y = Y - 1
    Render(Maze)
    if Maze[X][Y] == 'F ':
        Solving = False
    Maze[X][Y] = '. '
    

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