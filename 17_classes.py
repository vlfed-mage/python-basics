class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print('draw')

    def move(self):
        print('move')


point1 = Point(10, 5)
# point1.x = 10
# point1.y = 5
print(point1.y)
point1.draw()

point2 = Point(20, 50)  # diff object


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hi, I\'m {self.name}')


woman = Person('John Smith')

woman.talk()


class Animal:
    def walk(self):
        print('walk')


class Dog(Animal):
    pass  # just for leaving this class empty


class Cat(Animal):
    def meow(self):
        print('meow')


dog = Dog()
dog.walk()

cat = Cat()
cat.walk()
cat.meow()
