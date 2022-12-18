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


def student_avg_grade_course(student_list, course):
    sum_grade = 0
    count_grade = 0
    for i in student_list:
        sum_grade += sum(i.grades[course])
        count_grade += len(i.grades[course])
    student_avg_grade_course = round(sum_grade / count_grade, 1)
    return student_avg_grade_course

def lecturer_avg_grade_course(lecturer_list, course):
    sum_grade = 0
    count_grade = 0
    for i in lecturer_list:
        sum_grade += sum(i.grades[course])
        count_grade += len(i.grades[course])
    lecturer_avg_grade_course = round(sum_grade / count_grade, 1)
    return lecturer_avg_grade_course


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Python']
best_student.finished_courses += ['Git']

bad_student = Student('Вася', 'Пупкин', 'm')
bad_student.courses_in_progress += ['Git']
bad_student.courses_in_progress += ['Python']
bad_student.finished_courses += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

new_reviewer = Reviewer('Luter', 'King')
new_reviewer.courses_attached += ['Python']
new_reviewer.courses_attached += ['Git']

lecturer = Lecturer('Oleg', 'Bulygin', 'm')
lecturer.courses += ['Python']
lecturer.courses += ['Git']

lecturer1 = Lecturer('Oleg', 'Boiko', 'm')
lecturer1.courses += ['Python']
lecturer1.courses += ['Git']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Git', 7)

cool_reviewer.rate_hw(bad_student, 'Python', 8)
cool_reviewer.rate_hw(bad_student, 'Git', 5)
cool_reviewer.rate_hw(bad_student, 'Python', 7)

best_student.rate_lecturer(lecturer, 'Python', 10)
best_student.rate_lecturer(lecturer, 'Python', 8)
best_student.rate_lecturer(lecturer, 'Python', 4)
bad_student.rate_lecturer(lecturer, 'Git', 2)
bad_student.rate_lecturer(lecturer1, 'Python', 9)
best_student.rate_lecturer(lecturer1, 'Git', 7)

print(best_student)
print(lecturer)
print(cool_reviewer)
print(best_student < bad_student)
print(lecturer < lecturer1)
print(student_avg_grade_course([best_student, bad_student], 'Python'))
print(lecturer_avg_grade_course([lecturer, lecturer1], 'Git'))
