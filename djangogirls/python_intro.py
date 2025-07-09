#코드 저장하기!
print('Hello, Django girls!')

#If...elif...else
if 3 > 2:
    print('It works!')

#조건이 참(True) 이 아니라면 어떻게 되나요?
if 5 > 2:
    print('5 is indeed greater than 2')
else:
    print('5 is not greater than 2')

name = 'Sonja'
if name == 'Ola':
    print('Hey Ola!')
elif name == 'Sonja':
    print('Hey Sonja!')
else:
    print('Hey anonymous!')

volume = 57
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")

#주석
# volume 값을 바꿔보세요
if volume < 20 or volume > 80:
    volume = 10
    print("That's better!")

#나만의 함수 만들기!
def hi():
    print('Hi there!')
    print('How are you?')

hi()

def hi(name):
    if name == 'Ola':
        print('Hi Ola!')
    elif name == 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymous!')

hi("Ola")
hi("Sonja")
hi("anonymous")

def hi(name):
    print('Hi ' + name + '!')

hi("Rachel")

def hi(name):
    print('Hi ' + name + '!')

#반복하기
girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi(name)
    print('Next girl')

for i in range(1, 6):
    print(i)