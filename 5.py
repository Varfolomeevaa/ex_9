class Game:
    '''
    Class for playing basketball.
    '''

    def __init__(self, command):
        self.command = command

    def ball_thrown(self, command, points):
        if command == 'command1':
            self.command['command1'] += points
        else:
            self.command['command2'] += points

    def get_score(self):
        first = self.command['command1']
        second = self.command['command2']
        tpl = (first, second)
        return tpl

    def get_winner(self):
        first = self.command['command1']
        second = self.command['command2']
        if first > second:
            return 'command1'
        elif second > first:
            return 'command2'
        else:
            return 'Ничья'

    def __str__(self):
        return f'Команды: {self.command}'

    def __repr__(self):
        return self.__str__()
