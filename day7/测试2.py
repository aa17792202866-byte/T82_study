import random

a = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8"]

random.shuffle(a)

dict1 = {
    1: a[0:3],
    2: a[3:6],
    3: a[6:8]
}

print(dict1)