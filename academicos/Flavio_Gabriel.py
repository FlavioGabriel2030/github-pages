#1.Construa o programa que calcule a média aritmética dos números pares e a média aritmética dos números ímpares. 
# O usuário fornecerá os valores de entrada que pode ser um número qualquer par ou ímpar. A condição de saída será o número 0 (zero).
#Na tela de saída, mostre também a quantidade total de números digitados e a soma total de números digitados.

somaT  = 0
qntT   = 0
usuario= 0
mediaP = 0
mediaI = 0
qntI   = 0
impares= 0
qntP   = 0
pares  = 0 
while True:
    usuario = int((input("Digite valores [DIGITE 0 PARA SAIR]")))
    if usuario == 0:
        break 
    
    if usuario % 2 == 0:
        impares += usuario
        qntI += 1

    if usuario % 2 != 0:
        pares += usuario
        qntP +=1

somaT = impares + pares 
qntT = qntP + qntI 
mediaP = pares/qntP
mediaI = impares/qntI
print(f"""Quantidade de pares:{qntP}
Media Pares : {mediaP:.2f}

Quantidade de impares : {qntI}
Media Ipares:{mediaI:.2f}

O total de numeros digitados foi de {qntT}
A soma dos numeros digitados foi de {somaT}""")









#2.Desenvolva o programa que leia vários valores reais e no final mostre as seguintes informações:
#A quantidade de valores digitados;
#A soma dos valores digitados;
#A média aritmética dos valores digitados;
#O maior valor digitado;
#O menor valor digitado;
#E a quantidade de valores digitados maior ou igual a 50.



formatacao = "___"
qntL = 0
menor =   99999
maior =   0
media =   0 
soma  =   0
qnt= 0
while True:
    usuario = int(input("Digite valores"))
    if usuario == 0:
        break
    qnt +=1
    soma +=usuario
    if qnt != 0:
        media = soma / qnt

    if usuario > maior:
        maior = usuario

    if usuario < menor:
        menor = usuario
    
    if usuario > 50:
        qntL += 1

    print(f"""{formatacao*15}
# A quantidade de valores digitados= {qnt:.2f};
# A soma dos valores digitados=  {soma:.2f}
# A média aritmética dos valores digitados= {media:.2f};
# O maior valor digitado;= {maior:.2f}
# O menor valor digitado= {menor:.2f};
# E a quantidade de valores digitados maior ou igual a 50= {qntL:.2f}
{formatacao*15}""")

















#3.Em uma eleição presidencial, existem três candidatos. Os votos são informados através de código. Os dados utilizados para escrutinagem obedecem à seguinte codificação: 
#1, 2, 3 - voto dos respectivos candidatos;
#5 - voto nulo;					6 - voto em branco;
#Elabore o programa que calcule o total de votos de cada candidato, total de votos nulos, total de votos em branco, percentual de votos nulos e percentual de votos em branco.
#
#4.Escreva o programa que leia o salário dos funcionários de uma empresa e calcule quantos ganham menos que cinco salários mínimos, quantos estão na faixa de cinco (inclusive) até dez (exclusive) e quantos ganham dez ou mais salários mínimos. O valor do salário mínimo será fornecido pelo usuário. Na tela de saída, além da quantidade de funcionários em cada faixa salarial, informe também o valor total da folha de pagamento da empresa.