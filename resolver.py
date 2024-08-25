# Acadêmico: Marianna Bove de Mello

# Enunciado: Para obter os pontos relativos a este trabalho, você deverá criar um programa, utilizando a
# linguagem Python, C, ou C++. Este programa, quando executado, irá apresentar os resultados de
# operações que serão realizadas entre dois conjuntos de dados.
# O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt)
# contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas
# em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas
# segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de
# operações que estão descritas no arquivo, este número de operações será um inteiro; as linhas
# seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o código da
# operação (U para união, I para interseção, D para diferença e C produto cartesiano), a segunda e
# terceira linhas conterão os elementos dos conjuntos separados por virgulas. 

arquivo_conjuntos = 'conjuntos.txt'

def ler_arquivo(arquivo_conjuntos):
    with open(arquivo_conjuntos, 'r') as file:
        linhas = file.readlines()
    num_operacoes = int(linhas[0].strip())
    operacoes = []

    for i in range(1, len(linhas), 3):
        operacao = linhas[i].strip()
        conjuntoA = set(map(int, linhas[i + 1].strip().split(',')))
        conjuntoB = set(map(int, linhas[i + 2].strip().split(',')))
        operacoes.append((operacao, conjuntoA, conjuntoB))

    return num_operacoes, operacoes

def realizar_operacao(operacao, conjuntoA, conjuntoB):
    if operacao == 'U':
        return 'União', conjuntoA.union(conjuntoB)
    if operacao == 'I':
        return 'Interseção', conjuntoA.intersection(conjuntoB)
    if operacao == 'D':
        return 'Diferença', conjuntoA.difference(conjuntoB)
    if operacao == 'C':
        return 'Produto Cartesiano', {f'({x}, {y})' for x in conjuntoA for y in conjuntoB}

def ordenar_produto_cartesiano(produto):
    def chave_ordenacao(par):
        x, y = par.split(',')
        return int(x[1:]), int(y[:-1])

    return sorted(produto, key=chave_ordenacao)

def formatar_saida(nome_operacao, conjuntoA, conjuntoB, resultado):
    conjuntoA_str = ", ".join(map(str, sorted(conjuntoA)))
    conjuntoB_str = ", ".join(map(str, sorted(conjuntoB)))

    if nome_operacao == 'Produto Cartesiano':
        resultado_ordenado = ordenar_produto_cartesiano(resultado)
        resultado_str = ", ".join(resultado_ordenado)
    else:
        resultado_str = ", ".join(map(str, sorted(resultado)))
        
    return (f"{nome_operacao}: \n\n Conjunto A: {{{conjuntoA_str}}} \n\n Conjunto B: {{{conjuntoB_str}}} \n\n Resultado: {{{resultado_str}}}")

def main():
    num_operacoes, operacoes = ler_arquivo(arquivo_conjuntos)
    for operacao, conjuntoA, conjuntoB in operacoes:
        nome_operacao, resultado = realizar_operacao(operacao, conjuntoA, conjuntoB)
        saida = formatar_saida(nome_operacao, conjuntoA, conjuntoB, resultado)
        print(saida)

if __name__ == "__main__":
    main()

