import random
import prompt

from brain_games.scripts.brain_games import main_greeting
import brain_games.cli


def generate_a_num():
    MIN_NUM = 1
    MAX_NUM = 100
    return random.randint(MIN_NUM, MAX_NUM)


def ask_game_question(question_body):
    print(f'Question: {str(question_body)}')
    answer = prompt.string("Your answer: ")
    return answer


def is_correct_answer(valid_answer, guess_answer):
    if str(guess_answer) == str(valid_answer):
        return True
    else:
        return False


def start_game(game_rules, questions, valid_answers):
    main_greeting()
    user_name = brain_games.cli.welcome_user()
    print(game_rules)
    ROUNDS_COUNT = 3
    current_round = 1
    is_last_round = False
    while current_round <= ROUNDS_COUNT:
        if current_round == ROUNDS_COUNT:
            is_last_round = True
        question = questions[current_round - 1]
        cor_answer = valid_answers[current_round - 1]
        guess_answer = ask_game_question(question).lower()
        if is_correct_answer(cor_answer, guess_answer) and not is_last_round:
            print("Correct!")
            current_round += 1
        elif is_correct_answer(cor_answer, guess_answer) and is_last_round:
            print("Correct!")
            print(f"Congratulations, {user_name}!")
            break
        else:
            print(f"'{guess_answer}' is wrong answer ;(. "
                  f"Correct answer was '{cor_answer}'.")
            print(f"Let's try again, {user_name}!")
            break
