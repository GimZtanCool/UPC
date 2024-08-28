#array global donde se almacenaran los pares que suman el valor indicado
sensor_equal_max_value = []

#este es el venceras, donde se recibe un subarreglo derecha e izquierda, luego se ordenan pues al ordenarse
#podemos ir sabiendo en que posiciones los pares sin van a sumar el valor indicado
#y luego se verifica iterando con cada uno de los numeros sumando ambos y verificando si suman el indicado, si se cumple se agrega la pareja
#de numeros a un arreglo que sirve para almacenar sus valores y mostrarlos en pantalla
#si la suma es menos significa que los numeros de la derecha (es decir los que son mayores a esos) puede ser que si sumen el valor indicado
#y no los de la izquierda (que son menores)
def count_cross_pairs(left, right, x):
    left.sort()
    right.sort()
    i = 0
    j = len(right) - 1
    count = 0

    while i < len(left) and j >= 0:
        if left[i] + right[j] == x:
            sensor_equal_max_value.append((left[i],right[j]))
            i += 1
            j -= 1
        elif left[i] + right[j] < x:
            i += 1
        else:
            j -= 1

#este es el divide, donde recibimos el arreglo y el valor que buscamos que los pares sumen
#se divide el arreglo en 2 y se usa recursividad para ir diviendo los arregllos hasta que sean de tamaño 1
def count_pairs_divide_and_conquer(arr, x):
    n = len(arr)
    if n < 2:
        return 0
    
    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]

    #la parte izquierda
    count_left = count_pairs_divide_and_conquer(left, x)
    
    #la parte derecha
    count_right = count_pairs_divide_and_conquer(right, x)

    #este es el venceras que la se mostro arriba
    count_cross = count_cross_pairs(left, right, x)

    
def main():
    #ingreso de datos
    #con split divido una fila de numeros a numeros independientes, pero son strings 
    input_list = input().split(", ")
    #aqui se convierte esos strings a int
    sensor_values = [int(num) for num in input_list]
    max_value = int(input())
    
    count_pairs_divide_and_conquer(sensor_values,max_value)
    print("El número de pares que suman ", max_value, " es: ",len(sensor_equal_max_value))
    print("Los pares de sensores son: {")
    for i in range(len(sensor_equal_max_value)):
        print("(",sensor_equal_max_value[i][0],",",sensor_equal_max_value[i][1],"), ")
    print("}")

if __name__ == "__main__":
    main()




