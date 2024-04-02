class Point:
    '''
    Class for point
    '''

    def __init__(self, coord=(0, 0)):
        '''
        method for initialization
        :param coord: coordinate of point
        '''
        self.coord = coord

    def get_x(self):
        '''
        method for getting x-coordinate
        :return: x-coordinate
        '''
        return self.coord[0]

    def get_y(self):
        '''
        method for getting y-coordinate
        :return: y-coordinate
        '''
        return self.coord[1]

    def distance(self, other):
        '''
        method for defining distance
        :param other: second point
        :return: distance
        '''
        dist = ((self.get_x() - other.get_x()) ** 2 + (self.get_y() - other.get_y()) ** 2) ** 0.5
        return dist

    def sum(self, other):
        '''
        method for creating new point
        :param other: second point
        :return: new point
        '''
        x_new = self.get_x() + other.get_x()
        y_new = self.get_y() + other.get_y()
        new = Point((x_new, y_new))
        return new

    def __str__(self):
        '''
        method for string representation
        :return: string with point's coordinates
        '''
        return f'Точка, имеющая координаты: {self.coord}'

    def __repr__(self):
        '''
        method for interactive presentation
        :return: string with point's coordinates
        '''
        return self.__str__()
