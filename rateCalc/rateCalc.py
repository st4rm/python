total_rate = 0

while True:
    try:
        debt = float(input('대출 금액(원): '))
        pay = float(input('한달에 갚을 금액(원): '))
        ratio = float(input('이율(%): ')) * 0.01
        period_m = input('거치 기간(개월): ')
        period_m = float(period_m)
        break
    except ValueError:
        print('숫자만 입력하세요.\n')

i = 1
while(i <= period_m):
    rate = debt * ratio / 365 * 30
    debt -= pay
    total_rate += rate 
    print('\n', i, '개월 째의 이자는', rate)
    print('남은 빚은', debt)
    i += 1

print('\n\n 지급한 총 이자는', total_rate)

input('\n\n 종료하려면 아무 키나 누르세요...')