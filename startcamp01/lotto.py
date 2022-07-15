import random
#로또 번호 1~45 사이의 수를 6개
numbers = range(1,46) #1부터 시작해서 46-1까지의 범위
# 그 범위 중에 6개를 뽑아서 리스트 만들기

lucky_numbers = random.sample(numbers, 6) #sample(값의 범위, 갯수)==> 갯수만큼의 크기를 가진 리스트를 변환
# 그 리스트 안의 갑스이 범위 

print(lucky_numbers) #6개의 숫자, 범위는 1~45까지의 숫자중 랜덤 선택
print(sorted(lucky_numbers)) #sorted: 정렬해주는 함수