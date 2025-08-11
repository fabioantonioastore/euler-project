from array import array


FILE_NAME = "problem_11.txt"


def get_matrix() -> list[array]:
    matrix = []
    with open(FILE_NAME, "r") as file:
        for line in file.readlines():
            row = array("I")
            for number in line.split(" "):
                row.append(int(number))
            matrix.append(row)
    return matrix


matrix = get_matrix()

max_product = 0

for row in range(len(matrix)):
    for collumn in range(len(matrix[0])):
        p_down = 1
        p_right = 1
        p_diagonal = 1
        p_rev_diagonal = 1
        for i in range(4):
            try:
                p_down *= matrix[row + i][collumn]
            except:
                pass
            try:
                p_right *= matrix[row][collumn + i]
            except:
                pass
            try:
                p_diagonal *= matrix[row + i][collumn + i]
            except:
                pass
            try:
                p_rev_diagonal *= matrix[row - i][collumn + i]
            except:
                pass
        max_prod = max(p_diagonal, p_down, p_right, p_rev_diagonal)
        if max_prod > max_product:
            max_product = max_prod

print(max_product)
