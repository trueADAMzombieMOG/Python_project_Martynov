import random
A = [random.randint(-10, 10) for i in range(10)]
print(A)
B =[]
for i in A:
    if i < 0 and i%5==0:
        B+=[i]
print(len(B),B)