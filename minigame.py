from random import choice
from time import sleep

vitorias_jogador = 0
vitorias_maquina = 0


def palpite_jogador():
    print("Sua sorte foi lançada!")
    array = [1, 2, 3, 4, 5, 6]
    escolha_jogador = choice(array)
    print(f"Seu dado caiu do lado {escolha_jogador}")
    return escolha_jogador


def palpite_maquina():
    array = [1, 2, 3, 4, 5, 6]
    escolha_maquina = choice(array)
    return escolha_maquina


while True:

    print(30 * '-')
    opcao_jogador = palpite_jogador()
    
    sleep(1)
    
    opcao_maquina = palpite_maquina()
    print(30 * '-')

    if opcao_jogador > opcao_maquina:
        print(f"Seu dado caiu no {opcao_jogador}"
              f" e o da máquina no {opcao_maquina}. Parabéns! você ganhou.")
        vitorias_jogador += 1
    elif opcao_jogador == opcao_maquina:
        print(f"Seu dado caiu no {opcao_jogador}"
              f" e o da máquina no {opcao_maquina}. Empate.")
    else:
        print(f"Seu dado caiu no {opcao_jogador}"
              f" e o da máquina no {opcao_maquina}. Que pena! Você perdeu.")
        vitorias_maquina += 1
    
    sleep(1)
    
    print(30 * '-')
    print(f"Vitórias do jogador: {vitorias_jogador}")
    print(f"Vitórias da Máquina: {vitorias_maquina}")
    print(30 * '-')

    opcao = input("Você deseja jogar novamente?: ")
    if opcao in ["SIM", "Sim", "sim", "s", "S"]:
        pass
    elif opcao in ["NAO", "Nao", "nao", "n", "N"]:
        print("Encerrando Mini Game. ")
        break
    else:
        print("Opção Inválida! Encerrando Mini Game.")
        break
