import random

def generate_random_number():
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:3]

def get_user_input():
    while True:
        user_input = input("세 자리 숫자를 입력하세요: ")
        if len(user_input) == 3 and user_input.isdigit():
            return list(map(int, user_input))
        else:
            print("잘못된 입력입니다. 세 자리 숫자를 입력해주세요.")

def compare_numbers(random_number, user_number):
    strikes = 0
    balls = 0
    outs = 0
    for i in range(3):
        if user_number[i] == random_number[i]:
            strikes += 1
        elif user_number[i] in random_number:
            balls += 1
    if strikes == 0 and balls == 0:
        outs = 1
    return strikes, balls, outs

def play_game():
    random_number = generate_random_number()
    attempts = 0
    max_attempts = 5
    game_over = False

    print("숫자 맞추기 게임을 시작합니다!")

    while not game_over:
        user_number = get_user_input()
        strikes, balls, outs = compare_numbers(random_number, user_number)
        attempts += 1

        if strikes == 3:
            print("축하합니다! 정답을 맞추셨습니다.")
            game_over = True
        elif attempts == max_attempts:
            print(f"게임 오버! 정답은 {random_number}입니다.")
            game_over = True
        else:
            print(f"결과: 스트라이크 {strikes}, 볼 {balls}, 아웃 {outs}")
            print(f"기회가 {max_attempts - attempts}번 남았습니다. 다시 시도해보세요.")

play_game()
