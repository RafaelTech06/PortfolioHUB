# Define uma função que mostra um valor
def mostra_valor(p_valor):
    print("Parâmetro recebido:", p_valor)

# Define uma função que mostra dois valores
def mostra_dois_valores(valor1, valor2):
    print("Valor 1:", valor1)
    print("Valor 2:", valor2)

# Início do programa
if __name__ == '__main__':
    # Chamadas diretas
    mostra_valor(5)
    mostra_valor(23.8)
    mostra_valor(-55)

    # Usando variáveis
    v_inteiro = 5
    mostra_valor(v_inteiro)

    numero = 23.8
    mostra_valor(numero)

    negativo = -55
    mostra_valor(negativo)

    # Usando entrada do usuário
    v_inteiro = int(input("Digite um número inteiro: "))
    mostra_valor(v_inteiro)

    v_real = float(input("Digite um número decimal: "))
    mostra_valor(v_real)

    v_negativo = int(input("Digite um número negativo: "))
    mostra_valor(v_negativo)

    # Mostra dois valores fixos
    mostra_dois_valores(5, 10)

    # Mostra dois valores digitados
    v1 = input("Digite o primeiro valor: ")
    v2 = input("Digite o segundo valor: ")
    mostra_dois_valores(v1, v2)
