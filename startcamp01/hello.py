#greeting = '안녕하세요'
#print(greeting)

#파이썬 파일을 실행시키는 가장 기본적인 방법
#python "파이썬 파일이름"

#안녕하세요를 4번 반복해서 출력하는 코드 작성 (While 사용)

count = 0 #내가 반복을 몇번했는지 세는 변수
greeting = '안녕하세요'

while count<4:#반복횟수가 4가 될 때까지
    print(greeting)
    count=count+1 #count += 1 : count = count+1 을 줄여서 사용 

print('==============================')

#for에서 단순히 반복만 할 때 사용하는 방법 range()함수 사용 , 기본적으로 0부터 시작, 주어진 숫자 -1까지 
#range(4) : 0,1,2,3 range는 리스트가 아님! 파이썬에는 range라는 타입이 따로 존재

for i in range(4): #4번 반복
    print(i)
    print(greeting)