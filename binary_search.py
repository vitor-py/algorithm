import time
import os
import pyfiglet
from colorama import init, Fore
init(autoreset=True)

def adivinhar():

    lista = (range(1, 101))
    chute = 50

    print('Pense em um número...')
    for i in range(3, 0, -1):
        print(f'{i}...', end='\r', flush=True)
        time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        print(f'{chute} seria o seu número?')
        resposta = input('sim / baixo / alto: ').lower()
        if resposta == 'sim':
            print('FACIL KKKKKK')
            break
        meio = len(lista) // 2
        if resposta == 'baixo':
            lista = lista[meio:]
        elif resposta == 'alto':
            lista = lista[:meio - 1]
        chute = lista[len(lista) // 2]

titulo = pyfiglet.figlet_format("Pesquisa Binaria", font="speed")
print(Fore.CYAN + titulo + Fore.RESET) 

print('Irei adivinhar o número que você pensar! \n')
iniciar = input('Deseja iniciar? sim/nao: ').lower()

if iniciar == 'sim':
    adivinhar()
else:
    print('tá com medo?')
