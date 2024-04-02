class TrafficLight:
    permissible_values = ['зелёный', 'жёлтый', 'красный']

    def __init__(self):
        self.current_signal = 'зелёный'
        self.previous_signal = 'зелёный'

    def next_signal(self):
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
        return f'Текущий цвет: {self.current_signal}'

    def __repr__(self):
        return self.__str__()


a1 = TrafficLight()
print(a1)
for i in range(6):
    a1.next_signal()
    print(a1)
