class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        result = Cell(self.cells + other.cells)
        return result

    def __sub__(self, other):
        if self.cells < other.cells:
            print('Вычитание невозможно')
        else:
            result = Cell(self.cells - other.cells)
            return result

    def __mul__(self, other):
        result = Cell(self.cells * other.cells)
        return result

    def __truediv__(self, other):
        result = Cell(self.cells // other.cells)
        return result

    def make_order(self, n):
        result = []
        for i in range(self.cells // n):
            result.append('*'*n + '\n')
        result.append('*'*(self.cells % n))
        return ''.join(result)


if __name__ == '__main__':
    a = Cell(5)
    b = Cell(25)
    c = Cell(13)
    g = a/b
    d = a*b*c
    e = a+b+c
    f = b-a-c
    print(g.cells, d.cells, e.cells, f.cells)
    print(a.make_order(2))
    print(b.make_order(6))
