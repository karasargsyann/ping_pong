#импорт нужных библиотек
import turtle
from random import choice, randint
#создание фона: название, размер, цвет
window = turtle.Screen()
window.title('Ping-Pong')
window.setup(width = 1.0,height = 1.0)
window.bgcolor('white')
window.tracer(1,5)

#отрисовка и заливка границ поля
line = turtle.Turtle()
line.speed(0)
line.color('light blue')
line.begin_fill()
line.goto(-500, 300)
line.goto(500, 300)
line.goto(500, -300)
line.goto(-500, -300)
line.goto(-500, 300)
line.end_fill()

#отрисовка линии, которая делит поле пополам
line.goto(0,300)
line.color('white')
#команда, чтобы стрелка смотрела вниз
line.setheading(270)
#делаем эту линию пунктирной
for i in range(25):
    if i % 2 == 0:
        line.forward(24)
    else:
        line.up()
        line.forward(24)
        line.down()

#команда, чтобы спрятать стрелку
line.hideturtle()

#создание первой платформы
rocket_1 = turtle.Turtle()
rocket_1.color('gray')
rocket_1.shape('square')
rocket_1.shapesize(stretch_len=1, stretch_wid=5)
rocket_1.penup()
rocket_1.goto(-450,0)

#шрифт счета
FONT = ('Arial', 44)

#счет
score_1 = 0
a1 = turtle.Turtle(visible=False)
a1.color('black')
a1.penup()
a1.setposition(-200, 300)
a1.write(score_1, font=FONT)

score_2 = 0
a2 = turtle.Turtle(visible=False)
a2.color('black')
a2.penup()
a2.setposition(200, 300)
a2.write(score_1, font=FONT)

#движение вверх первой платформы
def move_up_1():
    y = rocket_1.ycor() + 10
    #чтобы первая платформа не  выходила за верхнюю границу
    if y > 250:
        y = 250
    rocket_1.sety(y)

#движение вниз первой платформы
def move_down_1():
    y = rocket_1.ycor() - 10
    #чтобы первая платформа не  выходила за нижнюю границу
    if y < 250:
        y = -250
    rocket_1.sety(y)
    
#создание второй платформы
rocket_2 = turtle.Turtle()
rocket_2.color('gray')
rocket_2.shape('square')
rocket_2.shapesize(stretch_len=1, stretch_wid=5)
rocket_2.penup()
rocket_2.goto(450,0)

#движение вверх второй платформы
def move_up_2():
    y = rocket_2.ycor() + 10
    #чтобы вторая платформа не  выходила за верхнюю границу
    if y > 250:
        y = 250
    rocket_2.sety(y)

#движение вниз второй платформы
def move_down_2():
    y = rocket_2.ycor() - 10
    #чтобы первая платформа не  выходила за нижнюю границу
    if y < 250:
        y = -250
    rocket_2.sety(y)

#создаем мяч и задаем его параметры и скорость
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('black')
#первоначальные скорости мячика
ball.dx = 3
ball.dy = -3
ball.penup()

#команда, чтобы клавиши слушались
window.listen()

#привязываем кнопки к первой платформе
window.onkeypress(move_up_1, 'w')
window.onkeypress(move_down_1, 's')

#привязываем кнопки ко второй платформе
window.onkeypress(move_up_2, 'o')
window.onkeypress(move_down_2, 'k')

while True:
    window.update()
    #получаем текущее положение, добавляем превращеие по скорости и устанавливаем новую координату по 'x' и 'y'
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #отскок от верхней стенки
    #если координата мяча больше или равно 290(середина фигуры), делаем отскок в другую сторону
    if ball.ycor() >= 290:
        ball.dy = - ball.dy
    #анологичным способом делаем отскок с отражением от нижней стенки
    if ball.ycor() <= -290:
        ball.dy = -ball.dy

    #если мяч коснулась правой части поля, возвращаем его в рандомное положение от -150 до 150 по 'у'
    if ball.xcor() >= 490:
        score_2 += 1
        a2.clear()
        a2.write(score_2, font=FONT)
        ball.goto(0, randint(-510, 150))
        #мячик будет двигаться в разных направлениях с разной скоростью
        ball.dx = choice([-4, -3, -2, 2, 3, 4])
        ball.dy = choice([-4, -3, -2, 2, 3, 4])
    
    if ball.xcor() <= -490:
        score_1 += 1
        a1.clear()
        a1.write(score_1, font=FONT)
        ball.goto(0,randint(-150, 150))
        #мячик будет двигаться в разных направлениях с разной скоростью
        ball.dx = choice([-4, -3, -2, 2, 3, 4])
        ball.dy = choice([-4, -3, -2, 2, 3, 4])

    if ball.ycor() >= rocket_1.ycor() - 50 and ball.ycor() <= rocket_1.ycor() + 50 \
        and ball.xcor() >= rocket_1.xcor() - 5  and ball.xcor() <= rocket_1.xcor() + 5:
        ball.dx = -ball.dx
    
    if ball.ycor() >= rocket_2.ycor() - 50 and ball.ycor() <= rocket_2.ycor() + 50 \
        and ball.xcor() >= rocket_2.xcor() - 5  and ball.xcor() <= rocket_2.xcor() + 5:
        ball.dx = -ball.dx
        
#чтобы окно показывалось долгое время
window.mainloop()
