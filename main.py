nome = 'Victoria'
idade = 21 #int
altura = 1.65 #float
peso = 55 #int
e_maior = idade > 18
imc = peso / (altura ** 2)
ano_atual = 2020
nascimento = ano_atual - idade

print('{0} tem {1} anos de idade e pesa {2}kg '.format(nome,idade,peso))
print(f'Ela possui o imc de {imc:.2f}')
print(f'{nome} nasceu no ano de {nascimento}.')
