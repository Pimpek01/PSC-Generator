import os
import random
import time

def losowanie():
    for i in range(1, 17):
        if i == 1:
            print(0, end='')
        else:
             print(random.randint(0, 9), end='')
        if i % 4 == 0:
            print(' ', end='')

os.system("pause")
losowanie()
time.sleep(1)
os.system("pause")
