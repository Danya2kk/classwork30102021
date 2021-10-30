inviteList = []

for i in range(3):
    inviteList.append(input("Введите имя человека которого хотите пригласить: "))

while True:
    option = input("Хотите кого-то пригласить еще yes/no: ")
    if option == "yes":
        newName = input("Введите имя приглашенного: ")
        inviteList.append(newName)
    elif option == "no":
        break

for name in inviteList:
    print(name)

nameIndex = input("Введите одно из имен в списке: ")
print("Номер имени в списке", inviteList.index(nameIndex))

option2 = input("Хотите чтобы этот человек присуствовал на вечиринке? yes/no ")
if option2 == 'no':
    inviteList.remove(nameIndex)
    for name in inviteList:
        print(name)
elif option2 == 'yes':
    for name in inviteList:
        print(name)
