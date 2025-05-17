from game_utils import generate_random_number


def main():
    print("Добро пожаловать в игру 'Угадай число'!")

    min_value = 1
    max_value = 100
    random_number = generate_random_number(min_value, max_value)

    print(f"Я загадал число от {min_value} до {max_value}. Попробуй угадать!")

    attempts = 0
    while True:
        user_guess = int(input("Введите ваше число: "))
        attempts += 1

        if user_guess < random_number:
            print("Слишком мало! Попробуйте еще раз.")
        elif user_guess > random_number:
            print("Слишком много! Попробуйте еще раз.")
        else:
            print(f"Поздравляю! Вы угадали число {random_number} за {attempts} попыток.")
            break


if __name__ == "__main__":
    main()