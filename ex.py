qtdApple = int(input("Quantos kg de maçã vc comprou? "))
priceApple = float(input("Qual o valor do kg da maçã? "))
qtdBanana = int(input("Quantos kg de banana vc comprou? "))
priceBanana = float(input("Qual o valor do kg da banana? "))
payment = input("Vai pagar a vista? S ou N: ").upper()

totalApple = qtdApple * priceApple
totalBanana = qtdBanana * priceBanana

if qtdApple >= 5 and qtdApple < 10:
    print("Você recebeu um desconto de 10% na maçã")
    totalApple *= 0.9
elif qtdApple >= 10:
    print("Você recebeu um desconto de 20% na maçã")
    totalApple *= 0.8
if qtdBanana >= 5 and qtdBanana < 10:
    print("Você recebeu um desconto de 30% na banana")
    totalBanana *= 0.7
elif qtdBanana >= 10:
    print("Você recebeu um desconto de 50% na banana")
    totalBanana *= 0.5
    
total = totalApple + totalBanana

if payment == "S":
    print("Desconto de 10% aplicado na compra total")
    total *= 0.9

print(f"Preço final: R$ {total:.2f}")
