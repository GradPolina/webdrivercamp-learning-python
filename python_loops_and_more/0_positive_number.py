#!/usr/bin/python3
import random
random_num = random.randint(-10, 10)
if random_num < 0:
    print (random_num, "is negarive")
elif random_num ==0:
    print (random_num, "is xero")
else:
    print (random_num, "is positive")
