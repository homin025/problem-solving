

def solution(brown, yellow):
    answer = []
    
    total = brown + yellow
    
    pairs = []
    for div in range(1, total+1):
        res = total // div
        
        if div * res == total:
            pairs.append(sorted([div, res], reverse=True))
    
    for pair in pairs:
        r, c = pair
        
        if (r-2) * (c-2) == yellow:
            answer.append(r)
            answer.append(c)
            break
    
    return answer