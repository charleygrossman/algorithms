import random

def main():
    print("Enter [q] to quit")
    print("Generate M-by-N matrices, and zero-out rows and columns that contain a zero")
    for i in range(10):
        M = random.randrange(1,10)
        N = random.randrange(1,10)
        matrix = Matrix(M,N)
        print("====Before transformaton====")
        print(matrix)
        matrix.transform()
        print("====After transformation====")
        print(matrix)

class Matrix(object):

    def __init__(self, M=0, N=0):
        self.matrix = self.generate(M, N)

    def generate(self, M, N):
        matrix = [[0]*N for i in range(M)]
        for row in matrix:
            for column in range(len(row)):
                row[column] = random.randrange(10)
        return matrix

    def transform(self):
        zero_locations = []
        for row in self.matrix:
            for column in range(len(row)):
                if row[column] == 0:
                    zero_locations.append((self.matrix.index(row), column))

        for loc in zero_locations:
            # Zero-out the row
            self.matrix[loc[0]] = [0] * len(self.matrix[loc[0]])
            # Zero-out the columns
            for row in self.matrix:
                row[loc[1]] = 0

    def __str__(self):
        retval = ""
        for row in self.matrix:
            retval += str(row) + '\n'
        return retval

    def __repr__(self):
        return "<matrix representation>"

if __name__ == "__main__": main()
