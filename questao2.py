texto = input()

quantidadeAs = 0

#Daria pra utilizar funções nativas do Python, mas gostaria de deixar algo mais genérico.
for i in range(len(texto)):
    if (texto[i] == 'a' or texto[i] == 'A' 
        or texto[i] == 'á' or texto[i] == 'Á' 
        or texto[i] == 'à' or texto[i] == 'À' 
        or texto[i] == 'ã' or texto[i] == 'Ã' 
        or texto[i] == 'â' or texto[i] == 'Â'):
        quantidadeAs += 1

if quantidadeAs == 0:
    print("Nao ha letras 'a' ou 'A' no texto")
else:
    print(f"A quantidade de letras 'a' ou 'A' no texto eh: {quantidadeAs}")