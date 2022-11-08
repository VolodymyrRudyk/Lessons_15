import random
print(random.random())          #випадкове число с плаваючою крапкою від 0 до 1
print(random.randint(1, 10))    #випадкове число від 1 до 10
print(random.randint(1, 10))

print(random.choice(['Life of Brain', 'Holy Grail', 'Meaning of Life']))
print(random.choice(['Life of Brain', 'Holy Grail', 'Meaning of Life']))

suits = ['hearts', 'clubs', 'diamonds', 'spades']
random.shuffle(suits)
print(suits)

random.shuffle(suits)
print(suits)