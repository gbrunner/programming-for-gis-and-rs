import random
def randomList(a):
    b = []
    for i in range(len(a)):
        element = random.choice(a)
        a.remove(element)
        b.append(element)
    return b

students = ['Dennis Campbell',
            'Govind Chadalawada',
            'Carlissa Cole',
            'Allison Davis',
            'Emily Deeba',
            'John Hamill',
            'Grace Kenney',
            'Jiulin Li',
            'Mason Maimaitijiang',
            'Bethany Marshall',
            'Will McWay',
            'Amy Morris',
            'David Nixon',
            'Kyle Peterson',
            'Nicole Schaeg',
            'Steven Spiegel',
            'Jennifer Thomas',
            'Justin Vilbig']

print "There will be " + str(len(students)) + " presentations."
print "Students will present in the following order:"
print randomList(students)