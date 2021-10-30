program = ["голос", "импровизация", "что было дальше", "комедиклаб"]
for i in program:
    print(i)

program2 = input("Введите новую телепередачу: ")
index = int(input("Введите номер где она должна стоять в списке: "))

program.insert(index, program2)
print(program)