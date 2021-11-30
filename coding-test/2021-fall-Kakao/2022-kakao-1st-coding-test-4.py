

def calc_score(rian, apeach):
    rian_score = 0
    apeach_score = 0
    
    for i in range(10):
        rian_shot = int(rian[i])
        apeach_shot = int(apeach[i])
        if rian_shot > apeach_shot:
            rian_score += 10 - i
        elif rian_shot < apeach_shot:
            apeach_score += 10 - i
        elif rian_shot != 0:
            apeach_score += 10 - i
    
    return rian_score - apeach_score


def dfs(shots, info, diff, curr_shot, num_shot, is_shot):
    global answers, score

    if num_shot == 0: 
        gap = calc_score(shots, info)
        if gap > score:
            score = gap
            answers = [shots]
        elif score != 0 and gap == score:
            answers.append(shots)
        return
    elif curr_shot == 10 and num_shot != 0:
        shots = shots[:10] + str(int(shots[10]) + num_shot)
        gap = calc_score(shots, info)
        if gap > score:
            score = gap
            answers = [shots]
        elif gap == score:
            answers.append(shots)
        return

    if is_shot and num_shot - diff[curr_shot] >= 0:
        shots = shots[:curr_shot] + str(int(shots[curr_shot]) + diff[curr_shot]) + shots[curr_shot+1:]
        
        for is_shot in range(2):
            dfs(shots, info, diff, curr_shot+1, num_shot-diff[curr_shot], is_shot)
    else:
        for is_shot in range(2):
            dfs(shots, info, diff, curr_shot+1, num_shot, is_shot)


def solution(n, info):
    global answers, score
    answers = []
    score = 0
    
    diff = [i+1 for i in info]

    shots = "0" * 11
    for is_shot in range(2):
        dfs(shots, info, diff, 0, n, is_shot)

    if len(answers) == 0:
        return [-1]
    elif len(answers) == 1:
        return list(map(int, list(sorted(answers)[0])))
    else:
        reversed = []
        for answer in answers:
            reversed.append(answer[::-1])
        reversed = sorted(reversed, reverse=True)
        return list(map(int, reversed[0][::-1]))
