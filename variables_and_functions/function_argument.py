# 함수 들여쓰기.
# 파이썬은 빈 공백을 이용해 어떤것 안에 어떤게 있는지 이해한다....?
#뭐?
# ->print 는 첫 파이썬 함수 안에 있는거야. 라고 알려주려면, indent 가 있어야한다.
# two spaces or indent

# python 은 중괄호 블록 대신에 스페이스바 두개로 함수 범위를 결정한다.
# 넣으려면 띄우고 빼려면 안띄운다.
# def 밑에서 2spaces 면 전부 함수 내부 코드
# 당연히 4spaces 도 되네 지금은. 기본설정이니까.
def first_python_function():
    print("first python function")


first_python_function()