class Matrix(object):

    def __init__(self, matrix):
        self.matrix = matrix

    def invert(self):  # this function returns inverted matrix in the form of list of lists - where each row in the matrix is a list inside the parent list.
        new_matrix = []
        for i in range(len(matrix[0])):
            new_matrix.append([])
        row = 0
        column = 0
        new_matrix_row = 0
        for lst in matrix:
            for number in lst:
                new_matrix[new_matrix_row].append(matrix[row][column])
                column += 1
                new_matrix_row += 1
            row += 1
            column = 0
            new_matrix_row = 0
        return new_matrix

# Main program

with open('in.csv', 'r') as f:
    with open('out.csv', 'w') as f_out:
        matrix = [line.replace('\n','').replace(',','').split(' ') for line in f.readlines()] ## create matrix from file, and getting rid of new lines and spaces.
        rix = Matrix(matrix)  # create new Matrix object
        rix_inverted = rix.invert()  # call function invert() from Matrix class
        for lst in rix_inverted:  # write output to file out.csv
            for number in lst:
                f_out.write(number+', ')
            f_out.write('\n')
