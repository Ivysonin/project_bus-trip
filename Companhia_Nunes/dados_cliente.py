# Definindo cores usando sequência de escape ANSI
cor_ciano = '\033[1;36m'
cor_vermelho = '\033[31m'
reset_cor = '\033[0m' # Resetar a cor para o padrão

# Adquirindo dados dos clientes.

# Local da viagem
def local_viagem_cliente() -> str:
    local_viagem = str()
    while local_viagem not in ['1', '2', '3']:
        try:
            local_viagem = input(f'{cor_ciano}Qual o local de viagem deseja escolher: {reset_cor}')
            if local_viagem not in ['1', '2', '3']:
                raise ValueError
        except ValueError:
            print(f'\n{cor_vermelho}===== ERRO: Escolha um número apresentado (1, 2, 3) =====\n{reset_cor}')

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
    nome = input(f'{cor_ciano}Nome: {reset_cor}')
    return nome


# Idade do cliente
def idade_cliente() -> int:
    try:
        idade = int(input(f'{cor_ciano}Idade: {reset_cor}'))
    except ValueError:
        idade = 0
    return idade


# Dinheiro do cliente (True or false)
def dinheiro_cliente() -> str:
    dinheiro = input(f'{cor_ciano}Tem 25$ ou mais? (S / N): {reset_cor}').upper()
    if dinheiro == 'S':
        dinheiro = 'sim'
    elif dinheiro == 'N':
        dinheiro = 'não'
    else:
        dinheiro = 'Não há informações'
    return dinheiro


# Cliente está acompanhado ou não (True or False)
def acompanhado_cliente() -> str:
    acompanhado = input(f'{cor_ciano}Você está acompanhado? (S / N): {reset_cor}').upper()
    if acompanhado == 'S':
        acompanhado = 'sim'
    elif acompanhado == 'N':
        acompanhado = 'não'
    else:
        acompanhado = 'Não há informações'
    return acompanhado