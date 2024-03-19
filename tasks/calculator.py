# 덧셈 뺼셈 , 나눗셈, 제곱, 파라미터 없는 경우
def plus(a=0, b=0):
    return a + b


def minus(a=0, b=0):
    return a - b


def divide(a=1, b=1):
    return a / b if a > b else 0 if b == 0 else 0


def multiply(a=1, b=1):
    return a * b


def power(a=1, b=0):
    #for b ==0  # 반복문...?
    return a ^ b if b == 0 else 1


print(power(2, 3))
