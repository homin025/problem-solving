from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    
    reports = defaultdict(list)
    nums = defaultdict(int)
    
    report = list(set(report))
    for r in report:
        fr, to = r.split(" ")
        reports[fr].append(to)
        nums[to] += 1

    suspended = set()
    for name in list(nums):
        if nums[name] >= k:
            suspended.add(name)
    
    mailed = defaultdict(int)
    for fr in list(reports):
        for to in reports[fr]:
            if to in suspended:
                mailed[fr] += 1

    for name in id_list:
        answer.append(mailed[name])
    return answer
