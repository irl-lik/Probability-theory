import random

wins = 0
loses = 0

def get_ratio(a: int, b: int) -> float:
    a, b = max(a, 1), max(b, 1)
    return a / (a + b) * 100

def main() -> None:
    global wins, loses
    # Выбираем правильную дверь
    true_ans = random.choice([1, 2, 3])
    # Угадываем дверь
    user_choice = random.choice([1, 2, 3])
    
    remaining_doors = [door for door in [1, 2, 3] if door != user_choice and door != true_ans]
    # Ведущий открывает пустую дверь
    host_opened_door = random.choice(remaining_doors)
    # Получаем возможность поменять дверь или нет
    # Меняем свой выбор (Теоритический шанс на победу до смены двери: 33%. Теоритический шанс на победу после смены двеир: 66%)
    final_choice = [door for door in [1, 2, 3] if door != user_choice and door != host_opened_door][0]
    
    if final_choice == true_ans:
        wins += 1
    else:
        loses += 1
    
    print(f"Wins: {wins}  :  Loses: {loses}  :  Win ratio: {get_ratio(wins, loses):.2f}%")
    
for i in range(100):
    main()
