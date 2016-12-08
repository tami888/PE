import sys
import numpy as np

list1 = []
num = 600851475143
i = 2
while i * i <= num:
    while num % i == 0:
        num /= i
        list1.append(i)
    i += 1
if num > 1:
    list1.append(num)
print list1