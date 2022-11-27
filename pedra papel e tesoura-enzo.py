import random


i = 0
while i == 0:
    print("==================================")
    print("{!Pedra Papel E tesoura The GAME!}".upper())
    print("==================================")
    Escolha = input("escolha entre Pedra/Papel/Tesoura/Sair: ").lower()

    if Escolha == "sair":
        exit()

    if not Escolha == "pedra" and not Escolha == "papel" and not Escolha == "tesoura" and not Escolha == "modo secreto" :
        print("Eu sou uma maquina, eu trabalho com palavras especificas, por favor, escolha entre pedra/papel/tesoura")
        continue

    EscolhaDaMaquina = ["pedra", "papel", "tesoura"]
    EscolhaDaMaquina2 = random.choice(EscolhaDaMaquina)

    if Escolha == "modo secreto":
        perda_imediata = input("Escolha a sua derrota entre Pedra/Papel/Tesoura: ").lower()
        if perda_imediata == "pedra":
            print("A escolha da A.I.: Papel")
            print("Perdeu, voce nunca ira ganhar da maquina")
        elif perda_imediata == "papel":
            print("A escolha da A.I.: Tesoura")
            print("Perdeu, voce nunca ira ganhar da maquina")
        else:
            print("A escolha da A.I.: Pedra")
            print("Perdeu, voce nunca ira ganhar da maquina")
    else:
        print(f"A escolha da A.I.: {EscolhaDaMaquina2}")

    if Escolha == "pedra":
        if EscolhaDaMaquina2 == "papel":
            print("Tu perdeu")
        elif EscolhaDaMaquina2 == "tesoura":
            print("Voce ganhou!")
        else:
            print("Empatou")
    elif Escolha == "papel":
        if EscolhaDaMaquina2 == "tesoura":
            print("Tu perdeu")
        elif EscolhaDaMaquina2 == "pedra":
            print("Voce ganhou!")
        else:
            print("Empato")
    elif Escolha == "tesoura":
        if EscolhaDaMaquina2 == "pedra":
            print("Tu perdeu")
        elif EscolhaDaMaquina2 == "papel":
            print("Voce ganhou!")
        else:
            print("Empato")
    print("\t\t")
