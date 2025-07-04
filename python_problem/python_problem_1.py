import random

def brGame():
    num = 0
    turn = "computer"

    while num < 31:
        if turn == "player":
            while True:
                
                nums = input(f"부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :")

                if not nums.isdigit():
                    print("정수를 입력하세요")
                    continue

                nums = int(nums)
                if nums not in [1,2,3]:
                    print("1,2,3 중 하나를 입력하세요")
                    continue
                
                break
        
        else:
            nums = random.randint(1,3)

        for i in range(nums):
            num+=1
            print(f"{turn}: {num}")
            
            if num >= 31:
                winner = 'computer' if turn == 'player' else 'player'
                return winner

        turn = 'computer' if turn == 'player' else 'player'

winner = brGame()
print(f"{winner} win!")