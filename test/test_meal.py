from datetime import datetime

from src.meal import create_meal, create_member, assign_member_to_meal, assign_members_to_meal


def test_식사를_제안하기():
    meal = create_meal("강남", datetime(2022,1,1))
    member1 = create_member("김강산")
    member2 = create_member("강민규")
    assign_member_to_meal(meal, member1)

    assert meal.has(member1) is True
    assert meal.has(member2) is False

def test_팀_확정하기():
    meal = create_meal("제주", datetime(2022,1,1))
    member1 = create_member("a")
    member2 = create_member("b")
    member3 = create_member("c")
    member4 = create_member("d")

    members = [member1, member2, member3, member4]
    assign_members_to_meal(meal, members)

    meal.group_random(2)

    assert len(meal.teams) is 2

def test_동명이인():
    meal = create_meal("강남", datetime(2022,1,1))
    member1 = create_member("김강산")
    member2 = create_member("김강산")
    assign_member_to_meal(meal, member1)

    assert meal.has(member1) is True
    assert meal.has(member2) is False

# def test_추첨할meal들찾기():
# db 연결 후 테스트 할 것

