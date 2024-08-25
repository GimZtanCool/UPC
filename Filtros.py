# Leer la entrada desde un archivo
with open('input.txt', 'r') as file:
    lines = file.readlines()

index = 0

# Tamaño de la matriz
matrix_size = int(lines[index].strip())
index += 1

# Lectura de la matriz de entrada
matrix = []
for i in range(matrix_size):
    row = list(map(int, lines[index].strip().split()))
    matrix.append(row)
    index += 1

# Tipo de filtro
filter_type = int(lines[index].strip())
index += 1

# Tamaño del filtro
filter_size = int(lines[index].strip())
index += 1

# Lectura del filtro
filter_matrix = []
for i in range(filter_size):
    row = list(map(int, lines[index].strip().split()))
    filter_matrix.append(row)
    index += 1
# Lectura del divisor
divisor = int(lines[index].strip())
index+=1

#Lectura del rescalado
rescalate = int(lines[index].strip())
index+=1

# Aplicación del filtro de mediana
resulting_matrix = []
if filter_type == 2:
    for i in range(matrix_size):
        row = []
        for j in range(matrix_size):
            auxiliary_matrix = []
            for x in range(filter_size):
                for y in range(filter_size):
                    ni = i + x - filter_size // 2
                    nj = j + y - filter_size // 2
                
                    # Verificar si el índice está dentro de los límites de la matriz original
                    if 0 <= ni < matrix_size and 0 <= nj < matrix_size:
                        auxiliary_matrix.append(matrix[ni][nj])

            auxiliary_matrix.sort()
            size = len(auxiliary_matrix)
            row.append(auxiliary_matrix[size//2] if size%2!=0 else round((auxiliary_matrix[size//2]+auxiliary_matrix[size//2-1])/2))
        resulting_matrix.append(row)
elif filter_type==1: 
    for i in range(matrix_size):
        row = []
        for j in range(matrix_size):
            sum = 0
            for x in range(filter_size):
                for y in range(filter_size):
                    ni = i + x - filter_size // 2
                    nj = j + y - filter_size // 2
                
                    # Verificar si el índice está dentro de los límites de la matriz original
                    if 0 <= ni < matrix_size and 0 <= nj < matrix_size:
                        sum+=matrix[ni][nj]*filter_matrix[x][y]
            row.append(round(sum/divisor))
        resulting_matrix.append(row)
else:
    print("asdf")

print("Matriz resultante después de aplicar el filtro de mediana:")
for row in resulting_matrix:
        print(row)

if rescalate:
    # Encontrar los valores máximo y mínimo en la matriz resultante
    abs_max = max(max(row) for row in resulting_matrix)
    abs_min = min(min(row) for row in resulting_matrix)

    # Coeficiente de escalado
    m = 7 / (abs_max - abs_min)
    b = -m * abs_min

    # Aplicar la escalación
    rescalated_matrix = []
    for i in range(matrix_size):
        row = []
        for j in range(matrix_size):
            rescalated_value = m * resulting_matrix[i][j] + b
            row.append(round(rescalated_value))
        rescalated_matrix.append(row)

    print("Matriz rescalada:")
    for row in rescalated_matrix:
        print(row)
