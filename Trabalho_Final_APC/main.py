"""O codigo basicamente lê o arquivo de entrada e coloca as linhas desse arquivo na matriz "lista" até o primeiro termo da linha for um digito.
Quando o termo da linha for um digito, o código para de adicionar as linhas do arquivo na matriz "lista" e passa a adicionar as palavras das
linhas seguintes da linha do digito na lista "palavra". A quantidade de palavras a serem adicionadas na lista "palavra" é juntamente a quantidade
expressa no digito. A partir da matriz "lista", é gerada uma matriz "matriz" de mesma largura e altura e que preencherá seus termos com pontinhos que
no futuro serão substituidos pelas letras das palavras encontradas no caça-palavra. Depois disso, são analisados termo por termo da matriz "lista"
e procurados no código cada palavra da lista "palavra". Se a palavra for encontrada no caça-palavras da matriz "lista", as letras correspondentes
substituirão os pontinhos da matriz "matriz" em seus respectivos indices. No final, é printado na tela a matriz "matriz" com as palavras encontradas
e é gerado um arquivo de saída com nome escolhido pelo usuário que conterá o resultado final em forma de arquivo"""


def horizontal_esquerda_direita(lista, palavra, matriz, i, j, a):
    # lista que recebe somente cada letra letra da matriz original correspondente a cada letra de busca, sem as coordenadas
    t = []

    # lista que receberá cada letra na matriz original correspondente a cada letra da palavra busca, seguida da coordenada dessa letra na matriz original para substituir ela na matriz final
    q = []

    # variavel utilizada para saber a linha correspondente a letra presente na lista "q"
    c = 1

    # variavel utilizada para saber a coluna correspondente a letra presenta na lista "q"
    z = 2

    # variavel utilizada para saber qual a letra correspondente na lista "q"
    d = 0

    # variavel que recebe o valor da posição inicial horizontal e que vai acumular para analisar letra a letra
    n = j

    # variavel que recebe o valor da posição inicial da letra buscada e que vai acumular até chegar na ultima letra
    m = 0

    # Enquanto cada letra analisada da matriz original for correspondente a letra analisada da palavra buscada
    while lista[i][n] == palavra[a][m]:

        # t adiciona na lista cada letra correspondente da matriz original
        t.append(lista[i][n])

        # q adiciona na lista cada letra correspondente da matriz original
        q.append(lista[i][n])

        # q adiciona na lista a coordenada da linha da matriz original
        q.append(i)

        # q aidicona na lista a coordenada da coluna da matriz original
        q.append(n)

        # se o valor de m for igual a posição da ultima letra da palavra busca ou o valor de n for igual a posição limite do lado direito, a repetição acaba
        if m == (len(palavra[a]) - 1) or n == (len(lista[0]) - 1):
            break

        # Se a posição da letra da palavra buscada for menor que a posição da ultima letra da palavra
        if m < (len(palavra[a]) - 1):
            # posição seguinte horizontal
            n = n + 1

            # posição da proxima letra da palavra buscada
            m = m + 1

    # Se o numero de letras da lista t for igual ao numero de letras da palavra buscada
    if len(t) == len(palavra[a]):

        # analisando cada posição cada coordenada da matriz de pontinhos na ordem crescente vertical e crescente horizontal, se tiver as mesma coordenadas q[c] e q[z], substitui o ponto pela letra q[d]
        for k in range(len(lista)):
            for l in range(len(lista[0])):
                if q != []:
                    if q[c] == k and q[z] == l:
                        matriz[k][l] = q[d]
                        del (q[0:3])
        q = []
        t = []
    else:
        q = []
        t = []
        return matriz


