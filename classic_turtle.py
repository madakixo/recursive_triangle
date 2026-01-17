import turtle

def sierpinski_triangle(t, order, size):
    if order == 0:
        # Draw filled triangle
        t.begin_fill()
        for _ in range(3):
            t.forward(size)
            t.left(120)
        t.end_fill()
    else:
        size /= 2
        # Bottom left
        sierpinski_triangle(t, order-1, size)
        t.forward(size)
        # Bottom right
        sierpinski_triangle(t, order-1, size)
        t.backward(size)
        t.left(60)
        t.forward(size)
        t.right(60)
        # Top
        sierpinski_triangle(t, order-1, size)
        t.left(60)
        t.backward(size)
        t.right(60)

# ─── Main ───────────────────────────────────────────────
t = turtle.Turtle()
t.speed(0)           # 0 = fastest
t.penup()
t.goto(-200, -150)   # better positioning
t.pendown()
t.color("darkblue")
t.hideturtle()

sierpinski_triangle(t, order=6, size=400)

turtle.done()
