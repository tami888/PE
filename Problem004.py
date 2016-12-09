def palindrome():
    num = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            res = i * j
            num.append(res)
    num = map(str, num)
    num = filter(lambda x: x == x[::-1], num)
    print max(map(int, num))

if __name__ == '__main__':
    palindrome()