def horizontal_direita_esquerda(lista, palavra, matriz, i, j, a):
    # lista que recebe somente cada letra letra da matriz original correspondente a cada letra de busca, sem as coordenadas
    t = []

    # lista que receberá cada letra na matriz original correspondente a cada letra da palavra busca, seguida da coordenada dessa letra na matriz original para substituir ela na matriz final
    q = []

    # variavel utilizada para saber a linha correspondente a letra presente na lista "q"
    c = 1

    # variavel utilizada para saber a coluna correspondente a letra presenta na lista "q"
    z = 2

    # variavel utilizada para saber qual a letra correspondente na lista "q"
    d = 0

    # variavel que recebe o valor da posição inicial horizontal e que vai diminuir para analisar letra a letra
    n = j

    # variavel que recebe o valor da posição inicial da letra buscada e que vai acumular até chegar na ultima letra
    m = 0

    # Enquanto cada letra analisada da matriz original for correspondente a letra analisada da palavra buscada
    while lista[i][n] == palavra[a][m]:

        # t adiciona na lista cada letra correspondente da matriz original
        t.append(lista[i][n])

        # q adiciona na lista cada letra correspondente da matriz original
        q.append(lista[i][n])

        # q adiciona na lista a coordenada da linha da matriz original
        q.append(i)

        # q aidicona na lista a coordenada da coluna da matriz original
        q.append(n)

        # se o valor de m for igual a posição da ultima letra da palavra busca ou o valor de n for igual a posição limite do lado esquerdo, a repetição acaba
        if m == (len(palavra[a]) - 1) or n == 0:
            break

        # Se a posição da letra da palavra buscada for menor que a posição da ultima letra da palavra
        if m < (len(palavra[a]) - 1):
            # posição anterior horizontal
            n = n - 1

            # posição da proxima letra da palavra buscada
            m = m + 1

    # Se o numero de letras da lista t for igual ao numero de letras da palavra buscada
    if len(t) == len(palavra[a]):

        # analisando cada posição cada coordenada da matriz de pontinhos na ordem decrescente vertical e decrescente horizontal, se tiver as mesma coordenadas q[c] e q[z], substitui o ponto pela letra q[d]
        for k in range(len(lista)):
            rk = y - k - 1
            for l in range(len(lista[0])):
                rl = (len(lista[0]) - l - 1)
                if q != []:
                    if q[c] == rk and q[z] == rl:
                        matriz[rk][rl] = q[d]
                        del (q[0:3])

        q = []
        t = []
    else:
        q = []
        t = []
    return matriz


def vertical_cima_baixo(lista, palavra, matriz, i, j, a):
    # lista que recebe somente cada letra letra da matriz original correspondente a cada letra de busca, sem as coordenadas
    t = []

    # lista que receberá cada letra na matriz original correspondente a cada letra da palavra busca, seguida da coordenada dessa letra na matriz original para substituir ela na matriz final
    q = []

    # variavel utilizada para saber a linha correspondente a letra presente na lista "q"
    c = 1

    # variavel utilizada para saber a coluna correspondente a letra presenta na lista "q"
    z = 2

    # variavel utilizada para saber qual a letra correspondente na lista "q"
    d = 0

    # variavel que recebe o valor da posição inicial vertical e que vai acumular para analisar letra a letra
    n = i

    # variavel que recebe o valor da posição inicial da letra buscada e que vai acumular até chegar na ultima letra
    m = 0

    # Enquanto cada letra analisada da matriz original for correspondente a letra analisada da palavra buscada
    while lista[n][j] == palavra[a][m]:

        # t adiciona na lista cada letra correspondente da matriz original
        t.append(lista[n][j])

        # q adiciona na lista cada letra correspondente da matriz original
        q.append(lista[n][j])

        # q adiciona na lista a coordenada da linha da matriz original
        q.append(n)

        # q aidicona na lista a coordenada da coluna da matriz original
        q.append(j)

        # se o valor de m for igual a posição da ultima letra da palavra busca ou o valor de n for igual a posição limite do lado inferior, a repetição acaba
        if m == (len(palavra[a]) - 1) or n == y - 1:
            break

        # Se a posição da letra da palavra buscada for menor que a posição da ultima letra da palavra
        if m < (len(palavra[a]) - 1):
            # posição seguinte vertical
            n = n + 1

            # posição da proxima letra da palavra buscada
            m = m + 1

    # Se o numero de letras da lista t for igual ao numero de letras da palavra buscada
    if len(t) == len(palavra[a]):

        # analisando cada posição cada coordenada da matriz de pontinhos na ordem crescente vertical e crescente horizontal, se tiver as mesma coordenadas q[c] e q[z], substitui o ponto pela letra q[d]
        for k in range(len(lista)):
            for l in range(len(lista[0])):
                if q != []:
                    if q[c] == k and q[z] == l:
                        matriz[k][l] = q[d]
                        del (q[0:3])
        q = []
        t = []
    else:
        q = []
        t = []
    return matriz


