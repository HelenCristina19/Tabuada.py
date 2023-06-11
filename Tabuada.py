#Receba um número (inteiro ou decimal)
#Mostre a tabuada desse número

numero = float(input("Digite um número: "))

for fator in range(1,11):
    print(f"{numero} x {fator} = {numero*fator}".replace(".0",""))