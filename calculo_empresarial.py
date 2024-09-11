print("/n--- Insira os Valores ---")

# Entrada de Dados
faturamento = float(input("Digite seu faturamento: R$"))
custo = float(input("Digite seu custo: R$"))
ir_lucro = float(input("Digite o imposto sobre o lucro: %"))
imposto_estadual = float(input("Digite o seu imposto estadual: %"))

#Calculo
lucro_bruto = faturamento - custo
margem_lucro = lucro_bruto / faturamento * 1.0
lucro_liquido = lucro_bruto - ir_lucro - imposto_estadual

# Resultado
print(f"Seu faturamento é: R${faturamento:.2f}")
print(f"Seu custo é: R${custo:.2f}")
print(f"Seu lucro bruto é: R${lucro_bruto:.2f}")
print(f"Sua margem de lucro é: R${margem_lucro:.2f}")
print(f"Lucro liquido é: R${lucro_liquido:.2f}")
