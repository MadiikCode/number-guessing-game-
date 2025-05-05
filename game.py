import random


random_dev = random.randint(1,100)
k = 0


while True:
    user_dev = int(input('Угадай число от 1 до 100! :'))


    if  user_dev > random_dev:
        print(f"Меньше,вы сделали {k+1} попыток")
    elif user_dev < random_dev:
        print(f"Больше,вы сделали {k+1} попыток")
    else:
     print(f"Вы нашли. Число была равно {random_dev} ")
     break

k +=1