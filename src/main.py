from collections import defaultdict
from itertools import combinations
from random import shuffle
from typing import List


class TestDB:
    def __init__(self):
        self.storage = defaultdict(int)

    def get(self, a, b):
        tmp = sorted([a, b])
        return self.storage[tuple(tmp)]

    def increase(self, a, b):
        tmp = sorted([a, b])
        self.storage[tuple(tmp)] += 1


def inc_friend_score(friends, *, db):
    combies = combinations(friends, 2)
    for combie in combies:
        assert len(combie) == 2
        db.increase(*combie)


def get_friend_score(person_a, person_b, *, db):
    return db.get(person_a, person_b)


def get_min_friend_score_team(db, *teams_list) -> List:
    min_teams = (float("inf"), [])
    for teams in teams_list:
        score = (get_total_friend_score(teams, db=db), teams)
        min_teams = min(score, min_teams, key=lambda x: x[0])

    return min_teams[1]


def get_total_friend_score(teams, *, db):
    sum = 0
    for team in teams:
        sum += _get_total_friend_score(team, db=db)
    return sum


def _get_total_friend_score(team, *, db):
    sum = 0
    for combie in combinations(team, 2):
        sum += get_friend_score(*combie, db=db)
    return sum


def group_random(people: List, member_cnt) -> List:
    people_shuffled = shuffle_list(people)
    return group_list(people_shuffled, member_cnt)


def group_random_v2(people: List, member_cnt, *, db) -> List:
    people_shuffled_list = [group_random(people, member_cnt) for _ in range(100)]
    return get_min_friend_score_team(db, *people_shuffled_list)


def shuffle_list(people) -> List:
    people_shuffled = [*people]
    shuffle(people_shuffled)
    return people_shuffled


def group_list(people: List, member_cnt) -> List:
    total_people_cnt = len(people)
    orphan_cnt = (member_cnt - (total_people_cnt % member_cnt)) % member_cnt

    seperation = total_people_cnt - ((member_cnt-1) * orphan_cnt)

    team_a = _group_random(people[:seperation], member_cnt)
    team_b = _group_random(people[seperation:], member_cnt-1)

    return [*team_a, *team_b]


def _group_random(people: List, member_cnt) -> List:
    teams = [[] for _ in range(round(len(people)/member_cnt))]

    for i in range(len(people)):
        teams[i // member_cnt].append(people[i])

    return teams
