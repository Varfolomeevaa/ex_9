class Dog:
    '''
    Class of dogs.
    '''

    def __init__(self, name):
        '''
        method for initialization
        :param name: name of dog
        '''
        self.name = name

    def say(self):
        '''
         method for saying hello by dog
        :return: nothing
        '''
        print('Гав!')

    def __str__(self):
        '''
        method for string representation
        :return: string with dog's name
        '''
        return f'Собачка: {self.name}'

    def __repr__(self):
        '''
        method for interactive presentation
        :return: string with dog's name
        '''
        return self.__str__()
