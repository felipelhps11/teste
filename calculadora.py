not_stop = True

while not_stop == True:
    try:
        num_one = float(input("Digite o primeor número: "))
        num_two = float(input("Digite o primeor número: "))
        operation = input("Qual operação que desejas\n soma ")

        if operation == 'soma':
            print(num_one + num_two if operation == 'soma' else None)
    except ValueError:
        print("Só aceitamos Número :) ")