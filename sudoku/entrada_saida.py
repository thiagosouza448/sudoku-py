def le_sudoku(arquivo_texto):
    """ 
    Lê um arquivo de texto txt separado por espaços e
    retorna uma lista de listas com valores inteiros, que
    representam o sudoku
    """
    try:
        with open(arquivo_texto) as arquivo:
            sudoku = [[int(valor) 
                    for valor in linha.split()]
                    for linha in arquivo]
        if verifica_sudoku(sudoku):
            return sudoku
    except FileNotFoundError:
        print('Arquivo não encontrado.')
        pass
    except ValueError:
        print('Arquivo com dados inválidos.')
        pass
    except:
        print('Erro inesperado.')
        raise

def verifica_sudoku(sudoku):
    n = len(sudoku)
    if n != 9:
        print('Sudoku inconsistente. Contém {} linhas'.format(n))
        return False
    for i in range(9):
        n = len(sudoku[i])
        if n != 9:
            print('Sudoku inconsistente. A linha {} contém {} colunas'.format(i, n))
            return False
    return True

def imprime_sudoku(sudoku):
    saida = '# ' * 12 + '#\n'
    for i in range(9):
        saida += '# '
        for j in range(9):
            if j % 3 == 0 and j != 0:
                saida += '| '
            saida += str(sudoku[i][j]) + ' '
        if i % 3 == 2 and i != 8:
            saida += '#\n#' + ('-'*7 + '+')*2 + '-'*7
        saida += '#\n'
    saida += '# ' * 12 + '#'
    return saida

def salva_sudoku(sudoku, nome_do_arquivo):
    if verifica_sudoku(sudoku):
        try:
            arquivo = open(nome_do_arquivo, 'x')
        except FileExistsError:
            resp = input('Arquivo já existe. Deseja substituí-lo? (s/n)')
            if resp.lower() == 's':
                arquivo = open(nome_do_arquivo, 'w')
            else:
                print('O arquivo não foi gerado')
                return
        print('* * * Gerando arquivo * * *')
        print(imprime_sudoku(sudoku))
        for linha in sudoku:
            arquivo.writelines(str(linha).replace('[','').replace(',',' ').replace(']','') + '\n')
        print('* * * Arquivo gerado com sucesso * * *')
