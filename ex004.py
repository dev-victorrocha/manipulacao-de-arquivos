nome = 'frutas.txt'
contador_linhas = contador_palavras = 0
with open(nome, 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        contador_linhas += 1
        palavras = linha.split()
        for palavra in palavras:
            contador_palavras += 1

    print(f'O arquivo {nome} tem {contador_linhas} linhas e {contador_palavras} palavras')
