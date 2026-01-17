# recursive_triangle


# Golden Ratio Sierpiński Triangle  
**Python Turtle Graphics Implementation**

A visually elegant variation of the classic Sierpiński triangle,  
where each recursive subdivision scales by the **golden ratio conjugate**  
(φ⁻¹ ≈ 0.6180339887) instead of the conventional ½.

This creates a more spacious, harmonious and aesthetically pleasing fractal pattern  
with strong mathematical connections to the golden ratio (φ ≈ 1.618).

## Preview

![Golden Sierpiński Triangle - order 7](https://via.placeholder.com/800x600/111133/ffd700?text=Golden+Sierpiński+Triangle+-+order+7)  
*(dark background with golden outlines – actual result is more refined)*

Compared to the classic version (scale 0.5), the golden version feels  
more organic, airy and naturally balanced.

## Features

- Recursive construction using golden ratio scaling (1/φ)
- Correct turtle positioning (no overlaps or gaps)
- Fast rendering with `turtle.speed(0)`
- Customizable colors, size and recursion depth
- Clean code structure with separate triangle drawing function

## Mathematical Background

This variant is inspired by the **Kepler triangle** —  
the only right-angled triangle whose sides form a **geometric progression**  
with common ratio √φ:

side ratios:  1  :  √φ  :  φ    ≈  1 : 1.272 : 1.618

The scaling factor used in the recursion is exactly **1/φ ≈ 0.618**.

## Requirements

- Python 3.x
- Standard library module: `turtle`

No external packages needed.

## Usage

```bash
# Just run the script
python golden_sierpinski.py

Recommended starting parametersOrder
Size
Approximate time
Visual character
5–6
500
< 1 sec
Very elegant, spacious
7
600–700
1–3 sec
Beautiful balance of detail
8
800
5–12 sec
Rich but still clear
9
900+
20–60 sec
Very detailed, dense golden pattern

Customization Examplespython

# Dark & mysterious look
t.color("gold")
t.fillcolor("#0d001a")        # very dark purple

# Warm golden style
t.color("#ffcc00")
t.fillcolor("#3c2f00")        # deep amber

# Wireframe version (comment out begin_fill / end_fill)
# t.pencolor("gold")
# t.pensize(1.5)



LicenseMIT License — feel free to use, modify, and share.

