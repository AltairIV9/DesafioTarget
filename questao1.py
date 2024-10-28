numero = int(input())

aux1 = 0
aux2 = 1

while aux1 + aux2 <= numero:
    if aux1 + aux2 == numero:
        print(f"O numero {numero} pertence a sequencia de Fibonacci")
        break
    
    aux = aux1
    aux1 = aux2
    aux2 = aux + aux1

if aux1 + aux2 != numero:
    print(f"O numero {numero} nao pertence a sequencia de Fibonacci")
    