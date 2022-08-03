from functions import get_student_by_pk, get_profession_by_title, check_fitness


def main():
    result = {}

    print('Введите номер студента')
    pk = int(input())
    student = get_student_by_pk(pk)
    if student:
        print(f"Студент {student['full_name']}\nЗнает {', '.join(student['skills'])}")
    else:
        print("У нас нет такого студента")
        quit()

    print(f"Выберите специальность для оценки студента {student['full_name']}")
    title = input()
    profession = get_profession_by_title(title)
    if profession:
        result = check_fitness(student, profession)
    else:
        print("У нас нет такой специальности")
        quit()

    print(
        f"Пригодность {result['fit_percent']}%\n{student['full_name']} знает {', '.join(result['has'])}\n"
        f"{student['full_name']} не знает {', '.join(result['lacks'])}")


if __name__ == '__main__':
    main()
