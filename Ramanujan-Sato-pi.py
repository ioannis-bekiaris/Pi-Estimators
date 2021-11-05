import time
import math


def Ramanujan_Sato_pi(n):

    start_time = time.time()

    b = 0
    i = 2*math.sqrt(2)/math.pow(99, 2)
    for k in range(n):

        c = i*(26390*k+1103)/(math.pow(396, 4*k)) * \
            (math.factorial(4*k))/math.pow(math.factorial(k), 4)
        b += c
    pi = 1/b
    end_time = time.time()
    Dt = end_time - start_time
    print(pi)
    print("It took: "'%.60f' % Dt + " seconds!")
    print("%.60f" % ((math.pi - pi)))


Ramanujan_Sato_pi(10)
