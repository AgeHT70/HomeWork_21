from utils import load_data, get_statistics, create_questions
from random import shuffle


def main():
    URL = 'https://jsonkeeper.com/b/JSZH'
    data = load_data(URL)

    questions_list = create_questions(data)
    shuffle(questions_list)

    print("Игра начинается!")
    for one_question in questions_list:

        if not one_question.is_ask:
            one_question.is_ask = True
            print(one_question.build_question())

            one_question.user_answer = input()

            if one_question.is_correct():
                print(one_question.build_positive_feedback())
            else:
                print(one_question.build_negative_feedback())
    print(get_statistics(questions_list))


if __name__ == '__main__':
    main()