def vertical_baixo_cima(lista, palavra, matriz, i, j, a):
    # lista que recebe somente cada letra letra da matriz original correspondente a cada letra de busca, sem as coordenadas
    t = []

    # lista que receberá cada letra na matriz original correspondente a cada letra da palavra busca, seguida da coordenada dessa letra na matriz original para substituir ela na matriz final
    q = []

    # variavel utilizada para saber a linha correspondente a letra presente na lista "q"
    c = 1

    # variavel utilizada para saber a coluna correspondente a letra presenta na lista "q"
    z = 2

    # variavel utilizada para saber qual a letra correspondente na lista "q"
    d = 0

    # variavel que recebe o valor da posição inicial vertical e que vai diminuir para analisar letra a letra                          
    n = i

    # variavel que recebe o valor da posição inicial da letra buscada e que vai acumular até chegar na ultima letra
    m = 0

    # Enquanto cada letra analisada da matriz original for correspondente a letra analisada da palavra buscada
    while lista[n][j] == palavra[a][m]:

        # t adiciona na lista cada letra correspondente da matriz original
        t.append(lista[n][j])

        # q adiciona na lista cada letra correspondente da matriz original
        q.append(lista[n][j])

        # q adiciona na lista a coordenada da linha da matriz original
        q.append(n)

        # q aidicona na lista a coordenada da coluna da matriz original
        q.append(j)

        # se o valor de m for igual a posição da ultima letra da palavra busca ou o valor de n for igual a posição limite do lado superior, a repetição acaba
        if m == (len(palavra[a]) - 1) or n == 0:
            break

        # Se a posição da letra da palavra buscada for menor que a posição da ultima letra da palavra
        if m < (len(palavra[a]) - 1):
            # Posição anterior vertical
            n = n - 1

            # Posição da proxima letra da palavra buscada
            m = m + 1

    # Se o numero de letras da lista t for igual ao numero de letras da palavra buscada
    if len(t) == len(palavra[a]):

        # analisando cada posição cada coordenada da matriz de pontinhos na ordem decrescente vertical e decrescente horizontal, se tiver as mesma coordenadas q[c] e q[z], substitui o ponto pela letra q[d]
        for k in range(len(lista)):
            rk = y - k - 1
            for l in range(len(lista[0])):
                rl = (len(lista[0]) - l - 1)
                if q != []:
                    if q[c] == rk and q[z] == rl:
                        matriz[rk][rl] = q[d]
                        del (q[0:3])
        q = []
        t = []
    else:
        q = []
        t = []
    return matriz


def diagonal_inferior_direita(lista, palavra, matriz, i, j, a):
    # lista que recebe somente cada letra letra da matriz original correspondente a cada letra de busca, sem as coordenadas
    t = []

    # lista que receberá cada letra na matriz original correspondente a cada letra da palavra busca, seguida da coordenada dessa letra na matriz original para substituir ela na matriz final
    q = []

    # variavel utilizada para saber a linha correspondente a letra presente na lista "q"
    c = 1

    # variavel utilizada para saber a coluna correspondente a letra presenta na lista "q"
    z = 2

    # variavel utilizada para saber qual a letra correspondente na lista "q"
    d = 0

    # variavel que recebe o valor da posição inicial vertical e que vai acumular para analisar letra a letra
    n = i

    # variavel que recebe o valor da posição inicial horizontal e que vai acumular para analisar letra a letra
    g = j

    # variavel que recebe o valor da posição inicial da letra buscada e que vai acumular até chegar na ultima letra
    m = 0

    # Enquanto cada letra analisada da matriz original for correspondente a letra analisada da palavra buscada
    while lista[n][g] == palavra[a][m]:

        # t adiciona na lista cada letra correspondente da matriz original
        t.append(lista[n][g])

        # q adiciona na lista cada letra correspondente da matriz original
        q.append(lista[n][g])

        # q adiciona na lista a coordenada da linha da matriz original
        q.append(n)

        # q aidicona na lista a coordenada da coluna da matriz original
        q.append(g)

        # se o valor de m for igual a posição da ultima letra da palavra busca ou o valor de n for igual a posição limite do lado inferior ou g for igual a posição limite do lado direito , a repetição acaba
        if m == (len(palavra[a]) - 1) or n == y - 1 or g == (len(lista[0]) - 1):
            break

        # Se a posição da letra da palavra buscada for menor que a posição da ultima letra da palavra
        if m < (len(palavra[a]) - 1):
            # Posição seguinte vertical
            n = n + 1

            # Posição seguinte horizontal
            g = g + 1

            # Posição da proxima letra da palavra buscada
            m = m + 1

    # Se o numero de letras da lista t for igual ao numero de letras da palavra buscada
    if len(t) == len(palavra[a]):

        # analisando cada posição cada coordenada da matriz de pontinhos na ordem crescente vertical e crescente horizontal, se tiver as mesma coordenadas q[c] e q[z], substitui o ponto pela letra q[d]
        for k in range(len(lista)):
            for l in range(len(lista[0])):
                if q != []:
                    if q[c] == k and q[z] == l:
                        matriz[k][l] = q[d]
                        del (q[0:3])

        q = []
        t = []
    else:
        q = []
        t = []
    return matriz


