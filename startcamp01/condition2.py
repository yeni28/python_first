#dust = 49

#if dust > 70:
   # print('미세먼지 농도는 70보다 크다.')
#elif dust > 50: #dust가 70보다 크지 않을 때 조건 검사
   # print('미세먼지 농도는 50보다 크다.')  
#else:
    #pass

#pass는 이무것도 하지 않는 코드(자리만 차지)



# dust 변수에 들어있는 값을 기준으로 미세먼지 정보 출력
# dust가 150보다 크다 : 매우나쁨
# dust가 80보다 크고 150이하이다 : 나쁨
# dust가 30보다 크고 80이하이다 : 보통
# dust가 30이하 이다 : 좋음
# 이렇게 출력하는 조건문을 작성해봅시다. (dust는 150보다 작은 수라고 가정)


dust = 120

if dust > 150:
    print('매우 나쁨')
elif dust <= 150:  # 150>= dust >80 (python은 가능하다)
    print('나쁨')
elif dust <= 80:
    print('보통')
else:
    print('좋음')