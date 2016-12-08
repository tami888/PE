num1 = 1
num2 = 2
tmp = 0

sum1 = 2
while tmp <= 4000000:
    tmp = num1 + num2
    if tmp % 2 == 0:
        sum1 = sum1 + tmp

    num1 = num2
    num2 = tmp
print sum1