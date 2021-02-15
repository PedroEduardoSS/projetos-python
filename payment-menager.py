print("Gerenciador de pagamento")
cliente = float(input("Preço final: R$"))
pagamento = int(input('''Qual a opção de pagamento?
[1] à vista no dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão'''))
if pagamento == 1:
    total = cliente - (cliente * 10/100)
    print(f"Você recebeu desconto de 10%, seu valor final é: R${total}")
elif pagamento == 2:
    total = cliente - (cliente * 5/100)
    print(f"Você recebeu desconto de 5%, seu valor final é: R${total}")
elif pagamento == 3:
    total = cliente
    totalf = cliente/2
    print(f"Você dividiu em 2x de {total} no cartão, seu valor final é: R${totalf}")
elif pagamento == 4:
    total = cliente + (cliente * 10/100)
    parcelas = int(input("Quantas parcelas?"))
    totalf = total / parcelas
    print(f"Você dividiu em {parcelas} parcelas de {totalf}, seu valor final, COM JUROS DE 10%, é: R${total}")
