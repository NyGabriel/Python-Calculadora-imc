# Função para calcular o IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Função principal para executar a calculadora de IMC
def main():
    print("Calculadora de IMC")
    peso = float(input("Digite seu peso em quilogramas: "))
    altura = float(input("Digite sua altura em metros: "))
    imc = calcular_imc(peso, altura)
    print(f"Seu IMC é: {imc:.2f}")

    # Classificação do IMC
    if imc < 18.5:
        print("Classificação: Abaixo do peso")
    elif 18.5 <= imc < 24.9:
        print("Classificação: Peso normal")
    elif 24.9 <= imc < 29.9:
        print("Classificação: Sobrepeso")
    elif 29.9 <= imc < 34.9:
        print("Classificação: Obesidade grau I")
    elif 34.9 <= imc < 39.9:
        print("Classificação: Obesidade grau II")
    else:
        print("Classificação: Obesidade grau III ou mórbida")

# Executando a função principal
if __name__ == "__main__":
    main()
