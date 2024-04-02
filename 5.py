class Game:
    '''
    Class for playing basketball.
    '''

    def __init__(self, command):
        '''
        method for initialization
        :param command: dictionary with team and points
        '''
        self.command = command

    def ball_thrown(self, command, points):
        '''
        method for adding points to a team
        :param command: name of team
        :param points: number of points
        :return: nothing
        '''
        if command == 'command1':
            self.command['command1'] += points
        else:
            self.command['command2'] += points

    def get_score(self):
        '''
        method for getting score
        :return: tuple of points
        '''
        first = self.command['command1']
        second = self.command['command2']
        tpl = (first, second)
        return tpl

    def get_winner(self):
        '''
        method for defining winner
        :return: result of game
        '''
        first = self.command['command1']
        second = self.command['command2']
        if first > second:
            return 'command1'
        elif second > first:
            return 'command2'
        else:
            return 'Ничья'

    def __str__(self):
        '''
        method for string representation
        :return: string with teams' info
        '''
        return f'Команды: {self.command}'

    def __repr__(self):
        '''
        method for interactive presentation
        :return: string with teams' info
        '''
        return self.__str__()
