num = int(input('Digite um numero: '))
cont = 0
while cont <= 10:
    print(f'\033[32m {num} \033[m X \033[33m{cont}\033[m = ', num * cont)
    cont +=1