print("vamos calcular seu IMC")
x=float(input("Digite o valor inteiro do seu peso, ignorando casas decimais: "))
y=float(input("Digite sua altura, com ponto no lugar de virgula: "))
if (y<= 0) or (x<=0):
  print("Você não pode colocar esses numeros")
  exit()
z=(y*y)
imc=x/z
print(f'IMC: {round(imc, 1)}')
if (imc <= 18.5):
     print("você esta na classificação de: Magreza ")
elif (imc >18.5 ) and (imc <=25 ):
     print("você esta na class0ificação de: Normal ")
elif (imc >25 ) and (imc <=30 ):
     print("você esta na classificação de: Sobrepeso ")
elif (imc >30 ) and (imc <=40 ):
     print("você esta na classificação de: Obesidade de 2º grau ")
elif (imc >40 ):
     print("você esta na classificação de: Obesidade de 3º grau")