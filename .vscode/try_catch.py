class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print('한자리 숫자 나누기 전용 계산기 입니다.')
    num1 = int(input("첫 번째 숫자를 입력해세요 : "))
    num2 = int(input("두 번째 숫자를 입력해세요 : "))
    if num1 >=10 | num2 >=10 :
        raise BigNumberError("입력 값 : {0} {1}".format(num1,num2))
    print("{0} / {1} = {2}".format(num1,num2,int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다.")
except BigNumberError as err:
    print("에러가 발생하였습니다.")
    print(err)

finally:
    print("계산기를 이용해 주셔서 감사합니다.")