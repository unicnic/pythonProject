class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __avg_grade(self):
        sum_grade = 0
        count_grade = 0
        if len(self.grades) != 0:
            for i, j in self.grades.items():
                sum_grade += sum(j)
                count_grade += len(j)
            avg_grade = round(sum_grade / count_grade, 1)
        else:
            avg_grade = 0
        return avg_grade
    def __str__(self):
        str_courses_in_progress = ', '.join(self.courses_in_progress)
        str_finished_courses = ', '.join(self.finished_courses)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.__avg_grade()}\nКурсы в процессе изучения: {str_courses_in_progress}\nЗавершенные курсы: {str_finished_courses}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f'{other} не студент')
            return
        return self.__avg_grade() < other.__avg_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses = []
        self.grades = {}

    def __avg_grade(self):
        sum_grade = 0
        count_grade = 0
        if len(self.grades) != 0:
            for i, j in self.grades.items():
                sum_grade += sum(j)
                count_grade += len(j)
            avg_grade = round(sum_grade / count_grade, 1)
        else:
            avg_grade = 0
        return avg_grade

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__avg_grade()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f'{other} не лектор')
            return
        return self.__avg_grade() < other.__avg_grade()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res



