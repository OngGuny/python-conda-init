# 주석 남기는 방법
# 1. 맨앞에 # 해쉬태그 추가
# 2. """ 문법...

"""

from random import randint

user_choice = int(input("Enter a number: "))
pc_choice = randint(1, 50)  #

if user_choice == pc_choice:
    print("You won!")
elif user_choice < pc_choice:
    print("Lower! Computer chose..", pc_choice)
elif user_choice > pc_choice:
    print("Higher! Computer chose..", pc_choice)


    alt + shift 로 한줄 내리기
"""
# while 문. if 와 비슷하다.
"""
while True:
    print("Hello World!")
"""
# 위 코드는 메모리가 동날떄까지 계속된다....

# 어떤 사람이 일정 distance 를 달린다고 해보자.
distance = 0
while distance < 20:
    print("i'm running :", distance, "km")
    distance += 1
