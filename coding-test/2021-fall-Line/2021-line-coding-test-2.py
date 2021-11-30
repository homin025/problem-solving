from collections import defaultdict


def solution(research, n, k):
    answer = ''
    
    days = defaultdict(dict)
    keys = set()
    
    for day, keywords in enumerate(research):
        for keyword in set(keywords):
            days[day][keyword] = keywords.count(keyword)
            keys.add(keyword)
    
    answers = defaultdict(int)
    for key in keys:
        for day in range(len(days)-n+1):
            flag = True
            
            sums = 0
            for check in range(day, day+n):
                if key not in days[check]:
                    flag = False
                    break
                if days[check][key] < k:
                    flag = False
                    break
                sums += days[check][key]
            if sums < 2*n*k:
                flag = False
                continue
            
            if flag:
                answers[key] += 1
    
    nums = []
    for key in list(answers.keys()):
        nums.append([key, answers[key]])
    
    nums = sorted(nums, key=lambda elmt: (-elmt[1], elmt[0]))
    answer = "None" if not nums else nums[0][0]
    
    return answer