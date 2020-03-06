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


#https://www.hackerrank.com/challenges/time-conversion/problem
def timeConversion(s):
    splitted_time = s.split(':')
    new_time = ""
    hours = ''
    if splitted_time[2][2] == 'A':
        if splitted_time[0] == '12':
            hours = '00'
        else:
            hours = splitted_time[0]
        new_time = "{0}:{1}:{2}".format(hours, splitted_time[1], splitted_time[2].replace('AM', ''))
    else:
        if splitted_time[0] == '12':
            hours = '12'
        else:
            hours = int(splitted_time[0])+12
        new_time = "{0}:{1}:{2}".format(hours, splitted_time[1], splitted_time[2].replace('PM', ''))

    return new_time


#https://www.hackerrank.com/challenges/grading/problem
def gradingStudents(grades):
    new_grades = []

    for _, val in enumerate(grades):
        if val < 38:
            cur_grade = val
        elif val % 5 >= 3:
            cur_grade = 5 * round(val / 5)
        else:
            cur_grade = val

        new_grades.append(cur_grade)

    return new_grades


#https://www.hackerrank.com/challenges/apple-and-orange/problem
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_counter = 0
    oranges_counter = 0

    for _, val in enumerate(apples):
        g = a + val
        if g >= s and g <= t:
            apples_counter += 1

    for _, val in enumerate(oranges):
        g = b + val
        if g >= s and g <= t:
            oranges_counter += 1

    print("{0}\n{1}".format(apples_counter, oranges_counter))


#https://www.hackerrank.com/challenges/kangaroo/problem
def kangaroo(x1, v1, x2, v2):
    if v2 > v1 or v1 == v2:
        return "NO";

    return "YES" if (x2 - x1) % (v1 - v2) == 0 else "NO"



#https://www.hackerrank.com/challenges/between-two-sets/problem
def getTotalX(a, b):
    max_a = max(a)
    min_b = min(b)
    a_factor = list()
    result = list()

    for i in range(max_a, min_b + 1):
        if all(i % x == 0 for x in a):
            a_factor.append(i)

    for x in a_factor:
        if all(elem % x == 0 for elem in b):
            result.append(x)

    return len(result)


#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
def breakingRecords(scores):
    game_num = len(scores)
    min_score = scores[0]
    max_score = scores[0]
    highest_score = 0
    lowest_score = 0

    for i in range(game_num):
        if scores[i] > min_score:
            highest_score += 1
            min_score = scores[i]
        elif scores[i] < max_score:
            lowest_score += 1
            max_score = scores[i]

    return highest_score, lowest_score

if __name__ == '__main__':
    scores = [3, 4, 21, 36, 10,28, 35, 5, 24, 42]

    h, l = breakingRecords(scores)

    print("{0} {1}".format(h, l))
















