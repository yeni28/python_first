dust = {'영등포구':58, '강남구':40, '서대문구':54,'도봉구':70, '강동구':23,'종로구':50}
#딕셔너리 : {}를 이용해서 만든다. 식별키 : 값
#위에서 선언한 딕셔너리에서 영등포구의 미세먼지 농도를 알고싶다?
#list와 같이 []를 이용해서 값에 접근, 이때 그 값에 해당하는 키(key)를 넘겨주면 된다.
print(dust['영등포구'])
print(dust['강남구'])

#점심메뉴 리스트를 사용해서 딕셔너리를 만들어 봅시다. 그 메뉴에 해당하는 칼로리 값을 저장하는 딕셔너리
#'쇠고기미역국' : 736

menu = {'쇠고기미역국':'736Kcal','애호박찌개':'400Kcal','함박스테이크':'800kcal','제육볶음':'555kcal'}
#쇠고기미역국의 칼로리??
print(menu['쇠고기미역국'])
