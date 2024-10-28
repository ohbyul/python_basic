# Q
def std_weight(heigth, gender):
    constant = 0
    if(gender == 'M') : constant =22
    elif(gender == 'F') : constant = 21

    wei = (heigth/100)**2 * constant
    return round(wei , 2)

hei= 161
gender = 'F'
weight = std_weight(hei,gender)
print('키 {0}cm {1}의 표준 체중은 {2}kg 입니다.'.format(hei,gender,weight))


import sys
print("Python" , "Java" , file=sys.stdout)  # 표준출력
print("Python" , "Java" , file=sys.stderr )  # 표준에러

scores = {"수학" : 0 , "영어" : 10 , "코딩" : 100}
for subject,score in scores.items():
    print(subject.ljust(8), str(score).rjust(4),sep=":")

# 은행 대기번호
for num in range(1,11):
    print("대기 번호".ljust(8) , str(num).zfill(3).rjust(8) , sep=":")

print('{0:,}'.format(100000000000))
print('{0:+,}'.format(100000000000))