prime = []
count = 600851475143
i = 2
while 4 <= count:
    while count % i == 0:
        count /= i
        prime.append(i)
    i += 1
if count > 1:
    prime.append(count)
print prime