def diagonal_inferior_esquerda(lista, palavra, matriz, i, j, a):
    # lista que recebe somente cada letra letra da matriz original correspondente a cada letra de busca, sem as coordenadas
    t = []

    # lista que receberá cada letra na matriz original correspondente a cada letra da palavra busca, seguida da coordenada dessa letra na matriz original para substituir ela na matriz final
    q = []

    # variavel utilizada para saber a linha correspondente a letra presente na lista "q"
    c = 1

    # variavel utilizada para saber a coluna correspondente a letra presenta na lista "q"
    z = 2

    # variavel utilizada para saber qual a letra correspondente na lista "q"
    d = 0

    # variavel que recebe o valor da posição inicial vertical e que vai acumular para analisar letra a letra
    n = i

    # variavel que recebe o valor da posição inicial horizontal e que vai diminuir para analisar letra a letra
    g = j

    # variavel que recebe o valor da posição inicial da letra buscada e que vai acumular até chegar na ultima letra
    m = 0

    # Enquanto cada letra analisada da matriz original for correspondente a letra analisada da palavra buscada
    while lista[n][g] == palavra[a][m]:

        # t adiciona na lista cada letra correspondente da matriz original
        t.append(lista[n][g])

        # q adiciona na lista cada letra correspondente da matriz original
        q.append(lista[n][g])

        # q adiciona na lista a coordenada da linha da matriz original
        q.append(n)

        # q aidicona na lista a coordenada da coluna da matriz original
        q.append(g)

        # se o valor de m for igual a posição da ultima letra da palavra busca ou o valor de n for igual a posição limite do lado inferior ou g for igual a posição limite do lado esquerdo , a repetição acaba
        if m == (len(palavra[a]) - 1) or n == y - 1 or g == 0:
            break

        # Se a posição da letra da palavra buscada for menor que a posição da ultima letra da palavra
        if m < (len(palavra[a]) - 1):
            # Posição seguinte vertical
            n = n + 1

            # Posição anterior horizontal
            g = g - 1

            # Posição da proxima letra da palavra buscada
            m = m + 1

    # Se o numero de letras da lista t for igual ao numero de letras da palavra buscada
    if len(t) == len(palavra[a]):

        # analisando cada posição cada coordenada da matriz de pontinhos na ordem crescente vertical e decrescente horizontal, se tiver as mesma coordenadas q[c] e q[z], substitui o ponto pela letra q[d]
        for k in range(len(lista)):
            for l in range(len(lista[0])):
                rl = (len(lista[0])) - l - 1
                if q != []:
                    if q[c] == k and q[z] == rl:
                        matriz[k][rl] = q[d]
                        del (q[0:3])

        q = []
        t = []
    else:
        q = []
        t = []
    return matriz


