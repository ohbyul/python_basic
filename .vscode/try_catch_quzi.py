class SoldOutError(Exception):
    pass


chicken = 10
waithing = 1 # 홀 안에는 현재 만석, 대기번호 1부터 시작
while(True):
    try : 
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇마리 드려요?"))
        if order > chicken:
            print("재료가 부족합니다. [남은 치킨 : {0}]".format(chicken))
        elif order < 1:
            raise ValueError 
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waithing,chicken))
            waithing += 1
            chicken -= order
        
        if chicken == 0 :
           raise  SoldOutError
    except ValueError:
        print("잘못된 값을 입력했습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break
    
