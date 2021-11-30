from itertools import permutations


def solution(numbers):
    answer = 0
    
    numbers = list(numbers)
    
    check = set()
    for n in range(1, len(numbers) + 1):
        for perms in list(permutations(numbers, n)):
            number = int(''.join(perms))
            flag = True
            
            if number < 2 or number in check:
                continue
            
            check.add(number)
            
            for div in range(2, number // 2 + 1):
                if number % div == 0:
                    flag = False
                    break
            
            if flag:
                answer += 1
    
    return answer