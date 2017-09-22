a = int(input('숫자를 입력하세요'))

for i in range(a+1):
    for j in range(i):
        print('별',end='끝')
    print()
