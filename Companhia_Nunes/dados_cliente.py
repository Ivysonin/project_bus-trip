# Adquirindo dados dos clientes.

# Local da viagem
def local_viagem_cliente() -> str:
    local_viagem = str()
    while local_viagem not in ['1', '2', '3']:
        try:
            local_viagem = input('Qual o local de viagem deseja escolher: ')
            if local_viagem not in ['1', '2', '3']:
                raise ValueError
        except ValueError:
            print('\n===== ERRO: Escolha um número apresentado (1, 2, 3) =====\n')

    match local_viagem:
        case '1':
            local_viagem = 'Tamandaré'
        case '2':
            local_viagem = 'São José'
        case '3':
            local_viagem = 'Porto de Galinhas'
    return local_viagem


# Nome do cliente
def nome_cliente() -> str:
    nome = input('Nome: ')
    return nome


# Idade do cliente
def idade_cliente() -> int:
    try:
        idade = int(input('Idade: '))
    except ValueError:
        idade = 0
    return idade


# Dinheiro do cliente (True or false)
def dinheiro_cliente() -> str:
    dinheiro = input('Tem 25$ ou mais? (S / N): ').upper()
    if dinheiro == 'S':
        dinheiro = 'sim'
    elif dinheiro == 'N':
        dinheiro = 'não'
    else:
        dinheiro = 'Não há informações'
    return dinheiro


# Cliente está acompanhado ou não (True or False)
def acompanhado_cliente() -> str:
    acompanhado = input('Você está acompanhado? (S / N): ').upper()
    if acompanhado == 'S':
        acompanhado = 'sim'
    elif acompanhado == 'N':
        acompanhado = 'não'
    else:
        acompanhado = 'Não há informações'
    return acompanhado