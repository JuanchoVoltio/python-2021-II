#definir la matriz


def print_matrix(matrix):
    for curr_row in matrix:
        for curr_col in curr_row:
            print(curr_col, " ", end="")
        print()

    print("-" * 8)
#End of print_matrix()

def initialize_matrix(*rows): #Only positive numbers allowed
    print(type(rows))
    print(rows)
#End of initialize_matrix()


sample_row = [6, 7, 8]

initialize_matrix([4, 3, 1], [9, 5, 2], sample_row, "Hola")

'''my_matrix = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

print_matrix(my_matrix)

#Calcular la inversa de la matriz

print_matrix(my_matrix)'''
