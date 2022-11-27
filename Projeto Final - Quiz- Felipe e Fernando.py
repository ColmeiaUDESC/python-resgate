# Projeto de Felipe e Fernando
# Tema escolhido: Quiz

pontos = 0
quiz = {
    1: {
        'pergunta': 'Quantos segundos tem 1 dia? (Digite apenas o numero e faca os calculos na cabeca!)',
        'resposta': '86400'
    },
    2: {
        'pergunta': 'Em que pais o futebol foi criado?',
        'resposta': 'INGLATERRA'
    },
    3: {
        'pergunta': 'Quantos anos em media vive uma tartaruga? (Apenas digite o numero!)',
        'resposta': '150'
    },
    4: {
        'pergunta': 'Qual o clima predominante de Joinville? (Digite apenas o clima!)',
        'resposta': 'MESOTERMICO'
    },
    5: {
        'pergunta': 'Em que ano foi criado o primeiro console de videogame? (Apenas digite o numero!)',
        'resposta': '1972'
    }
}

print('-=-' * 10)
print('Bem-vindo ao quiz!')
print('-=-' * 10)

for i in quiz:
    print(quiz[i]['pergunta'])
    resp = str(input('Insira a resposta: ')).upper().replace(' ', '')
    print('-=-' * 10)

    if resp == quiz[i]['resposta']:
        pontos += 1
        print('Voce acertou! Parabens!')
        print('-=-' * 10)
    else:
        print('Voce errou...')
        print('-=-' * 10)

print('-=-' * 10)
print(f'Voce somou {pontos} pontos!')
print('Fim do quiz.')
print('-=-' * 10)
