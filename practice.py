# 숫자 자료형
# print(5)
# print(-10)
# print(3.14)
# print(1000)
# print(5+3)
# print(2*8)
# print(3*(3+1))

# 문자열 자료형
# print('풍선')
# print("나비")
# print('ㅋㅋㅋㅋㅋㅋㅋ')
# print('ㅋ'*10)

# boolean 자료형 (참 / 거짓)
# print( 5 > 10)
# print( 5 < 10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not (5>10))

# 변수
# 애완동물을 소개해 주세요~

# animal = '강아지'
# name = '연탄'
# age = 4
# hobby = '산책'
# is_adult = age >= 3

# print(f'우리집 {animal}의 이름은 {name}')
# hobby = '공놀이'
# print(f'{name}이는 {age}살이며, {hobby}을 좋아함')
# print(f'{name}이는 어른? {is_adult}')

# 주석
'''
주석 처리
'''

# Quiz) 변수를 이용하여 다음 문장을 출력하시오.
# 변수명: station
# 변수값: '사당','신도림','인천공항' 순서대로 입력
# 출력 문장: xx 행 열차가 들어오고 있습니다.
# station = '사당'
# print(f'{station} 행 열차가 들어오고 있습니다.')

# station = '신도림'
# print(f'{station} 행 열차가 들어오고 있습니다.')

# station = '인천공항'
# print(f'{station} 행 열차가 들어오고 있습니다.')

# 연산자
# print(1+1) # 2
# print(3-2) # 1
# print(5*2) # 10
# print(6/3) # 2

# print(2**3) # 8
# print(5%3) # 나머지 구하기 2
# print(5//3) # 몫 구하기 1
# print(10//3) # 3

# print( 10 > 3 ) # True
# print( 7 >= 4 ) # True
# print( 10 < 3 ) # False
# print( 5 <= 5) # True

# print( 3 == 3) # True
# print( 4 == 2) # False
# print (3+4 == 7) # True

# print(1 != 3) # True
# print(not(1 != 3)) # False

# print((3>0) and (3<5)) # True
# print((3>0) & (3<5)) # True

# print((3>0) or (3>5)) # True
# print((3>0) | (3>5)) # True

# print(3<5<7) # True
# print(3<5<4) # False

# 간단한 수식
# print(2+3*4) # 14
# print((2+3)*4) # 20
# number = 2 + 3 * 4 # 14
# print(number)
# number = number + 2 # 16
# print(number)
# number += 2 # 18
# print(number)
# number *= 2 # 36
# print(number)
# number /= 2 # 18
# print(number)
# number -= 2 # 16

# number %= 5 # 1
# print(number)

# 숫자 처리 함수
# print(abs(-5)) # 절대값
# print(pow(4,2)) # 4 * 4 = 16
# print(max(5,12)) # 12 
# print(min(5,12)) # 5
# print(round(3.14)) # 반올림, 3
# print(round(4.99)) # 반올림, 5

# from math import *
# print(floor(4.99)) # 내림, 4
# print(ceil(3.14)) # 올림, 4
# print(sqrt(16)) # 제곱근, 4

# 랜덤 함수
from math import e
from random import *

# print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
# print(random()*10) # 0.0 ~ 10.0 미만의 임의의 값 생성
# print(int(random()*10)) # 0 ~ 10 미만의 임의의 값 생성
# print(int(random()*10)) # 0 ~ 10 미만의 임의의 값 생성
# print(int(random()*10)) # 0 ~ 10 미만의 임의의 값 생성

# print(int(random()*10)+1) # 1 ~ 10 이하의 임의의 값 생성
# print(int(random()*10)+1) # 1 ~ 10 이하의 임의의 값 생성
# print(int(random()*10)+1) # 1 ~ 10 이하의 임의의 값 생성
# print(int(random()*10)+1) # 1 ~ 10 이하의 임의의 값 생성
# print(int(random()*10)+1) # 1 ~ 10 이하의 임의의 값 생성
# print(int(random()*10)+1) # 1 ~ 10 이하의 임의의 값 생성

# print(int(random()*45)+1) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random()*45)+1) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random()*45)+1) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random()*45)+1) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random()*45)+1) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random()*45)+1) # 1 ~ 45 이하의 임의의 값 생성

