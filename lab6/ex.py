def matrix_indx_power_scenario():
    with open('lab6/matrix.txt', 'r') as f:
        matrix = []
        for i, line in enumerate(f.readlines()):
            matrix.append([int(x)**(i+1) for x in line.split()])
    print(matrix)

if __name__ == "__main__":
    matrix_indx_power_scenario()