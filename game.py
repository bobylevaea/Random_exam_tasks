import random

def load_data(file_name):
    data = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
    for line in lines:
        key, value = line.split(', ')
        data[key] = value
    return data

def save_data(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as file:
        for key, value in data.items():
            file.write(f"{key}, {value}\n")

def game_menu():
    while True:
        print("МЕНЮ:")
        print("1 - Начать игру")
        print("0 - Выйти из игры")
        choice = input("Выберите пункт меню: ")
        if choice == '1':
            start_game()
        elif choice == '0':
            print("Игра завершена.")
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

def start_game():
    players = load_data("players.txt")
    questions = load_data("questions.txt")
    used_questions = {}

    player_names = list(players.keys())
    random.shuffle(player_names)

    print()
    print("ИГРА НАЧАЛАСЬ")
    print()

    while True:
        if len(questions) == 0:
            print("СТОП ИГРА!")
            break

        player = player_names.pop(0)
        if len(player_names) == 0:
            player_names = list(players.keys())
            random.shuffle(player_names)

        available_questions = list(questions.keys())
        if len(available_questions) == 0:
            print("СТОП ИГРА!")
            break

        question = random.choice(available_questions)
        question_text = questions[question]
        used_questions[question] = question_text
        del questions[question]
        print("К ДОСКЕ ИДЕТ...")
        print(f"{players[player]} - {question_text}")
        print()

        while True:
            print("МЕНЮ:")
            print("1 - Продолжить игру")
            print("0 - Выйти из игры")
            choice = input("Выберите пункт меню: ")
            print()
            if choice == '1':
                break
            elif choice == '0':
                print("Игра завершена.")
                save_data("used_questions.txt", used_questions)
                return
            else:
                print("Неверный выбор. Попробуйте еще раз.")

    print("СПАСИБО ЗА УЧАСТИЕ!")

game_menu()