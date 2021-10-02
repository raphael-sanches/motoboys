# Os motoboys podem ter exclusividade com as lojas, mas as lojas não possuem exclusividade com os motoboys.
#
# Hoje existem 10 pedidos para serem retirados em 3 lojas.
#
# Quando eu executar o script passando apenas o motoboy ou não passando nenhum motoboy, preciso ver:
# Quem é o motoboy e quantos pedidos terá?
# De qual loja é?
# Quanto vai ganhar?
#
# Dados do teste
#
# Motoboys
# Moto 1 - cobra R$2 reais por entrega e atende todas as lojas
# Moto 2 - cobra R$2 reais por entrega e atende todas as lojas
# Moto 3 - cobra R$2 reais por entrega e atende todas as lojas
# Moto 4 - cobra R$2 reais por entrega e atende apenas a loja 1
# Moto 5 - cobra R$3 reais por entrega e atende todas as lojas
#
# Lojas
# Loja 1 - 3 pedidos (PEDIDO 1 R$50, PEDIDO 2 R$50, PEDIDO 3 R$50) e paga 5% do valor pedido por entrega
# fora o valor fixo.
# Loja 2 - 4 pedidos (PEDIDO 1 R$50, PEDIDO 2 R$50, PEDIDO 3 R$50, PEDIDO 4 R$50) e paga 5% do valor pedido por entrega
# fora o valor fixo.
# Loja 3 - 3 pedidos (PEDIDO 1 R$50, PEDIDO 2 R$50, PEDIDO 3 R$100) e paga 15% do valor pedido por entrega
# fora o valor fixo.
#
# O Moto 1 atende todas as lojas
# O Moto 2 atende todas as lojas
# O Moto 3 atende todas as lojas
# O Moto 4 atende apenas a loja 1
# O Moto 5 atende todas as lojas

motoboys = {
    'Motoboy 1': {
        'Nome': 1,
        'Valor': 2,
        'Lojas': [1, 2, 3]},
    'Motoboy 2': {
        'Nome': 2,
        'Valor': 2,
        'Lojas': [1, 2, 3]},
    'Motoboy 3': {
        'Nome': 3,
        'Valor': 2,
        'Lojas': [1, 2, 3]},
    'Motoboy 4': {
        'Nome': 4,
        'Valor': 2,
        'Lojas': [1]},
    'Motoboy 5': {
        'Nome': 5,
        'Valor': 3,
        'Lojas': [1, 2, 3]}
}

lojas = {
    'Loja 1': {
        'Nome': 1,
        'TotalPedidos': 3,
        'Porcentagem': 5,
        'ValorPedidos': 150,
        'ValorPorcentagem': 7.5,
        'Pedidos': {'Pedido 1': {'Valor': 50},
                    'Pedido 2': {'Valor': 50},
                    'Pedido 3': {'Valor': 50}
                    }
    },
    'Loja 2': {
        'Nome': 2,
        'TotalPedidos': 4,
        'Porcentagem': 5,
        'ValorPedidos': 200,
        'ValorPorcentagem': 10,
        'Pedidos': {'Pedido 1': {'Valor': 50},
                    'Pedido 2': {'Valor': 50},
                    'Pedido 3': {'Valor': 50},
                    'Pedido 4': {'Valor': 50}
                    },
    },
    'Loja 3': {
        'Nome': 3,
        'TotalPedidos': 3,
        'Porcentagem': 15,
        'ValorPedidos': 200,
        'ValorPorcentagem': 30,
        'Pedidos': {'Pedido 1': {'Valor': 50},
                    'Pedido 2': {'Valor': 50},
                    'Pedido 3': {'Valor': 100}
                    }
        }
}


def calculounitario(motoboy, loja):
    for nome1 in lojas:
        if str(loja) in nome1:
            loja = nome1
            for nome2 in motoboys:
                if str(motoboy) in nome2:
                    motoboy = nome2
                    valor = motoboys[motoboy]['Valor'] + lojas[loja]['ValorPorcentagem']
                    pedidos = lojas[loja]['TotalPedidos']
                    print()
                    print(f'O valor a ser pago ao motoboy será de R$ {valor} para entregar {pedidos} pedidos')


def calculogeral(motoboy, loja):
    if loja == 0 and motoboy != 4:
        valorporcentagem = 0
        valor = 0
        pedidos = 0
        for nome1 in lojas:
            valorporcentagem += lojas[nome1]['ValorPorcentagem']
            pedidos += lojas[nome1]['TotalPedidos']
        for nome2 in motoboys:
            if str(motoboy) in nome2:
                valor = (motoboys[nome2]['Valor'] * 3) + valorporcentagem
        print()
        print(f'Ao atender todas as lojas o Motoboy {motoboy} terá {pedidos} pedidos e receberá o valor de R$ {valor}')


def dadosmotoboy(arg):
    for nome in motoboys:
        if str(arg) in nome:
            motoboy = nome
            lojasatendidas = str(motoboys[motoboy]['Lojas'])
            valor = motoboys[motoboy]['Valor']
            print(f'Você será atendido pelo motoboy: {motoboy}.')
            print(f'Disponível para as Lojas: {lojasatendidas}, pelo valor de R$ {valor} por entrega.')


def dadosloja(arg):
    for nome in lojas:
        if str(arg) in nome:
            print()
            loja = nome
            print(f'Você escolheu a loja: {loja}')
            print(lojas[loja])


def cadastromotoboys():
    print()
    print(f'Temos os seguintes Motoboys cadastrados:')
    for nome in motoboys:
        print(nome)
        print(motoboys[nome])
        print()


def cadastrolojas():
    print()
    print(f'Temos as seguintes Lojas cadastradas:')
    for nome in lojas:
        print(nome)
        print(lojas[nome])
        print()


motoboy = int(input("Escolha um Motoboy (de 1 a 5) ou digite (0): "))
loja = int(input("Escolha uma Loja (de 1 a 3) ou digite (0): "))
print()
if motoboy == 4 and loja != 1:
    print('O Motoboy 4 atende somente a Loja 1 nas seguintes condições:')
    dadosmotoboy(motoboy)
    dadosloja(1)
    calculounitario(motoboy, 1)
if motoboy == 0 and loja > 0:
    dadosloja(loja)
    calculogeral(motoboy, loja)
    cadastromotoboys()
if loja == 0 and motoboy > 0 and motoboy != 4:
    dadosmotoboy(motoboy)
    calculogeral(motoboy, loja)
    cadastrolojas()
if motoboy == 0 and loja == 0:
    cadastromotoboys()
    cadastrolojas()
if motoboy > 0 and motoboy != 4 and loja > 0:
    dadosmotoboy(motoboy)
    dadosloja(loja)
    calculounitario(motoboy, loja)
