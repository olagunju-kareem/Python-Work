import random

def flip():
    numberOfStreaks = 0
    for i in range(10_000):
        choices = ['H' if random.randint(0, 1) == 0 else 'T' for x in range(100)]

        count = 1
        streakFound = False
        for i in range(1, 100):
            if choices[i] == choices[i - 1]:
                count += 1
                if count == 6:
                    streakFound = True
                    break
            else:
                count = 1
        if streakFound:
            numberOfStreaks += 1

    print(f'Chance of streak: {numberOfStreaks / 100}%')