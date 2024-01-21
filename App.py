from random import randint

n, m = 2, 60
num = randint(n,m)

print("Програма загадала число від 2 до 60")

p = int(input("Вгадай число:"))

while p != num:
    if p < num:
        print("Моє число більше, спробуй ще!")
    if p > num:
        print("Моє число менше, спробуй ще!")
    
    p = int(input("Вгадай число:"))


print("Так, ти вгадав, це число", num)
