

def time_to_second(time):
    h, m, s = map(int, time.split(':'))
    return h * 3600 + m * 60 + s


def second_to_time(second):
    h = str(second // 3600).zfill(2)
    second %= 3600
    m = str(second // 60).zfill(2)
    second %= 60
    s = str(second).zfill(2)
    return ':'.join([h, m, s])


def solution(play_time, adv_time, logs):
    answer = 0

    play_sec = time_to_second(play_time)
    adv_sec = time_to_second(adv_time)
    
    start_sec = []
    end_sec = []
    for log in logs:
        start_time, end_time = log.split('-')
        start_sec.append(time_to_second(start_time))
        end_sec.append(time_to_second(end_time))
    
    total_sec = [0 for _ in range(play_sec+1)]
    for idx in range(len(logs)):
        total_sec[start_sec[idx]] += 1
        total_sec[end_sec[idx]] -= 1
    
    for sec in range(1, play_sec+1):
        total_sec[sec] += total_sec[sec-1]
        
    for sec in range(1, play_sec+1):
        total_sec[sec] += total_sec[sec-1]
    
    answer = [0, total_sec[adv_sec] - total_sec[0]]
    for sec in range(adv_sec+1, play_sec+1):
        played = total_sec[sec] - total_sec[sec - adv_sec]
        answer = [sec - adv_sec + 1, played] if played > answer[1] else answer
    
    answer = second_to_time(answer[0])
    return answer