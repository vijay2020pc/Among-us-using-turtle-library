import turtle

BODY_COLOR =  'white'
BODY_SHADOW = ''
GLASS_COLOR = 'cyan'
GLASS_SHADOW = ''
BODY_COLOR2 = 'yellow'
BODY_SHADOW2 = ''
GLASS_COLOR2 = 'skyblue'
GLASS_SHADOW2 = ''
BODY_COLOR3 = 'red'
BODY_SHADOW3 = ''
GLASS_COLOR3 = 'skyblue'
GLASS_SHADOW3 = ''
s = turtle.getscreen()
t = turtle.Turtle()

# it can move forward backward left right
def body():
    """ draws the body """
    t.pensize(20)
    #t.speed(15)

    t.fillcolor(BODY_COLOR)
    t.begin_fill()

    # right side
    t.right(90)
    t.forward(50)
    t.right(180)
    t.circle(40, -180)
    t.right(180)
    t.forward(200)

    # head curve
    t.right(180)
    t.circle(100, -180)

    # left side
    t.backward(20)
    t.left(15)
    t.circle(500, -20)
    t.backward(20)

    #t.backward(200)
    t.circle(40, -180)
    #t.right(90)
    t.left(7)
    t.backward(50)

    # hip
    t.up()
    t.left(90)
    t.forward(10)
    t.right(90)
    t.down()
    #t.right(180)
    #t.circle(25, -180)
    t.right(240)
    t.circle(50, -70)

    t.end_fill()


def glass():
    t.up()
    #t.right(180)
    t.right(230)
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.right(90)

    t.down()
    t.fillcolor(GLASS_COLOR)
    t.begin_fill()

    t.right(150)
    t.circle(90, -55)

    t.right(180)
    t.forward(1)
    t.right(180)
    t.circle(10, -65)
    t.right(180)
    t.forward(110)
    t.right(180)
    
    #t.right(180)
    t.circle(50, -190)
    t.right(170)
    t.forward(80)

    t.right(180)
    t.circle(45, -30)

    t.end_fill()

def backpack():
    t.up()
    t.right(60)
    t.forward(100)
    t.right(90)
    t.forward(75)

    t.fillcolor(BODY_COLOR)
    t.begin_fill()

    t.down()
    t.forward(30)
    t.right(255)

    t.circle(300, -30)
    t.right(260)
    t.forward(30)

    t.end_fill()


body()
glass()
backpack()
def body2():
    """ draws the body """
    t.pensize(20)
    #t.speed(15)
    t.up()
    
    t.forward(400)
    t.right(90)
    t.forward(100)

    t.down()
    t.fillcolor(BODY_COLOR2)
    t.begin_fill()

    # right side

    t.forward(50)
    t.right(180)
    t.circle(40, -180)
    t.right(180)
    t.forward(200)

    # head curve
    t.right(180)
    t.circle(100, -180)

    # left side
    t.backward(20)
    t.left(15)
    t.circle(500, -20)
    t.backward(20)

    #t.backward(200)
    t.circle(40, -180)
    #t.right(90)
    t.left(7)
    t.backward(50)

    # hip
    t.up()
    t.left(90)
    t.forward(10)
    t.right(90)
    t.down()
    #t.right(180)
    #t.circle(25, -180)
    t.right(240)
    t.circle(50, -70)

    t.end_fill()


def glass2():
    t.up()
    #t.right(180)
    t.right(230)
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.right(90)

    t.down()
    t.fillcolor(GLASS_COLOR2)
    t.begin_fill()

    t.right(150)
    t.circle(90, -55)

    t.right(180)
    t.forward(1)
    t.right(180)
    t.circle(10, -65)
    t.right(180)
    t.forward(110)
    t.right(180)
    
    #t.right(180)
    t.circle(50, -190)
    t.right(170)
    t.forward(80)

    t.right(180)
    t.circle(45, -30)

    t.end_fill()

def backpack2():
    t.up()
    t.right(60)
    t.forward(100)
    t.right(90)
    t.forward(75)

    t.fillcolor(BODY_COLOR2)
    t.begin_fill()

    t.down()
    t.forward(30)
    t.right(255)

    t.circle(300, -30)
    t.right(260)
    t.forward(30)

    t.end_fill()


body2()
glass2()
backpack2()
def body3():
    """ draws the body """
    t.pensize(20)
    #t.speed(15)
    t.up()
    
    t.backward(550)
    t.right(90)
    t.forward(200)

    t.down()
    t.fillcolor(BODY_COLOR3)
    t.begin_fill()

    # right side

    t.forward(50)
    t.right(180)
    t.circle(40, -180)
    t.right(180)
    t.forward(200)

    # head curve
    t.right(180)
    t.circle(100, -180)

    # left side
    t.backward(20)
    t.left(15)
    t.circle(500, -20)
    t.backward(20)

    #t.backward(200)
    t.circle(40, -180)
    #t.right(90)
    t.left(7)
    t.backward(50)

    # hip
    t.up()
    t.left(90)
    t.forward(10)
    t.right(90)
    t.down()
    #t.right(180)
    #t.circle(25, -180)
    t.right(240)
    t.circle(50, -70)

    t.end_fill()


def glass3():
    t.up()
    #t.right(180)
    t.right(230)
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.right(90)

    t.down()
    t.fillcolor(GLASS_COLOR3)
    t.begin_fill()

    t.right(150)
    t.circle(90, -55)

    t.right(180)
    t.forward(1)
    t.right(180)
    t.circle(10, -65)
    t.right(180)
    t.forward(110)
    t.right(180)
    
    #t.right(180)
    t.circle(50, -190)
    t.right(170)
    t.forward(80)

    t.right(180)
    t.circle(45, -30)

    t.end_fill()

def backpack3():
    t.up()
    t.right(60)
    t.forward(100)
    t.right(90)
    t.forward(75)

    t.fillcolor(BODY_COLOR3)
    t.begin_fill()

    t.down()
    t.forward(30)
    t.right(255)

    t.circle(300, -30)
    t.right(260)
    t.forward(30)

    t.end_fill()


body3()
glass3()
backpack3()
