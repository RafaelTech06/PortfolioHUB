import random

# Letra a: Gerar 20 números aleatórios de -2 até 2
print("Letra a:")
for i in range(20):
    numero = random.randint(-2, 2)
    print(numero)

# Letra b: Gerar 12 números aleatórios de 1 até 6, sem usar variável intermediária
print("\nLetra b:")
for i in range(12):
    print(random.randint(1, 6))

# Letra c: Somar 12 números aleatórios de 1 a 6
print("\nLetra c:")
soma = 0
for i in range(12):
    numero = random.randint(1, 6)
    soma += numero
    print(numero)
print("Soma dos números:", soma)

# Letra d: Contar quantas vezes cada número de 1 a 6 aparece em 60 sorteios
print("\nLetra d:")
contagem = [0, 0, 0, 0, 0, 0]
for i in range(60):
    numero = random.randint(1, 6)
    contagem[numero - 1] += 1
    print(numero)

for i in range(6):
    print(f"Número {i + 1} apareceu {contagem[i]} vezes")

# Letra e: Calcular a porcentagem de ocorrência de cada número
print("\nLetra e:")
total = sum(contagem)
for i in range(6):
    porcentagem = (contagem[i] / total) * 100
    print(f"Número {i + 1}: {porcentagem:.2f}%")
