dust = [58 , 40 , 70 , 60 , 120 , 54 ,23 , 50]
#여러개의 값을 연속적으로 저장할 수 있는 저장공간 => list
#특이하게도 프로그래밍 언어에서는 리스트 안에 있는 값의 위치(인덱스)는
#1이 아니라 0부터 시작한다 : dust라는 list의 0번째 값은 => 58
#1번쨰 값 +> 40 ....... 7번째 값 => 50
#값의 위치(인덱스)의 범위 => 0 ~ 리스트의 길이 -1

number1 = dust[7] # dust라는 리스트의 7번째(마지막)에 있는 값을 가져온다.
print(number1)