not_stop = True

while not_stop == True:
    try:
        num_one = float(input("Digite o primeor número: "))
        num_two = float(input("Digite o primeor número: "))
        operation = input("Qual operação que desejas\n soma \n subtracao \n multiplicacao \n divisao ")

        if operation == 'soma':
            print(num_one + num_two)

        elif operation == 'subtracao':
            print(num_one - num_two)
            
        elif operation == 'multiplicacao':
            print(num_one * num_two)

        elif operation == 'divisao':
            if num_two == 0:
                print("Não dividimos por 0..")
            
            else:
                print(num_one / num_two)
            
        repetir = input("Desejas continuar [S]im ou [N]ão")

        if repetir == 'S':
            ...
        else:
            print("Obrigado, Volte Sempre !! :)")
            break
    except ValueError:
        print("Só aceitamos Número :) ")