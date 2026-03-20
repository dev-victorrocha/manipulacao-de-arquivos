from datetime import datetime

with open('diario.txt', 'a', encoding='utf-8') as arquivo:
    anotacao = str(input('Adicione uma anotação: '))
    agora = datetime.now().strftime('%d/%m/%Y %H:%M')
    arquivo.write(f'Anotação adicionada em: {agora} | ')
    arquivo.write(f'{anotacao}\n')
