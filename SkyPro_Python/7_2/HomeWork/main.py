from os import path
from functions import load_students, load_professions, get_student_by_pk, get_profession_by_title, check_fitness


def main():
    STUDENTS_FILE = path.join("Data", "students.json")
    PROFESSIONS_FILE = path.join("Data", "professions.json")

    result = {}

    students_data = load_students(STUDENTS_FILE)
    professions_data = load_professions(PROFESSIONS_FILE)

    print('Введите номер студента: ')
    pk = int(input())
    student = get_student_by_pk(pk, students_data)
    if student:
        print(f"Студент {student['full_name']}\nЗнает {', '.join(student['skills'])}")
    else:
        print("У нас нет такого студента.")
        quit()

    print(f"Выберите специальность для оценки студента {student['full_name']}")
    title = input()
    profession = get_profession_by_title(title, professions_data)
    if profession:
        result = check_fitness(student, profession)
    else:
        print("У нас нет такой специальности.")
        quit()

    print(
        f"Пригодность: {result['fit_percent']}%\n{student['full_name']} знает: {', '.join(result['has'])}\n"
        f"{student['full_name']} не знает: {', '.join(result['lacks'])}")


if __name__ == '__main__':
    main()