def diagonal_superior_direita(lista, palavra, matriz, i, j, a):
    # lista que recebe somente cada letra letra da matriz original correspondente a cada letra de busca, sem as coordenadas
    t = []

    # lista que receberá cada letra na matriz original correspondente a cada letra da palavra busca, seguida da coordenada dessa letra na matriz original para substituir ela na matriz final
    q = []

    # variavel utilizada para saber a linha correspondente a letra presente na lista "q"
    c = 1

    # variavel utilizada para saber a coluna correspondente a letra presenta na lista "q"
    z = 2

    # variavel utilizada para saber qual a letra correspondente na lista "q"
    d = 0

    # variavel que recebe o valor da posição inicial vertical e que vai diminuir para analisar letra a letra
    n = i

    # variavel que recebe o valor da posição inicial horizontal e que vai acumular para analisar letra a letra
    g = j

    # variavel que recebe o valor da posição inicial da letra buscada e que vai acumular até chegar na ultima letra
    m = 0

    # Enquanto cada letra analisada da matriz original for correspondente a letra analisada da palavra buscada
    while lista[n][g] == palavra[a][m]:

        # t adiciona na lista cada letra correspondente da matriz original
        t.append(lista[n][g])

        # q adiciona na lista cada letra correspondente da matriz original
        q.append(lista[n][g])

        # q adiciona na lista a coordenada da linha da matriz original
        q.append(n)

        # q aidicona na lista a coordenada da coluna da matriz original
        q.append(g)

        # se o valor de m for igual a posição da ultima letra da palavra busca ou o valor de n for igual a posição limite do lado superior ou g for igual a posição limite do lado direito , a repetição acaba
        if m == (len(palavra[a]) - 1) or n == 0 or (g == len(lista[0]) - 1):
            break

        # Se a posição da letra da palavra buscada for menor que a posição da ultima letra da palavra
        if m < (len(palavra[a]) - 1):
            # Posição anterior vertical
            n = n - 1

            # Posição seguinte horizontal
            g = g + 1

            # Posição da proxima letra da palavra buscada
            m = m + 1

    # Se o numero de letras da lista t for igual ao numero de letras da palavra buscada
    if len(t) == len(palavra[a]):

        # analisando cada posição cada coordenada da matriz de pontinhos na ordem decrescente vertical e crescente horizontal, se tiver as mesma coordenadas q[c] e q[z], substitui o ponto pela letra q[d]
        for k in range(len(lista)):
            rk = y - k - 1
            for l in range(len(lista[0])):
                if q != []:
                    if q[c] == rk and q[z] == l:
                        matriz[rk][l] = q[d]
                        del (q[0:3])

        q = []
        t = []
    else:
        q = []
        t = []
    return matriz


def diagonal_superior_esquerda(lista, palavra, matriz, i, j, a):
    # lista que recebe somente cada letra letra da matriz original correspondente a cada letra de busca, sem as coordenadas
    t = []

    # lista que receberá cada letra na matriz original correspondente a cada letra da palavra busca, seguida da coordenada dessa letra na matriz original para substituir ela na matriz final
    q = []

    # variavel utilizada para saber a linha correspondente a letra presente na lista "q"
    c = 1

    # variavel utilizada para saber a coluna correspondente a letra presenta na lista "q"
    z = 2

    # variavel utilizada para saber qual a letra correspondente na lista "q"
    d = 0

    # variavel que recebe o valor da posição inicial vertical e que vai diminuir para analisar letra a letra
    n = i

    # variavel que recebe o valor da posição inicial horizontal e que vai diminuir para analisar letra a letra
    g = j

    # variavel que recebe o valor da posição inicial da letra buscada e que vai acumular até chegar na ultima letra
    m = 0

    # Enquanto cada letra analisada da matriz original for correspondente a letra analisada da palavra buscada
    while lista[n][g] == palavra[a][m]:

        # t adiciona na lista cada letra correspondente da matriz original
        t.append(lista[n][g])

        # q adiciona na lista cada letra correspondente da matriz original
        q.append(lista[n][g])

        # q adiciona na lista a coordenada da linha da matriz original
        q.append(n)

        # q aidicona na lista a coordenada da coluna da matriz original
        q.append(g)

        # se o valor de m for igual a posição da ultima letra da palavra busca ou o valor de n for igual a posição limite do lado superior ou g for igual a posição limite do lado esquerdo , a repetição acaba
        if m == (len(palavra[a]) - 1) or n == 0 or g == 0:
            break

        # Se a posição da letra da palavra buscada for menor que a posição da ultima letra da palavra
        if m < (len(palavra[a]) - 1):
            # Posição anterior vertical
            n = n - 1

            # Posição anterior horizontal
            g = g - 1

            # Posição da proxima letra da palavra buscada
            m = m + 1

    # Se o numero de letras da lista t for igual ao numero de letras da palavra buscada
    if len(t) == len(palavra[a]):

        # analisando cada posição cada coordenada da matriz de pontinhos na ordem decrescente vertical e decrescente horizontal, se tiver as mesma coordenadas q[c] e q[z], substitui o ponto pela letra q[d]
        for k in range(len(lista)):
            rk = y - k - 1
            for l in range(len(lista[0])):
                rl = len(lista[0]) - l - 1
                if q != []:
                    if q[c] == rk and q[z] == rl:
                        matriz[rk][rl] = q[d]
                        del (q[0:3])

        q = []
        t = []
    else:
        q = []
        t = []
    return matriz


