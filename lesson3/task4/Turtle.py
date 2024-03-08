import turtle

# Настройка окна
window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("Hello, kitty")

# Создание кота
cat = turtle.Turtle()
cat.color("orange")
cat.pensize(5)

# Рисуем голову
cat.penup()
cat.goto(0, -100)
cat.pendown()
cat.circle(100)

# Рисуем глаза
for i in ((-35, 5), (35, 5)):
    cat.penup()
    cat.goto(i)
    cat.pendown()
    cat.fillcolor('white')
    cat.color('white')
    cat.begin_fill()
    cat.circle(20)
    cat.end_fill()

for n in ((-35, 20), (35, 20)):
    cat.penup()
    cat.goto(n)
    cat.pendown()
    cat.fillcolor('black')
    cat.color('black')
    cat.begin_fill()
    cat.circle(5)
    cat.end_fill()

# Рисуем нос
cat.penup()
cat.goto(-5, -20)
cat.color('orange')
cat.pendown()
cat.fd(20)
cat.left(120)
cat.fd(20)
cat.left(120)
cat.fd(20)

# Рисуем улыбку
cat.penup()
cat.goto(-50, -40)
cat.color('orange')
cat.pendown()
cat.setheading(-60)
cat.circle(60, 120)

# Рисуем ушки
cat.penup()
cat.goto(-60, 80)
cat.color('orange')
cat.pendown()
cat.left(125)
cat.fd(40)
cat.right(-90)
cat.fd(40)

cat.penup()
cat.goto(60, 80)
cat.pendown()
cat.right(280)
cat.fd(40)
cat.right(90)
cat.fd(40)

# Рисуем челочку
cat.penup()
cat.goto(0, 100)
cat.pendown()
cat.fd(30)
cat.goto(0, 100)
cat.right(45)
cat.fd(30)
cat.goto(0, 100)
cat.left(-270)
cat.fd(30)

cat.screen.exitonclick()
cat.screen.mainloop()