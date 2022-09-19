from utils import generate_questions_list, get_user_answer, load_data, show_result

STOP_WORDS = ('close', 'exit', 'quit', 'stop')


def main():
    questions = load_data('./data/questions.json')
    question_objects = generate_questions_list(questions)
    player_answer = {}

    print('Игра начинается!\n')

    for idx, question_obj in enumerate(question_objects, 1):
        question_obj.ask_question = True
        print(question_obj.build_question())

        user_answer = get_user_answer()

        if user_answer in STOP_WORDS:
            break

        question_obj.player_answer = user_answer
        print(question_obj.build_feedback())

        player_answer[idx] = question_obj.points_by_question if question_obj.is_correct() else 0

    show_result(player_answer)


if __name__ == '__main__':
    main()
