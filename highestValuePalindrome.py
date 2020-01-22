#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the highestValuePalindrome function below.
def highestValuePalindrome(s, n, k):
    changed = {}
    s = [int(i) for i in s.strip()]
    #
    for i in range(n // 2):
        j = -i - 1
        k -= (s[i] != s[j])
        changed[i] = (s[i] != s[j])
        s[i] = max(s[i], s[j])
        s[j] = s[i]
    #
    if k < 0:
        return('-1')
    #
    for i in range(n // 2):
        if (k >= 2) & (s[i] != 9):
            s[i] = 9
            s[-i-1] = 9
            k -= (2 - changed[i])
        elif (k >= 1) & (changed[i]) & (s[i] != 9):
            s[i] = 9
            s[-i-1] = 9
            k -= 1
    if (k > 0) & (n % 2) == 1:
        s[n // 2] = 9
    #
    return(''.join([str(i) for i in s]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
