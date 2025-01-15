from fractals import *
from time import sleep
from turtle import mainloop


def main_loop():
    stay = True
    while stay:
        print("Which fractal would you like to draw ?")
        choice = int(input("1.Tree \n2.Snowflakes \n3.Hilbert curve"))
        if is_valid(choice):
            if choice == 1:
                speed(int(input("How fast would you like your tree to draw ?")))
                t_size = int(input("How large would you like your tree to draw ?"))
                lev = int(input("How many levels should it have"))
                ang = int(input("How incline would you like your tree to be?"))
                sleep(3)
                tree(t_size, lev, ang)
                mainloop()

            elif choice == 2:
                speed(int(input("How fast would you like your tree to draw ?")))
                s_sides = int(input("How many sides should it have ?"))
                s_len = int(input("How high should the length be ?"))
                sleep(3)
                create_snowflake(s_sides, s_len)
                mainloop()
            elif choice == 3:
                speed(0)
                hi_order = int(input("order?"))
                hi_size = int(input("The size?"))
                hi_direction = int(input("Direction ?"))
                sleep(3)
                hilbert(hi_order, hi_size, hi_direction)
                mainloop()
            stay_choice = input("Would you like to stay ?")

            if stay_choice == "no":
                return


def is_valid(_choice):
    while _choice < 1 or _choice > 3:
        _choice = int(input("The value should be between 1 and 3. Try again."))
    return True
