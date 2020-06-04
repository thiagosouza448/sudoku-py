def ver_possiveis(candidatos, lista):
    """
    Retorna uma lista de valores posssiveis para a lista fornecida
    """
    for candidato in candidatos.copy():
        if candidato in lista:
            candidatos.remove(candidato)

def lin_lista(sudoku, linha):
    """ 
    Retorna uma linha do sudoku
    É relativamente fácil obter o resultado desta função
    portanto não é totalmente necessária
    """
    return sudoku[linha]

def col_lista(sudoku, coluna):
    """
    Retorna uma coluna do sudoku
    """
    return [sudoku[i][coluna]
            for i in range(9)]

def qua_lista(sudoku, linha, coluna):
    """
    Retorna um quadrado do sudoku em forma de lista
    """
    linha = linha // 3 * 3
    coluna = coluna // 3 * 3
    return [sudoku[i][j]
             for j in range(coluna, coluna + 3)
            for i in range(linha, linha + 3)]

def sudoku_zeros(sudoku):
    """ Conta a quantidade de zeros existentes no sudoku """
    zeros = 0
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                zeros += 1
    # Seria possível reduzir o código para apenas 1 linha:
    # return [linha for linha in sudoku].count(0)
    return zeros