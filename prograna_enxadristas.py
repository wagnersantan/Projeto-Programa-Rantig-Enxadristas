import pandas as pd

enxadristas = []

while True:
    # Dicionário para armazenar os dados de um enxadrista
    enxadrista = {}
    enxadrista['nome'] = input('Nome do enxadrista: ').strip().ljust(25)
    
    while True:
        try:
            # Solicita o número de partidas jogadas
            tot = int(input(f'Quantas partidas {enxadrista["nome"]} jogou?: '))
            if tot < 0:
                raise ValueError  # Garante que o número de partidas não seja negativo
            break
        except ValueError:
            print("Erro! Digite um número inteiro válido.")

    # Lista para armazenar os pontos de cada partida
    partidas = []
    for c in range(tot):
        while True:
            try:
                # Solicita os pontos obtidos em cada partida
                pontos = int(input(f'Quantos pontos na partida {c + 1}? '))
                partidas.append(pontos)
                break
            except ValueError:
                print("Erro! Digite um número inteiro válido.")

    # Armazena os pontos e a soma total no dicionário do enxadrista
    enxadrista['medalhas'] = partidas
    enxadrista['Total'] = sum(partidas)

    # Entrada para medalhas com validação
    for medalha in ['ouro', 'prata', 'bronze']:
        while True:
            try:
                # Solicita a quantidade de medalhas do enxadrista
                enxadrista[medalha] = int(input(f'Quantas medalhas de {medalha} {enxadrista["nome"]} possui? '))
                if enxadrista[medalha] < 0:
                    raise ValueError  # Garante que o número de medalhas não seja negativo
                break
            except ValueError:
                print("Erro! Digite um número inteiro válido.")

    # Adiciona o enxadrista à lista de enxadristas
    enxadristas.append(enxadrista)

    # Adicione as linhas abaixo aqui
    df = pd.DataFrame(enxadristas)  # Criação do DataFrame
    df['pontos_por_medalha'] = (df['ouro'] * 3) + (df['prata'] * 2) + (df['bronze'] * 1)

    df['media_pontos_por_partida'] = df['Total'] / tot


    # Exibir o DataFrame com os dados
    print(df[['nome', 'Total', 'ouro', 'prata', 'bronze','pontos_por_medalha','media_pontos_por_partida']])  # Exibição do DataFrame

    while True:
        # Pergunta se deseja cadastrar outro enxadrista
        resp = input('Deseja cadastrar outro enxadrista? [S/N] ').strip().upper()
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N.')

    if resp == 'N':
        break  # Encerra o loop de cadastro

# Verifica se há enxadristas cadastrados antes de exibir os dados finais
if enxadristas:
    print('-=' * 30)
    print(f'{"Código":<3} {"Nome":<20} {"Total":<5} {"Ouro":<5} {"Prata":<5} {"Bronze":<6}')
    print('-=' * 70)

    # Exibe os dados de cada enxadrista
    for k, v in enumerate(enxadristas):
        print(f'{k:<3} {v["nome"]:<25} {str(v["Total"]):<5} {str(v["ouro"]):<5} {str(v["prata"]):<5} {str(v["bronze"]):<6}')

    print('-=' * 70)

    while True:
        try:
            # Permite buscar os detalhes de um enxadrista pelo índice
            busca = int(input('Mostrar dados de qual enxadrista? (999 para parar): '))
            if busca == 999:
                break  # Encerra a busca
            if 0 <= busca < len(enxadristas):
                print(f'--- LEVANTAMENTO DO ENXADRISTA {enxadristas[busca]["nome"]}')
                print(f'Medalhas: Ouro: {enxadristas[busca]["ouro"]}, Prata: {enxadristas[busca]["prata"]}, Bronze: {enxadristas[busca]["bronze"]}')
                print(f'Partidas jogadas: {len(enxadristas[busca]["medalhas"])}')
                print('-=' * 30)
            else:
                print(f'ERRO! Não existe enxadrista com código {busca}.')
        except ValueError:
            print("Erro! Digite um número inteiro válido.")
    
    def encontrar_campeoes(enxadristas):
        if not enxadristas:
            print("A lista de enxadristas está vazia.")
        return

    campeao_ouro = max(enxadristas, key=lambda x: x["ouro"])['nome']
    campeao_prata = max(enxadristas, key=lambda x: x["prata"])['nome']
    campeao_bronze = max(enxadristas, key=lambda x: x["bronze"])['nome']
    campeao_geral = max(enxadristas, key=lambda x: x['Total'])['nome']
    
    print(f'O enxadrista com mais pontos totais é: {campeao_geral}')
    print(f'O enxadrista com mais medalhas de ouro é: {campeao_ouro}')
    print(f'O enxadrista com mais medalhas de prata é: {campeao_prata}')
    print(f'O enxadrista com mais medalhas de bronze é: {campeao_bronze}')

print('<< Volte sempre >>')



