import math


class Probabilidade:

    def calcular_probabilidade(eventos_favoraveis, eventos_possiveis):
        probabilidade = eventos_favoraveis / eventos_possiveis
        return probabilidade


    def calcular_probabilidade_porcentagem(eventos_favoraveis, eventos_possiveis):
        probabilidade = eventos_favoraveis / eventos_possiveis
        probabilidadepocentagem = probabilidade * 100
        return probabilidadepocentagem
# usei class para me organisar experintação, pos foi recentimemente proposto o uso por outro professor.
# e no momento da progamação ainda não tinha intedido no que se aplicava tal metodo.
class ProbabilidadeBinomial:

    def calcular_probabilidade_binomial(resultados_desejados, lancamentos_feitos, probabilidade_resultado):
        numero_total_eventos = lancamentos_feitos
        numero_eventos_desejados = resultados_desejados
        probabilidade_resultado = probabilidade_resultado

        probabilidade = (math.comb(numero_total_eventos, numero_eventos_desejados)) * \
            (probabilidade_resultado ** numero_eventos_desejados) * \
            ((1 - probabilidade_resultado) ** (numero_total_eventos - numero_eventos_desejados))

        return probabilidade

class ProbabilidadePoisson:

    def calcular_probabilidade_poisson(media, numero_de_ocorrencias):
        probabilidade = (math.exp(-media) * media ** numero_de_ocorrencias) / math.factorial(numero_de_ocorrencias)
        return probabilidade

def calcular_probabilidade_total_poisson(media_desejada, numero_ocorrencias_desejadas):
    probabilidade_total = 0
    for k in range(numero_ocorrencias_desejadas + 1):
        probabilidade_poisson = ProbabilidadePoisson.calcular_probabilidade_poisson(media_desejada, k)
        probabilidade_total += probabilidade_poisson
    return probabilidade_total

# Escolha do cálculo
print("Escolha o cálculo desejado (probabilidade (pro) / binomial (bin)/ poisson poi")
escolha = input(" pro  / bin /  poi): \n").lower()

if escolha == "pro":
    eventos_favoraveis = int(input("Numero de eventos favoráveis:\n "))
    eventos_possiveis = int(input("Numero TOTAL de eventos possíveis:\n "))
    probabilidade = Probabilidade.calcular_probabilidade(eventos_favoraveis, eventos_possiveis)
    porcentagem_probabilidade = Probabilidade.calcular_probabilidade_porcentagem(eventos_favoraveis, eventos_possiveis)
    #'Probabilidade.calcular_probabilidade' seve para chamar algo na especifica class.

    print(f"A probabilidade é: {probabilidade:.8f}")
    print(f"A porcentagem é: {porcentagem_probabilidade:.2f}%")

elif escolha == "bin":
    resultados_desejados = int(input("Numero de resultados desejados:\n "))
    lancamentos_feitos = int(input("Numero de lançamentos feitos:\n "))
    probabilidade_resultado = float(input("Probabilidade do resultado desejado:\n "))
    probabilidade_binomial = ProbabilidadeBinomial.calcular_probabilidade_binomial(resultados_desejados, lancamentos_feitos, probabilidade_resultado)
    #'ProbabilidadeBinomial.calcular_probabilidade_binomial' seve para chamar algo na especifica class.
    print(f"A probabilidade binomial é: {probabilidade_binomial:.8f}")

elif escolha == "poi":
    forma = input("Forma simples? (s ou n): \n")

    if forma == "s":
        media_desejada = float(input("Media de ocorrências :\n "))
        numero_ocorrencias_desejadas = int(input("Numero de ocorrências desejadas:\n "))
        probabilidade_poisson = ProbabilidadePoisson.calcular_probabilidade_poisson(media_desejada, numero_ocorrencias_desejadas)
        #'ProbabilidadePoisson.calcular_probabilidade_poisson' seve para chamar algo na especifica class.
        print(f"A probabilidade de ocorrerem {numero_ocorrencias_desejadas} ocorrencias com media de {media_desejada} e {probabilidade_poisson:.8f}")
    else:
        media_desejada = float(input("Media desejada:\n "))
        numero_ocorrencias_desejadas = int(input("Numero de ocorrências desejadas:\n "))
        probabilidade_total = ProbabilidadePoisson.calcular_probabilidade_total_poisson(media_desejada, numero_ocorrencias_desejadas)
        #'calcular_probabilidade_total_poisson' seve para chamar algo na especifica class.
        print(f"A probabilidade de ocorrerem menos que {numero_ocorrencias_desejadas} ocorrencias com media desejada de {media_desejada} e {probabilidade_total:.8f}")

else:
    print("Escolha invalida.")

