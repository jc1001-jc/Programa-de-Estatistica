def Resolucao (sistema_o):
  media = sum(sistema_o) / len(sistema_o)

  somas = [0] * 4

  for i in range (4):
    desvio = sistema_o[i] - media
    somas[i] = (desvio)**2 

  variancia = sum(somas) / len (somas)

  desvio_padrao = (variancia)**(1/2)

  print(f"Média: {media}")
  print(f"Variancia: {variancia}")
  print(f"Desvio Padrão: {desvio_padrao:.2f}")

sistema_a = [18, 20, 20, 22]
print("Sistema A")
Resolucao (sistema_a)

print(" ")

sistema_b = [10, 20, 20, 30]
print("Sistema B")
Resolucao (sistema_b)
