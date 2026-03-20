with open('frutas.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Maçã\n')
    arquivo.write('Banana\n')
    arquivo.write('Laranja\n')
    arquivo.write('Melão\n')
    arquivo.write('Melancia')

with open('frutas.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
    