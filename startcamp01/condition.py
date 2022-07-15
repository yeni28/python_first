dust = 60

if dust > 50:
    print('50초과')
    print('미세먼지 보통') #if문의 범위(들여쓰기로 구분)
else:
    print('50이하')
    print('미세먼지 좋음')

#else없이, 들여쓰기 되지 않은 print를 쓸 경우, if 문의 범위에 포함되지 않아 조건과 상관없이 실행된다.
