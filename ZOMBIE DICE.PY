import random
from time import sleep

def Coletar_Dados(dados_extra=list(),passos = 0): #Função para coletar os dados do copo que serão jogados

    global copo
    global jogador

    dados_rodada=dados_extra
    vermelho = 0
    verde = 0
    amarelo = 0
    num_vermelho = 0
    num_verde = 0
    num_amarelo = 0
    for i in range(0, len(copo)):  #Este laço checa quais dados que ainda estão no copo, sendo que o número de dados e tipo variam conforme os mesmos são retirados, em jogadas subsequentes (mas resetados quando passa o turno para o outro jogador)
        if copo[i] == 'CPCTPC':
            num_verde += 1
        elif copo[i] == 'TPCTPC':
            num_amarelo += 1
        else:
            num_vermelho += +1
    print(f'O copo de dados contém {num_verde} dado(s) verde(s), {num_amarelo} dado(s) amarelo(s) e {num_vermelho} dado(s) vermelho(s)')
    if len(copo)+len(dados_rodada)<3:
        print(f'Você não tem dados suficientes para jogar mais uma rodada, são necessários pelo menos três dados e há apenas{len(copo)+len(dados_rodada)} dados disponíveis')
        Etapa_Pontuacao()
    else:
        for i in range(passos, 3):     #Este laço pega aleatoriamente dados do copo (removendo-os do copo) e adiciona para  a lista dados_rodada, sendo que os dados serão sacados até que tenham 3 dados no total para serem jogados
            dado = random.choice(copo)
            copo.remove(dado)
            dados_rodada.append(dado)
        for i in range (0,3):           #Laço para checar exatamente quais dados foram sacados e retorna essa informação para o jogador de forma compreensível
            if dados_rodada[i] == 'CPCTPC':
                verde+=1
            elif dados_rodada[i] == 'TPCTPC':
                amarelo += 1
            else:
                vermelho += +1
        if jogador == True:
            print(f'{nome1} sacou {verde} dado(s) verde(s), {amarelo} dado(s) amarelo(s) e {vermelho} dado(s) vermelho(s)')
        else:
            print(f'{nome2} sacou {verde} dado(s) verde(s), {amarelo} dado(s) amarelo(s) e {vermelho} dado(s) vermelho(s)')
        input('Aperte qualquer tecla para rolar os dados...')
        return dados_rodada                                     #retorna os dados que serão utilizados pela função Rolar_dados()

def Rolar_Dados(dados_rodada=list()): #Função para rolar os dados sacados pela função Coletar_Dados()
    global cerebros
    global tiros
    global dado_verde # 6 dados verdes
    global dado_amarelo # 4 dados amarelos
    global dado_vermelho # 3 dados vermelhos

    passos_rodada = 0
    cerebros_rodada = 0
    tiros_rodada=0
    print('Rolando os dados...')
    sleep(1.5)
    dados_extras = []
    for i in range(0,3):            #Laço que roda os dados sacados por cor e mostra ao jogador o que cada dado rolou.
        tipo = random.choice(dados_rodada[i])
        if dados_rodada[i] == dado_verde:
            print('Dado Verde -> ', end='')
            if tipo =='C':
                print('Céééérebros...')
                cerebros_rodada = cerebros_rodada + 1
            elif tipo == 'T':
                print('Bang-Bang!')
                tiros_rodada+=1
            else:
                print('Fuujaam!!')
                passos_rodada+=1
                dados_extras.append(dados_rodada[i])
        elif dados_rodada[i] == dado_amarelo:
            print('Dado Amarelo -> ', end = '')
            if tipo =='C':
                print('Céééérebros...')
                cerebros_rodada = cerebros_rodada + 1
            elif tipo == 'T':
                print('Bang-Bang!')
                tiros_rodada+=1
            else:
                print('Fuujaam!!')
                passos_rodada+=1
                dados_extras.append(dados_rodada[i])
        else:
            print('Dado Vermelho -> ', end = '')
            if tipo =='C':
                print('Céééérebros...')
                cerebros_rodada = cerebros_rodada + 1
            elif tipo == 'T':
                print('Bang-Bang!')
                tiros_rodada+=1
            else:
                print('Fuujaam!!')
                passos_rodada+=1
                dados_extras.append(dados_rodada[i])
    cerebros += cerebros_rodada
    tiros += tiros_rodada            #O resultado dos dados é mostrado ao jogador de forma compreensível, sendo que o número de cérebros e tiros é guardado e cumulativo até o fim de sua jogada.
    print(f'Você comeu {cerebros_rodada} cérebro(s), tomou {tiros_rodada} tiros()) e {passos_rodada} vítima(s) escaparam.\n Total de cérebros comidos neste turno: {cerebros} \n Total de tiros tomados neste turno: {tiros}')
    continuar = ''
    if tiros < 3:  #Se o jogador acumulou menos que três tiros, é dado a ele a oportunidade de continuar sacando novos dados, bem como reutilizando os dados de vítimas que fugiram (se este evento ocorrer). que são guardados na lista dados_extra().
        while continuar != 'N':
            if len(dados_extras)>0:
                verde=0
                amarelo=0
                vermelho=0
                for i in range(0, len(dados_extras)): #Laço para checar quantidade e cor dos dados de vítimas que fugiram (se este evento ocorrer)  e que serão reutilizados, repassando essa informação ao jogador
                    if dados_extras[i] == 'CPCTPC':
                        verde += 1
                    elif dados_extras[i] == 'TPCTPC':
                        amarelo += 1
                    elif dados_extras[i] == 'TPTCPT':
                        vermelho += +1
                print(f'Dados extras correspondente às vítimas que escaparam: {verde} dado(s) verde(s), {amarelo} dado(s) amarelo(s) e {vermelho} dado(s) vermelho(s)')
                continuar = str(input(f'{passos_rodada} vítimas escaparam. Gostaria de continuar a perseguição pela cidade, reutilizando os dados das vítimas que escaparam? [S/N] ')).upper()
            else:
                continuar = str(input(f'Gostaria de continuar a perseguição por mais vítimas? [S/N] ')).upper()
            if continuar == 'N':  #Se não quiser continuar a jogar, vai para a etapa de pontuação, considerando os cérebros comidos.
                dados_rodada.clear()
                Etapa_Pontuacao()
                break
            elif continuar == 'S': #Se quiser continuar a jogar, ele coleta novos dados do copo (até três) e rola os dados novamente.
                novos_Dados = Coletar_Dados(dados_extras, passos_rodada)
                Rolar_Dados(novos_Dados)
                dados_rodada.clear()
                break
    else:  #Caso ele tenha acumnulado três tiros entre suas jogadas, perde todos os cérebros que comeu e vai para a etapa de pontuação.
        print(f'Você tomou {tiros} tiros nesse turno, todos os cérebros comidos explodiram para fora do seu estômago e todas as pessoas conseguiram escapar.')
        cerebros = 0
        dados_rodada.clear()
        Etapa_Pontuacao()

