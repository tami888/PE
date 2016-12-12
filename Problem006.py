# -*- coding: utf-8 -*-


def squared(n):
    num1 = 0
    num2 = 0
    for i in range(n):
        tmp = i+1
        num1 += tmp * tmp       # 二乗の和をnum1に代入
        num2 += tmp             # 和の二乗を求めるためnum2に代入しておく
    return num2 ** 2 - num1     # 和の二乗と二乗の和の差を求める

if __name__ == '__main__':
    print squared(100)
