import turtle

def main():
    arch = turtle.Turtle()
    turtle.setup(600, 500)

    def draw_arch(direction, angle, length):
        if direction == 'right':
            arch.right(angle)
        else:
            arch.left(angle)
        arch.forward(length)

    # Задает цвет
    arch.fillcolor('#a5a6a1')

    # Начало закраски
    arch.begin_fill()

    # Размер пера
    arch.pensize(2)

    # Цикл для рисования верхней части арки
    i = 0
    while i < 4:
        if i % 2 == 0:
            draw_arch('right', 90, 200)
        else:
            draw_arch('right', 90, 100)
        i += 1

    # Конец закраски
    arch.end_fill()
    arch.fillcolor('#a5a6a1')
    arch.begin_fill()


    draw_arch('right', 90, 200)
    draw_arch('right', 90, 60)
    draw_arch('left', 90, 20)
    draw_arch('left', 90, 100)
    draw_arch('right', 90, 20)
    draw_arch('right', 90, 90)
    draw_arch('right', 20, 30)
    draw_arch('right', 70, 30)
    draw_arch('right', 90, 15)
    draw_arch('left', 90, 200)
    arch.end_fill()
    draw_arch('left', 90, 37)
    draw_arch('left', 90, 30)

    arch.fillcolor('#fff019')
    arch.begin_fill()
    draw_arch('right', 90, 60)
    arch.circle(15, 180)
    draw_arch('left', 0, 60)
    draw_arch('right', 90, 80)
    draw_arch('right', 90, 60)
    arch.circle(15, 180)
    draw_arch('left', 0, 60)
    arch.end_fill()
    draw_arch('left', 90, 160)


















    turtle.done()
if __name__ == '__main__':
    main()