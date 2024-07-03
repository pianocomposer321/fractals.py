import turtle

def draw_edge(length: float, depth: int, level: int):
    if level == depth:
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
    else:
        draw_edge(length/2, depth, level + 1)
        turtle.right(180)
        draw_edge(length/2, depth, level + 1)
        draw_edge(length/2, depth, level + 1)
        draw_edge(length/2, depth, level + 1)
        turtle.right(180)
        draw_edge(length/2, depth, level + 1)

def draw_vicsek(length: float, depth: int):
    length *= ((2/3)**(depth+1))
    turtle.up()
    turtle.right(180)
    turtle.forward(length * 3)
    turtle.right(180)
    turtle.down()
    for _ in range(4):
        draw_edge(length, depth, 0)
        turtle.right(180)

def main():
    turtle.speed(0)
    turtle.hideturtle()
    draw_vicsek(200, 4)
    turtle.done()

if __name__ == '__main__':
    main()
