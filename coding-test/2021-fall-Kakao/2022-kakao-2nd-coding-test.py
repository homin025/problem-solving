import json
import requests
import random

BASE_URL = ''
X_AUTH_TOKEN = ''


def start_api(problem):
    url = BASE_URL + "/start"
    headers = {'X-Auth-Token': X_AUTH_TOKEN, 'Content-Type': 'application/json'}
    params = {'problem': problem}
    return requests.post(url=url, headers=headers, data=json.dumps(params)).json()


def waiting_line_api(auth_key):
    url = BASE_URL + "/waiting_line"
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    return requests.get(url=url, headers=headers).json()


def game_result_api(auth_key):
    url = BASE_URL + "/game_result"
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    return requests.get(url=url, headers=headers).json()


def user_info_api(auth_key):
    url = BASE_URL + "/user_info"
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    return requests.get(url=url, headers=headers).json()


def match_api(auth_key, pairs):
    url = BASE_URL + "/match"
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    params = {'pairs': pairs}
    return requests.put(url=url, headers=headers, data=json.dumps(params)).json()


def change_grade_api(auth_key, commands):
    url = BASE_URL + "/change_grade"
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    params = {'commands': commands}
    return requests.put(url=url, headers=headers, data=json.dumps(params)).json()


def score_api(auth_key):
    url = BASE_URL + "/score"
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    return requests.get(url=url, headers=headers).json()


class User:
    def __init__(self, _id):
        self.id = _id
        self.power = 40000

        self.num_matches = 0
        self.num_matches_vs_weak = 0
        self.num_loses_vs_weak = 0
        self.is_abuser = False

    def match(self, users, waiting_line):
        min_user = None
        min_power = 100001

        for user_id, _ in waiting_line:
            if self.id == user_id:
                continue

            if not self.is_abuser:
                comp_user = users[user_id - 1]
                diff = abs(self.power - comp_user.power)

                if min_power > diff:
                    min_power = diff
                    min_user = comp_user

            else:
                comp_user = users[user_id - 1]
                diff = comp_user.power - self.power

                if comp_user.is_abuser:
                    continue

                if 0 < diff < min_power:
                    min_power = diff
                    min_user = comp_user

        return min_user

    def check(self):
        if self.num_matches_vs_weak >= 10:
            lose_rate = int(self.num_loses_vs_weak / self.num_matches_vs_weak * 100)
            if lose_rate >= 80:
                self.is_abuser = True


def remove_user_by_id(waiting_line, target_id):
    for user_id, user_time in waiting_line:
        if user_id == target_id:
            waiting_line.remove([user_id, user_time])
            break


def calc_weight(taken):
    delta = (40 - taken + random.randint(-5, 5))
    if delta < 0:
        delta = 0
    if delta > 35:
        delta = 35
    return int(delta * 99000 / 35)


if __name__ == '__main__':
    problem = 2
    num_users = 30 if problem == 1 else 900
    users = [User(_id) for _id in range(1, num_users + 1)]

    start_response = start_api(problem=problem)

    auth_key = start_response['auth_key']
    time = 0

    while time <= 595:
        print("***", time, "***")
        waiting_line = []

        waiting_line_response = waiting_line_api(auth_key=auth_key)
        for user in waiting_line_response['waiting_line']:
            user_id = user['id']
            user_from = user['from']
            waiting_line.append([user_id, time - user_from])

        game_result_response = game_result_api(auth_key=auth_key)
        for game_result in game_result_response['game_result']:
            winner = users[game_result['win'] - 1]
            loser = users[game_result['lose'] - 1]
            taken = game_result['taken']

            if problem == 2:
                winner.num_matches += 1
                loser.num_matches += 1

                if loser.power > winner.power:
                    loser.num_matches_vs_weak += 1
                    loser.num_loses_vs_weak += 1
                elif loser.power < winner.power:
                    winner.num_matches_vs_weak += 1

                if loser.num_matches >= 20:
                    loser.check()

            # 계산 가중치 및 실제 차이의 영향을 75% 반영
            match_weight = calc_weight(taken=taken) * 0.75
            diff = abs(winner.power - loser.power) * 0.75

            if match_weight != 0:
                applied_weight = int((match_weight - diff) * 0.5)
            else:
                applied_weight = 0

            winner.power += applied_weight
            if int(winner.power) >= 100000:
                winner.power = 99999
            elif winner.power < 0:
                winner.power = 0

            loser.power -= applied_weight
            if int(loser.power) < 1000:
                loser.power = 1000
            elif loser.power >= 100000:
                loser.power = 99999

        if time == 595:
            commands = []

            # 중복 없이 실력대로 줄 세우기
            # ranks = []
            # for user in users:
            #     ranks.append([user.id, user.power])
            # ranks = sorted(ranks, key=lambda elmt: elmt[1])
            # for idx, rank in enumerate(ranks):
            #     commands.append({"id": rank[0], "grade": idx})

            # 중복 있이 실력대로 줄 세우기
            for user in users:
                commands.append({"id": user.id, "grade": int(user.power / 10)})
            change_grade_api(auth_key=auth_key, commands=commands)

        pairs = []
        for user_id, user_time in waiting_line:
            curr_user = users[user_id - 1]
            match_user = curr_user.match(users=users, waiting_line=waiting_line)

            if not match_user:
                continue

            # 실력 차이가 많이 날 경우, 1번 더 대기
            if abs(curr_user.power - match_user.power) > 10000:
                if user_time >= 1:
                    remove_user_by_id(waiting_line=waiting_line, target_id=curr_user.id)
                    remove_user_by_id(waiting_line=waiting_line, target_id=match_user.id)
                    pairs.append([curr_user.id, match_user.id])
                else:
                    continue

            remove_user_by_id(waiting_line=waiting_line, target_id=curr_user.id)
            remove_user_by_id(waiting_line=waiting_line, target_id=match_user.id)
            pairs.append([curr_user.id, match_user.id])
        match_response = match_api(auth_key=auth_key, pairs=pairs)

        time += 1

    score_response = score_api(auth_key=auth_key)
    print(score_response)
