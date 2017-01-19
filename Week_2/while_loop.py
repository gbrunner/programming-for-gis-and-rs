import random

i = 1
while i <= 10:
    random_val = random.randint(1, 2)
    if random_val == 1:
        print("Trial " + str(i) + ": " + str(random_val) + " is Odd")
    else:
        print("Trial " + str(i) + ": " + str(random_val) + " is Even")
    i += 1