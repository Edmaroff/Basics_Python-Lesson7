class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lector(self, lecturer, course, grade):
        # 1 ВОПРОС - Следующая строка 121 символ, по PEP8 должно быть 120, как можно преобразовать это строку?
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        sum_ = 0
        len_ = 0
        for list_grades in self.grades.values():
            sum_ += sum(list_grades)
            len_ += len(list_grades)
        res = round((sum_ / len_), 2)
        return res

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade()}' \
              f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}' \
              f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f'{other} is is not a student')
            return
        return self.average_grade() < other.average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        sum_ = 0
        len_ = 0
        for list_grades in self.grades.values():
            sum_ += sum(list_grades)
            len_ += len(list_grades)
        res = round((sum_ / len_), 2)
        return res

    def __str__(self):
        res = f'Имя = {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f'{other} is is not a lecturer')
            return
        return self.average_grade() < other.average_grade()


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
        res = f'Имя = {self.name}\nФамилия: {self.surname}'
        return res


oleg_lec = Lecturer('Oleg', 'Sidorov')
oleg_lec.courses_attached = ['Py', 'Git']
oleg_lec.grades = {'Py': [7, 8, 9, 10], 'Git': [7, 8, 9, 10]}

zina_lec = Lecturer('Zina', 'Soboleva')
zina_lec.courses_attached = ['Py', 'Git']
zina_lec.grades = {'Py': [7, 8, 9, 1000], 'Git': [7, 8, 9, 10]}

# # Проверка методов
# print(oleg_lec.average_grade())
# print(zina_lec.average_grade())
# print(oleg_lec)
# print(zina_lec)
# print(oleg_lec < zina_lec)


ivan_st = Student('Ivan', 'Ivanov', 'men')
ivan_st.courses_in_progress = ['Py', 'Git']
ivan_st.finished_courses = ['List', 'Dict']
ivan_st.grades = {'Py': [7, 8, 9, 10], 'Git': [7, 8, 9, 10]}

rita_st = Student('Rita', 'Petrova', 'women')
rita_st.courses_in_progress = ['Py', 'Git']
rita_st.finished_courses = ['List', 'Dict']
rita_st.grades = {'Py': [7, 8, 9, 100], 'Git': [7, 8, 9, 10]}

# # Проверка методов 
# ivan_st.rate_lector(oleg_lec, 'Py', 7)
# print(oleg_lec.grades)
# rita_st.rate_lector(zina_lec, 'Py', 8)
# print(zina_lec.grades)
# print(ivan_st.average_grade())
# print(rita_st.average_grade())
# print(ivan_st)
# print(rita_st)
# print(ivan_st < rita_st)
# print(ivan_st > rita_st)


alex_rev = Reviewer('Alex', 'Vetrov')
alex_rev.courses_attached = ['Py']

victor_rev = Reviewer('Victor', 'Ladov')
victor_rev.courses_attached = ['Git']

# # Проверка методов
# print(alex_rev)
# print(victor_rev)
# alex_rev.rate_hw(ivan_st, 'Py', 0)
# print(ivan_st.grades)
# victor_rev.rate_hw(rita_st, 'Git', 0)
# print(rita_st.grades)