def analise(palavra, lista, matriz):
    # lista que receberá cada letra na matriz original correspondente a cada letra da palavra busca, seguida da coordenada dessa letra na matriz original para substituir ela na matriz final
    q = []

    # variavel acumuladora que será util para analisar cada letra da palavra buscada
    m = 0

    # variavel utilizada para saber a linha correspondente a letra presente na lista "q"
    c = 1

    # variavel utilizada para saber a coluna correspondente a letra presenta na lista "q"
    z = 2

    # variavel utilizada para saber qual a letra correspondente na lista "q"
    d = 0

    # lista que recebe somente cada letra letra da matriz original correspondente a cada letra de busca, sem as coordenadas
    t = []

    # ANALISE

    # Para cada palavra da lista palavra, será analisada cada linha e coluna até achar uma letra que seja igual à primeira letra da palavra buscada
    for a in range(len(palavra)):
        for i in range(len(lista)):
            for j in range(len(lista[i])):

                # SE LETRA NA MATRIZ FOR IGUAL A PRIMEIRA LETRA DA PALAVRA ANALISADA
                if lista[i][j] == palavra[a][0]:

                    # horizontal

                    # Se a distancia da posição do termo até a borda direita for maior ou igual ao numero de letras da palavra buscada ou a distancia da posição do termo até a borda esquerda for maior ou igual ao numero de letras da palavra buscada
                    if len(lista[0]) - (lista[i].index(lista[i][j])) >= len(palavra[a]) or (
                            lista[i].index(lista[i][j]) + 1) >= len(palavra[a]):

                        # horizontal esquerda-direita

                        # Se a distancia da posição do termo até a borda direita for maior ou igual ao numero de letras da palavra buscada
                        if len(lista[0]) - lista[i].index(lista[i][j]) >= len(palavra[a]):
                            horizontal_esquerda_direita(lista, palavra, matriz, i, j, a)

                        # horizontal direita-esquerda

                        # Se a distancia da posição do termo até a borda esquerda for maior ou igual ao numero de letras da palavra buscada
                        if (lista[i].index(lista[i][j]) + 1) >= len(palavra[a]):
                            horizontal_direita_esquerda(lista, palavra, matriz, i, j, a)

                    # vertical

                    # Se a distancia da posição do termo até a borda inferior for maior ou igual ao numero de letras da palavra buscada ou a distancia da posição do termo até a borda superior for maior ou igual ao numero de letras da palavra buscada
                    if y - i >= len(palavra[a]) or i + 1 >= len(palavra[a]):

                        # vestical cima-baixo
                        if y - i >= len(palavra[a]):
                            vertical_cima_baixo(lista, palavra, matriz, i, j, a)

                        # vertical baixo-cima
                        if i + 1 >= len(palavra[a]):
                            vertical_baixo_cima(lista, palavra, matriz, i, j, a)

                    # Diagonal

                    # Se a distancia da posição do termo até a borda direita for maior ou igual ao numero de letras da palavra buscada ou a distancia da posição do termo até a borda esquerda for maior ou igual ao numero de letras da palavra buscada
                    # e se a distancia da posição do termo até a borda inferior for maior ou igual ao numero de letras da palavra buscada ou a distancia da posição do termo até a borda superior for maior ou igual ao numero de letras da palavra buscada
                    if len(lista[0]) - lista[i].index(lista[i][j]) + 1 >= len(palavra[a]) or lista[i].index(
                            lista[i][j]) + 1 >= len(palavra[a]) and y - i >= len(palavra[a]) or i + 1 >= len(
                            palavra[a]):

                        # Diagonal Inferior Direita

                        # Se a distancia  posição da letra inicial até a borda direita e até a borda inferior for maior ou igual que o tamanho da palavra buscada
                        if len(lista[0]) - lista[i].index(lista[i][j]) + 1 >= len(palavra[a]) and y - i >= len(
                                palavra[a]):
                            diagonal_inferior_direita(lista, palavra, matriz, i, j, a)

                        # Diagonal Inferior esquerda

                        # Se a distancia  posição da letra inicial até a borda esquerda e até a borda inferior for maior ou igual que o tamanho da palavra buscada
                        if lista[i].index(lista[i][j]) + 1 >= len(palavra[a]) and y - i >= len(palavra[a]):
                            diagonal_inferior_esquerda(lista, palavra, matriz, i, j, a)

                        # Diagonal superior direita

                        # Se a distancia  posição da letra inicial até a borda direita e até a borda superior for maior ou igual que o tamanho da palavra buscada
                        if len(lista[0]) - lista[i].index(lista[i][j]) + 1 >= len(palavra[a]) and i + 1 >= len(
                                palavra[a]):
                            diagonal_superior_direita(lista, palavra, matriz, i, j, a)

                        # Diagonal superior esquerda

                        # Se a distancia  posição da letra inicial até a borda esquerda e até a borda superior for maior ou igual que o tamanho da palavra buscada
                        if lista[i].index(lista[i][j]) + 1 >= len(palavra[a]) and i + 1 >= len(palavra[a]):
                            diagonal_superior_esquerda(lista, palavra, matriz, i, j, a)
    return matriz


