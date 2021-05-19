print(True)
print(False)


print(1 < 2)
print(2 < 1)

print(1 <= 2)
print(2 <= 1)

print(1 == 1)
print(1 != 1)


print("You're win! True or False?")
win = bool(input("if you're lose, Just press enterKey"))
if win:
    print("게임에서 승리하였습니다")
else:
    print("게임에서 패배하였습니다")

a = int(input('A팀 스코어: '))
b = int(input('B팀 스코어: '))
if a > b:
    print("A팀 승리")
elif b > a:
    print("B팀 승리")
else:
    print("무승부")

pokemons = ['파이리', '꼬북이', '이상해씨', '피카츄']
print("여기는 태초마을! 함께 여정을 떠날 첫번재 포켓몬을 선택하자")
num = int(input("1.불 2.물 3.풀 4.전기 : "))
if (num <= 0) | (num >= 5):
   print("숫자를 잘못 입력했습니다.")
else:
   print("당신과 여정을 떠날 포켓몬은 " + pokemons[num-1] +"입니다.")

pokemons = ['피카츄', '파이리', '꼬북이']
for pokemon in pokemons:
    print(pokemon)
for letter in '잠만보':
    print(letter)

for num in range(3):
    print(f"피카츄 {num}마리")

pokemons = ['피카츄', '파이리', '꼬부기']
for num in range(3):
    pokemons[num] = "이브이"
print(pokemons)
print(num)

num = 0
while num < 3:
    print(f'이상해씨가 {num}일째 씨 뿌리는 중')
    num = num + 1
print("다 심었다!")

from random import randint

print("로켓단이 나타났다! '피카츄' 로 로켓단을 무찌르자!")
pi_hp = 10 # 피카츄, 로켓단의 HP
ro_hp = 10

while True:

   if pi_hp <= 0:
       print("'피카츄'가 쓰러졌다!")
       break

   elif ro_hp <= 0:
       print("'로켓댠'이 쓰러졌다!")
       break

   else:
       print("'피카츄'가 시도할 공격을 선택하세요.")
       num1 = int(input("1.몸통박치기 2.아이언테일 3.백만볼트 : "))
       num2 = randint(1, 3)
       print(f"피카츄가 공격했다! 로켓단은 -{num1}의 데미지를 입었다.")
       ro_hp -= num1
       print(f"로켓단이 공격했다! 피카츄는 -{num2}의 데미지를 입었다.")
       pi_hp -= num2
       #continue