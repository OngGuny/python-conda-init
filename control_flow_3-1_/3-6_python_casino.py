# standard_library 에서 만든 게임과 while 을 합침
# 카지노 게임
# 컴퓨터의 숫자와 내가 뽑은 숫자 중 기준 숫자와 가까운걸 뽑으면 이기는게임
from random import randint

print("Welcome to the PyCasino")
# user_choice  = int(input("Enter a number: "))
pc_choice = randint(1, 50)
# user_choice = int(input("Enter a number: "))
user_choice = 0
# print(pc_choice)

while user_choice != pc_choice:
    user_choice = int(input("Choose a number (1~50) : "))
    if user_choice < pc_choice:
        # print("Higher! Computer chose..", pc_choice)
        print("Higher!")
    elif user_choice > pc_choice:
        # print("Lower! Computer chose..", pc_choice)
        print("Lower!")

print("You won!")
