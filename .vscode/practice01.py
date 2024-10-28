# int
print(5)
print(-10)
print(3.14)
print(10-2*112/11)
# string
print('풍선')
print("나비")
print('ㅋ'*10)
# boolean
print(5>10)
print(1==1)
print(not True)
print(not (1==1))
# 애완동물을 소개해주세요
animal="강아지"
name="연탄이"
age=4
isAdult = age >= 3
print("우리집" + animal + "의 이름은" + name + "예요. 나이는 " + str(age) + "살 입니다. 어른 강아지 일까요? " + str(isAdult))
print("우리집", animal , "의 이름은" , name ,"예요. 나이는 ", age , "살 입니다. 어른 강아지 일까요?",isAdult)
# 연산
print(2**9)
print(True and False)
print(True & False)
print( 1 < 4 < 7)
print( 10 < 4 < 7)
number = 2+3*4
print(number)
number += 2
print(number)
number -= 2
print(number)
number *= 2
print(number)
number /= 2
print(number)
# 숫자 함수
print(abs(-5))
print(pow(4,2)) # 4^2
print(max(2,5,89))
print(round(4.99))

from math import *
print(floor(4.99))
print(ceil(3.14))
print(sqrt(16))

from random import *
lotto = int(random() * 45) + 1
print(lotto)
print(randrange(1,46))
print(randint(1,45))

# Quzi
day = int(randint(4,28))
print(day)

site = "http://google.com"
print(site)
index = site.index('/')
index = site.index('/',index+1)
print(index)
dot=site.index('.')

word = site[index+1 :dot]

pwd = word[:3]+str(len(word))+str(word.count('e'))+'!'
print("{0}의 비밀번호는 {1}입니다.".format(site,pwd))

'''
리스트 [] 순서가 있는 객체 모음
튜플 () 변경되지않는 리스트
set {} 중복안됨, 순서없음
'''
 
users = list(range(1,21))
print(users)
shuffle(users)
print(users)
winners = sample(users,4)
print('''
---당첨자 발표---
치킨당첨자 : {0}
커피당첨자 : {1}
---축하합니다.---
'''.format(winners[0],winners[1:]))

nums = list(range(1,21))
for item in range(1,21) :
    print("대기번호 : {}".format(item))

# Quzi
index = 0
passible = range(5,16)
for user in range(1,51) :
    drive = randint(5,50)
    if(drive in passible) :
        print("[O] {0}번째 손님 ( 소요시간 : {1}분 )".format(user,drive))
        index += 1
    else :
        print("[ ] {0}번째 손님 ( 소요시간 : {1}분 )".format(user,drive))
print("총 탑승 승객 : {0} 분".format(index))

