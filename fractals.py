from turtle import *

def tree(size, levels, angle):
    if levels == 0:
        color("green")
        dot(size)
        color("black")
        return

    #Going straight up
    forward(size)
    right(angle)

    #recursion until it happened levels times
    tree(size * 0.8, levels - 1, angle)

    left(angle * 2)

    tree(size * 0.8, levels - 1, angle)

    right(angle)
    backward(size)


def snowflake_side(length, levels):
    if levels == 0:
        forward(length)
        return
    length /= 3.0
    snowflake_side(length, levels - 1)
    left(60)
    snowflake_side(length, levels - 1)
    right(120)
    snowflake_side(length, levels - 1)
    left(60)
    snowflake_side(length, levels - 1)

def create_snowflake(sides, length):
    for _ in range(sides):
        snowflake_side(length, sides)
        right(360/ sides)
    #draw number of sides that we pass and rotate with the next side depending on how many side we have


#koch
def hilbert(order, size, direction):
    if order == 0:
        return right(direction * 90)
    hilbert(order - 1, size, -direction)
    forward(size)
    left(direction * 90)
    hilbert(order - 1, size, direction)
    forward(size)
    hilbert(order - 1, size, direction)
    left(direction * 90)
    forward(size)
    hilbert(order - 1, size, -direction)
    right(direction * 90)