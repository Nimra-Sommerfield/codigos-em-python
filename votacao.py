total_eleitores = int(input("Insira o total de eleitores da cidade: "))
brancos = int(input("Insira o total de votos brancos: "))
nulos = int(input("Insira o total de votos nulos: "))
validos = int(input("Insira o total de votos válidos: "))

#calculos
perc_brancos = float((brancos / total_eleitores) * 100)
perc_nulos = float((nulos / total_eleitores) * 100)
perc_validos = float((validos / total_eleitores) * 100)

#printar
print(f"Total de eleitores: {total_eleitores}\nVotos brancos: {perc_brancos:.2f}%\nVotos nulos: {perc_nulos:.2f}%\nVotos válidos: {perc_validos:.2f}%")
