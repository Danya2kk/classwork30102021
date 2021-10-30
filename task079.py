nums = []

while True:
    number = int(input("Вводите последовательно числа: "))
    nums.append(number)
    for num in nums:
        print(num)
    if len(nums) == 3:
        option = input("Хотите оставить последнее введенное число в списке? yes/no ")
        if option == 'no':
            nums.pop(-1)
            for num in nums:
                print(num)
            continue
        if option == 'yes':
            for num in nums:
                print(num)
            break