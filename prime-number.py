# Write a Python program to check if a number is prime.

# method 1
def p1(number):
    is_prime = True
    if number == 1:
        print("The Number is not Prime.",number)
        return
    for i in range (2 ,number):
        if number%i == 0:
            print("The Number is not Prime.",number)
            is_prime = False
            break
    if is_prime:
        print("The Number is Prime.",number)   

# method 2
def p2(number):
    is_prime = True
    if number == 1:
        print("The Number is not Prime.",number)
    for i in range (2 ,(number//2)):
        if number%i == 0:
            print("The Number is not Prime.")
            is_prime = False
            break
    if is_prime:
        print("The Number is Prime.")   

# method 3
from math import sqrt

def p3(number):
    is_prime = True
    if number ==1:
        print("The Number is not Prime.",number)
    for i in range (2 ,int(sqrt(number))):
        if number%i == 0:
            print("The Number is not Prime.")
            is_prime = False
            break
    if is_prime:
        print("The Number is Prime.")        


# To check which method take more time
from time import time

t = 100000
start1 = time()
for i in range(1 , t ):
    p1(i)
end1 = time()

start2 = time()
for i in range(1 , t ):
    p2(i)
end2 = time()

start3 = time()
for i in range(1 , t ):
    p3(i)
end3 = time()

print("time of p1",end1-start1)
print("time of p2",end2-start2)
print("time of p3",end3-start3)
