import random as rand
import math as mt

n= 100000  #no.of trails
j= 0
for i in range(n):
    x=mt.pi*rand.random()
    y=rand.random()
    fx=mt.sin(x)
    if y<=fx:
        j=j+1
ifx=mt.pi*j/n
print(ifx)        
    