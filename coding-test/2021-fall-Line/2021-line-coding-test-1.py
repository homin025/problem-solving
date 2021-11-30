

def solution(student, k):
    answer = 0
    
    enrolled = []
    
    for idx, stu in enumerate(student):
        if stu == 1:
            enrolled.append(idx)
    
    for idx in range(len(enrolled)-k+1):
        left = enrolled[idx]
        if idx-1 >= 0:
            leftmore = enrolled[idx-1]+1
        else:
            leftmore = 0
        
        right = enrolled[idx+k-1]
        if idx+k < len(enrolled):
            rightmore = enrolled[idx+k]-1
        else:
            rightmore = len(student)-1
        
        answer += (left-leftmore+1) * (rightmore-right+1)
    
    return answer