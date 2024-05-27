
for i in range(100):
  tempo = int(input(f"Insira tempo do estudante {i+1}: "))
  dia = int(input("Dias da semana:\n1 - Segunda\n2 - Terça\n3 - Quarta\n4 - Quinta\n5 - Sexta\nSelecione o dia da semana: "))
  if dia == 1:
    tempo += 15
    print(f"tempo de deslocamento total do estudante {i+1} é {tempo} minutos")
  elif dia == 2:
    tempo += 35
    print(f"tempo de deslocamento total do estudante {i+1} é {tempo} minutos")
  elif dia == 3:
    tempo += 10
    print(f"tempo de deslocamento total do estudante {i+1} é {tempo} minutos")
  elif dia == 4:
    tempo += 20
    print(f"tempo de deslocamento total do estudante {i+1} é {tempo} minutos")
  elif dia == 5:
    tempo += 5
    print(f"tempo de deslocamento total do estudante {i+1} é {tempo} minutos")
