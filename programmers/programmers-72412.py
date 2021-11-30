from itertools import combinations


def solution(infos, queries):
    answer = []
    
    users = {}
    for info in infos:
        info = info.split(' ')
        score = int(info[-1])
        info = info[:-1]
        
        for num in range(5):
            for user in list(combinations(info, num)):
                user = ''.join(user) + '-' * (4 - num)
                
                if user not in users:
                    users[user] = [score]
                else:
                    users[user].append(score)
    
    for user in users:
        users[user].sort()
        
    for query in queries:
        query = query.split(' ')
        score = int(query[-1])
        
        query = ''.join(query[:-1])
        query = query.replace('and', '')
        query = query.replace('-', '') + '-' * query.count('-')
        
        if query in users:
            scores = users[query]
            
            start = 0
            end = len(scores)
            while start < end:
                mid = (start + end) // 2
                if scores[mid] >= score:
                    end = mid
                else:
                    start = mid + 1
            
            answer.append(len(scores) - start)
        else:
            answer.append(0)
    
    return answer