# print(randrange(1,46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1,46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1,46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1,46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1,46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1,46)) # 1 ~ 46 미만의 임의의 값 생성

# print(randint(1,45) ) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1,45) ) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1,45) ) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1,45) ) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1,45) ) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1,45) ) # 1 ~ 45 이하의 임의의 값 생성

# # Quiz) 당신은 최그네 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

# 조건1: 랜덤으로 날짜를 뽑아야 함
# 조건2: 월별 날짜는 다름을 감안하여 최소 일수일 28 이내로 정함
# 조건3: 매월 1 ~ 3일은 스터디 준비를 해야 하므로 제외

# (출력문 예제)
# # 오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.
# from random import *
# date = randint(4,28)
# print(f'오프라인 스터디 모임 날짜는 매월 {date}일로 선정되었습니다.')

# 문자열
# sentence = '나는 소년입니다.'
# print(sentence)
# sentence2 = '파이썬은 쉬워요'
# print(sentence2)
# sentence3 = '''
# 나는 소년이고,
# 파이썬은 쉬워요
# '''
# print(sentence3)

# # 슬라이싱
# jumin = '990120-1234567'

# print(f'성별: {jumin[7]}')
# print(f'연: {jumin[0:2]}') # 0부터 2 직전까지 [0,1]
# print(f'월: {jumin[2:4]}')
# print(f'일: {jumin[4:6]}')

# print(f'생년월일: {jumin[:6]}') # 처음부터 6 직전까지
# print(f'뒤에 7자리: {jumin[7:]}') # 7부터 끝까지
# print(f'뒤에 7자리(뒤에부터): {jumin[-7:]}')
# # 맨 뒤에서 7번째부터 끝까지

# 문자열 처리 함수
# python = 'Python is Amazing'
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace('Python','Java'))

# index = python.index('n')
# print(index)
# index = python.index('n', index + 1)
# print(index)

# print(python.find('Java')) # .find() 에서는 원하는 값이 없을 시 -1 return
# #print(python.index('Java'))
# print(python.count('n'))

# 문자열 포맷팅
# 방법 1
# print('나는 %d살입니다.' % 20)
# print('나는 %s을 좋아해요.' % '파이썬')
# print('Apple은 %c로 시작해요.' % A)

# %s
# print('나는 %s살입니다.' % 20)
# print('나는 %s색과 %s색을 좋아해요.' %('파란','빨간'))

# 방법 2
# print('나는 {}살입니다.'.format(20))
# print('나는 {}색과 {}색을 좋아해요.'.format('파란','빨간'))
# print('나는 {0}색과 {1}색을 좋아해요.'.format('파란','빨간'))
# print('나는 {1}색과 {0}색을 좋아해요.'.format('파란','빨간'))

# 방법 3
# print('나는 {age}살이며, {color}색을 좋아해요.'.format(age = 20, color='빨간'))

# # 방법 4
# age = 20
# color = '빨간'
# print(f'나는 {age}살이며, {color}색을 좋아해요.')

# # 탈출 문자
# # \n 줄바꿈
# print('백문이 불여일견\n백견이 불여일타') 

# # \' 문장 내에서 따옴표
# print('저는 \'김태건\'입니다.')

# # \\: 문장 내에서 \

# # \r: 커서를 맨 앞으로 이동
# print('Red Apple\rPine') 

# # \b: 백스페이스 (한 글자 삭제)
# print('Redd\bApple')

# # \t: 탭
# print('Red\tApple')

# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.
# 예) http://naver.com
# 규칙1: http:// 부분은 제외 => naver.com
# 규칙2: 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + '!'로 구성

# 예) 생성된 비밀번호 : nav51!
# 내가 푼 것
# address = 'http://naver.com'
# address = address[7:]
# address = address[:-4]

# address3 = address[0:3]
# addresslen = len(address)
# addresse= address.count('e')

# print(f'{address3}{addresslen}{addresse}!')

# url = 'http://naver.com'
# my_str = url.replace('http://','') # 규칙 1
# my_str = my_str[:my_str.index('.')] # 규칙 2
# password = my_str[:3]+ str(len(my_str)) + str(my_str.count('e')) + '!'

# print('{0}의 비밀번호는 {1}입니다.'.format(url,password))





























































































































 





















































































































