# Importações
from Companhia_Nunes.Carteira_de_Viagem import Carteira_viagem
from Companhia_Nunes.dados_cliente import *


# Iniciando programa
print('\n===== Bem-vindo(a) a Companhia Nunes =====\n')

print('Nossas Passagens disponíveis:\n')
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

print('\n===== Boa viagem !!! =====\n') 