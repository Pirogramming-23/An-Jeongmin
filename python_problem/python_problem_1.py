num = 0

while True:
    nums = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :")

    if not nums.isdigit():
        print("정수를 입력하세요")
        continue

    nums = int(nums)
    if nums not in [1,2,3]:
        print("1,2,3 중 하나를 입력하세요")
        continue

    break

for i in range(1, nums+1):
    num+=1
    print(f"playerA : {num}")
