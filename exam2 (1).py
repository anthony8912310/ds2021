#!/bin/python3

import math
import os
import random
import re
import sys
from heapq import heapify

def WinScore(HaruUraraAbility, TokaiTeioAbility):
    heapify(HaruUraraAbility)
    heapify(TokaiTeioAbility)
    score = 0
    while HaruUraraAbility and TokaiTeioAbility:
        if max(HaruUraraAbility) > max(TokaiTeioAbility):
            HaruUraraAbility.remove(max(HaruUraraAbility))
            score += len(TokaiTeioAbility)
        else:
            TokaiTeioAbility.remove(max(TokaiTeioAbility))
    return score

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    dataLength = int(input().strip())

    HaruUraraAbility = list(map(int, input().rstrip().split()))

    TokaiTeioAbility = list(map(int, input().rstrip().split()))

    res = WinScore(HaruUraraAbility, TokaiTeioAbility)

    fptr.write(str(res) + '\n')

    fptr.close()
