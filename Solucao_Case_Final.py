# Importa os módulos do pacote sudoku e estabelece os alias
import sudoku.entrada_saida as sd_io
import sudoku.util as sd_ut

# Nome do arquivo que será aberto
# Pode localizar os arquivos de forma automática ou 
# Solicitar ao usuário para informar o nome dos arquivos ou
# Preparar um laço que passe por todos os arquivos de teste
nome_do_arquivo = 'sudoku01.txt'

# A variável lcq armazena as funções de listar linha, coluna e quadrado
# Exatamente nesta ordem
# Desta forma é possível chamar cada uma das funções de forma mais rápida
# Outra solução seria utilizar imports de cada uma delas e fornecer um alias diferente para cada uma
# import sudoku.util.lin_lista as l
# import sudoku.util.col_lista as c
# import sudoku.util.qua_lista as q
lcq = sd_ut.lin_lista, sd_ut.col_lista, sd_ut.qua_lista

sudoku = sd_io.le_sudoku(nome_do_arquivo)
print('Sudoku lido com sucesso')
print(sd_io.imprime_sudoku(sudoku))

# Variável que indica quando terminar o laço
repetir = True
while repetir:
    # Conta os zeros para utilizar como condição de saída
    zeros = sd_ut.sudoku_zeros(sudoku)

    # Cria a lista de linhas e colunas que faltam verificar
    linhas = list(range(9))
    colunas = list(range(9))
    while len(linhas) + len(colunas) > 0:
        maior_linha = maior_coluna = -1, -1
        for i in linhas:
            n = 9 - lcq[0](sudoku, i).count(0)  # Conta a quantidade de valores preenchida na linha
            if n > maior_linha[1]:  # Verifica se encontrou uma linha com um numero maior de elementos preenchidos
                maior_linha = i, n
        for j in colunas:
            m = 9 - lcq[1](sudoku, j).count(0)  # Conta a quantidade de valores preenchida na coluna
            if m > maior_coluna[1]:  # Verifica se encontrou uma coluna com um numero maior de elementos preenchidos
                maior_coluna = j, m
        if maior_coluna[1] > maior_linha[1]:
            colunas.remove(maior_coluna[0])
            coluna = lcq[1](sudoku, maior_coluna[0])
            for i in range(9):
                if coluna[i] == 0:
                    pos = list(range(1, 10))
                    l = lcq[0](sudoku, i)
                    c = lcq[1](sudoku, maior_coluna[0])
                    q = lcq[2](sudoku, i, maior_coluna[0])
                    for k in [l, c, q]:
                        sd_ut.ver_possiveis(pos, k)
                    if len(pos) == 1:
                        sudoku[i][maior_coluna[0]] = pos[0]
                    elif len(pos) == 0:
                        repetir = False
                        print('''Impossível de Resolver.\n
                            Não há valor possível para a linha {} e coluna {}.'''.format(i, maior_coluna[0]))
        else:
            linhas.remove(maior_linha[0])
            linha = lcq[0](sudoku, maior_linha[0])
            for j in range(9):
                if linha[j] == 0:
                    pos = list(range(1, 10))
                    l = lcq[0](sudoku, maior_linha[0])
                    c = lcq[1](sudoku, j)
                    q = lcq[2](sudoku, maior_linha[0], j)
                    for k in [l, c, q]:
                        sd_ut.ver_possiveis(pos, k)
                    if len(pos) == 1:
                        sudoku[maior_linha[0]][j] = pos[0]
                    elif len(pos) == 0:
                        repetir = False
                        print('''Impossível de Resolver.\n
                            Não há valor possível para a linha {} e coluna {}.'''.format(maior_linha[0], j))
    if zeros == 0:
        repetir = False
        print('Sudoku concluído. Preparando para salvar o resultado.')
    elif zeros == sd_ut.sudoku_zeros(sudoku):
        repetir = False
        print('Impossível de Resolver. O sudoku não é muito fácil')

sd_io.salva_sudoku(sudoku, 'solucao\\' + nome_do_arquivo)
