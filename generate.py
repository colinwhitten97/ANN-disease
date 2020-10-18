from random import randint
import pandas as pd
smokers = []
ages = []
exercise = []
serious = []
population = 80

for i in range(population):
    smoke = randint(0,100)
    if smoke <= 35:
        count = 1
    elif smoke > 35:
        count = 0
    smokers.append(count)

for i in range(population):
    value = randint(0,100)
    if value >= 70:
        age = 1
    else:
        age = 0

    ages.append(age)

for i in range(population):
    runs = randint(0,1)
    exercise.append(runs)

for i in range(population):
    if ages[i] >= 70:
        if smokers[i] == 1:
            chance = randint(0,12)
        elif smokers[i] == 0:
            chance = randint(0,15)
    elif ages[i] < 70:
        if smokers[i] == 1:
            chance = randint(0,80)
        elif smokers[i] == 0:
            chance = randint(0,150)
    if chance <= 10:
        case = 1
    elif chance > 10:
        case = 0
    serious.append(case)


    
cases = {'Age': ages, 'Smoker': smokers, 'Exercise': exercise, 'Serious': serious}

df = pd.DataFrame(cases, columns = ['Age', 'Smoker', 'Exercise', 'Serious'])
df.to_csv (r'export1.csv', index = False, header = True)
    


