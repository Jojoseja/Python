#This is a comment 

import random

max_number = 10
mylist = [10,20,30,40,50,60,70,80,90,100]
number = "%09d" % random.randint(0,999999999)
def rc(a):
    return random.choice(a)

with open("output.txt", "w") as archivo:
    i=0
    while (i < max_number):
        archivo.write(str(rc(mylist)) + "\n") 
        i = i+1
