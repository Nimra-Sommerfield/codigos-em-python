qtt_cartoes = int(input("Insira quantidade de cartões: "))
lista = []
mulheres = 0
homens = 0


for i in range(qtt_cartoes):
  cartao = int(input(f"Insira número do cartão {i+1}: "))
  lista.append(cartao)

for j in range(qtt_cartoes):
  if lista[j] % 2 == 0:
    mulheres += 1
  else :
    homens += 1

if mulheres == homens:
  print("sim")
else:
  print("não")
