import os
def votoRepublicano():
    votoRepublicano.cont_republicano+=1
    print(f'Voto partido republicano')
    input('Presione "ENTER" para continuar')
    os.system('cls')

def votoDemocrata():
    votoDemocrata.cont_democrata+=1
    print('Voto partido democrata')
    input('Presione "ENTER" para continuar')
    os.system('cls')

def contarVotos():
    print('Totalización de los votos')
    print(f'Total de votos Republicanos: {votoRepublicano.cont_republicano}')
    print(f'Total de votos Demócratas: {votoDemocrata.cont_democrata}')
    print(f'Cantidad total de votos: {votoRepublicano.cont_republicano+votoDemocrata.cont_democrata}')
    input('Presione "ENTER" para continuar')
    os.system('cls')

opcion =0
votoRepublicano.cont_republicano = 0
votoDemocrata.cont_democrata = 0

while opcion !=4:
    print('\t*** MENU ***')
    print('=============================')
    print('[1] -> Partido Republicano')
    print('[2] -> Partido Demócrata')
    print('[3] -> Totalización de Votos')
    print('[4] -> Salir del Sistema')
    print('=============================')
    opcion=int(input('Ingrese opción: '))

    if opcion==1:
        votoRepublicano()
    if opcion==2:
        votoDemocrata()
    if opcion==3:
        contarVotos()
    if opcion==4:
        print('Saliendo de sistema de votación...')
    
