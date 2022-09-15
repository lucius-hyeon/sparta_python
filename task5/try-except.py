# 중괄호 두번 씌우기 변수 중괄호 까지 총 3개씩
count = 0
while True:
    print('입력: ', end='')
    temp = input()

    try:
        data = int(temp)*2
        count += 1
        print(f'출력: {data}')
    except ValueError:
        if temp == 'exit':
            break
        print(f"입력한 문자는  {{{temp}}}  입니다.")

    if count == 5:
        break