def resultado_final(matriz):
    # Printa a Matriz como pedido no trabalho
    for o in range(y):
        for u in range(len(lista[0])):
            # Imprime termo por termo da matriz na tela
            print(matriz[o][u], end=" ")

            # Escreve termo por termo da matriz no arquivo de saída
            arquivo_de_saida.write(matriz[o][u] + " ")
        arquivo_de_saida.write("\n")
        print()


print("--------------------------------------------------------")
print(
    "Digite o nome de um arquivo de entrada e\nescolha um nome para um arquivo de saída\ncom seus respectivos formatos.\n\nExemplo: arquivo.txt")
print("--------------------------------------------------------")
# Recebe o nome do arquivo de entrada a ser analisado
resposta_entrada = str(input("Digite o nome do arquivo de entrada: "))

# Recebe o nome do arquivo de saída a ser criado(se não existir) ou substituir(se já existir)
resposta_saida = str(input("Escolha um nome para o arquivo de saída:"))

# Abre o arquivo de entrada no modo leitura para ser analisado
arquivo = open(str(resposta_entrada), "r")

# Abre o arquivo de saída no modo de escrita para ser preenchido no final
arquivo_de_saida = open(str(resposta_saida), "w")

# Matriz que vai ser preenchida por cada linha do arquivo de entrada
teste = []

# variavel acumuladora que indicará a quantidade de linhas da matriz original/final
y = 0

# matriz auxiliar é uma lista usada para montar uma matriz só com pontos
matriz_auxiliar1 = []

# palavra é uma lista que contem todas as palavras a serem buscadas no caça-palavra
palavra = []

# matriz é uma matriz que originalmente será preenchida por pontinhos e esses pontinhos serão substituidos por letras conforme forem encontradas as palavras no caça-palavra
matriz = []

# lista conterá a matriz com o caça-palavras
lista = []

# Leitura de cada linha do arquivo de entrada e colocando-as dentro da matriz "teste"
for l in arquivo:
    teste.append(l.split())

# Analisando cada linha da matriz "teste" e adicionando na matriz "lista"
for linha in range(len(teste)):

    # Se o primeiro termo de uma linha for um digito, a leitura para
    if teste[linha][0].isdigit():
        # x recebe a parte inteira do digito
        x = int(teste[linha][0])

        # ks é a linha seguinte da linha do digito, em que estará a primeira palavra a ser buscada
        ks = linha + 1
        break
    y = y + 1
    lista.append(teste[linha])

# Adiciona as palavras a serem buscadas a lista "palavra"
for i in range(x):
    # Adiciona as palavras a serem buscadas presente na matriz "teste" na lista "palavra"
    palavra = palavra + teste[ks]

    # Variavel acumuladora que adiciona 1 no indice anterior, para conseguir adicionar a proxima palavra na lista "palavra"
    ks = ks + 1

# Criação da matriz com pontinhos
for e in range(y):
    for i in range(len(lista[0])):
        matriz_auxiliar1.append(".")

        # Toda vez que a "matriz_auxiliar" preencher todos os termos de uma linha com pontinhos, a "matriz" adiciona a linha da "matriz_auxiliar"
        if i == len(lista[0]) - 1:
            matriz.append(matriz_auxiliar1)

            matriz_auxiliar1 = []

# Chama a função de analise
resultado_final(analise(palavra, lista, matriz))