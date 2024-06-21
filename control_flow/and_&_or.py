# 성인 나이 계산기 만들어보기

age = input("How old are you?")  # 하나의 arg 만 받는 함수, 그리고 콘솔에서 사용자가 입력을 해야 함수가 끝난다.
# input 은 built-in

print(age)
print(type(age)) # str 이 나오는데, 키보드 입력으로 받았기 때문. num 으로 변환할 필요가 있다.

age = int(age)

if age < 19:
    print("E-Eee")
else:
    print("drink!")
