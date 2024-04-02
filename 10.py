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


class Segment:
    def __init__(self, first, second, inter):
        self.start = first
        self.finish = second
        self.one_intersection = inter

    def __str__(self):
        return f'Отрезок,имеющий координаты: {self.start}, {self.finish}.Признак пересекаемости:{self.one_intersection}'

    def __repr__(self):
        return self.__str__()


class CoordinateSystem:
    def __init__(self, segments):
        self.segments = segments

    def add_segment(self, segment):
        self.segments.append(segment)

    def axis_intersection(self):
        count = 0
        for i in range(len(self.segments)):
            if self.segments[i].one_intersection:
                x1 = self.segments[i].start.get_x()
                x2 = self.segments[i].finish.get_x()
                y1 = self.segments[i].start.get_y()
                y2 = self.segments[i].finish.get_y()
                if (x1 * x2 >= 0 >= y1 * y2 or x1 * x2 <= 0 <= y1 * y2) and not (x1 * x2 == 0 and y1 * y2 == 0):
                    count += 1
        return count

    def __str__(self):
        return f'Плоскость, имеющая отрезки: {self.segments}'

    def __repr__(self):
        return self.__str__()

'''
a1 = Point((1, 2))
a2 = Point((2, 3))
s1 = Segment(a1,a2,True)
b1 = Point((0, 3))
b2 = Point((-1, 2))
s2 = Segment(b1,b2,True)
c = CoordinateSystem([s1,s2])
print(c.axis_intersection())
'''
