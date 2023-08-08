# bounce.py
#
# Exercise 1.5

height = 100
bounce_nr = 1
regression = 0.6

while bounce_nr <= 10:
    height *= regression
    print("Bounce:", bounce_nr, "current height: ", round(height, 4))
    bounce_nr += 1
