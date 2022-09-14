from calc import calc

print("""2개의 숫자와 연산자를 띄어쓰기를 통해 입력해주세요
ex) 2 + 2
0 0 0을 입력하면 프로그램이 종료됩니다.""")


def main():
    num1, operator, num2 = input().split()
    return calc.calculator(int(num1), int(num2), operator)


result = ''
while (1):
    try:
        if result == 'exit':
            break
        else:
            result = main()
        print(result)
    except:
        print('숫자를 입력하세요')
