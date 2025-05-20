#int é para numero;
#input é para a pessoa digitar;
idade = int(input('Sua idade: '))
#pede para a pessoa digitar a idade

carteira = input('Tem Carteira? (sim/não): ') .strip().lower()
#Pergunta se a pessoa tem carteira
#.strip() remove os espaços;
#.lower() deixa tudo minusculo

if idade >= 18 and carteira == "sim": #Se a idade for maior ou igual a '18' e a resposta sobre carteira for 'sim' mostrar "Pode dirigir!"
    print("Pode dirigir!")
else: #Caso o contrario mostrar "Não Pode Dirigir!"
    print("Não Pode Dirigir!")