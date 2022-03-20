from collections import defaultdict
from time import monotonic

import pytest

from src.group import group_random, get_friend_score, inc_friend_score, get_total_friend_score, \
    get_min_friend_score_team, group_random_v2


def test_배열을_넣으면_주어진_숫자만큼_묶어서_준다():
    people = [i for i in range(20)]
    teams = group_random(people, 4)
    for team in teams:
        assert len(team) == 4

    assert len(teams) == 5

    people = [i for i in range(18)]
    teams = group_random(people, 3)
    for team in teams:
        assert len(team) == 3

    assert len(teams) == 6


def test_배열을_넣으면_끝에거는_3개_준다():
    people = [i for i in range(19)]
    teams = group_random(people, 4)
    assert len(teams[-1]) == 3
    assert len(teams) == 5


def test_배열을_넣으면_뒤에_두개_3개_준다():
    people = [i for i in range(18)]
    teams = group_random(people, 4)
    assert len(teams[-1]) == 3
    assert len(teams[-2]) == 3
    assert len(teams) == 5


def test_멤버는_친밀도라는게_있다(test_db):
    member_a = "강민규"
    member_b = "김강산"

    inc_friend_score([member_a, member_b], db=test_db)
    assert get_friend_score(member_a, member_b, db=test_db) == 1


def test_랜덤런치_총_친밀도_계산(test_db):
    test_db.storage[(1, 2)] = 1
    test_db.storage[(1, 3)] = 1
    test_db.storage[(7, 8)] = 1

    teams = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    assert get_total_friend_score(teams, db=test_db) == 3


def test_랜덤런치_총_친밀도_최저(test_db):
    test_db.storage[(1, 2)] = 1
    test_db.storage[(1, 3)] = 1
    test_db.storage[(7, 8)] = 1

    teams_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    teams_b = [[1, 5, 6], [4, 2, 3], [7, 8, 9]]
    teams_c = [[1, 5, 6], [4, 8, 3], [7, 2, 9]]

    assert get_min_friend_score_team(test_db, teams_a, teams_b, teams_c) == teams_c


def test_랜덤런치_엔드투엔드(test_db):
    start =monotonic()
    test_db.storage[(1, 2)] = 1
    test_db.storage[(1, 3)] = 1
    test_db.storage[(7, 8)] = 1

    people = [i for i in range(100)]
    team = group_random_v2(people, 4, db=test_db)
    print(team)
    print(start - monotonic())


@pytest.fixture
def test_db():
    class HashMap:
        def __init__(self):
            self.storage = defaultdict(int)

        def get(self, a, b):
            tmp = sorted([a, b])
            return self.storage[tuple(tmp)]

        def increase(self, a, b):
            tmp = sorted([a, b])
            self.storage[tuple(tmp)] += 1

    return HashMap()
