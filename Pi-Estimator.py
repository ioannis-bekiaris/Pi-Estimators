import random
import math
import time


def geom_pi(n):

    begin_time = time.time()
    inner_points = 0
    outter_points = 0

    for i in range(n):

        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        dist = math.sqrt(x**2 + y**2)

        if dist < 1:
            inner_points += 1
        outter_points += 1
    kpi = inner_points/outter_points
    pi = 4*kpi

    print(pi)
    end_time = time.time()
    Dt = end_time - begin_time
    print("It took: " + str(Dt) + " seconds")


geom_pi(10000000)
