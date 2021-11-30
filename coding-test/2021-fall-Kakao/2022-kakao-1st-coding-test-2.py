import math
from collections import defaultdict


def check_prime_number(dp, n):
    if n in dp:
        return dp[n]
    
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            dp[n] = False
            return False
    dp[n] = True
    return True


def solution(n, k):
    answer = 0

    string = ""
    while n > 0:
        string += str(n % k)
        n = n // k
    string = string[::-1]

    numbers = string.split("0")
    numbers = list(map(int, [number for number in numbers if number != '']))
    
    dp = defaultdict()
    dp[0] = False
    dp[1] = False
    print(numbers)               
    for number in numbers:
        if check_prime_number(dp, number):
            answer += 1
    
    return answer