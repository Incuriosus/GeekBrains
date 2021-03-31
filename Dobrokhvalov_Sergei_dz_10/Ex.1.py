class Matrix:
    def __init__(self, matrix):
        if isinstance(matrix, list):
            chek_list = [i for i in matrix if isinstance(i, list)]
            if len(chek_list) == len(matrix):
                for idx in range(len(matrix)):
                    chek_list = [i for i in matrix[idx] if isinstance(i, int)]
                    if len(chek_list) == len(matrix[idx]) == len(matrix[idx - 1]):
                        continue
                    else:
                        raise ValueError('Матрица задана неверно')
                self.matrix = matrix
            else:
                raise ValueError('Матрица должна содержать только списки')
        else:
            raise ValueError('Матрица должна быть передана в виде списка')

    def __str__(self):
        result = []
        for i in self.matrix:
            i_str = []
            for j in i:
                i_str.append(str(j))
            result.append(' '.join(i_str))
        return '\n'.join(result)

    def __iter__(self):
        return (el for el in self.matrix)

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            result = Matrix([[self.matrix[i][j]+other.matrix[i][j] for j in range(len(self.matrix[i]))]
                             for i in range(len(self.matrix))])
            return result
        else:
            raise ValueError('Матрицы разной размерности')


if __name__ == '__main__':
    matrix_1 = Matrix([[1, 2, 3, 4], [3, 4, 5, 6]])
    matrix_2 = Matrix([[4, 3, 2, 1], [6, 5, 4, 3]])
    matrix_3 = Matrix([[1, 3, 5, 7], [7, 5, 3, 1]])
    print(matrix_1)
    print(matrix_2)
    print(matrix_1 + matrix_2 + matrix_3)
