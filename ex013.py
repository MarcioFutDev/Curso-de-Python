num = int(input('Digite um numero: '))
cont = 0
while cont <=10:
    print(f'{num} X {cont} = ', '\033[36m',num*cont,'\033[m')
    cont+=1
