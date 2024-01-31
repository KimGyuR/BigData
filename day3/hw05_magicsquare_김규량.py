# 홀수차 마방진
# 힌트: 2차원 리스트 생성
# n = 5   변경 가능(화면 입력)
# square = [[0 for col in range(n)] for row in range(n)]
#                 열 생성               행 생성

n = int(input("홀수차 배열의 크기를 입력하세요: "))
if n % 2 != 0:
    square = [[0 for col in range(n)]for row in range(n)]
    print(square)
else:
    print('짝수를 입력하였습니다. 다시 입력하세요.')
