

def solution(phone_book):
    answer = True
    
    phone_book = sorted(phone_book)
    
    prev = ''
    for phone in phone_book:
        if not prev:
            prev = phone
            continue
        
        curr = phone
        if curr.startswith(prev):
            answer = False
            break
        prev = curr
        
    return answer