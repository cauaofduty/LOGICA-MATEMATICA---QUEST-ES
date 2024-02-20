numero = int(input("Digite um número: "))

if numero % 2 == 1 and (numero ** 2) % 2 == 1:
    print("O quadrado de", numero, "é ímpar e", numero, "também é ímpar.")
else:
    print("Condição não atendida.")