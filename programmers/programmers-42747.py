

def solution(citations):
    answer = 0
    
    citations = sorted(citations, reverse=True)
    
    for n in reversed(range(1, len(citations)+1)):
        count = n
        for citation in citations:
            if citation >= n:
                count -= 1
                
                if count == 0:
                    answer = n
                    return answer
            else:
                break
                
    return answer