# Викторина
# игра на выбор правильного ответа
# вопросы которой читаются из тестового файла
import sys
import pickle
player_table1 = {}

def show_champions():
    print("\n\t\t\tСписок лучших игроков\n")

def score_table(name, player_score):
        player_table1[name] = player_score
        return player_table1




def open_file(file_name, mode):
    # открывает файл
    try:
        the_file = open(file_name, mode, encoding='utf-8')
    except IOError as e:
        print('Невозможно открыть файл', file_name, 'Работа прогаммы будет завершена.\n', e)
        input('\n\nНажмите Enter, что бы выйти.')
        sys.exit()
    else:
        return the_file


def next_line(the_file):
    line = the_file.readline()
    line = line.replace('/', '\n')
    return line


def next_block(the_file):
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explanations = next_line(the_file)
    return category, question, answers, correct, explanations,


def universal_score(the_file):
    universal_score_value = next_line(the_file)
    return universal_score_value



def welcome(title):
    print('\t\tДобро пожаловать в игру "викторина"!\n')
    print('\t\t', title, '\n')


def main():
    name = input('введите ваше имя перед игрой: ')
    score = 0
    trivia_file = open_file('trivia.txt', "r")
    title = next_line(trivia_file)
    welcome(title)
    category, question, answers, correct, expianation = next_block(trivia_file)
    universal_score_value = universal_score(trivia_file)
    while category:
        """вывод вопроса на экран"""
        print(category)
        print(question)
        for i in range(4):
            print('\t', i + 1, '-', answers[i])
        answer = input('Ваш ответ: ')
        # проверка ответа
        if answer == correct:
            print('\nДа!', end=' ')
            score += int(universal_score_value)
            score_for_table = score
            best_player_table = open('best_player_table', 'wb')
            pickle.dump(score_table(name, score_for_table), best_player_table)
            best_player_table.close()

        else:
            score_for_table = score
            best_player_table = open('best_player_table', 'wb')
            pickle.dump(score_table(name, score_for_table), best_player_table)
            best_player_table.close()
        print('\nНет!', end=' ')
        print(expianation)
        print('Счет:', score, '\n\n')
        # Переход к следующему вопросу
        category, question, answers, correct, expianation = next_block(trivia_file)
        universal_score_value = universal_score(trivia_file)
    trivia_file.close()
    best_player_table = open('best_player_table', 'rb')
    best_player_table1 = pickle.load(best_player_table)
    print('Это был последний вопрос!')
    print('На вашем счету', score, 'очков\nВот список игроков и их достижения\n')
    print(best_player_table1)




while True:
    main()
