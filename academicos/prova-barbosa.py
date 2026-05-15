
qnt = 0
usuario = int(input("Digite seu valor"))
for i in range(usuario):
  qnt+=1
  print(i+1)
print(f"Contadador = {qnt}")




qnt = 0
usuario = int(input("Digite seu valor"))
for i in range(usuario,-1,-1):
  qnt+=1
  print(i)
print(f"Contadador = {qnt}")






qnt = 0
usuario = 501
for i in range(1,usuario):
  qnt+=1
  print(i)
print(f"Contadador = {qnt}")





soma = 0

for numero in range(1, 501):
    if numero % 2 != 0 and numero % 3 == 0:
        soma += numero

print(f"A soma dos números ímpares e múltiplos de 3 (de 1 a 500) é: {soma}")









print("Todas as pedras de um dominó (incluindo repetições invertidas):")

for lado_esquerdo in range(7):
    for lado_direito in range(7):
        print(f"[{lado_esquerdo} | {lado_direito}]")











print("Todas as pedras de um dominó (sem repetição):")
for lado_esquerdo in range(7):
    for lado_direito in range(lado_esquerdo, 7):
        print(f"[{lado_esquerdo} | {lado_direito}]")