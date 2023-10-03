from random import randint

chips = 100

while chips > 0 :
    input ('Нажми клавишу чтобы переиграть ')
    player_1 = randint (2, 12)
    player_2 = randint (2, 12)
    print ('Игрок выбросил', player_1)
    print ('Компьютер выбросил', player_2)
    if player_1 > player_2:
        print ('Вы победили')
        chips = chips + 25
        print ('У тебя осталось', chips, 'фишек')
    elif player_2 > player_1:
        print ('Компьютер победил')
        chips = chips - 25
        print ('У тебя осталось', chips, 'фишек')
    else :
        print ('Ничья')
    
print ('Ты все проиграл')
