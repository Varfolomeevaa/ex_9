class StrandsDNA:
    def __init__(self, strands):
        self.all_strands = strands

    def add_strands(self, strands):
        self.all_strands.append(strands.split())

    def get_max_strands(self):
        ptr_lst = []
        max_len = 0
        ptr = ''
        for i in range(len(self.all_strands)):
            if len(self.all_strands[i]) >= max_len:
                max_len = len(self.all_strands[i])
                for j in range(len(ptr_lst)):
                    if len(ptr_lst[j]) != max_len:
                        ptr_lst.pop(j)
                if self.all_strands[i] not in ptr_lst:
                    ptr_lst.append(self.all_strands[i])
        ptr_lst.sort()
        for i in ptr_lst:
            ptr = ptr + i + ' '
        return ptr

    def __str__(self):
        return f'Цепочка ДНК: {self.all_strands}'

    def __repr__(self):
        return self.__str__()


'''
a1 = StrandsDNA(['ABCD', 'ADC', 'AD', 'ADDC', 'RTH', 'ABCD', 'ABHE'])
print(a1.get_max_strands())
'''
