from utils import load_data, Question, get_question, create_questions
import pprint
import abc

if __name__ == '__main__':
    # print_hi('PyCharm')

    URL = 'https://jsonkeeper.com/b/JSZH'
    data = load_data(URL)
    # print(data)
    quest = create_questions(data)
    for first_question in quest:
        # first_question = get_question(quest)
        if not first_question.is_question:
            first_question.is_question = True
            print(first_question.build_question())
            user_input = input()
            first_question.user_answer = user_input
            # print(repr(first_question))
            if first_question.is_correct():
                print(first_question.build_positive_feedback())
            else:
                print(first_question.build_negative_feedback())

    # pprint.pprint(load_data(URL))7
    # print(info)
    #
    # print(questions)
