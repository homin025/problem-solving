import sys

input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())

    numbers = list(range(N + 1))
    is_prime = [False, False] + [True] * (N - 1)

    for idx, number in enumerate(numbers):
        if is_prime[idx]:
            for offset in range(2, N // number + 1):
                is_prime[idx * offset] = False

    prime_numbers = [number for idx, number in enumerate(numbers) if is_prime[idx]]

    count = 0
    for idx in range(len(prime_numbers)):
        prime_sum = 0

        while prime_sum < N and idx < len(prime_numbers):
            prime_sum += prime_numbers[idx]
            idx += 1

            if prime_sum == N:
                count += 1
                break

    print(count)
