from typing import List


class Singleton:
    _instance: dict = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__new__(cls)

        return cls._instance[cls]


class SchoolHead(Singleton):
    def __init__(self, name: str, age: int, birthday: str):
        self.name = name
        self.age = age
        self.birthday = birthday


class Teacher:
    def __init__(self, name=None, age=None, birthday=None):
        self.name = name
        self.age = age
        self.birthday = birthday


class Child:
    def __init__(self, name=None, age=None, birthday=None):
        self.name = name
        self.age = age
        self.birthday = birthday


class School:
    def __init__(self, school_head: SchoolHead, teachers: List[Teacher], children: List[Child]):
        self.school_head = school_head
        self.teachers = teachers
        self.children = children


if __name__ == '__main__':
    kids = [Child(), Child(), Child(), Child(), Child(), Child(), Child(), Child(), Child()]
    teachers = [Teacher(), Teacher(), Teacher()]
    first_schoolhead = SchoolHead('Sam', 39, '01.01.1983')
    second_schoolhead = SchoolHead('Dan', 40, '01.01.1982')

    school = School(first_schoolhead, teachers, kids)
    school.school_head = second_schoolhead

    print(f'school.school_head: {id(school.school_head)}')
    print(f'first_schoolhead:   {id(first_schoolhead)}')
    print(f'second_schoolhead:  {id(second_schoolhead)}')
