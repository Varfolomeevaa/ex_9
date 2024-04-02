class Dog:
    '''
    Class of dogs.
    '''

    def __init__(self, name):
        self.name = name

    @classmethod
    def say(cls):
        print('Гав!')

    def __str__(self):
        return f'Собачка: {self.name}'

    def __repr__(self):
        return self.__str__()
