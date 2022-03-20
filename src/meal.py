import uuid

from src import group

class Meal:
    def has(self, target):
        for member in self.members:
            if member.pk == target.pk:
                return True
        return False

    def group_random(self, count):
        self.teams = group.group_random_v2(self.members, count, db=self.db)

    def __init__(self, db=None):
        self.members = []
        self.teams = []
        self.db = group.TestDB2() if db is None else db

class Member:
    def __init__(self, name):
        self.name = name
        self.pk = get_pk()

def get_pk():
    return uuid.uuid1()


def create_meal(location, date):
    return Meal()

def create_member(name):
    return Member(name)

def assign_member_to_meal(meal, member):
    meal.members.append(member)

def assign_members_to_meal(meal, members):
    meal.members.extend(members)