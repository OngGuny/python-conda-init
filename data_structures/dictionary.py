# 키 - 값 요소를 가짐.
# 중괄호 사용
player = {
    'name': ' Thwane',
    'age': 666,
    'alive': False,

}

# 앞의 list 나 tuple 은 ordered 된 배열들이라 [] 로 꺼내 올 수 있지만.
# dictionary 에서는 메소드로 가져와야 한다.
print(player)
print(player.get('age'))

# Mutable 하다.
player.pop('alive')
print(player)

player.clear()
print(player)
# 추가는 어떻게하지?

player['xp'] = 2200  # Nani?
print(player)

player['fav_food'] = ['🍊', '🍌']
print(player)
player['fav_food'].append('🥝')
print(player)

# 추가하는게 좀 특이하네.
