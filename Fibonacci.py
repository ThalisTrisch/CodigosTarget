Num = int(input(" digite um número para verificar se ele está na sequência de Fibonacci: "))
Penultimo = 0;
Ultimo = 0;
Proximo = 0;
FibonacciNums = [];

while(Num > Ultimo):
    if(Ultimo == 0):
        FibonacciNums.append(0)
        Ultimo = 1
    elif(Ultimo == 1):
        FibonacciNums.append(1)
    Proximo = Ultimo+Penultimo;
    FibonacciNums.append(Proximo)
    
    Penultimo = Ultimo
    Ultimo = Proximo
    
    # print(Ultimo)
    # print(Penultimo,"\n")
    
if(Ultimo == Num):
    print("\n O número",Num,"pertence à sequencia de fibonacci")
else:
    print("\n O número digitado não está sequência de Fibonacci")
# print(FibonacciNums)
    

