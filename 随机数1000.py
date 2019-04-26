import random
ran= [random.randint(0,100) for i in range(1000)]

rans = set(ran)
for i in rans:
    print(i,': ',ran.count(i))