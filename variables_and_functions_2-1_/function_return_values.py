def tax_cal(money):
    return money * 0.35
# return 을 함수 밖으로 값을 내보내기 위해 사용한다. 


def pay_tax(tax):
    print("thanks you for paying", tax)


pay_tax(tax_cal(15000))