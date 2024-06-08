def say_hello(user_name): # parameter
    print("hello",user_name,"how r u?")


say_hello("GaoGaiGa") # argument

# 파라미터란 함수가 생성될 때, 데이터가 들어갈 공간을 만들어 주는것
# 파라미터는 역시 함수 안에서만 유효하다. 두칸띄워야지만 유효해.

say_hello("Jojo")

# 근데 , 로 한칸 띄워지는게 되네?


#Take 2 : Multiple Parameters

# print 함수처럼 파라미터 여러개 넣고싶어.
# 파라미터는 함수로 전달하는 데이터를 저장하기 위한 그릇(placeHolder)
#
def say_hello(user_name, user_age):
    print("hello",user_name)
    print("you are",user_age,"years old.")


say_hello("Son", 12)
# 파라미터는 무한으로 사용할수 있어. 그런데 그러지 않고 * 를 사용해.
# 무한한 파라미터들을 받을 수도 있게 만들어 놨다. 나중에.