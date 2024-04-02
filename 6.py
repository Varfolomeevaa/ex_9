class Point:
    '''
    Class for point
    '''

    def __init__(self, coord=(0, 0)):
        self.coord = coord

    def get_x(self):
        return self.coord[0]

    def get_y(self):
        return self.coord[1]

    def distance(self, other):
        dist = ((self.get_x() - other.get_x()) ** 2 + (self.get_y() - other.get_y()) ** 2) ** 0.5
        return dist

    def sum(self, other):
        x_new = self.get_x() + other.get_x()
        y_new = self.get_y() + other.get_y()
        new = Point((x_new, y_new))
        return new

    def __str__(self):
        return f'Точка, имеющая координаты: {self.coord}'

    def __repr__(self):
        return self.__str__()


'''
pnt_1 = Point((2,4))
print(pnt_1)
print(pnt_1.get_x())
pnt_2 = Point()
print(pnt_1.distance(pnt_2))
print(pnt_1.sum(pnt_2))
'''
