import random


class NotSleeping:
    '''
    Class for person that is not sleeping
    '''

    def __init__(self, name):
        self.name = name
        self.sheep = 0

    def add_sheep(self):
        '''
        Method for counting sheep.
        :return: count of sheep
        '''
        self.sheep += 1

    def lost(self):
        number = random.randint(1, 50)
        if self.sheep == number:
            self.sheep = 0

    def get_count_sheep(self):
        return self.sheep

    def __str__(self):
        return f'Человек, пытающийся заснуть: {self.name}'

    def __repr__(self):
        return self.__str__()


person = NotSleeping('Vika')
for i in range(50):
    person.add_sheep()
    person.lost()
    print(person.get_count_sheep())

