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
        :return: string with point's info
        '''
        return self.__str__()


class Segment:
    '''
    Class of segments
    '''

    def __init__(self, first, second):
        '''
        method for initialization
        :param first: first point
        :param second: second point
        '''
        self.start = first
        self.finish = second
        x1 = self.start.get_x()
        x2 = self.finish.get_x()
        y1 = self.start.get_y()
        y2 = self.finish.get_y()
        if x1 * x2 > 0 and y1 * y2 > 0:
            self.one_intersection = False
        else:
            self.one_intersection = True

    def __str__(self):
        '''
        method for string representation
        :return: string with coordinate segment's info
        '''
        return f'Отрезок,имеющий координаты: {self.start}, {self.finish}.Признак пересекаемости:{self.one_intersection}'

    def __repr__(self):
        '''
        method for interactive presentation
        :return: string with segment's info
        '''
        return self.__str__()


class CoordinateSystem:
    '''
    Class of coordinate systems
    '''

    def __init__(self, segments):
        '''
        method for initialization
        :param segments: segments of coordinate system
        '''
        self.segments = segments

    def add_segment(self, segment):
        '''
        method for adding segment
        :param segment: segment
        :return: nothing
        '''
        self.segments.append(segment)

    def axis_intersection(self):
        '''
        method for getting amount of segments with only one intersection
        :return: count
        '''
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
        '''
        method for string representation
        :return: string with coordinate system's info
        '''
        return f'Плоскость, имеющая отрезки: {self.segments}'

    def __repr__(self):
        '''
        method for interactive presentation
        :return: string with coordinate system's info
        '''
        return self.__str__()
