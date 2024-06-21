# Method 는 함수랑 다를게 없다 거의.  다만 호출하는 주체가 있어야 한다.
# 저게 쿤 차이점.
days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print(days_of_week.count("Wed"))
# days_of_week.clear()  # List 를 직접적으로 수정(Modify) 함. === Mutate 변경.
days_of_week.reverse()
print(days_of_week)

days_of_week.append("Rest")

print(days_of_week)

days_of_week.append("Rest2")
print(days_of_week)

days_of_week.remove("Rest")
print(days_of_week)
