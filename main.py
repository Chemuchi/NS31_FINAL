from time import sleep

from final.func.translator import translate
from final.func.word import dic
from final.func.han import temp


def delay():
    print("\n5초 후 메인화면으로 돌아갑니다..")
    sleep(5.0)

while(1):
    print("----------------------------------------")
    print("NS31 최종 프로젝트에 오신것을 환영합니다.")
    print("\n원하시는 옵션을 선택해주세요.")
    print("\n1. 한강 수온 체크")
    print("\n2. 사전")
    print("\n3. 번역")
    print("\n4. 종료")
    try:
        sel = int(input("\n선택:"))
        if(sel == 1):
            temp()
            delay()
        elif(sel == 2):
            dic()
            delay()
        elif(sel == 3):
            translate()
            delay()
        elif(sel == 4):
            print("프로그램을 종료합니다.")
            break
        else:
            print("알맞은 값을 입력해주세요.")
            delay()
    except ValueError:
        print("알맞은 값을 입력해주세요.")
        delay()




