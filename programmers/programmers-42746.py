import re


def solution(numbers):
    answer = ''
    
    numbers = sorted(list(map(str, numbers)), key=lambda elmt: elmt * 3, reverse=True)
    
    answer = ''.join(numbers)

    if re.match('[0]+', answer):
        answer = '0'
    
    return answer