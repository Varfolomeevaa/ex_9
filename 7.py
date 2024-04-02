class TrafficLight:
    '''
    Class for traffic lights
    '''
    permissible_values = ['зелёный', 'жёлтый', 'красный']

    def __init__(self):
        '''
        method for initialization
        '''
        self.current_signal = 'зелёный'
        self.previous_signal = 'зелёный'

    def next_signal(self):
        '''
        method for defining new colour
        :return: nothing
        '''
        if self.current_signal == 'зелёный':
            self.current_signal = 'жёлтый'
            self.previous_signal = 'зелёный'

        elif self.current_signal == 'жёлтый':

            if self.previous_signal == 'зелёный':
                self.current_signal = 'красный'
                self.previous_signal = 'жёлтый'

            else:
                self.current_signal = 'зелёный'
                self.previous_signal = 'жёлтый'

        else:
            self.current_signal = 'жёлтый'
            self.previous_signal = 'красный'

    def __str__(self):
        '''
        method for string representation
        :return: string with current colour
        '''
        return f'Текущий цвет: {self.current_signal}'

    def __repr__(self):
        '''
        method for interactive presentation
        :return: string with current colour
        '''
        return self.__str__()
