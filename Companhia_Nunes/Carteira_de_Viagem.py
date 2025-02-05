# Definindo cores usando sequência de escape ANSI
cor_ciano = '\033[1;36m'
cor_verde = '\033[1;32m'
cor_vermelho = '\033[31m'
reset_cor = '\033[0m' # Resetar a cor para o padrão


class Carteira_viagem:
    def __init__(self, nome_cliente: str, idade_cliente: int, dinheiro_cliente: str, acompanhado_cliente: str, local_viagem: str):
        self.nome = nome_cliente
        self.idade = idade_cliente
        self.dinheiro = dinheiro_cliente
        self.acompanhado = acompanhado_cliente
        self.local_viagem = local_viagem
        self.passagem = str()


    # Comprando a passagem
    def comprar_passagem(self) -> str:
        escolha = input(f'{cor_ciano}Deseja comprar a passagem? (S / N): {reset_cor}').upper()
        if escolha == 'S':
            self.passagem = 'sim'
        elif escolha == 'N':
            self.passagem = 'não'
        else:
            self.passagem = 'Não há informações'
        return self.passagem


    # Exibindo as informações do cliente
    def panfletos_passagem(self):
        if (self.idade > 14 and self.passagem == 'sim') or (self.idade < 14 and self.passagem == 'sim' and self.acompanhado == 'sim'):
            print(f'{cor_verde}\n===== Aqui está seu cartão de viagem =====\n{reset_cor}')
            print(f'{cor_verde}| ==================================={reset_cor}')
            print(f'{cor_verde}|{reset_cor} Nome: {self.nome}') 
            print(f'{cor_verde}| ==================================={reset_cor}')
            print(f'{cor_verde}|{reset_cor} Idade: {self.idade}')
            print(f'{cor_verde}| ==================================={reset_cor}')
            print(f'{cor_verde}|{reset_cor} Acompanhado: {self.acompanhado}')
            print(f'{cor_verde}| ==================================={reset_cor}')
            print(f'{cor_verde}|{reset_cor} Passagem: {self.passagem}')
            print(f'{cor_verde}| ==================================={reset_cor}')
            print(f'{cor_verde}|{reset_cor} Lugar: {self.local_viagem}')
            print(f'{cor_verde}| ==================================={reset_cor}')
        else:
            print(f'{cor_vermelho}\n===== Infelizmente, você não pode viajar porque não está cumprindo os requisitos. ====={reset_cor}')