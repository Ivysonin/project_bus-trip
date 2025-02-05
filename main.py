# Importações
from Companhia_Nunes.Carteira_de_Viagem import Carteira_viagem
from Companhia_Nunes.dados_cliente import *


# Definindo cores usando sequência de escape ANSI
cor_ciano = '\033[1;36m'
reset_cor = '\033[0m' # Resetar a cor para o padrão


# Iniciando programa
print(f'{cor_ciano}\n===== Bem-vindo(a) a Companhia Nunes =====\n{reset_cor}')

print(f'{cor_ciano}Nossas Passagens disponíveis:\n{reset_cor}')
print('1. Tamandaré')
print('2. São José')
print('3. Porto de Galinhas\n')
local_viagem = local_viagem_cliente()

# Coletando informações do cliente
print('\n--- Informe seus dados ---\n')
nome = nome_cliente()
idade = idade_cliente()
dinheiro = dinheiro_cliente()
acompanhado = acompanhado_cliente()

cliente = Carteira_viagem(nome, idade, dinheiro, acompanhado, local_viagem)

cliente.comprar_passagem() # Comprando a pagassem
cliente.panfletos_passagem() # Exibindo informações da passagem

print(f'{cor_ciano}\n===== Obrigado por escolher nossa Companhia !!! =====\n{reset_cor}')