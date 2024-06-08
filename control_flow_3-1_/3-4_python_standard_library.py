from random import randint

# 카지노 게임 만들기
# 컴퓨터의 숫자와 내가 뽑은 숫자 중 기준 숫자와 가까운걸 뽑으면 이기는게임

# 사용자의 숫자 받기
user_choice = int(input("Enter a number: "))
pc_choice = randint(1, 50)  # should be random

if user_choice == pc_choice:
    print("You won!")
elif user_choice < pc_choice:
    print("Lower! Computer chose..", pc_choice)
elif user_choice > pc_choice:
    print("Higher! Computer chose..", pc_choice)

# standard library
# 언어 자체에 포함되어 있는 built-in function 들.
# input 이나 print 같은건 그냥 쓸 수 있지만,
# 스탠다드 전부를 항상 갖다놓을순 없으니, improt 해서 사용할수있게 만들어두었다.
