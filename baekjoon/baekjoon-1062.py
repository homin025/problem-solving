import sys
from itertools import combinations

input = sys.stdin.readline


if __name__ == "__main__":
    N, K = map(int, input().split())

    if K < 5:
        print(0)
    elif K == 26:
        print(N)
    else:
        words = [0] * N
        for idx in range(N):
            for char in str(input())[4:-4]:
                words[idx] |= 1 << ord(char) - ord('a')

        need = 0
        for char in ['a', 'n', 't', 'i', 'c']:
            need |= 1 << ord(char) - ord('a')

        alphabet = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                    'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']

        answer = 0

        for comb in combinations(alphabet, K - 5):
            learn = need
            for char in comb:
                learn |= 1 << ord(char) - ord('a')

            count = 0
            for word in words:
                if learn | word == learn:
                    count += 1

            answer = max(answer, count)

        print(answer)
