import random
import time

seguidores = 0
dinheiro = 0
dias = 1
visualizacoes = 0


print('----Seja Bem-Vindo ao mundo da musica----')
print('A partir desse momento, você vai se tornar um dos maiores artistas da atualidade')

nome_artista = str(input('Digite seu nome artistico: '))
idade_artista = int(input('Digite sua idade: '))
cidade = str(input('Digite a cidade onde você quer começar a sua carreira: '))

generos_musicais = ['MegaFunk','Funk','Electronica','Pop']

print(f'Olá {nome_artista}, agora, escolha seu genero musical:')
for i, genero in enumerate(generos_musicais, start=1):
    print(f'{i}- {genero}')

escolha_genero = int(input('Digite o numero do genero escolhido: '))

if escolha_genero == 1:
    print('Você se tornou um artista de MegaFunk')
    
elif escolha_genero == 2:
    print('Você se tornou um artista de Funk')
    
elif escolha_genero == 3:
    print('Você se tornou um artista de Electronica')

elif escolha_genero == 4:
    print('Você se tornou um artista de Pop')
    
else:
    print('Você digitou uma opção invalida!')
    
print(f'------------- DIA {dias} -------------')
print('Otimo, agora que você escolheu seu genero, chegou a hora de começar a sua carreira!')
print(f'Boa sorte na sua carreira {nome_artista}!!')

print('-------- O GRANDE COMEÇO --------')
print('Você atualmente e um artista pequeno, porem, tem o mundo pela frente')
print('A primeira coisa sera tentar achar um clube noturno para você se apresentar pela primeira vez')

clubes_noturnos_iniciais = ['King of Vegas', 'Nice Lounge', 'Route 66']
nome_clubes = ['King of Vegas', 'Nice Lounge', 'Route 66']

while True:
    print('Agora, escolha onde você quer tentar arranjar seu primeiro evento:')

    for i, clubes_iniciais in enumerate(clubes_noturnos_iniciais, start=1):
        print(f'{i}- {clubes_iniciais}')

    escolha_clube_inicial = int(input('Digite o numero do Clube desejado:'))

    if escolha_clube_inicial == 1:
        opcoes = ['Os proprietários David e Gomes gostaram de você, seu primeiro show será na King!', 'O Proprietário da King não gostou do seu set, lamento!']
        
    elif escolha_clube_inicial == 2:
        opcoes = ['Os proprietário da Nice gostaram de você, e seu primeiro show será na Nice!', 'O Proprietário da Nice não gostou do seu set, lamento!']
        
    elif escolha_clube_inicial == 3:
        opcoes = ['Os proprietário da Route 66 gostaram de você, e seu primeiro show será na Route 66!', 'O proprietário da Route 66 não gostou do seu set, lamento!']
        
    else:
        print('Você digitou uma opção inválida!')
        continue
    
    aceitacao_clube = random.choice(opcoes)
    print(f'{aceitacao_clube}')
    
    if 'gostaram' in aceitacao_clube:
        break
   

escolha_clube = ['King of Vegas', 'Nice Lounge', 'Route 66']
escolha_clube == escolha_clube_inicial

dias += 1
print(f'------------- DIA {dias} -------------')

produza_musicas_ganhar = 'Faça shows ou produza musicas para ganhar mais!'
nome_clube_escolhido = nome_clubes[escolha_clube_inicial - 1]
print(f'Seu primeiro show sera no clube {nome_clube_escolhido}')
print(f'Você atualmente tem R${dinheiro}! {produza_musicas_ganhar}')
print(f'Você atualmente tem {seguidores} seguidores! {produza_musicas_ganhar}')
print(f'Você mora numa casa velha e sua internet e muito inestavel! Isso pode produzir varios problemas na hora de produzir ou postar musicas!')


dias += 1
print(f'------------- DIA {dias} -------------')


