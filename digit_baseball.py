import random

sol = random.sample(range(0,10), 4)

unsolved = True

attempt = 0
while unsolved:
    attempt += 1
    answer = input('Enter a 4 digit number :')
    try:
        answer = list(map(int, answer))
        
    except:
        print('!!!! Your answer is not a 4 digit number')
        continue
        
    if len(answer) != 4:
        print('!!!! Your answer is not a 4 digit number')
        continue
    
    if len(set(answer)) != 4:
        print('!! There are overlapping digits')
        continue
    
    ball = 0
    strike = 0
    for i, a in enumerate(answer):
        for j, b in enumerate(sol):
            if a == b:
                if i == j:
                    strike += 1
                else:
                    ball += 1

    if strike == 4:
        unsolved = False
        print(f'correct! You tried {attempt} times')
        continue
                    
    print(f'{strike} strike, {ball} ball')