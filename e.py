#!/bin/python3

import math
import os
import random
import re
import sys
def get_k_max_value(lst, k):
    if len(lst) == 0:
        return None
    pivot = random.choice(lst)
    lst1, lst2 = [], []
    for i in lst:
        if i > pivot:
            lst1.append(i)
        elif i < pivot:
            lst2.append(i)
    if k <= len(lst1):
        return get_k_max_value(lst1, k)
    elif k > len(lst) - len(lst2):
        return get_k_max_value(lst2, k - (len(lst) - len(lst2)))
    return pivot
def KthElements(k, n, a):
    ans=[]
    for _ in range(k,n+1):
        tmp=get_k_max_value(a[:_], len(a[:_])-k+1)
        ans.append(tmp)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    N = int(first_multiple_input[0])
    K = int(first_multiple_input[1])
    list_a = list(map(int, input().rstrip().split()))
    res = KthElements(K, N, list_a)
    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