def Etapa_Pontuacao(): #Função de etapa de pontuação, sendo que após calcular a pontuação do jogador e guardar essa informação, zera os parâmetros e reinicia o copo de dados, para não interferir com o turno do próximo jogador
    global turno_jogador1
    global turno_jogador2
    global copo
    global tiros
    global cerebros
    global pontuacao_jogador1
    global pontuacao_jogador2
    global jogador
    global turno
    global vencedor
    global finalizado

    if jogador == True:
        pontuacao_jogador1 += cerebros
        jogador=False
    else:
        pontuacao_jogador2 += cerebros
        jogador = True
    print(f'Pontuação total de {nome1}: {pontuacao_jogador1}/13')
    print(f'Pontuação total de {nome2}: {pontuacao_jogador2}/13')
    cerebros = 0
    tiros = 0
    copo = ['CPCTPC', 'CPCTPC', 'CPCTPC', 'CPCTPC', 'CPCTPC', 'CPCTPC', 'TPCTPC', 'TPCTPC', 'TPCTPC', 'TPCTPC',
            'TPTCPT', 'TPTCPT', 'TPTCPT']
    turno+=1
    if turno_jogador1 == turno_jogador2:
        if pontuacao_jogador1>=13 and pontuacao_jogador2<pontuacao_jogador1:
            print(f'Pontuação {nome1}: {pontuacao_jogador1}\n'
                  f'Pontuação {nome2}: {pontuacao_jogador2}\n'
                  f'{nome1} é o vencedor!!!')
            finalizado = True
            vencedor = nome1
        elif pontuacao_jogador2>=13 and pontuacao_jogador1<pontuacao_jogador2:
            print(f'Pontuação {nome2}: {pontuacao_jogador2}\n'
                  f'Pontuação {nome2}: {pontuacao_jogador1}\n'
                  f'{nome2} é o vencedor!!!')
            finalizado = True
            vencedor = nome2
    print('Fim do Turno.')

#Inicio do Programa principal

cerebros = 0
tiros = 0
pontuacao_jogador1 = 0
pontuacao_jogador2 = 0
turno_jogador1 = 0
turno_jogador2 = 0
turno = 1
nome1 = ''
nome2 = ''
finalizado = False
jogador = True
copo = ['CPCTPC', 'CPCTPC', 'CPCTPC', 'CPCTPC', 'CPCTPC', 'CPCTPC', 'TPCTPC', 'TPCTPC', 'TPCTPC', 'TPCTPC', 'TPTCPT', 'TPTCPT', 'TPTCPT']
dado_verde = 'CPCTPC'
dado_amarelo = 'TPCTPC'
dado_vermelho ='TPTCPT'

#Início do jogo

print('''                                                                      
            /|x x|    
           /\( - )                                                          
   ___.-._/\/            WELCOME ZOMBIE DICE IN PYTHON!                            
  /=`_'-'-'/  !!                                                            
  |-{-_-_-}     !                                                           
  (-{-_-_-}    !                                                            
   \{_-_-_}   !                                                             
    }-_-_-}                                                                 
    {-_|-_}                                                                 
    {-_|_-}                                                                 
    {_-|-_}                                                                 
    {_-|-_}                                                               
____%%@ @%%____''')

nome1 = str(input('Digite o nome do primeiro jogador: '))
nome2 = str(input('Digite o nome do segundo jogador: '))

while finalizado == False: #Laço infinito do jogo, até que o vencedor seja declarado, momento em que finalizado vira para "True" e ele sai do laço 'while'.
    print(f'{turno}º Turno')

    if jogador == True:
        input(f'{nome1}, agora é sua vez. Aperte qualquer tecla para iniciar a coleta de dados...')
        turno_jogador1 += 1
        dados_rodada = Coletar_Dados()
        Rolar_Dados(dados_rodada)
    else:
        input(f'{nome2}, agora é sua vez. Aperte qualquer tecla para iniciar a coleta de dados...')
        turno_jogador2 += 1
        dados_rodada = Coletar_Dados()
        Rolar_Dados(dados_rodada)
    print('-='*20)

print(f'Fim da partida, o vencedor foi {vencedor}. Obrigado por jogar!')    #Fim do jogo.