import random
"""
facep1 = random. randint (0 , 10 )
facep2 = random. randint (1 , 10 )
face = facep1 + facep2
print(f"{face}\n")
"""
"""# melhor ficaria 
 mface = random. randint (1 , 20 )
 print(f"{mface}\n")"""



import random

class Dados:
    def __init__(self, Nfaces, face0):
        self.Nfaces = Nfaces
        self.face0 = face0
        self.resultados = []  # Lista para armazenar os resultados dos lançamentos
    
    def rolagem(self, limite_consecutivo):
        resultado = random.randint(self.face0, self.Nfaces)
        
        # Verifica se o resultado é igual ao último resultado da lista
        if len(self.resultados) > 0 and resultado == self.resultados[-1]:
            contagem = 1
            while contagem < limite_consecutivo and resultado == self.resultados[-1]:
                resultado = random.randint(self.face0, self.Nfaces)
                contagem += 1
        
        self.resultados.append(resultado)  # Adiciona o resultado à lista de resultados
        print(f"Resultado do lançamento: {resultado}")

# Função para realizar o lançamento do dado e perguntar se deseja continuar
def realizar_lancamento(dados, limite_consecutivo):
    dados.rolagem(limite_consecutivo)
    resposta = input("Deseja rodar o dado novamente? (s/n): ")
    return resposta.lower() == 's'

# Criação de um objeto da classe Dados
Nfaces = int(input("Número de faces do dado: "))
face0 = 1  # Valor mínimo do dado
dados = Dados(Nfaces, face0)

# Definindo o limite de resultados consecutivos
limite_consecutivo = 5

# Realização de lançamentos
continuar = True
while continuar:
    continuar = realizar_lancamento(dados, limite_consecutivo)

# Exibição dos resultados dos lançamentos
print("Resultados dos lançamentos:", dados.resultados)