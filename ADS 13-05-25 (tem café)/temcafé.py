cafe = input("Tem café? (sim/não): ") .strip() .lower()

if cafe == "sim":
    print("Tem sim")
elif cafe == "nao" or cafe == "não":
    print("Tem não meu fi!")
else:    print("Resposta invalida!")