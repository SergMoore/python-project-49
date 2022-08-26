import random

from brain_games.engine import start_game


def generate_arithmet_progression():
    (min_border_for_a0_d, max_border_for_a0_d) = (1, 15)
    (min_members_number, max_members_number) = (5, 10)
    a0 = random.randint(min_border_for_a0_d, max_border_for_a0_d)
    d = random.randint(min_border_for_a0_d, max_border_for_a0_d)
    members_num = random.randint(min_members_number, max_members_number)
    hidden_member = ".."
    hidden_member_index = random.randint(0, members_num - 1)
    progression = ""
    for i in range(members_num):
        if i == hidden_member_index:
            current_element = hidden_member
        else:
            current_element = str(a0 + i * d)
        progression = f"{progression} {current_element}"
    return progression


def find_element_of_progr(str_expression):
    series = str_expression.split()
    last_i = len(series) - 1
    hidden_i = series.index("..")
    if hidden_i == last_i:
        return int(2 * int(series[last_i - 1]) - int(series[last_i - 2]))
    elif hidden_i == 0:
        return int(2 * int(series[1]) - int(series[2]))
    else:
        return int((int(series[hidden_i - 1]) + int(series[hidden_i + 1])) / 2)


def generate_questions():
    rounds_number = 3
    list_of_questions = []
    for i in range(rounds_number):
        progression = generate_arithmet_progression()
        list_of_questions.append(progression)
    return list_of_questions


def form_answers_list(list_of_questions):
    list_of_answers = []
    for i in range(len(list_of_questions)):
        list_of_answers.append(find_element_of_progr(list_of_questions[i]))
    return list_of_answers


def brain_progression_game():
    game_rules = 'What number is missing in the progression?'
    questions_list = generate_questions()
    answers_list = form_answers_list(questions_list)
    start_game(game_rules, questions_list, answers_list)
