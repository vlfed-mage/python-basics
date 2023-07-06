import random

for i in range(3):
    print(random.random())  # random from 0 to 1

# 0.5822023277763815
# 0.8766765563201582
# 0.31610587860151595

print(random.randint(10, 20))  # random from 10 to 20

members = ['John', 'Mary', 'Vlad', 'Bob']
leader = random.choice(members)
print(leader)  # Vlad


class Dice:
    def roll(self, start, end):
        # when you want to return a tuple from a function you don't have to add parenthesis
        return random.randint(start, end), random.randint(start, end)


dice = Dice()
print(dice.roll(1, 10))
