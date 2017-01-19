data = [1,2,3,4,5,6,7,8,9,10]
for val in data:
    if val % 2 == 0:
        print(val,"No remainder") # the % sign is the modulus operator and tests for a remainder
    elif val % 3 == 2:
        print(val,"Remainder of Two")
    else:
        print("Final Case")