menu_opcoes = ['Pular para o proximo show', 'Produzir uma musica', 'Abrir Redes Sociais', 'Abrir Conta Bancaria', 'Fazer compras' ]
while True:
    print('Escolha o que deseja fazer:')
    
    for i, opcoes_menu in enumerate(menu_opcoes, start= 1):
        print(f'{i}- {opcoes_menu}')
    
    escolha_menu = int(input('Digite a opção que deseja realizar: ')) 
    
    if escolha_menu == 1:
        while True:
            nome_dia_semana = ['Sexta-Feira', 'Sabado', 'Quinta-Feira']
            escolha_dia_semana = random.choice(nome_dia_semana)
        
            if seguidores >= 0 <= 100:
                valor_cache_inicial = random.randint(100, 200)
            
            if seguidores >= 100 <= 500:
                valor_cache_inicial = random.randint(200, 400)
            
            if seguidores >= 500 <= 10000:
                valor_cache_inicial = random.randint(400, 500)
                
            if seguidores >= 1000 <= 10000:
                valor_cache_inicial = random.randint(500, 700)
                
            if seguidores >= 10000 <= 20000:
                valor_cache_inicial = random.randint(700, 1000)
            if seguidores > 20000:
                valor_cache_inicial = random.randint(1000, 10000)
                
            print(f'Hoje e {escolha_dia_semana}, dia do seu primeiro show!', flush=True)
            time.sleep(1)
            print('Chegou a hora do seu grande show! Espero que esteja preparado!', flush=True)
            time.sleep(3)
            print(f'O valor do cache ficou acordado em R${valor_cache_inicial}')
            print('-------------- Dirigindo-se ate o local --------------')
            time.sleep(3)
            print(f'Você chegou na {nome_clube_escolhido}!')
            time.sleep(3)
            publico_festa1 = list(range(40, 101))
            publico_festa_sorteado1 = random.randint(40, 100)
            print(f'Tem atualmente {publico_festa_sorteado1} pessoas no local! Boa sorte')
            time.sleep(3)
            
            max_seguidores_win = publico_festa_sorteado1 - random.randint(40, publico_festa_sorteado1)
            min_seguidores_win = publico_festa_sorteado1 - random.randint(1, publico_festa_sorteado1)   
            while True:
                max_seguidores_win = publico_festa_sorteado1 - random.randint(40, publico_festa_sorteado1)
                min_seguidores_win = publico_festa_sorteado1 - random.randint(1, publico_festa_sorteado1)   
                entrada_comeco_festa = ['Entrada Propia', 'Entrada convencional', 'Começar diretamente com uma musica']
                
                for i, escolha_entrada1 in enumerate(entrada_comeco_festa, start=1 ):
                    print(f'{i}- {escolha_entrada1}') 

                escolha_entrada = int(input('Digite o numero da Entrada desejada: ')) 
                
                if escolha_entrada == 1:
                    print('O publico não gostou da sua entrada!')
                    valor_cache = valor_cache_inicial - 10
                    seguidores_ganhos = random.randint(max_seguidores_win, min_seguidores_win)
                    seguidores = seguidores_ganhos - seguidores
                    print(f'O seu cache caiu para R${valor_cache}') 
                    print(f'Você perdeu {seguidores_ganhos}')
                    print(f'Você atualmente tem {seguidores} seguidores')
                    break
                    
                elif escolha_entrada == 2:
                    print('O publico gostou da sua entrada! Bom começo!')
                    valor_cache = valor_cache_inicial + 20
                    seguidores_ganhos = random.randint(max_seguidores_win, min_seguidores_win)
                    seguidores = seguidores_ganhos + seguidores
                    print(f'O seu cache aumentou para R${valor_cache}')
                    print(f'Você ganhou +{seguidores_ganhos} seguidores, parabens!')
                    print(f'Você atualmente tem {seguidores} seguidores')
                    break
                
                elif escolha_entrada == 3:
                    print('Ninguem percebeu que você começou a tocar')
                    break
                
                else:
                    print('Você digitou uma opção invalida!')
                    continue
                
            while True:
                musicas_festa_megafunk_outros = ['Mega Funk Roça na Loirinha', 'Mega Funk Atras do Caminhão', 'Mega Funk do Akon', 'Mega Funk Desande', 'Mega Funk Perfil Verificado', 'Mega Funk Hitmado', 'Finalizar Show']
                for i, escolha_musica_outros in enumerate(musicas_festa_megafunk_outros, start=1):
                    print(f'{i}- {escolha_musica_outros}')
                            
                escolha_musica_usuario = int(input('Digite a opção desejada: '))
                            
                if escolha_musica_usuario == 7:
                    print("Fim do show!")
                    break

                opcao_publico = ['O Publico adorou a musica', 'O publico não gostou da musica']
                opcao_publico_random = random.choice(opcao_publico)
                            
                if 'adorou' in opcao_publico_random:
                    seguidores = seguidores + seguidores_ganhos
                    valor_cache = valor_cache + 20
                    print(f'{opcao_publico_random}')
                    print(f'Teu cache aumentou para {valor_cache}')
                    print(f'Você ganhou {seguidores_ganhos} seguidores')
                if 'não' in opcao_publico_random:
                    seguidores = seguidores - seguidores_ganhos
                    valor_cache = valor_cache - 10
                    print(f'{opcao_publico_random}')
                    print(f'Teu cache diminuiu para {valor_cache}')
                    print(f'Você perdeu {seguidores_ganhos} seguidores')

            print(f"Você ganhou {seguidores} seguidores durante o show!")
            print(f"Seu cache final é de {valor_cache} reais.")
            break
                
    if escolha_menu == 2:
    
        while True:
            menu_producao = ['Criar musica nova', 'Ver minhas musicas atuais', 'Voltar']
            
            for i, escolha_producao in enumerate(menu_producao, start=1):
                print(f'{i}- {escolha_producao}')
        
            escolha_producao1 = int(input('Digite o numero da opção desejada: '))
            musicas_criadas = []
            
            if escolha_producao1 == 1:
                nome_musica = str(input('Digite o nome da sua nova musica: '))
                print(f'---------- Criando musica: {nome_musica} ----------')
                sim_nao_musica = [f'Você conseguiu produzir {nome_musica} com sucesso!', f'Você não conseguiu inspiração para criar {nome_musica}']
                producao_musica_escolha = random.choice(sim_nao_musica)
                
                if 'conseguiu' in producao_musica_escolha:
                    nota_musica1 = list(range(3, 10))
                    nota_musica = random.randint(3, 10)
                    print(f'Os teus amigos deram uma pontuação {nota_musica}/10 para sua nova musica! ')
                    publicar_musica = str(input('Você quer publicar a musica? [S] ou [N]: '))
                    
                    if 'S' or 's' in publicar_musica:
                        musicas_criadas.append(nome_musica)
                        print('Parabens, sua musica esta sendo um sucesso!')
                        if nota_musica >= 7:
                            visualizacoes_ganhas = random.randint(100, 500)
                            visualizacoes = visualizacoes_ganhas + visualizacoes
                            seguidores_ganhos = random.randint(10,20)
                            seguidores = seguidores + seguidores_ganhos
                            print(f'Você ganhou {seguidores_ganhos} seguidores!')
                            print(f'Você ganhou {visualizacoes_ganhas} visualizações!')
                            break
                        if nota_musica >= 4 <= 6:
                            visualizacoes_ganhas = random.randint(50, 300)
                            visualizacoes = visualizacoes_ganhas + visualizacoes
                            seguidores_ganhos = random.randint(5,10)
                            seguidores = seguidores + seguidores_ganhos
                            print(f'Você ganhou {seguidores_ganhos} seguidores!')
                            time.sleep(0.2)
                            print(f'Você ganhou {visualizacoes_ganhas} visualizações!')
                            time.sleep(0.2)
                            break
                        if nota_musica >= 0 <= 4:
                            visualizacoes_ganhas = random.randint(0, 100)
                            visualizacoes = visualizacoes_ganhas + visualizacoes
                            seguidores_ganhos = random.randint(1,5)
                            seguidores = seguidores + seguidores_ganhos
                            print(f'Você ganhou {seguidores_ganhos} seguidores!')
                            time.sleep(0.2)
                            print(f'Você ganhou {visualizacoes_ganhas} visualizações!')
                            time.sleep(0.2)
                            break
                        
                    elif 'N' or 'n' in publicar_musica:
                        print(f'Você excluiu {nome_musica} do seu computador!')
                        time.sleep(0.2)
                        break
                    else: 
                        print('Opção invalida!')
                        continue
                        
            if escolha_producao1 == 2:
                print(musicas_criadas)
                break
            
            if escolha_producao1 == 3:
                break
            
            else:
                print('Você digitou uma opção invalida!')
            
    if escolha_menu == 3:
        
        while True:
            opcoes_menu_redes_sociais = ['Ver informações sobre o canal', 'Monetizar canal', 'Excluir musica', 'Voltar']
            
            for i, menu_redes_escolha in enumerate(opcoes_menu_redes_sociais, start=1):
                print(f'{i}- {menu_redes_escolha}')
            
            escolha_redes_sociais = int(input('Digite a opção desejada: '))
            
            if escolha_redes_sociais == 1:
                print(f'Você tem {seguidores} seguidores!')
                print(f'Você tem {visualizacoes} seguidores!')
                continue
            
            elif escolha_redes_sociais == 2:
                if seguidores >= 1000 and visualizacoes >= 10000:
                    print('Você monetizou o seu canal com sucesso! A partir de hoje qualquer musica que você produza ira gerar R$')
                    continue
                if seguidores < 1000 or visualizacoes < 10000:
                    print('Você precisa de 1000 seguidores e 10.000 visualizações para poder monetizar teu canal!')
                    continue
                
            elif escolha_redes_sociais == 3:
                print('Em construção')
                continue
            
            elif escolha_redes_sociais == 4:
                break
            
            else:
                print('Você digitou uma opção invalida!')
                continue
                
    if escolha_menu == 4:
        print(f'Você tem R${dinheiro}')
        continue
    
    if escolha_menu == 5:
        
        while True:
            opcoes_menu_compras = ['Loja de propiedades', 'Loja de carros', 'Efeitos para show', 'Loja de Drogas (ilegal)', 'Voltar']
            
            for i, menu_compras in enumerate(opcoes_menu_compras, start=1):
                print(f'{i}- {menu_compras}')
                
            escolha_menu_compras = int(input('Digite a opção desejada: '))
            
            if escolha_menu_compras == 1:
                print('Em construção')
                continue
            
            elif escolha_menu_compras == 2:
                print('Em construção')
                continue
            elif escolha_menu_compras == 3:
                print('Em construção')
                continue
            elif escolha_menu_compras == 4:
                print('Em construção')
                continue
            elif escolha_menu_compras == 5:
                break
                
            else:
                print('Você digitou uma opção invalida!')
                continue
                    