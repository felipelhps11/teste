not_stop = True

while not_stop == True:
    try:
        num_one = float(input("Digite o primeor número: "))
        num_two = float(input("Digite o primeor número: "))
        operation = input("Qual operação que desejas\n soma \n subtracao ")

        if operation == 'soma':
            print(num_one + num_two)

        elif operation == 'subtracao':
            print(num_one - num_two)
            
    except ValueError:
        print("Só aceitamos Número :) ")