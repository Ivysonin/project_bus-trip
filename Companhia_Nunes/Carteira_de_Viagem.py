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
        escolha = input('Deseja comprar a passagem? (S / N): ').upper()
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
            print('\n===== Aqui está seu cartão de viagem =====\n')
            print(f'| ===================================')
            print(f'| Nome: {self.nome}') 
            print(f'| ===================================')
            print(f'| Idade: {self.idade}')
            print(f'| ===================================')
            print(f'| Acompanhado: {self.acompanhado}')
            print(f'| ===================================')
            print(f'| Passagem: {self.passagem}')
            print(f'| ===================================')
            print(f'| Lugar: {self.local_viagem}')
            print(f'| ===================================')
        else:
            print('\n===== Infelizmente, você não pode viajar porque não está cumprindo os requisitos. =====\n')