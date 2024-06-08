# if elif else

# 연산자
#: < > <= >= == !=

winner_point = 49
# 10, 50, 25, 50
if winner_point != 49:  # 여기도 바꿔가면서 테스트
    print("정확한 10점이 아니에요")
elif winner_point <= 25:
    print("좀더 노력")
elif winner_point <= 49:
    print("Almost!")
else:
    print("무슨점수야 이게!")
