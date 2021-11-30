

def solution(participant, completion):
    answer = ''
    
    names = {}
    for name in participant:
        if name not in names:
            names[name] = 1
        else:
            names[name] += 1
            
    for name in completion:
        names[name] -= 1
        if names[name] == 0:
            names.pop(name)
            
    answer = list(names.keys())[0]
    return answer