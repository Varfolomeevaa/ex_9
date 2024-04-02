class NotSleeping:
    '''
    Class for person that is not sleeping
    '''

    def __init__(self, name):
        '''
        method for initialization
        :param name: name of person
        '''
        self.name = name
        self.sheep = 0

    def add_sheep(self):
        '''
        Method for counting sheep.
        :return: nothing
        '''
        self.sheep += 1

    def __str__(self):
        '''
        method for string representation
        :return: string with person's name
        '''
        return f'Человек, пытающийся заснуть: {self.name}'

    def __repr__(self):
        '''
        method for interactive presentation
        :return: string with person's name
        '''
        return self.__str__()
