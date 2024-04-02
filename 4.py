class User:
    '''
    Class of users.
    '''

    def __init__(self, id, nick_name, first_name, last_name=None, middle_name=None, gender=None):
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender

    def __str__(self):
        return (f'ID: {self.id}, Псевдоним: {self.nick_name}, Имя: {self.first_name}, Фамилия: {self.last_name}, '
                f'Отчество: {self.middle_name}, Пол: {self.gender}')

    info = ['id', 'nick_name', 'first_name', 'last_name', 'middle_name', 'gender']

    def update(self):
        print('Что вы хотите обновить?')
        inf = User.info
        for i in range(len(inf)):
            print(i, User.info[i])
        flag = False
        while not flag:
            try:
                answer = int(input('Введите нужную цифру: '))
                par = inf[answer]
                new = input('Введите новое значение: ')

                if par == 'id':
                    self.id = new
                elif par == 'nick_name':
                    self.nick_name = new
                elif par == 'first_name':
                    self.first_name = new
                elif par == 'last_name':
                    self.last_name = new
                elif par == 'middle_name':
                    self.middle_name = new
                else:
                    self.gender = new

                flag = True
            except:
                print('Ошибка! Попробуйте ещё раз')

    def __repr__(self):
        return self.__str__()
