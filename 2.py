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

    def __str__(self):
        return f'Человек, пытающийся заснуть: {self.name}'

    def __repr__(self):
        return self.__str__()
