#random 모듈 불러오기
import random
# 파이썬 파일이름과 모듈이름이 겹치게 사용하지 않도록 주의!
# 저녁메뉴 뭐 먹지?

menu = ['치킨','마라탕','시리얼','피자','갈비']

# 이중에서 랜덤으로 하나를 고르고 싶다.
# random 모듈의 choice 라는 함수를 사용해서 리스트 안의 값을 랜덤으로 선택하기
# 모듈안의 함수를 사용하는 방법 ==> 모듈이름.함수이름()

dinner = random.choice(menu)
print(dinner)
