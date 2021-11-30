import math
from collections import defaultdict


def get_min_prime_number(n):
    visit = [True] * (n + 1)

    for i in range(2, int(math.sqrt(n)) + 1):
        if visit[i]:
            for j in range(2, n // i):
                visit[i * j] = False

    for i in range(2, n + 1):
        if visit[i] and n % i == 0:
            return i


def solution(n):
    answer = []

    num = n
    arr = [i + 1 for i in range(n)]

    while num > 1:
        mpn = get_min_prime_number(num)

        swap = defaultdict(list)
        for i in range(n // num):
            for j in range(num * i, num * (i + 1)):
                swap[i * mpn + j % mpn].append(arr[j])

        arr = []
        for elmt in list(swap.values()):
            arr += elmt

        num = num // mpn

    answer = arr
    return answer
