

def solution(answers):
    N = len(answers)
    
    user_1 = [1, 2, 3, 4, 5] * (N // 5 + 1)
    user_2 = [2, 1, 2, 3, 2, 4, 2, 5] * (N // 8 + 1)
    user_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (N // 10 + 1)
    scores = [0, 0, 0]
    for idx in range(N):
        answer = answers[idx]
        
        if answer == user_1[idx]:
            scores[0] += 1
        
        if answer == user_2[idx]:
            scores[1] += 1
            
        if answer == user_3[idx]:
            scores[2] += 1
    
    answer = []
    for idx in range(3):
        if scores[idx] == max(scores):
            answer.append(idx+1)
            
    return answer