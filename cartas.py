cartas_1 = []
cartas_2 = []
cartas_3 = []
res = 0
jogador = 0

for i in range(10) :
  carta1 = int(input(f"Valor da carta {1} do jogador {i+1}: "))
  carta2 = int(input(f"Valor da carta {2} do jogador {i+1}: "))
  carta3 = int(input(f"Valor da carta {3} do jogador {i+1}: "))

  cartas_1.append(carta1)
  cartas_2.append(carta2)
  cartas_3.append(carta3)
for j in range(10) :
  soma = cartas_1[j] + cartas_2[j] + cartas_3[j]
  
  if soma > res:
    res = soma
    jogador = j+1

print(f"O jogador {jogador} ganhou com {res} pontos")
