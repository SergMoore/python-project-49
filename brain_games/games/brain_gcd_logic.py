from brain_games.engine import generate_a_num, start_game


def find_gcd_from_str(str_expression):
    elements = str_expression.split()
    num1 = int(elements[0])
    num2 = int(elements[1])
    gcd_value = 1
    for i in range(2, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcd_value = i
    return gcd_value


def generate_questions():
    rounds_number = 3
    list_of_questions = []
    for i in range(rounds_number):
        num1 = generate_a_num()
        num2 = generate_a_num()
        question = f"{num1} {num2}"
        list_of_questions.append(question)
    return list_of_questions


def form_answers_list(list_of_questions):
    list_of_answers = []
    for i in range(len(list_of_questions)):
        list_of_answers.append(find_gcd_from_str(list_of_questions[i]))
    return list_of_answers


def brain_gcd_game():
    game_rules = 'Find the greatest common divisor of given numbers.'
    questions_list = generate_questions()
    answers_list = form_answers_list(questions_list)
    start_game(game_rules, questions_list, answers_list)