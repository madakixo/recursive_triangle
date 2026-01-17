import turtle

PHI = (1 + 5**0.5) / 2          # ≈ 1.6180339887
SCALE = 1 / PHI                 # ≈ 0.6180339887  ← golden ratio conjugate

def draw_triangle(t, size):
    """Draw one filled equilateral triangle"""
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

def golden_sierpinski(t, order, size):
    if order == 0:
        draw_triangle(t, size)
        return
    
    new_size = size * SCALE
    
    # Bottom-left
    golden_sierpinski(t, order-1, new_size)
    
    # Move to bottom-right
    t.forward(size)
    golden_sierpinski(t, order-1, new_size)
    
    # Back & up to top position
    t.backward(size)
    t.left(60)
    t.forward(size)
    t.right(60)
    
    # Top triangle
    golden_sierpinski(t, order-1, new_size)
    
    # Return to start position & orientation
    t.left(60)
    t.backward(size)
    t.right(60)


# ─── Main ────────────────────────────────────────────────────
screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)                    # 0 = fastest
t.penup()
t.goto(-320, -280)            # nice centering on most screens
t.pendown()
t.color("gold")               # outline color
t.fillcolor("#1e1e4d")        # dark mystical fill
t.hideturtle()

golden_sierpinski(t, order=7, size=600)

screen.exitonclick()
