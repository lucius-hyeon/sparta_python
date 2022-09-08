import random
import time
from datetime import datetime, timedelta


def baseball_game(num):
    start_time = time.time()  # 게임 시작 시간
    count = 0  # 게임 진행 횟수(정답까지 걸린 횟수)
    temp_data = set()  # 랜덤한 숫자n개를 받아오기전의 임시 저장소
    qst = []  # 풀어야 하는 게임 문제
    while (len(temp_data) < num):
        temp_data.add(str(random.randint(1, 9)))
    qst = list(temp_data)
    random.shuffle(qst)

    # print(f'qst : {qst}')
    ans = []  # 제출한 게임 문제답
    while (('exit' in ans) != True):
        ans = list(input().split())
        if ('exit' in ans) == True:
            print('프로그램을 종료합니다')
            continue
        elif len(ans) > num:
            print('입력 범위를 초과하였습니다')
            continue
        elif len(ans) < num:
            print('입력수 보다 적게 입력하였습니다.')
            continue

        count += 1
        # print(f'qst : {qst}')
        # print(f'ans : {ans}')
        # 정답일 경우
        if qst == ans:
            print('스트라이크')
            print(f"정답까지 진행한 횟수 : {count}")
            end_time = -(start_time - time.time())
            end_day = datetime.strftime(datetime.now(), "%Y년%m월%d일 %H시%M분")

            print(f'정답을 맞추기까지 소요된 시간: {end_time:.3f}초')
            print(f'정답을 맞춘 날짜/시간: {end_day}')
            break
        else:
            strike = 0
            ball = 0
            for i, _ in enumerate(qst):
                if qst[i] == ans[i]:
                    strike += 1

            # print(len(set(qst) - set(ans)))
            # 정답과 답안지가 정확하게 일치 하지 않지만 숫자가 모두 일치하는 경우
            if len(set(qst) - set(ans)) == 0:
                ball = len(set(qst)) - strike
            # 정답과 답안지의 숫자가 어느 하나라도 같은 경우
            elif len(set(qst) - set(ans)) != len(qst):
                ball = len(set(qst) & set(ans)) - strike
            # 정답과 답안지의 숫자가 모두 불일치 하는경우
            else:
                print(f'아웃')
            print(f'{strike}strike / {ball}ball')


def main():
    exit = False
    while (not exit):
        try:
            print('숫자를 입력하세요: ', end=" ")
            num = input()
            num = int(num)
            if int(num):
                if num > 10:
                    print("최대 10까지 입력 가능합니다")
                else:
                    baseball_game(num)
                    exit = True
                    break
        except:
            if num == 'exit':
                print('프로그램을 종료합니다')
                break
            else:
                print('잘못 입력하셨습니다. 숫자를 입력하세요')


main()

# baseball_game(int(input()))
# 로그인 기능입니다.
