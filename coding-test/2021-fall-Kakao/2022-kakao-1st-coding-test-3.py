from collections import defaultdict


def calc_minutes(date):
    h, m = map(int, date.split(":"))
    return h*60+m+1


def solution(fees, records):
    answer = []

    duration = defaultdict(int)
    parking = defaultdict(int)
    for record in records:
        date, num, _ = record.split(" ")

        if parking[num] == 0:
            parking[num] = calc_minutes(date)
        else:
            duration[num] += calc_minutes(date) - parking[num]
            parking[num] = 0
        
    for num in parking:
        if parking[num] != 0:
            duration[num] += calc_minutes("23:59") - parking[num]
    print(parking)
    print(duration)
            
    min_time = fees[0]
    min_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]
    payment = []
    
    for num in duration:
        fee = 0
        if duration[num] <= min_time:
            fee = min_fee
        else:
            if (duration[num] - min_time) % unit_time == 0:
                fee = min_fee + ((duration[num] - min_time) // unit_time) * unit_fee
            else:
                fee = min_fee + ((duration[num] - min_time) // unit_time + 1) * unit_fee
        payment.append([num, fee])
    
    answer = [fee for num, fee in sorted(payment)]
    return answer
