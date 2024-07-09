# bounce.py
#
# Exercise 1.5
# A rubber ball is dropped from a height of 100 meters and each time it hits the ground, it bounces back up to 3/5 the height it fell. Write a program bounce.py that prints a table
# showing the height of the first 10 bounces.

current_height = 100
bounce = 3 / 5

number_of_bounces = 0
while number_of_bounces <= 10:
    print(
        f"Current height is {round(current_height, 4)}, bounce number is {number_of_bounces}"
    )
    current_height = current_height * bounce
    number_of_bounces += 1
