with open('compras.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('LISTA DE COMPRAS\n')
    while True:
        novo_item = str(input("Item que será adicionado na lista (escreva 'sair' para sair): ")).lower()
        if novo_item == "sair":
            break

        arquivo.write(f'{novo_item}\n')

with open('compras.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
