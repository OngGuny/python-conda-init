# 문자열 안에 변수를 넣는 기능

my_name = "Neo"
my_age = 33
my_color_eyes = "blue"

# 3개의 변수를 string 한개로 합치고싶다면
# f 는 format 약자
print(f"Hello I'm {my_name}, my age is {my_age}, my color is {my_color_eyes}")
print("Hello I'm {my_name}, my age is {my_age}, my color is {my_color_eyes}")


# 이제 본격적인 recap 주스메이커만들기 recap return

def make_juice(fruit):
    return f"{fruit} +🥤🥤"


def add_ice(juice):
    return f"{juice}+🧊"


def add_sugar(iced_juice):
    return f"{iced_juice}+🍬"


juice = make_juice("🍎")
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)

print(perfect_juice)
