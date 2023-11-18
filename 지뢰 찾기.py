import random

# 게임 설정
BOARD_SIZE = 10
NUM_MINES = 15

# 보드 초기화
board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
revealed = [[False] * BOARD_SIZE for _ in range(BOARD_SIZE)]
mines = set()

# 지뢰 위치 설정
while len(mines) < NUM_MINES:
    x = random.randint(0, BOARD_SIZE - 1)
    y = random.randint(0, BOARD_SIZE - 1)
    mines.add((x, y))

# 보드에 지뢰 표시
for x, y in mines:
    board[x][y] = -1

# 지뢰 주변 영역 카운트
for x in range(BOARD_SIZE):
    for y in range(BOARD_SIZE):
        if board[x][y] == -1:
            continue
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and board[nx][ny] == -1:
                    count += 1
        board[x][y] = count


# 게임 실행
def play_game():
    print("== 지뢰 게임 ==")
    print(f"전체 지뢰 개수: {NUM_MINES}")

    while True:
        print_board()
        x, y = get_user_input()

        if (x, y) in mines:
            print("지뢰를 클릭했습니다! 게임 오버!")
            reveal_board()
            print_board()
            if play_again():
                reset_game()
            else:
                break
        else:
            reveal_cell(x, y)
            if check_win():
                print("모든 지뢰를 찾았습니다! 승리!")
                print_board()
                if play_again():
                    reset_game()
                else:
                    break


# 보드 출력
def print_board():
    for row, revealed_row in zip(board, revealed):
        print(" ".join([str(cell) if is_revealed else "." for cell, is_revealed in zip(row, revealed_row)]))


# 사용자 입력 받기
def get_user_input():
    while True:
        try:
            x = int(input("x 좌표를 입력하세요: "))
            y = int(input("y 좌표를 입력하세요: "))
            if not (0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE):
                raise ValueError()
            if revealed[x][y]:
                print("이미 공개된 셀입니다.")
                continue
            return x, y
        except ValueError:
            print("잘못된 입력입니다. 다시 시도해주세요.")


# 셀 공개하기
def reveal_cell(x, y):
    revealed[x][y] = True
    if board[x][y] == 0:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and not revealed[nx][ny]:
                    reveal_cell(nx, ny)


# 보드 전체 공개하기
def reveal_board():
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            revealed[x][y] = True


# 승리 여부 확인
def check_win():
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if not revealed[x][y] and board[x][y] != -1:
                return False
    return True


# 새로운 게임 시작 여부 확인
def play_again():
    while True:
        answer = input("새로운 게임을 시작하시겠습니까? (y/n): ").lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")


# 게임 초기화
def reset_game():
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            board[x][y] = 0
            revealed[x][y] = False
    mines.clear()
    while len(mines) < NUM_MINES:
        x = random.randint(0, BOARD_SIZE - 1)
        y = random.randint(0, BOARD_SIZE - 1)
        mines.add((x, y))
    for x, y in mines:
        board[x][y] = -1
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if board[x][y] == -1:
                continue
            count = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and board[nx][ny] == -1:
                        count += 1
            board[x][y] = count


# 게임 실행
play_game()

