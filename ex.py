qtdM = int(input("Quantos kg de maçã vc comprou? "))
pcM = int(input("Qual o valor do kg da maçã? "))
qtdB = int(input("Quantos kg de banana vc comprou? "))
pcB = int(input("Qual o valor do kg da banana? "))
payment = input("Vai pagar a vista? S ou N")
descM = 0
descB = 0
desctTot = 0
if qtdM >= 5 and qtdM < 10:
    print(f'Você recebeu um desconto de 10% no preço da maçã')
    descM = pcM * 0.9
elif qtdM >= 10:
    print(f'Você recebeu um desconto de 20% no preço da maçã')
    descM = pcM * 0.8
if qtdB >= 5 and qtdB < 10:
    print(f'Você recebeu um desconto de 30% no preço da banana')
    descB = pcB * 0.7
elif qtdB >= 10:
    print(f'Você recebeu um desconto de 50% no preço da banana')
    descB = pcB * 0.5
if payment == "S": 
    print(f'Desconto de 10% aplicado na compra')
    desctTot = (descM + descB) * 0.9
    print(desctTot)
elif payment == "N":
    print(f"Preço final {descB + descM}")