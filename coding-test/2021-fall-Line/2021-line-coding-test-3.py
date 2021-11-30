from collections import defaultdict


def solution(jobs):
    answer = []

    work = [0, 0]
    time = 0

    pend = [[n, 0, 0] for n in range(101)]

    while jobs:
        # Initialization
        if work[0] == 0:
            # Request not arrived
            if time != jobs[0][0]:
                work[1] -= 1
                time += 1
            # Request arrived
            else:
                _, dur, num, _ = jobs.pop(0)
                work = [num, dur]
                answer.append(work[0])
                work[1] -= 1
                time += 1

        # Not idle
        elif work[1] != 0:
            # Request not arrived
            if time != jobs[0][0]:
                work[1] -= 1
                time += 1
            # Request arrived
            else:
                _, dur, num, imp = jobs.pop(0)
                # Same work
                if work[0] == num:
                    work[1] += dur
                # Diff work
                else:
                    pend[num][1] += imp
                    pend[num][2] += dur
                work[1] -= 1
                time += 1
        # Idle
        else:
            # Request not arrived
            if time != jobs[0][0]:
                # No pended works
                if sorted(pend, key=lambda elmt: (-elmt[1], elmt[0]))[0][1] == 0:
                    work[1] -= 1
                    time += 1
                # Pended works
                else:
                    num, _, dur = sorted(pend, key=lambda elmt: (-elmt[1], elmt[0]))[0]
                    pend[num] = [num, 0, 0]

                    work[0] = num
                    work[1] = dur
                    answer.append(work[0])

                    work[1] -= 1
                    time += 1
            # Request arrived
            else:
                _, dur, num, imp = jobs.pop(0)
                # Same work
                if work[0] == num:
                    work[1] += dur
                # Diff work
                else:
                    pend[num][1] += imp
                    pend[num][2] += dur

                    num, _, dur = sorted(pend, key=lambda elmt: (-elmt[1], elmt[0]))[0]
                    pend[num] = [num, 0, 0]

                    work[0] = num
                    work[1] = dur
                    answer.append(work[0])

                work[1] -= 1
                time += 1

    pend = sorted(pend, key=lambda elmt: (-elmt[1], elmt[0]))

    for num, imp, _ in pend:
        if imp != 0:
            answer.append(num)
        else:
            break

    return answer
