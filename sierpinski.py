import turtle

def draw_left(length: float):
    turtle.seth(240)
    turtle.forward(length)

def draw_bottom(length: float, depth: int, level: int):
    turtle.seth(0)
    if level == depth:
        turtle.forward(length)
    else:
        draw_bottom(length/2, depth, level + 1)
        draw_right(length/2)
        draw_bottom(length/2, depth, level + 1)
        draw_left(length/2)
        draw_bottom(length/2, depth, level + 1)

def draw_right(length: float):
    turtle.seth(120)
    turtle.forward(length)

def draw_sierpinski_triangle(length: float, depth: int):
    def impl(length: float, depth: int, level: int):
        draw_left(length)
        draw_bottom(length, depth, level)
        draw_right(length)

    impl(length, depth, 0)
    turtle.done()

def main():
    turtle.speed(0)
    turtle.hideturtle()
    draw_sierpinski_triangle(350, 7)

if __name__ == '__main__':
    main()
