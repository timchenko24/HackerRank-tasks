import math


#https://www.hackerrank.com/challenges/diagonal-difference/problem
def diagonalDifference(arr):
    i = 0
    j = len(arr[0]) - 1
    sum1 = 0
    sum2 = 0
    for _, row in enumerate(arr):
        sum1 += row[i]
        sum2 += row[j]
        i += 1
        j -= 1
    return abs(sum1 - sum2)


#https://www.hackerrank.com/challenges/plus-minus/problem
def plusMinus(arr):
    num_of_values = len(arr)
    pos = 0
    neg = 0
    zero = 0
    for val in arr:
        if val > 0:
            pos += 1
        elif val < 0:
            neg += 1
        else:
            zero += 1

    frac_pos = pos / num_of_values
    frac_neg = neg / num_of_values
    frac_zero = zero / num_of_values

    print("{0:.6f}\n{1:.6f}\n{2:.6f}".format(frac_pos, frac_neg, frac_zero))


#https://www.hackerrank.com/challenges/staircase/problem
def staircase(n):
    for i in range(1, n+1):
        print(' ' * (n - i) + '#' * i)


#https://www.hackerrank.com/challenges/mini-max-sum/problem
def miniMaxSum(arr):
    arr_len = len(arr)
    min_sum = sum(arr)
    max_sum = 0
    for i in range(arr_len):
        cur_sum = sum(arr) - arr[i]
        if min_sum > cur_sum:
            min_sum = cur_sum
        if max_sum < cur_sum:
            max_sum = cur_sum
        else:
            continue

    print("{0} {1}".format(min_sum, max_sum))


#https://www.hackerrank.com/challenges/birthday-cake-candles/problem
def birthdayCakeCandles(ar):
    max_candle_hight = max(ar)
    counter = 0

    for _, val in enumerate(ar):
        if val == max_candle_hight:
            counter += 1

    return counter